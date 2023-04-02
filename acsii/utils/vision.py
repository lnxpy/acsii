from typing import IO

import cv2
from numpy import ndarray

RANGES = {
    0: '-',
    255: '#',
}


class ImageCoder:
    """
    worker interface between open-cv and ascii art making
    """

    # TODO: add docstrings to methods

    def __init__(self, image: IO) -> None:
        """
        Args:
            image(IO): path to image file
        """

        self.image: ndarray = cv2.imread(str(image), cv2.IMREAD_GRAYSCALE)
        _, self.image = cv2.threshold(self.image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        # for caching purposes in calculate_size
        self.serialized_context: list = list()
        self.width = None
        self.height = None

    def serialize(self, height_shift: int = 1, width_shift: int = 1) -> list:
        """
        Turns the entered image into an ASCII matrix based on the defined ranges

        Args:
            height_shift(int): the amount shift you want to reduce from the matrix height
            width_shift(int): the amount shift you want to reduce from the matrix width

        Returns:
            list: serialized image into ASCII
        """

        serialized: list = list()
        for line in self.image:
            serialized.append([RANGES[i] for i in line[::width_shift]])

        self.serialized_context = serialized[::height_shift]
        return self.serialized_context

    def calculate_size(self) -> None:
        """
        Evaluates the dimensions as ``obj.width`` and ``obj.height`` attributes
        """

        if not self.serialized_context:
            _ = self.serialize()
        self.width = len(self.serialized_context[0])
        self.height = len(self.serialized_context)