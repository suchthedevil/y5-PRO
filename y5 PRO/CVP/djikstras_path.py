graph = {}

with open("y5 PRO/CVP/mesta.txt","r", encoding="utf-8-sig") as f:
    for line in f:
        m1, m2, km, cas = line.strip().split(",")
        if m1 in graph:
            graph[m1].append([m2,int(km),cas])
        else:
            graph[m1] = [[m2,int(km),cas]]
        if m2 in graph:
            graph[m2].append([m1,int(km),cas])
        else:
            graph[m2] = [[m1,int(km),cas]]

roads = {}
for town in graph:
    roads[town] = [float("inf"),"-"]

start = 'Bratislava'
end = 'Nitra'
visited = []
naj = float("inf")
roads[start] = [0,start]

while start != end:
    for town in graph[start]:
        km = town[1]
        if roads[start][0] + km < roads[town[0]][0]:
            roads[town[0]] = [km,start]
            pom = town[0]
    start = pom
    visited.append(roads[start])
    del roads[start]


for town, content in roads.items():
    print(town, content)

