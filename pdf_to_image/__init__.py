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

    lh  = logging.StreamHandler(sys.stdout)
    fmt = logging.Formatter(Config.LOG_FORMAT)
    lh.setFormatter(fmt)

    app.logger.setLevel(Config.LOG_LEVEL)
    app.logger.handlers = [lh]

    @app.post("/pdfToJson")
    @app.post("/pdfToJson/<format>")
    @app.post("/pdfToJson/<format>/<mode>")
    def pdf_to_image_json(
        format: str = IMAGE_FORMAT__PNG,
        mode: str = ImageMode.VERTICAL.value,
    ):
        data = request.get_json()
        image_content = pdf_to_base64_image(data["pdfContent"], format, mode)
        return jsonify({
            "timestamp": dt.datetime.now(tz=pytz.utc).isoformat(),
            "contentType": f"image/{format}",
            "imageContent": image_content,
        })

    @app.post("/pdfToImage")
    @app.post("/pdfToImage/<format>")
    @app.post("/pdfToImage/<format>/<mode>")
    def pdf_to_image_format(
        format: str = IMAGE_FORMAT__PNG,
        mode: str = ImageMode.VERTICAL.value
    ):
        data = request.get_json()
        image_content = pdf_to_image(data["pdfContent"], format, mode)

        headers = {
            "Content-Type": f"image/{format}",
            "X-Timestamp": dt.datetime.now(tz=pytz.utc).isoformat(),
        }

        return Response(image_content, headers=headers)

    return app
