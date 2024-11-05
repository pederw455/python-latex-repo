# Dockerfile
FROM python:3.9-slim

# Install Git and Poetry dependencies
RUN apt-get update && apt-get install -y git curl && \
    curl -sSL https://install.python-poetry.org | python3 - && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Add Poetry to PATH
ENV PATH="/root/.local/bin:$PATH"

# Set the working directory
WORKDIR /app

# Copy pyproject.toml, and optionally poetry.lock if it exists
COPY pyproject.toml poetry.lock* ./

# Install dependencies, ignoring any missing poetry.lock file
RUN poetry install --no-root || true

# Copy the rest of the project files
COPY . .

# Define default command
CMD ["poetry", "run", "python", "src/main.py"]
