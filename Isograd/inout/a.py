#*******
#* Read input from STDIN
#* Use: echo or print to output your result to STDOUT, use the /n constant at the end of each result line.
#* Use: sys.stderr.write() to display debugging information to STDERR
#* ***/
import sys
from collections import defaultdict

lines = []
for line in sys.stdin:
	lines.append(line.rstrip('\n'))

n, m = map(int, lines[0].split())
station_dep, station_arr = map(int, lines[1].split())
n_stations = map(int, lines[2].split()) # number stations by line

stations = list()
station_lines = defaultdict(list)
for idx, line in enumerate(lines[3:]):
    row = list(map(int, line.split()))
    for s in row:
        station_lines[s].append(idx)
    stations.append(row)


fringe = list()
costs = defaultdict(lambda: float("inf"))
for line in station_lines[station_dep]:
    fringe.append((station_dep, line))
    costs[(station_dep, line)] = 0
explored =  defaultdict(lambda: False)

is_found = False
while len(fringe)!=0:
    node = fringe.pop(0)
    if node[0] == station_arr:
        is_found = True
        break
    else:
        if not explored[node]:
            line_idx = node[1]
            for s in stations[line_idx]:
                if costs[node] < costs[(s, line_idx)]:
                    costs[s] = costs[node]
                    fringe.append((s, line_idx))
            for s in station_lines[node[0]]:
                if costs[node] < costs[(node[0], s)]:
                    costs[(node[0], s)] = costs[node] + 1
                    fringe.append((node[0], s))
            explored[node] = True
        fringe.sort(key = lambda s: costs[s])

cost = float("inf")
for key in costs:
    if key[0] == station_arr:
        cost = min(costs[key], cost)
        
if is_found:
    print(cost+1)
else:
    print(-1)
    
