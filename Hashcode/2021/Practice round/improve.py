import itertools
import time


class Pizza:
    def __init__(self, ingredients):
        self.ingredients = ingredients
        self.n_ingredients = len(self.ingredients)


input_filename, output_filename, new_output_filename = "c.in", "c.out_711885847", "c.out"

pizzas = []
with open(input_filename, "r") as f:
    n_pizzas, *_ = map(int, f.readline().split())
    for _ in range(n_pizzas):
        n_ingredients, *ingredients = f.readline().split()
        pizzas.append(Pizza(ingredients=ingredients))


class Delivery:
    pizzas_all = pizzas

    def __init__(self, pizzas_ids):
        self.pizzas_ids = pizzas_ids
        self.team_size = len(self.pizzas_ids)

        ingredients = []
        for pizza_id in self.pizzas_ids:
            ingredients = list(set(ingredients + self.pizzas_all[pizza_id].ingredients))
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


deliveries = []
with open(output_filename, "r") as f:
    n_deliveries = int(f.readline())
    for _ in range(n_deliveries):
        team_size, *pizzas_ids = map(int, f.readline().split())
        deliveries.append(Delivery(pizzas_ids=pizzas_ids))


def run():
    starttime = time.time()

    for i in range(400, 500):
        print(i)
        for j in range(n_deliveries):
            if i == j:
                continue
            # print(deliveries[i].pizzas_ids, deliveries[j].pizzas_ids)
            pizzas_ids_ij = deliveries[i].pizzas_ids + deliveries[j].pizzas_ids
            # print("Pizzas ids ij", pizzas_ids_ij)

            for new_pizzas_ids_i in itertools.combinations(pizzas_ids_ij, deliveries[i].team_size):
                new_pizzas_ids_j = set(pizzas_ids_ij) - set(new_pizzas_ids_i)
                # print("New i: ", new_pizzas_ids_i, "New j:", new_pizzas_ids_j)
                new_delivery_i = Delivery(pizzas_ids=list(new_pizzas_ids_i))
                new_delivery_j = Delivery(pizzas_ids=list(new_pizzas_ids_j))
                current_score_ij = deliveries[i].n_ingredients ** 2 + deliveries[j].n_ingredients ** 2
                new_score_ij = new_delivery_i.n_ingredients ** 2 + new_delivery_j.n_ingredients ** 2
                if new_score_ij > current_score_ij:
                    # print("Current score ij", current_score_ij, "New score ij", new_score_ij)
                    # print(new_delivery_i.pizzas_ids, new_delivery_j.pizzas_ids)
                    deliveries[i], deliveries[j] = new_delivery_i, new_delivery_j

    submission = Submission(deliveries)
    submission.create_submission_file(filename=new_output_filename)

    print("Execution time (s): ", time.time() - starttime)


if __name__ == '__main__':
    run()
