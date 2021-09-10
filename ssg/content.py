import re
from yaml import load, FullLoader
from collections.abc import Mapping

class Content(Mapping):
    __delimiter = "^(?:-|\+){3}\s*$"
    __regex = re.compile(__delimiter, flags=re.MULTILINE)

    @classmethod
    def load(cls, string):
        _, fm, content = __regex.split(string)
        load(fm, Loader=FullLoader)
        return  cls(metadata, content)

    def __init__(self, metadata, content):
        self.data = metadata
        self.data["content"] = content

    def __getitem__(self, key):
        return self.data[key]

    def __iter__(self):
        self.data.item()

    def __len__(self):
        return len(self.data.keys())
    
    def __repr__(self):
        data = {}
        for key, value in self.data.items():
            if key != "content":
                data[key] = value
        return str(data)

    @property
    def type(self):
        if "type" in self.data.keys():     
            return self.data["type"] 
        else: 
            return None

    @type.setter
    def type(self, type):
        self.data["type"] = type