def inter(slot1, slot2):
   slot = slot1+slot2
   slot.sort()
   return slot[1:3]

def is_inter_available(slot1, slot2, duration):
    slot = inter(slot1, slot2)
    return slot[1]-slot[0]>=duration, [slot[0], slot[0]+duration]
    
def minAvailableDuration(slots1, slots2, duration):
    slots1.sort(key=lambda k: k[0])
    slots2.sort(key=lambda k: k[0])
    
    idx2, n2 = 0, len(slots2)
    
    for slot1 in slots1:
        comp = idx2
        is_idx2_updated = False
        while comp<n2:
            slot2 = slots2[comp]
            if slot2[0]>slot1[1]-duration:
                break
            if not is_idx2_updated and slot2[1]>=slot1[1]+duration:
                idx2 = comp
            comp += 1
            if slot2[1]<slot1[0]+duration:
                continue
            is_i_a, slot = is_inter_available(slot1, slot2, duration)
            if is_i_a:
                return slot
        if not is_idx2_updated:
            idx2 = comp
    return []

if __name__=='__main__':
    slots1 = [[10,50],[60,120],[140,210]]
    slots2 = [[0,15],[60,70]]
    duration = 8
    result = minAvailableDuration(slots1, slots2, duration)
