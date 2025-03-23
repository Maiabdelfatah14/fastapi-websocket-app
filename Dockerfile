# Use the official lightweight Python image
FROM python:3.11-slim

# Set the working directory inside the container
WORKDIR /app

# Copy dependencies file first to optimize caching
COPY requirements.txt .

# Install required dependencies with minimal size
RUN pip install --no-cache-dir -r requirements.txt

# Copy the remaining project files
COPY main.py .
COPY static ./static

# Add a non-root user for better security
RUN useradd -m appuser
USER appuser

# Expose the application port dynamically
ENV PORT=8000  
EXPOSE 8000

# Run the application using Uvicorn with dynamic port
CMD ["sh", "-c", "uvicorn main:app --host 0.0.0.0 --port ${PORT} --workers 4"]
