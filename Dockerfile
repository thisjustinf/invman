FROM python:3.13-slim-bookworm

ARG ENVIRONMENT=development

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*


ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements/ requirements/

COPY scripts/ scripts/

RUN pip install --no-cache-dir -r requirements/base.txt

RUN pip install --no-cache-dir -r requirements/${ENVIRONMENT}.txt

COPY . .

EXPOSE 8000

# Make scripts executable
# RUN chmod +x ./generate-sql.sh
RUN chmod +x ./scripts/entrypoint-${ENVIRONMENT}.sh
RUN chmod +x ./scripts/run-migrations.sh

ENTRYPOINT [ "./scripts/entrypoint-${ENVIRONMENT}.sh" ]
