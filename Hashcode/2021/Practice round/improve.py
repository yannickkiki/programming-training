import itertools
import time


class Pizza:
    def __init__(self, idx, ingredients):
        self.idx = idx
        self.ingredients = ingredients
        self.n_ingredients = len(self.ingredients)


class Delivery:

    def __init__(self, pizzas):
        self.team_size = len(pizzas)

        self.pizzas_ids, ingredients = [], set()
        for pizza in pizzas:
            self.pizzas_ids.append(pizza.idx)
            ingredients = ingredients.union(pizza.ingredients)
        self.n_ingredients = len(ingredients)


class Submission:
    def __init__(self, deliveries):
        self.deliveries = deliveries

    def create_submission_file(self, filename):
        score = 0
        result = f"{len(self.deliveries)}\n"
        for delivery in self.deliveries:
            team_size = len(delivery.pizzas_ids)
            result += str(team_size) + " " + " ".join(map(str, delivery.pizzas_ids)) + "\n"
            score += delivery.n_ingredients ** 2

        print("Creating submission with score ", score)
        with open(f"{filename}_{score}", "w") as f:
            f.write(result)


def run():
    input_filename, output_filename, new_output_filename = "b.in", "b.out_13479", "b.out"

    pizzas_all = []
    with open(input_filename, "r") as f:
        n_pizzas, *_ = map(int, f.readline().split())
        for idx in range(n_pizzas):
            n_ingredients, *ingredients = f.readline().split()
            pizzas_all.append(Pizza(idx=idx, ingredients=ingredients))

    deliveries = []
    with open(output_filename, "r") as f:
        n_deliveries = int(f.readline())
        for _ in range(n_deliveries):
            team_size, *pizzas_ids = map(int, f.readline().split())
            deliveries.append(Delivery(pizzas=[pizzas_all[idx] for idx in pizzas_ids]))

    time_start = time.time()

    for i in range(n_deliveries):
        for j in range(n_deliveries):
            if i == j:
                continue

            pizzas_ids_ij = deliveries[i].pizzas_ids + deliveries[j].pizzas_ids

            for new_pizzas_ids_i in itertools.combinations(pizzas_ids_ij, deliveries[i].team_size):
                new_pizzas_ids_j = set(pizzas_ids_ij) - set(new_pizzas_ids_i)
                new_delivery_i = Delivery(pizzas=[pizzas_all[idx] for idx in new_pizzas_ids_i])
                new_delivery_j = Delivery(pizzas=[pizzas_all[idx] for idx in new_pizzas_ids_j])
                current_score_ij = deliveries[i].n_ingredients ** 2 + deliveries[j].n_ingredients ** 2
                new_score_ij = new_delivery_i.n_ingredients ** 2 + new_delivery_j.n_ingredients ** 2
                if new_score_ij > current_score_ij:
                    deliveries[i], deliveries[j] = new_delivery_i, new_delivery_j

    submission = Submission(deliveries)
    submission.create_submission_file(filename=new_output_filename)

    print("Execution time (s): ", time.time() - time_start)


if __name__ == '__main__':
    run()
