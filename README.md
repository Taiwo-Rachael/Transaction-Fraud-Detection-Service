# Transaction-Fraud-Detection-Service
FastAPI service built on a robust XGBoost model to classify financial transactions as fraudulent or non-fraudulent. Features Pydantic-based request validation, a custom preprocessing and inference pipeline for reliable predictions, and full Docker containerization for seamless cross-platform deployment.
  
## Table of Contents
1. [Project Structure](#project-structure)
2. [Local Development](#local-development)
3. [Docker Setup](#docker-setup)
4. [Configure Environment Variables](#configure-environment-variables)

## Project Structure
```bash
Transaction-Fraud-Detection-Service/   
├── model/                         
│   └── fraud_detection_model.joblib    # Trained fraud detection model  
│
├── src/                                # Source code files   
│   ├── base_model.py                   # Pydantic input schema definitions
│   ├── encoder.joblib                  # OneHotEncoder
│   ├── Fraud_Detection_Model.ipynb     # Model training notebook
│   ├── inference.py                    # custom preprocessing function  
│   └── scaler.joblib                   # Feature scaler 
│
├── .dockerignore                       # Docker ignore file  
├── .gitignore                          # Git ignore file  
├── Dockerfile                          # Docker build instructions  
├── main.py                             # FastAPI entrypoint  
├── README.md                           # Project documentation  
└── requirements.txt                    # Python dependencies  

```

## Local Development
### 1. Clone the Repository:  
```bash
git clone https://github.com/Taiwo-Rachael/Transaction-Reports-Download-Bots.git
cd Transaction-Reports-Download-Bots
```
 
### 2. Create and Activate a Virtual Environment:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 3. Install Dependencies:
```bash
pip install -r requirements.txt
```

### 4. Run Locally:
```bash
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```
The API will be available at http://127.0.0.1:8000.

## Docker Setup
### Build the Docker Image
```bash
docker build -t taiworachel/reports-downloader-bots .
```
### Run a Container
```bash
docker run --rm \
  -p 8000:8000 \
  --env-file .env \
  --env DISPLAY=$(grep nameserver /etc/resolv.conf | awk '{print $2}'):0.0 \
  -v ~/Downloads:/root/Downloads \
  -v /tmp/.X11-unix:/tmp/.X11-unix \
  taiworachel/reports-downloader-bots
```
The application is now available at http://localhost:8000

## Configure Environment Variables

In your project root, create a .env file and add the following variables:
```bash
NIP_USER
NIP_PW



