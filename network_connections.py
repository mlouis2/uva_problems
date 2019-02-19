import sys

class disjoint_set:
    def __init__(self):
        self.relationships = {}
    def add(self, name):
        if (name not in self.relationships):
            self.relationships[name] = [name, 1]
    def find(self, name):
        if (self.relationships[name][0] == name):
            return self.relationships[name]
        else:
            return self.find(self.relationships[name][0])
    def merge(self, name1, name2):
        data1 = self.find(name1)
        data2 = self.find(name2)
        parentOfData1 = self.find(data1[0])
        parentOfData2 = self.find(data2[0])
        if (parentOfData1 != parentOfData2):
            if (parentOfData1[1] >= parentOfData2[1]):
                parentOfData1[1] += parentOfData2[1]
                data2[0] = data1[0]
            else:
                parentOfData2[1] += parentOfData1[1]
                data1[0] = data2[0]

sys.stdin.readline()
first_line = True
for line in stdin:
    if (line == '\n'):
        first_line = True
    else:
        if (first_line):
            num_computers = int(sys.stdin.readline().strip())
        else:
            letter, compA, compB = sys.stdin.readline().strip().split()
            
        first_line = False
