FROM python:3.10-alpine

RUN apk update && \
  apk upgrade && \
  apk add poppler-utils

WORKDIR /app
COPY . .
RUN pip install -U pip && \
  pip install -r requirements.txt

EXPOSE 5000

CMD ["gunicorn", "pdf_to_image:create_app()", "--bind", "0.0.0.0:5000"]
