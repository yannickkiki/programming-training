from collections import defaultdict

if __name__ == "__main__":
    # datasets = ["a", "b", "c", "d", "e"]
    datasets = ["b"]
    
    for dataset in datasets:
        print(f"Dataset {dataset} ...")
        with open(dataset + ".in", "r") as f:
            max_n_pizza_slices, n_pizzas = map(int, f.readline().split())
            n_slices_list = list(map(int, f.readline().split()))
            
        is_pizza_to_order_dict, total_n_slices, n_pizzas_to_order = defaultdict(lambda: False), 0, 0
        for idx, n_slice in enumerate(reversed(n_slices_list)):
            pizza_type_idx = n_pizzas - idx - 1
            
            if total_n_slices + n_slice <= max_n_pizza_slices:
                is_pizza_to_order_dict[pizza_type_idx] = True
                total_n_slices += n_slice
                n_pizzas_to_order += 1
                
            if total_n_slices == max_n_pizza_slices:
                break
        
        old_right_pizza_type_to_order_idx, new_right_pizza_type_to_order_idx = None, None
        for _idx, is_to_order in reversed(list(is_pizza_to_order_dict.items())):
            idx = n_pizzas - _idx - 1
            print(_idx)
            if old_right_pizza_type_to_order_idx is None:
                print("Here", idx)
                if is_to_order:
                    old_right_pizza_type_to_order_idx = idx
            else:
                print("There", idx)
                if not is_to_order and n_slices_list[idx] != n_slices_list[old_right_pizza_type_to_order_idx]:
                    new_right_pizza_type_to_order_idx = idx
                    break
                
        old_left_pizza_type_to_order_idx, new_left_pizza_type_to_order_idx = None, None
        for idx, is_to_order in list(is_pizza_to_order_dict.items()):
            if old_left_pizza_type_to_order_idx is None:
                if is_to_order:
                    old_left_pizza_type_to_order_idx = idx
            else:
                if not is_to_order and n_slices_list[idx] != n_slices_list[old_left_pizza_type_to_order_idx]:
                    new_left_pizza_type_to_order_idx = idx
                    break
        
        with open(dataset + ".out", "w") as f:
            f.write(f"{n_pizzas_to_order}\n")
            
            pizzas_type_to_order_str = ""
            for pizza_type_idx, is_to_order in is_pizza_to_order_dict.items():
                if is_to_order:
                    pizzas_type_to_order_str = str(pizza_type_idx) + " " + pizzas_type_to_order_str
            f.write(pizzas_type_to_order_str)
