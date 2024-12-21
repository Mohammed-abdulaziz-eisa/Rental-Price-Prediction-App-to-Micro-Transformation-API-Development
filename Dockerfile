# Step 1: Use a lightweight Python base image
FROM python:3.9-slim

# Step 2: Set a working directory inside the container
WORKDIR /app

# Step 3: Copy project files into the container
COPY . /app

# Step 4: Install dependencies
# Use pyproject.toml with Poetry or requirements.txt
RUN pip install --no-cache-dir poetry
RUN poetry install --no-dev

# Step 5: Expose the port your Flask app runs on
EXPOSE 5000

# Step 6: Set the command to run the Flask app
CMD ["poetry", "run", "python3", "app/run.py"]