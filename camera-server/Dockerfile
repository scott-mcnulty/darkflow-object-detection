FROM python:3.6-slim

# Add camera server code
COPY server /app/server
COPY requirements.txt /app/server
WORKDIR /app/server

RUN apt-get update && apt-get install -y \
    libgtk2.0-dev

# Install dependencies
RUN pip install --upgrade pip -r requirements.txt

# Default command
CMD [ "gunicorn", "--config", "server/configs/gunicorn_config.py", "server.app:create_app()" ]