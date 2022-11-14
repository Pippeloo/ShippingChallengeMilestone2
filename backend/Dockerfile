FROM python:alpine3.16

# Set the working directory to /code
WORKDIR /code

# Copy the requirements file to the working directory
COPY requirements.txt /code

# Install fastapi
RUN pip install -r /code/requirements.txt

# Copy the app
COPY app /code/app

# Expose the port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]