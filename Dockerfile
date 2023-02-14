# Pull base image
FROM python:3.11


# Set environment Variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# Set working directory

# copy code to /code
COPY . /code/

# Copy the Requirments 
COPY requirements.txt ./code


WORKDIR /code
RUN pip install -r requirements.txt
