import sys


class Query:

    StdBegin = \
        '''BEGIN {FS=",";FPAT = "[^,]*|\"[^\"]*\""}'''

    def __


class QueryFromCSV(Query):
    def __init__(self, source_path):
        self.source_path = source_path


print("Hello")
print("|"+Query.StdBegin+"|")
