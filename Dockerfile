FROM python:3.11

# Install awscli
RUN apt update -y && apt install -y awscli

# Set the working directory
WORKDIR /app

# Copy project files
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Run the application
CMD ["python3", "app.py"]
