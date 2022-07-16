from enum import Enum

FORMATS = {
    "png": "PNG",
    "jpg": "JPEG",
}

IMAGE_FORMAT__PNG = "png"


class ImageMode(Enum):
    VERTICAL = "vertical"
    HORIZONTAL = "horizontal"
