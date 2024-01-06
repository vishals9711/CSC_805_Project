# Use an official Node.js runtime as the base image
FROM node:18-alpine as build

# Set the working directory inside the container
WORKDIR /app

# Copy the rest of the application code
COPY frontend .

RUN npm install --legacy-peer-deps

# RUN npm run lint:fix
RUN ls -la
# Build the application
RUN npm run build

# Step 2: Create a Dockerfile for Flask Deployment
FROM python:3.8-slim

# Set the working directory to /app
WORKDIR /app

# Copy the Flask app code to the container
COPY ./flask_server /app

# remove all files from the template folder
RUN rm -rf /app/templates/*

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the built React app from the previous stage
COPY --from=build /app/build /app/templates

# Expose port 8976 for Flask app
EXPOSE 8765

# Define environment variable
# ENV FLASK_APP=app.py

# Run Flask when the container launches

# gunicorn -w 4 'app:app'

CMD ["gunicorn", "-w", "4", "--bind", "0.0.0.0:8765", "app:app"]