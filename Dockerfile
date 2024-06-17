FROM python:3.12-slim

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "--host", "main", "0.0.0.0", "--port", "80"]