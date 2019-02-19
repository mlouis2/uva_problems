import sys

class DisjointSet:
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

num_test_cases = int(sys.stdin.readline().strip())
for i in range(0, num_test_cases):
    social_network = DisjointSet()
    num_friendships = int(sys.stdin.readline().strip())
    for j in range(0, num_friendships):
        friendA, friendB = sys.stdin.readline().strip().split()
        social_network.add(friendA)
        social_network.add(friendB)
        social_network.merge(friendA, friendB)
        print(social_network.find(social_network.find(friendA)[0])[1])
