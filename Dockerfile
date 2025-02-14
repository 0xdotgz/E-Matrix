FROM python:3.11-slim-buster

WORKDIR /app

RUN python -m pip install --no-cache-dir --upgrade pip

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

CMD ["python", "e-matrix.py"]
