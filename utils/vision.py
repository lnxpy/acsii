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
        self.image: ndarray = cv2.imread(str(image), cv2.IMREAD_GRAYSCALE)
        _, self.image = cv2.threshold(self.image, 128, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        self.serialized_context: list = list()
        self.width, self.height = 0, 0

    def serialize(self, height_shift: int = 1, width_shift: int = 1) -> str:
        serialized: list = list()
        for line in self.image:
            serialized.append([RANGES[i] for i in line[::width_shift]])

        self.serialized_context = serialized[::height_shift]
        return self.serialized_context

    def calculate_size(self) -> None:
        if not self.serialized_context:
            _ = self.serialize()
        self.width = len(self.serialized_context[0])
        self.height = len(self.serialized_context)