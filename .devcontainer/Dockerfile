# Dockerfile
FROM python:3.10-slim

# Install Git, Curl, and TeX Live (including pdflatex and necessary fonts)
RUN apt-get update && \
    apt-get install -y git curl texlive-latex-base texlive-fonts-recommended texlive-fonts-extra texlive-latex-extra && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Install Poetry
RUN curl -sSL https://install.python-poetry.org | python3 - && \
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
