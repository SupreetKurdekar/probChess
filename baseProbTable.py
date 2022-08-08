import numpy as np

class baseProbTable():
    def __init__(self):

        self.probTable = np.zeros((9,9))

    def setAllToHalf(self):
        # np.fill(self.probTable,0.5)
        self.probTable = np.full(self.probTable.shape,0.5)