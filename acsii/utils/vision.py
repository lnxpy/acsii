from typing import IO

import cv2
from numpy import ndarray

from os import get_terminal_size

from acsii.utils.serializer import serialize


class Encoder:
    """
    Image encoder interface between open-cv and ascii art making
    """

    def __init__(self, image: IO, typeset: str, size: tuple = get_terminal_size()) -> None:
        """
        Args:
            image: path to image file
            typeset: ASCII characters type set
            size: image size (it fits to terminal size by default)
        """

        self.image: ndarray = cv2.imread(str(image), cv2.IMREAD_GRAYSCALE)
        self.image = cv2.resize(self.image, size)

        # for caching purposes in calculate_size
        self.serialized_context: list = list()
        self.typeset = typeset
        self.width = None
        self.height = None

    def serialize(self) -> list:
        """
        Turns the entered image into an ASCII matrix
        Returns:
            a matrix that contains the serialized columns of the image
        """

        serialized: list = list()
        for line in self.image:
            serialized.append([serialize(i, self.typeset) for i in line])

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