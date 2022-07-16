FROM python:3.9-slim

RUN apt update -y && \
  apt upgrade -y && \
  apt install -y poppler-utils

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5000

# ENV FLASK_APP="pdf_to_image:create_app()"
# ENV FLASK_RUN_PORT="5000"
# ENV WORKERS="1"

CMD ["gunicorn", "pdf_to_image:create_app()", "--bind", "0.0.0.0:5000", "--workers", "1"]
