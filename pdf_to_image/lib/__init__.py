import base64
from pdf2image import convert_from_bytes
from PIL import Image
from io import BytesIO

from .constants import (
    FORMATS,
    IMAGE_FORMAT__PNG,
    ImageMode,
)


def pdf_to_image(
    encoded_pdf: str,
    format: str = IMAGE_FORMAT__PNG,
    mode: str = ImageMode.VERTICAL.value,
) -> bytes:
    """
    Receives a PDF file content encoded in base64 format and returns the binary content (bytes) of an image with the whole content inside.
    """

    pdf_content = base64.b64decode(encoded_pdf)
    images = convert_from_bytes(pdf_content)

    page_width, page_height = images[0].size
    if mode == ImageMode.VERTICAL.value:
        size = (page_width, page_height * len(images))
    elif mode == ImageMode.HORIZONTAL.value:
        size = (page_width * len(images), page_height)

    full_image = Image.new("RGB", size)

    for index, page_image in enumerate(images):
        if mode == ImageMode.VERTICAL.value:
            coords = (0, index * page_height)
        elif mode == ImageMode.HORIZONTAL.value:
            coords = (index * page_width, 0)

        full_image.paste(page_image, coords)

    full_image_file = BytesIO()
    full_image.save(full_image_file, FORMATS.get(format, IMAGE_FORMAT__PNG))

    full_image_file.seek(0)
    return full_image_file.read()


def pdf_to_base64_image(
    encoded_pdf: str,
    format: str = IMAGE_FORMAT__PNG,
    mode: str = ImageMode.VERTICAL.value,
) -> str:
    """
    Receives a PDF file content encoded in base64 format and returns the content of an image with the whole content inside in base64 format. Suitable to send a JSON response.
    """
    full_image_encoded = base64.b64encode(pdf_to_image(encoded_pdf, format, mode))
    return full_image_encoded.decode("utf8")
