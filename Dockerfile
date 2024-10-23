# Use the official Python image from the Docker Hub
FROM python:3.11-slim

# Set the working directory
# set work directory
WORKDIR /usr/src/app
 
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
 
VOLUME ["/app"]

# install dependencies
RUN pip install --upgrade pip
COPY ./requirements.txt .
RUN pip install -r requirements.txt
 
# copy project
COPY . .

# run uvicorn
CMD ["uvicorn", "webapp.main:app", "--host", "0.0.0.0", "--port", "8000"]
