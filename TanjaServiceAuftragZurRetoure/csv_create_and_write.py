import numpy as np
from settings import *

def createNewCsv(nameDesNeuenFiles, src):
    np.savetxt(nameDesNeuenFiles, src, delimiter = ';', fmt='% s')