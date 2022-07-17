from flask import Flask, jsonify, request, Response
from .config import Config
import logging
import sys
import datetime as dt
import pytz
from .lib import (
    IMAGE_FORMAT__PNG,
    ImageMode,
    pdf_to_base64_image,
    pdf_to_image,
)


def create_app():
    app = Flask(__name__)

    app.config.from_object(Config)

    loggin_handler  = logging.StreamHandler(sys.stdout)
    logging_formatter = logging.Formatter(Config.LOG_FORMAT)
    loggin_handler.setFormatter(logging_formatter)

    app.logger.setLevel(Config.LOG_LEVEL)
    app.logger.handlers = [loggin_handler]

    @app.post("/pdfToJson")
    @app.post("/pdfToJson/<format>")
    @app.post("/pdfToJson/<format>/<mode>")
    def pdf_to_json_route(
        format: str = IMAGE_FORMAT__PNG,
        mode: str = ImageMode.VERTICAL.value,
    ):
        pdf_content = request.get_data()
        image_content = pdf_to_base64_image(pdf_content, format, mode)
        return jsonify({
            "timestamp": dt.datetime.now(tz=pytz.utc).isoformat(),
            "contentType": f"image/{format}",
            "imageContent": image_content,
        })

    @app.post("/pdfToImage")
    @app.post("/pdfToImage/<format>")
    @app.post("/pdfToImage/<format>/<mode>")
    def pdf_to_image_route(
        format: str = IMAGE_FORMAT__PNG,
        mode: str = ImageMode.VERTICAL.value
    ):
        pdf_content = request.get_data()
        image_content = pdf_to_image(pdf_content, format, mode)

        headers = {
            "Content-Type": f"image/{format}",
        }

        return Response(image_content, headers=headers)

    return app
