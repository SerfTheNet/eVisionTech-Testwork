FROM python:3.8.10-slim
RUN mkdir /app
COPY ./main.py /app
COPY config.py /app
WORKDIR /app/
COPY requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt
CMD ["uvicorn", "--host", "0.0.0.0", "main:app"]
