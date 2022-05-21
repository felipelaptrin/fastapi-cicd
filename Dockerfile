FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt
COPY ./api .
RUN groupadd -r api && useradd -r -g api api
USER api
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80"]