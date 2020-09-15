import os


class GetPath:
    def getPath(self, path):
        r = os.path.abspath(path)
        return r


if __name__ == '__main__' :
    a = GetPath().getPath('./get_GetPath.py')
    print(a)
