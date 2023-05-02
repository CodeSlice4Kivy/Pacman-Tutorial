# in order to move our ghost we will need to use an algorithym
# We will use the dijkstra algorythm
# Its an algorthym that allows our ghost to find the shortest path to the player
from heapq import *
import math

# to call calculate distance between 2 points
def distance(pointA, pointB):
    return math.sqrt((pointA[0]-pointB[0])**2+(pointA[1]-pointB[1])**2)

# this function will return an index of the minimum list it will be important later
def argmin(f, l, j):
    arg = j
    for i in range(len(l)):
        if f(l[i]) < f(arg):
            arg = l[i]
    return arg

# this function here finds the shortest path using the graph we will provide
def dijkstra(s,t,graph):
    M = set()
    d = {s: 0}
    p = {}
    following = [(0, s)]

    while following != []:

        dx, x = heappop(following)
        if x in M:
            continue

        M.add(x)

        for w,y in nearby(x,graph):
            if y in M:
                continue
            dy = dx + w
            if y not in d or d[y] > dy:
                d[y] = dy
                heappush(following, (dy, y))
                p[y] = x

    path = [t]
    x = t
    while x != s:
        x = p[x]
        path.insert(0,x)

    return d[t], path

def nearby(s,graph):
    # basically through this function we will return nearby points from the graph we will create
    return graph[s]

# Most import here, we greate a graph using close points and our point lists.
def pts_graph(the_close_list, the_points_list):
    gr={}
    for i in range(1, len(the_close_list)+1):
        gr[i]=[]
        for j in the_close_list[i-1]:
            gr[i].append((distance(the_points_list[j],the_points_list[i]), j))
    return(gr)
    
# Done Done Done
