# Hello CloudNexus 🚀

## 📌 Project Overview

**Hello CloudNexus** is an end-to-end DevOps deployment project demonstrating how to containerize an application, store Docker images securely, and deploy them automatically on AWS using a CI/CD pipeline.

This project covers **everything from zero to production**, including manual deployment, automation, security, and real-world troubleshooting.

The final outcome is:

> **A single `git push` automatically builds, pushes, and deploys the application on AWS EC2.**

---

## 🧠 Problem Statement

Deploy an application using:

* Git & GitHub
* Docker
* GitHub Actions (CI/CD)
* AWS EC2 (compute)
* AWS ECR (container registry)

Requirements:

* Application must run on EC2
* Docker images must be stored in ECR
* Deployment must be automated
* No access keys stored on EC2
* Include proper documentation and troubleshooting

---

## 🏗️ Architecture Overview

```
Developer
   |
   | git push
   v
GitHub Repository
   |
   | triggers
   v
GitHub Actions (CI)
   |
   | docker build
   | docker push
   v
Amazon ECR
   |
   | docker pull
   v
Amazon EC2 (Amazon Linux)
   |
   v
Browser (Public Access)
```

---

## 🧰 Tools & Technologies Used

| Category           | Tools                     |
| ------------------ | ------------------------- |
| Version Control    | Git, GitHub               |
| Containerization   | Docker                    |
| CI/CD              | GitHub Actions            |
| Cloud Compute      | AWS EC2 (Amazon Linux)    |
| Container Registry | AWS ECR                   |
| Security           | IAM Roles, IAM Users, SSH |

---

## 📁 Project Structure

```
hello-cloudnexus/
├── app.py
├── requirements.txt
├── Dockerfile
├── .github/
│   └── workflows/
│       └── deploy.yml
└── README.md
```

---

## 🚀 Application Details

### app.py

A simple Flask application exposing:

* `/` → Main UI
* `/health` → Health check endpoint

The app listens on `0.0.0.0:5000` so it can run inside Docker and be accessed externally.

---

## 🐳 Dockerization

### Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 5000

CMD ["python3", "app.py"]
```

### What this does

* Uses a lightweight Python base image
* Installs dependencies
* Copies application code
* Exposes port 5000
* Starts the Flask app

---

## ☁️ AWS Setup (Manual Deployment Phase)

### 1️⃣ EC2 Setup

* Amazon Linux 2 instance
* Port **22** (SSH) and **5000** (app) opened in Security Group
* Docker installed and enabled

### 2️⃣ IAM Role for EC2

* Role attached directly to EC2
* Policy used:

  * `AmazonEC2ContainerRegistryReadOnly`

👉 This allows EC2 to pull images from ECR **without access keys**.

---

### 3️⃣ Amazon ECR Setup

* Private ECR repository created
* Image tag mutability: **Mutable**
* Used to store Docker images

---

### 4️⃣ Manual Docker Flow (Validation)

Steps performed manually to validate understanding:

1. Build Docker image on EC2
2. Tag image for ECR
3. Push image to ECR
4. Pull image back from ECR
5. Run container from ECR image

This confirmed the full:

```
EC2 → Docker → ECR → EC2
```

flow works correctly.

---

## 🔐 IAM for CI/CD (GitHub Actions)

### IAM User Created

* Name: `github-actions-ecr`
* Purpose: Allow GitHub Actions to push images to ECR
* Policy attached:

  * `AmazonEC2ContainerRegistryFullAccess`

### Access Keys

* Access Key ID and Secret Access Key generated
* Stored securely in GitHub Secrets

---

## 🤖 CI/CD Automation with GitHub Actions

### Workflow Trigger

* Triggered on `push` to `main` branch

### Workflow Responsibilities

* Checkout code
* Build Docker image
* Push image to Amazon ECR
* SSH into EC2
* Pull new image
* Restart container

### deploy.yml

```yaml
name: Deploy Hello CloudNexus to EC2

on:
  push:
    branches:
      - main

jobs:
  deploy:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Configure AWS credentials
        uses: aws-actions/configure-aws-credentials@v4
        with:
          aws-access-key-id: ${{ secrets.AWS_ACCESS_KEY_ID }}
          aws-secret-access-key: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
          aws-region: ap-south-1

      - name: Login to Amazon ECR
        uses: aws-actions/amazon-ecr-login@v2

      - name: Build Docker image
        run: docker build -t hello-cloudnexus .

      - name: Tag Docker image
        run: docker tag hello-cloudnexus:latest <ECR_URI>:latest

      - name: Push Docker image
        run: docker push <ECR_URI>:latest

      - name: Deploy to EC2
        uses: appleboy/ssh-action@v1
        with:
          host: ${{ secrets.EC2_HOST }}
          username: ec2-user
          key: ${{ secrets.EC2_SSH_KEY }}
          script: |
            docker stop cloudnexus-app || true
            docker rm cloudnexus-app || true
            docker pull <ECR_URI>:latest
            docker run -d -p 5000:5000 --name cloudnexus-app <ECR_URI>:latest
```

---

## 🔐 GitHub Secrets Used

| Secret Name           | Purpose             |
| --------------------- | ------------------- |
| AWS_ACCESS_KEY_ID     | IAM user access key |
| AWS_SECRET_ACCESS_KEY | IAM user secret     |
| EC2_HOST              | EC2 public IP / DNS |
| EC2_SSH_KEY           | EC2 private SSH key |

---

## 🧪 Final Verification

* GitHub Actions workflow ran successfully ✅
* Docker image built & pushed automatically ✅
* EC2 pulled image & restarted container ✅
* Application accessible via browser:

```
http://<EC2_PUBLIC_IP>:5000
```

---

## 🛠️ Troubleshooting (REAL ISSUES FACED)

### pip3 not found

* Fixed by installing `python3-pip` on Amazon Linux

### App not accessible in browser

* Security Group missing port 5000

### ECR push denied

* EC2 role had ReadOnly policy
* Temporarily added FullAccess

### SSH Permission denied (publickey)

* SSH key mismatch between EC2 and GitHub
* Fixed using correct public key + ssh-agent

### GitHub Actions deploy failed: missing server host

* Secret name mismatch (`EC2_HOST_PUB_IP` vs `EC2_HOST`)

### EC2 public IP changed after stop/start

* Updated GitHub secret with new IP

---

## 🏁 Conclusion

This project demonstrates a **complete DevOps lifecycle**:

* Manual deployment
* Secure AWS integration
* CI/CD automation
* Real-world troubleshooting

It is production-aligned, interview-ready, and showcases hands-on DevOps skills.

---
##
Deployed & documented as part of DevOps internship preparation.

---
