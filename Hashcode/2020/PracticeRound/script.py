if __name__ == "__main__":
    datasets = ["a", "b", "c", "d", "e"]
    
    for dataset in datasets:
        print(f"Dataset {dataset} ...")
        with open(dataset + ".in", "r") as f:
            max_n_pizza_slices, n_pizzas = map(int, f.readline().split())
            n_slices_list = list(map(int, f.readline().split()))
            
        pizzas_type_to_order, total_n_slices = list(), 0
        for idx, n_slice in enumerate(reversed(n_slices_list)):
            pizza_type_idx = n_pizzas - idx - 1
            
            if total_n_slices + n_slice <= max_n_pizza_slices:
                pizzas_type_to_order.insert(0, pizza_type_idx)
                total_n_slices += n_slice
                
            if total_n_slices == max_n_pizza_slices:
                break
    
        with open(dataset + ".out", "w") as f:
            f.write(f"{len(pizzas_type_to_order)}\n")
            pizzas_type_to_order_str = " ".join(map(str, pizzas_type_to_order)) + "\n"
            f.write(pizzas_type_to_order_str)
