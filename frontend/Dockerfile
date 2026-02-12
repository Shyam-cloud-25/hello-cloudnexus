FROM python:3.11-alpine

WORKDIR /app

# Copy requirements first (better caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y pip setuptools wheel \
    && rm -rf /root/.cache

# Copy app code
COPY . .

EXPOSE 5000

CMD ["python", "app.py"]

