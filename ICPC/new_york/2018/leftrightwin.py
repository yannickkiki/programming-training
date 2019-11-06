with open('f.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        k, n, player_idx, p_left, p_right = f.readline().strip().split()
        k, n, player_idx = int(k), int(n), int(player_idx)
        p_left, p_right = float(p_left), float(p_right)
        
        ck, dk, sum_ck, sum_dk = [1, 0], [0, 1], 1, 1
        for ik in range(2,n):
            elt = (ck[ik-1] - p_left*ck[ik-2])/p_right
            ck.append(elt)
            sum_ck += elt
            
            elt = (dk[ik-1] - p_left*dk[ik-2])/p_right
            dk.append(elt)
            sum_dk += elt
       
        coef_a, coef_b = 1-(p_left*ck[n-1]), -p_right-(p_left*dk[n-1])
        coef_c, coef_d, coef_e, coef_f = 1-p_left-p_right, sum_ck, sum_dk, 1
        
        den = coef_b*coef_d-coef_e*coef_a
        p_0 = (coef_b*coef_f-coef_e*coef_c)/den
        p_1 = (coef_d*coef_c-coef_a*coef_f)/den
        
        result = "%.2f" % (100*(ck[player_idx]*p_0 + dk[player_idx]*p_1))
        
        print(f"{k} {result}")
