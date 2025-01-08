# Dockerfile
FROM python:3.12-slim

# Set work directory
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Install Playwright browsers
RUN pip install playwright
RUN playwright install

# Copy the rest of your application
COPY . .

# Set the environment variable
WORKDIR /app/tests

# Command to run the tests
CMD ["pytest"]

