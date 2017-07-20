import json

class JsonToPython:

    def __init__(self,fileName,type):
        self.fileName = fileName
        self.type = type

    def readJson(self):
        with open(self.fileName,self.type) as f:
            return json.load(f)
