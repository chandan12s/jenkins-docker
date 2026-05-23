pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
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
                    dockerImage = docker.build("${env.IMAGE_NAME}")
                    echo "Docker image built: ${dockerImage.id} with tag: ${env.BUILD_NUMBER}"
                }
            }
        }

        stage('Tag Image') {
            steps {
                script {
                    echo "Tagging image ${dockerImage.id} with tag: ${env.BUILD_NUMBER}"
                    dockerImage.tag('${env.BUILD_NUMBER}')
                }
            }
        }

        stage('Docker Push') {
            steps {
                withCredentials([usernamePassword(credentialsId: '${env.DOCKERHUB_CREDENTIALS}', usernameVariable: 'DOCKER_USER', passwordVariable: 'DOCKER_PASS')]) {
                    script {
                        docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-creds') {
                            dockerImage.push('${env.BUILD_NUMBER}')
                            echo "Docker image pushed: ${env.IMAGE_NAME}:${env.BUILD_NUMBER}"
                        }
                    }
                }
            }
        }
    }
}