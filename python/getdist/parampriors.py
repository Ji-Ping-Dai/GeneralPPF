import os


class ParamBounds(object):
    """
    Class for holding list of parameter bounds (e.g. for plotting, or hard priors). 
    A limit is None if not specified, denoted by 'N' if read from a string or file

    :ivar names: list of parameter names
    :ivar lower: dict of lower limits, indexed by parameter name
    :ivar upper: dict of upper limits, indexed by parameter name
    """

    def __init__(self, fileName=None):
        """
        :param fileName: optional file name to read from
        """
        self.names = []
        self.lower = {}
        self.upper = {}
        if fileName is not None: self.loadFromFile(fileName)

    def loadFromFile(self, fileName):
        self.filenameLoadedFrom = os.path.split(fileName)[1]
        with open(fileName) as f:
            for line in f:
                strings = [text.strip() for text in line.split()]
                if len(strings) == 3:
                    self.setRange(strings[0], strings[1:])

    def __str__(self):
        s = ''
        for name in self.names:
            valMin = self.getLower(name)
            if valMin is not None:
                lim1 = "%15.7E" % valMin
            else:
                lim1 = "    N"
            valMax = self.getUpper(name)
            if valMax is not None:
                lim2 = "%15.7E" % valMax
            else:
                lim2 = "    N"
            s += "%22s%17s%17s\n" % (name, lim1, lim2)
        return s

    def saveToFile(self, fileName):
        """
        Save to a plain text file

        :param fileName: file name to save to
        """
        with open(fileName, 'w') as f:
            f.write(str(self))

    def setRange(self, name, strings):
        if strings[0] != 'N' and strings[0] is not None: self.lower[name] = float(strings[0])
        if strings[1] != 'N' and strings[1] is not None: self.upper[name] = float(strings[1])
        if not name in self.names: self.names.append(name)

    def getUpper(self, name):
        """
        :param name: parameter name
        :return: upper limit, or None if not specified
        """
        return self.upper.get(name, None)

    def getLower(self, name):
        """
        :param name: parameter name
        :return: lower limit, or None if not specified
        """
        return self.lower.get(name, None)
