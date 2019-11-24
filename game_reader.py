import constants as const

class MapReader():

    def __init__(self, path):
        """Read a map."""
        self._path = path
        with open(path, "r") as doc:
            self.read(doc)

    def read(self, file):
        """Read all the file line by line."""
        #get the map_size
        self.MAP_SIZE = tuple(map(int, file.readline().split(",")))
        #read the map
        self.MAP = self.readMap(file)
        #if map linked
        self.LINKS = self.readLinks(file)

    def readMap(self, file):
        """Read the map matrix."""
        result = []
        for i in range(self.MAP_SIZE[1]):
            line = file.readline()
            line = line.split(",")
            #check if length of line is valid
            if len(line) < self.MAP_SIZE[0]:
                raise SystemError()
            #append the line to result
            result.append(list(map(int, line)))
        return result[:]

    def readLinks(self, file):
        """Read the last line. If contains a link or not"""
        #links
        links = []
        #lines
        line = file.readline()
        if line.startswith("LINKS"):
            _, n = line.split()
        else:
            return None
        for i in range(int(n)):
            line = file.readline()
            if line.startswith("LINK"):
                _, pos, path = line.split()
                links.append((tuple(map(int, pos.split(","))), path))
        return links
