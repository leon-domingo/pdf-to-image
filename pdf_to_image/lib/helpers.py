from typing import Tuple
from .constants import ImageMode


def get_size(
    page_width: int,
    page_height: int,
    num_pages: int,
    mode: str
) -> Tuple[int, int]:
    if mode == ImageMode.VERTICAL.value:
        return (page_width, page_height * num_pages)
    elif mode == ImageMode.HORIZONTAL.value:
        return (page_width * num_pages, page_height)
