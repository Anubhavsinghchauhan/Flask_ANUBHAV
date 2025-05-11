
FROM python:3.13.1-slim-bullseye

# Set the working directory inside the container
WORKDIR /docker

# Copy only the requirements first (for caching)
COPY requirements.txt ./

# Upgrade pip and install requirements
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copy the rest of the application files
COPY . .

# Set the default command to run the Flask app
CMD ["python", "-m", "flask", "--app", "hello", "run", "--host=0.0.0.0"]

