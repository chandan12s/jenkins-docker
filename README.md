# Simple Python Calculator

This repository contains a small Python CLI calculator and a Dockerfile to containerize it.

Usage

- Run locally (REPL):

```bash
python app.py
```

- Evaluate a single expression:

```bash
python app.py "2 + 3 * (4 - 1)"
```

Docker

- Build the image:

```bash
docker build -t simple-calc .
```

- Run the container (REPL):

```bash
docker run -it --rm simple-calc
```

- Run a single expression:

```bash
docker run --rm simple-calc  "2 + 2"
```
