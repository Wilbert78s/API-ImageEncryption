# Use an official Python runtime as a parent image
FROM python:3.9

# Set the working directory to /app
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Make port 80 available to the world outside this container
EXPOSE 8080

# Set the environment variable from file
COPY key.json /app/key.json
ENV GOOGLE_APPLICATION_CREDENTIALS=/app/key.json

# Define environment variable
ENV NAME World

# Run app.py when the container launches
CMD ["python", "app.py"]