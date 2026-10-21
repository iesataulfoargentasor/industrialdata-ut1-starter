FROM python:3.12.9-slim-bookworm
ENV PYTHONUNBUFFERED=1 PYTHONDONTWRITEBYTECODE=1 PIP_DISABLE_PIP_VERSION_CHECK=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
ENV PYTHONPATH=/app/src
COPY src src
COPY dashboard dashboard
COPY tests tests
COPY scripts scripts
COPY pyproject.toml .
CMD ["python", "-m", "industrialdata.run", "--input", "/data/raw"]
