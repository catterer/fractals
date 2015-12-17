#!/usr/bin/env python3

import sys

class Vertax:
    def __init__(self, name):
        self.name = name
        self.color = "white"
        self.neighbors = [] # neighbor list
    def __str__(self):
        s = self.name + ": "
        for v in self.neighbors:
            s = s + v.name + " "
        return s
    def addNeighbor(self, neighbor):
        self.neighbors.append(neighbor)


class OrGraph:
    def __init__(self, branches):
        self.vertaxes = {}
        self.buildNeighbours(branches)
 
    def __str__(self):
        s = ""
        for v in self.vertaxes:
            vert = self.vertaxes[v]
            s = s + "\n" +  str(vert) + "\n"
        return s
 
    def buildNeighbours(self, branches):
        for start, end in branches:
            startV = self.vertaxes.get(start, Vertax(start))
            endV = self.vertaxes.get(end, Vertax(end))
           
            startV.addNeighbor(endV)
            self.vertaxes[start] = startV
            self.vertaxes[end] = endV
           
 
 
    def depthSearch(self):# returns depth search order
        depthOrder = []
        for v in self.vertaxes:
            vert = self.vertaxes[v]
            vert.color = "white"
       
        # here must be your code
 
        depthOrder.reverse()
 
        return depthOrder
 
           
 
def file_split(f, delim=',', bufsize=1024):
    prev = ''
    while True:
        s = f.read(bufsize)
        if not s:
            break
        split = s.split(delim)
        if len(split) > 1:
            yield prev + split[0]
            prev = split[-1]
            for x in split[1:-1]:
                yield x
        else:
            prev += s
    if prev:
        yield prev
 
def graphRestore(input):
    branches = []
    for s in file_split(input):
        sss = s.split()
        if len(sss) == 2:
            startVert = sss[0]
            endVert = sss[1]
            branches.append([startVert, endVert])
    return OrGraph(branches)

if __name__ == '__main__':
    input = sys.stdin
    if len(sys.argv) > 1:
        input = open(sys.argv[1], 'r')
    graph = graphRestore(input)
    
    print(graph)
    print(graph.depthSearch())
