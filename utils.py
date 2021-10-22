import matplotlib.pyplot as plt
from typing import List, Tuple, Optional
import numpy as np
import math


def computeRowsCols(N : int, m : int, n : int) -> Tuple[int, int]:
    """
    Compute number of rows and columns for subplot
    :param N: number of subfigures
    :param m: rows preference
    :param n: columns preference
    :return: resulting number of rows and colums
    """
    if m is None:
        m = math.sqrt(N)
        if n is None:
            n = math.ceil(N / m)
        else:
            m = math.ceil(N / n)
    else:
        if n is None:
            n = math.ceil(N / m)
        else:
            m = math.ceil(N / n)
    m, n = max(1, m), max(1, n)
    m, n = math.ceil(m), math.ceil(n)
    return m, n


def show_ims(imgs: List[np.array], m: Optional[int] = None, n: Optional[int] = None,
             title: str = "", subtitles: Optional[List[str]] = None):
    """
    Show a group of images in subplots of the same figure
    :param imgs: images to show
    :param m: number of rows preference
    :param n: number of columns preference
    :param title: global title
    :param subtitles: list of subtitles for subplots
    :return: None
    """
    N = len(imgs)

    m, n = computeRowsCols(N, m, n)
    fig = plt.figure()
    for i in range(1, N + 1):
        plt.subplot(m, n, i)
        if len(imgs[i-1].shape) == 3:
            plt.imshow(imgs[i-1])
        else:
            plt.imshow(imgs[i-1], cmap="gray")
        if subtitles is not None:
            plt.title(subtitles[i - 1])
    fig.suptitle(title)
    plt.show(block=True)
