# Compliance Checking API with FastAPI, Celery, and Flower

This project is a web application that checks product compliance against predefined policies using FastAPI and Celery for background processing. It also includes a Flower dashboard for monitoring tasks.

## Features

- FastAPI for building the API.
- Celery for handling background tasks.
- Flower for monitoring Celery tasks.
- Simple frontend for inputting compliance and product URLs.

## Prerequisites

Before you begin, ensure you have met the following requirements:

- Python 3.8 or higher
- Docker and Docker Compose installed
- A Docker Hub account (optional for pushing images)
- An OpenAI API key (sign up at [OpenAI](https://platform.openai.com/signup) if you don't have one)

## Project Structure

```
.
├── app
│   ├── __init__.py
│   ├── main.py             # FastAPI app entry point
│   ├── celery_worker.py    # Celery worker definition
│   ├── tasks.py            # Celery tasks
│   ├── templates           # Jinja2 templates
│   │   └── index.html
│   └── static              # Static files (CSS, JS)
├── docker-compose.yml
├── Dockerfile
├── README.md
└── requirements.txt
```

## Setup

### 1. Clone the Repository

Clone the repository to your local machine:

```bash
git clone https://github.com/Ish2K/Compliance-Checker.git
cd Compliance-Checker
```

### 2. Set Up Environment Variables

Create a `.env` file in the `webapp` directory and add your OpenAI API key:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### 3. Build the Docker Images

To build the Docker images, run the following command:

```bash
docker-compose build
```

### 4. Start the Services

You can start the application and its dependencies (including Celery and Flower) with Docker Compose:

```bash
docker-compose up
```

### 5. Access the Application

Once the services are running, you can access the application in your web browser at:

```
http://localhost:8000
```

### 6. Using the Flower Dashboard

To monitor your Celery tasks, access the Flower dashboard at:

```
http://localhost:5555
```

### 7. Stopping the Services

To stop the running services, use:

```bash
docker-compose down
```

## Usage

### Frontend

1. Open the web application in your browser.
2. Enter the URLs for compliance and product texts in the provided form.
3. Submit the form to check compliance.

### Backend

The API endpoints can be accessed for direct integration or testing. The primary endpoint for compliance checking will be documented in the `main.py` file.
