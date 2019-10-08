from collections import defaultdict

def get_real_time(time, offset):
    rt = dict()
    rt['h'], rt['m'] = time['h']-offset['h'], time['m']-offset['m']
    rt['h'], rt['m'] = rt['h']+(rt['m']//60), rt['m']%60
    rt['h'] = rt['h']%12
    if rt['h']==0: rt['h'] = 12
    return str(rt['h']) + ':' + str(rt['m']).zfill(2)
    
with open('e.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        k, n = map(int, f.readline().strip().split())
        
        times = list()
        for _ in range(n):
            h, m = map(int, f.readline().strip().split(':'))
            times.append({'h': h, 'm': m})
            
        offsets = list()
        for _ in range(n):
            h, m = f.readline().strip().split(':')
            if h[0]=='-': m = -int(m)
            offsets.append({'h': int(h), 'm': int(m)})
            
        init_times = [get_real_time(times[0], offset) for offset in offsets]
        offsets_idxs = defaultdict(list)
        for idx, time in enumerate(init_times):
            offsets_idxs[time].append((0, idx))
        
        for ti, time in enumerate(times[1:]):
            for idx, offset in enumerate(offsets):
                real_time = get_real_time(time, offset)
                time_idxs = offsets_idxs.get(real_time)
                # if ti==2:
                    # print(time, offset, real_time)
                if time_idxs:
                    time_idxs.append((1+ti, idx))
        
        # print(offsets_idxs)
        results = list()
        for time, idxs in offsets_idxs.items():
            if len(list(set([var[0] for var in idxs])))==len(list(set([var[1] for var in idxs])))==n:
                results.append(time)
                
        display = 'none'
        n_results = len(results)
        if n_results==1:
            display = results[0]
        elif n_results>1:
            display = n_results
        print(f"{k} {display}")
