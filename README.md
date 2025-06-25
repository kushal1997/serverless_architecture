# 🧠 Serverless Architecture & Cloud Automation – Graded Assignments

## 📘 Overview

This repository documents AWS-based automation assignments completed as part of the *Serverless Architecture & Cloud Automation* coursework. Each task demonstrates real-world serverless automation using **AWS Lambda**, **Boto3**, and other AWS services.

---

## 📚 Table of Contents

| Assignment | Title                                                                 | Link                          |
|------------|-----------------------------------------------------------------------|-------------------------------|
| 1          | EC2 Auto-Start & Auto-Stop                                            | [Assignment 1](#-assignment-1-ec2-auto-start--auto-stop) |
| 2          | S3 Bucket File Cleanup                                                | [Assignment 2](#-assignment-2-s3-bucket-file-cleanup)     |
| 4          | EBS Snapshot Automation                                               | [Assignment 4](#-assignment-4-ebs-snapshot-automation)    |
| 5          | Auto-Tagging EC2 on Launch                                            | [Assignment 5](#-assignment-5-auto-tagging-ec2-on-launch) |

> 📝 More assignments will be added here as they're completed!

---

## ✅ Assignments & Descriptions

### 📌 Assignment 1: EC2 Auto-Start & Auto-Stop

**Goal**: Automatically start or stop EC2 instances based on tags (`Auto-Start`, `Auto-Stop`).

📂 [`Assignment-1`](./Assignment-1)  
📸 Includes screenshots:
- EC2 instance before & after Lambda execution
- Lambda logs
- Test event & code

---

### 📌 Assignment 2: S3 Bucket File Cleanup

**Goal**: Delete files older than 30 days in an S3 bucket.

📂 [`Assignment-2`](./Assignment-2)  
📸 Includes screenshots:
- S3 bucket before and after cleanup
- Lambda code
- IAM policy
- Test configuration

---

### 📌 Assignment 4: EBS Snapshot Automation

**Goal**: Create snapshots of EBS volumes and clean up those older than 30 days.

📂 [`Assignment-4`](./Assignment-4)  
📄 `requirements.txt` included  
📸 Includes screenshots:
- Snapshot creation & deletion
- Lambda code and logs
- IAM role & EventBridge schedule

---

### 📌 Assignment 5: Auto-Tagging EC2 on Launch

**Goal**: Automatically tag newly launched EC2 instances with launch date and a custom label.

📂 [`Assignment-5`](./Assignment-5)  
📄 `requirements.txt` included  
📸 Includes screenshots:
- EventBridge trigger
- Lambda code
- Logs
- Tagged EC2 instance view

---

## 🚀 How to Run / Reproduce

Each assignment includes:

1. Python code (`lambda_function.py`)
2. Required IAM roles and permissions
3. Manual test events (JSON)
4. EventBridge or CloudWatch triggers (where applicable)
5. Screenshot folder `screenshots/`
6. Step-by-step guide in `README.md`

> 📦 Some assignments require installing dependencies:
```bash
pip install -r requirements.txt
