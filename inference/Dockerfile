FROM ubuntu:18.10

#Install git
RUN apt-get update && apt-get install -q -y \
    git \
    gcc \
    libgtk2.0-dev \
    build-essential python3.6 python3.6-dev python3-pip \
    # build-essential python3.6 python3-pip \
    # --no-install-recommends \
    && \
    rm -rf /var/lib/apt/lists/*

# Add inference server code
COPY inference /app/inference
COPY requirements.txt /app/inference
WORKDIR /app

# Install dependencies
RUN pip3 install --upgrade pip -r inference/requirements.txt

# Get weights
RUN git clone https://github.com/leetenki/YOLOtiny_v2_chainer.git
RUN mv YOLOtiny_v2_chainer/tiny-yolo-voc.weights /app/inference/weights
RUN rm -rf YOLOtiny_v2_chainer

# Get darkflow
RUN git clone https://github.com/thtrieu/darkflow.git

# Install darkflow
WORKDIR /app/darkflow
RUN pip3 install .
RUN cp -r cfg /app/inference

# Default command
WORKDIR /app/inference
CMD [ "gunicorn", "--config", "configs/gunicorn_config.py", "app:create_app()" ]