import cv2
import matplotlib as mpl
import matplotlib.cm as mtpltcm
from PIL import Image
import numpy as np
def filterThermal(frame, colorData, frameSize):
    cv2.waitKey(1)

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    colormap = mpl.cm.jet
    cNorm = mpl.colors.Normalize(vmin=colorData[0], vmax=colorData[1])
    scalarMap = mtpltcm.ScalarMappable(norm=cNorm, cmap=colormap)
    colors = scalarMap.to_rgba(gray)

    #Rescale to 0-255 and convert to uint8
    rescaled = (255.0 / colors.max() * (colors - colors.min())).astype(np.uint8)

    colors = Image.fromarray(rescaled)
    colors = np.array(colors)
    colors = cv2.cvtColor(colors, cv2.COLOR_BGR2RGB)
    colors = cv2.resize(colors, frameSize)
    colors = cv2.imencode('.jpg', colors)[1].tobytes()
    return colors