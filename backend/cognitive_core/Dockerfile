# Base image
FROM python:3.10

# Set working directory
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project files
COPY . .

# Expose the port
EXPOSE 5000

# Run the application
CMD ["uvicorn", "local_core:app", "--host", "0.0.0.0", "--port", "5000"]