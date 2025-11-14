# gunicorn_conf.py
# Use the Uvicorn worker class for high performance with FastAPI/ASGI
worker_class = "uvicorn.workers.UvicornWorker"

# Define the number of worker processes
# A common starting recommendation is 2 * CPU_CORES + 1
workers = 4 

# Bind the server to all interfaces on port 8000
bind = "0.0.0.0:8000"

# Set the log level
loglevel = "info"