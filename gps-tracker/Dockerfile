FROM python:3.11-slim
ENV PYTHONUNBUFFERED=1 
WORKDIR /app
COPY . /app
RUN pip install -r requirements.txt
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
