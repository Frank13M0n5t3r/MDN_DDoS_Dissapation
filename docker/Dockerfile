
FROM python:3.9-slim as builder

WORKDIR /build
COPY requirements.txt .
# Install dependencies needed for the build
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 \
    build-essential \
    python3-dev \
    libevent-dev && \
    pip install --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Clean up to reduce layer size
RUN apt-get remove --purge -y build-essential libevent-dev python3-dev && \
    apt-get autoremove -y && apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Stage 2: Runtime stage with only necessary artifacts
FROM python:3.9-slim
WORKDIR /app

# Re-install runtime libraries
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1-mesa-glx \
    libglib2.0-0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Copy only the necessary artifacts from the builder stage
COPY --from=builder /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY app.py .
COPY object_detection.py .
COPY yolo_tiny_configs ./yolo_tiny_configs

ENV PATH="/root/.local/bin:$PATH"
EXPOSE 5010
CMD ["python", "app.py"]
