# Dockerfile
FROM python:3.9

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Make port 5000 available to the world outside this container
EXPOSE 5000

# Define environment variable
ENV NAME World

# Ensure the start.sh script is executable
RUN chmod +x start.sh

# Run the start.sh script when the container launches
CMD ["./start.sh"]
