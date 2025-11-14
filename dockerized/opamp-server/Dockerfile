# Stage 1: Build Dependencies
FROM python:3.11-slim AS build
ENV PYTHONUNBUFFERED=1
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
# ----------------------------------------------------
# Stage 2: Final Runtime Image (Updated)
# ----------------------------------------------------
FROM python:3.11-slim

RUN adduser --system --uid 1001 --group appuser
WORKDIR /app
ENV PORT=8000

# 1. Copy the Python packages/libraries
COPY --from=build /usr/local/lib/python3.11/site-packages /usr/local/lib/python3.11/site-packages

# 2. FIX: Copy the Python executable binaries (like 'gunicorn' and 'uvicorn')
# The Python slim image already includes /usr/local/bin in its PATH, so we copy the files there.
COPY --from=build /usr/local/bin/ /usr/local/bin/

COPY server.py .
COPY anyvalue_pb2.py .
COPY anyvalue_pb2.pyi .
COPY env_vars.py .
COPY opamp_pb2.py .
COPY opamp_pb2.pyi .
COPY gunicorn_conf.py .

USER appuser
EXPOSE ${PORT}
#CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "server:app", "--bind", "0.0.0.0:8000"]
CMD ["gunicorn", "-c", "gunicorn_conf.py", "server:app"]