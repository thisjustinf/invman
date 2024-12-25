FROM python:3.13-slim-bookworm

ARG ENVIRONMENT=development

WORKDIR /app

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/ requirements/

RUN pip install --no-cache-dir -r requirements/${ENVIRONMENT}.txt

# COPY requirements.txt .

# RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

# Make scripts executable
RUN chmod +x scripts/entrypoint-${ENVIRONMENT}.sh
RUN chmod +x scripts/setup-db.sh
RUN chmod +x scripts/run-migrations.sh

# CMD ["fastapi", "dev", "app/main.py", "--host", "0.0.0.0", "--port", "8000"]
ENTRYPOINT [ "./scripts/entrypoint-${ENVIRONMENT}.sh" ]
