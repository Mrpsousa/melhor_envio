import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm
from PIL import Image
import numpy as np


def filterSimple(frame, frameSize):
    cv2.waitKey(1)

    frame = Image.fromarray(frame)
    frame = np.array(frame)
    resized = cv2.resize(frame, frameSize)
    frame = cv2.imencode('.jpg', resized)[1].tobytes()
    return frame