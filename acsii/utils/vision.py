from typing import IO

import cv2
from numpy import ndarray

from os import get_terminal_size

RANGES = {
    0: '-',
    255: '#',
}


class ImageCoder:
    """
    worker interface between open-cv and ascii art making
    """

    # TODO: add docstrings to methods

    def __init__(self, image: IO, size: tuple = get_terminal_size()) -> None:
        """
        Args:
            image(IO): path to image file
            size(tuple): image size (it fits to terminal size by default)
        """

        self.image: ndarray = cv2.imread(str(image), cv2.IMREAD_GRAYSCALE)
        self.image = cv2.resize(self.image, size)
        _, self.image = cv2.threshold(self.image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # for caching purposes in calculate_size
        self.serialized_context: list = list()
        self.width = None
        self.height = None

    def serialize(self) -> list:
        """
        Turns the entered image into an ASCII matrix

        Returns:
            list: serialized image into ASCII
        """

        serialized: list = list()
        for line in self.image:
            serialized.append([RANGES[i] for i in line])

        self.serialized_context = serialized
        return self.serialized_context

    def calculate_size(self) -> None:
        """
        Evaluates the dimensions as ``obj.width`` and ``obj.height`` attributes
        """

        if not self.serialized_context:
            _ = self.serialize()
        self.width = len(self.serialized_context[0])
        self.height = len(self.serialized_context)