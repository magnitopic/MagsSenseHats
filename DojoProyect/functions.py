import json
import os


def getInfo(name):
    if name not in getNames():
        return None
    with open(f'data/{name}.json') as f:
        file = json.load(f)
    return file


def getNames():
    names = []
    for file in os.listdir("data"):
        if file.endswith(".json"):
            names.append(os.path.splitext(file)[0])
    return names


if __name__ == "__main__":
    pass
