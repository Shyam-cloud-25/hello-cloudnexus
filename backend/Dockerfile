FROM python:3.11-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip uninstall -y pip setuptools wheel \
    && rm -rf /root/.cache

COPY . .

EXPOSE 5001

CMD ["python", "app.py"]

