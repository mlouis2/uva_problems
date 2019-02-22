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

sys.stdin.readline()
first_line_in_case = True
first_line = True
correct_questions = 0
incorrect_questions = 0
for line in sys.stdin:
    if (line == '\n'):
        if (not first_line):
            print(str(correct_questions) + ',' + str(incorrect_questions))
            print('')
        first_line = False
        computer_connections = DisjointSet()
        correct_questions = 0
        incorrect_questions = 0
        first_line_in_case = True
    else:
        if (first_line_in_case):
            num_computers = int(line.strip())
            for i in range(1, num_computers + 1):
                computer_connections.add(str(i))
        else:
            letter, compA, compB = line.strip().split()
            if (letter == 'c'):
                computer_connections.merge(compA, compB)
            elif (letter == 'q'):
                if (computer_connections.find(compA) == computer_connections.find(compB)):
                    correct_questions += 1
                else:
                    incorrect_questions += 1
        first_line_in_case = False
print(str(correct_questions) + ',' + str(incorrect_questions))
