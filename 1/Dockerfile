FROM python:3.10-slim

WORKDIR /app

COPY . .

RUN pip3 install -r requirements.txt --no-cache-dir
RUN alembic revision --message="Initial" --autogenerate
RUN alembic upgrade head

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
