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
            
        eventual_times = [get_real_time(times[0], offset) for offset in offsets]
        matches = defaultdict(list) #real time -> (time_idx,offset_idx)
        for offset_idx, time in enumerate(eventual_times):
            matches[time].append((0, offset_idx))
        
        for time_idx, time in enumerate(times[1:]):
            for idx, offset in enumerate(offsets):
                real_time = get_real_time(time, offset)
                time_idxs = matches.get(real_time)
                # if ti==2:
                    # print(time, offset, real_time)
                if time_idxs:
                    time_idxs.append((1+time_idx, idx))
        
        # print(matches)
        results = list()
        for time, match in matches.items():
            if len(list(set([var[0] for var in match])))==len(list(set([var[1] for var in match])))==n:
                results.append(time)
                
        n_results = len(results)
        display = ''
        if n_results==0:
            display = 'none'
        elif n_results==1:
            display = results[0]
        elif n_results>1:
            display = n_results
        print(f"{k} {display}")
