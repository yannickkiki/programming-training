class FoundException(Exception):
    pass

with open('a.in', 'r') as f:
    t = int(f.readline().strip())
    for i in range(t):
        k, c, *weights = map(int, f.readline().strip().split())
        possible_sums = {0}
        try:
            for weight in weights:
                precedent_sums = list(possible_sums)
                for s in precedent_sums:
                    new_s = s+weight
                    if new_s == c:
                        raise FoundException()
                    possible_sums.add(new_s)
        except FoundException:
            print(f"{k} YES")
        else:
            print(f"{k} NO")
