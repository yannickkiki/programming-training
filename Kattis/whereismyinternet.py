def find(idx):
    if parent[idx]==idx:
        return idx
    parent[idx] = find(parent[idx])
    return parent[idx]

def union(idx_A,idx_B):
    parent[find(max(idx_A,idx_B))] = find(min(idx_A,idx_B))

number_of_houses, number_of_cables = map(int,input().split(" "))
parent = list(range(number_of_houses))
    
for _ in range(number_of_cables):
    houseA_idx, houseB_idx = map(lambda v : int(v)-1,input().split(" "))
    union(houseA_idx, houseB_idx)
    
connected_set_repr = find(0)

all_connected = True
for house_idx,set_repr in enumerate(parent):
    if find(set_repr)!=connected_set_repr:
        print(house_idx+1)
        all_connected = False
if all_connected:
    print("Connected")