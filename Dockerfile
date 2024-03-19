FROM python:alpine3.19

# Set unbuffered output for python
ENV PYTHONUNBUFFERED 1

# Label
LABEL maintainer="benjamin"

# WORKING DIRECTORY
WORKDIR /app

# Install app dependencies
COPY requirements.txt .
RUN pip install -r requirements.txt

# Set the working directory
COPY . .

EXPOSE 8000

