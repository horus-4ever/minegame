import os

#path and check if file exist
CONFIGURATION_PATH = "configuration.rc"
if not os.path.exists(CONFIGURATION_PATH):
    raise SystemError()

class Reader():
    _datas = None
    def __init__(self, path):
        """Read all the file"""
        with open(path, "r") as doc:
            self._datas = doc.read()
        #read the paths
        self.read()

    def read(self):
        """Read the paths that should be in the file."""
        argcount = 0
        for line in self._datas.splitlines(False):
            if not line.__contains__(" ") or len(line) == 0:
                continue
            #line of type 'cmd arg'
            cmd, arg = line.split()
            setattr(self, cmd, arg)
        #if all was read
        return True

#read all
READER = Reader(CONFIGURATION_PATH)