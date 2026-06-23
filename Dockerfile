# Step 1: base image (Python installed)
FROM python:3.12

# Step 2: set working directory inside container
WORKDIR /app

# Step 3: copy files into container
COPY . .

# Step 4: install dependencies
RUN pip install -r requirements.txt

# Step 5: expose port
EXPOSE 5000

# Step 6: run application
CMD ["python", "app.py"]