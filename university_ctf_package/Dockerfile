FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies directly
RUN pip install flask flask-sqlalchemy flask-graphql graphene graphene-sqlalchemy gunicorn psycopg2-binary

# Copy application code
COPY . .

# Create data directory for SQLite
RUN mkdir -p data

# Expose port
EXPOSE 5000

# Set environment variables for offline mode
ENV FLASK_ENV=production
ENV DATABASE_URL=sqlite:///data/ctf_challenge.db

# Run the application
CMD ["python", "-m", "gunicorn", "--bind", "0.0.0.0:5000", "--workers", "4", "main:app"]