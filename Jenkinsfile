pipeline {
    agent any

    environment {
        IMAGE_NAME = "chandans12/simple-calc"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/chandan12s/jenkins-docker.git'            }
        }

        stage('Docker Build') {
            steps {
                script {
                    dockerImage = docker.build("${env.IMAGE_NAME}:${env.BUILD_NUMBER}")
                    echo "Docker image built: ${dockerImage.id} with tag: ${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Tag Image') {
            steps {
                script {
                    echo "Tagging image ${dockerImage.id} with latest tag"
                    dockerImage.tag('latest')
                }
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                            dockerImage.push('latest')
                            echo "Docker image pushed: ${env.IMAGE_NAME}:latest"
                        }
                    }
                }
            }
        }
    }
}