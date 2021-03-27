import bisect


class State:
    def __init__(self, last_elt, cursor_idx=1, cost=0):
        self.last_elt = last_elt
        self.cursor_idx = cursor_idx
        self.cost = cost

    def __lt__(self, other):
        return self.cost < other.cost

    def __eq__(self, other):
        return self.cost == other.cost

    def __gt__(self, other):
        return self.cost > other.cost


n_tests = int(input())
for idx_test in range(n_tests):
    cost_cj_str, cost_jc_str, mural_initial = input().split(" ")
    cost_cj, cost_jc = int(cost_cj_str), int(cost_jc_str)
    mural_size = len(mural_initial)
    fringe = list()
    if mural_initial[0] in ["C", "J"]:
        bisect.insort(fringe, State(last_elt=mural_initial[0]))
    else:
        assert mural_initial[0] == "?"
        bisect.insort(fringe, State(last_elt="C"))
        bisect.insort(fringe, State(last_elt="J"))

    cost_min = None
    while fringe:
        state = fringe.pop(0)
        if state.cursor_idx == mural_size:
            cost_min = state.cost
            break

        new_elt = mural_initial[state.cursor_idx]
        if new_elt == "C":
            if state.last_elt == "C":
                bisect.insort(fringe, State(last_elt="C", cursor_idx=state.cursor_idx + 1, cost=state.cost))
            elif state.last_elt == "J":
                bisect.insort(fringe, State(last_elt="C", cursor_idx=state.cursor_idx + 1, cost=state.cost + cost_jc))
            else:
                raise AssertionError
        elif new_elt == "J":
            if state.last_elt == "C":
                bisect.insort(fringe, State(last_elt="J", cursor_idx=state.cursor_idx + 1, cost=state.cost + cost_cj))
            elif state.last_elt == "J":
                bisect.insort(fringe, State(last_elt="J", cursor_idx=state.cursor_idx + 1, cost=state.cost))
            else:
                raise AssertionError
        else:
            assert new_elt == "?"
            if state.last_elt == "C":
                bisect.insort(fringe, State(last_elt="C", cursor_idx=state.cursor_idx + 1, cost=state.cost))
                bisect.insort(fringe, State(last_elt="J", cursor_idx=state.cursor_idx + 1, cost=state.cost + cost_cj))
            elif state.last_elt == "J":
                bisect.insort(fringe, State(last_elt="C", cursor_idx=state.cursor_idx + 1, cost=state.cost + cost_jc))
                bisect.insort(fringe, State(last_elt="J", cursor_idx=state.cursor_idx + 1, cost=state.cost))
            else:
                raise AssertionError

    print(f"Case #{1 + idx_test}: {cost_min}")
