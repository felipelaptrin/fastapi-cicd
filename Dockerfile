FROM python:3.9
WORKDIR /app
COPY ./requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt
COPY ./api /app/api
RUN groupadd -r api && useradd -r -g api api
USER api
CMD ["uvicorn", "api.main:app", "--host", "0.0.0.0", "--port", "80"]