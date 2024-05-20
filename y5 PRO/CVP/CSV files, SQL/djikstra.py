nodes = {}
distances = {}
with open('y5 PRO/CVP/CSV files, SQL/mesta.csv', encoding='utf-8-sig') as f:
    for line in f:
        node, dest, km, time = line.strip().split(",")
        if node in nodes.keys():
            nodes[node].append([dest,int(km)])
        else:
            nodes[node] = [[dest,int(km)]]
            distances[node] = float('inf')
        if dest in nodes.keys():
            nodes[dest].append([node,int(km)])
        else:
            nodes[dest] = [[node,int(km)]]
            distances[dest] = float('inf')

#find shortest path from Bratislava to Kosice

start = 'Bratislava'
distances[start] = 0
end = 'Košice'
visited = []
path = {}
path[start]= [start,0]

while start != end:
    for town in nodes[start]:
        km = town[1]
        if path[start][1] + km < path[town[0]][1]:
            path[town[0]] = [start,km]
            next = town[0]
    start = next

print(distances)
"""

for i, j in nodes.items():
    print(i,j)
"""