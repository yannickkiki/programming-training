#include <iostream>
#include <chrono>
#include <vector>
#include <stdio.h>
#include <set>
#include <algorithm>
#include <string>
#include <sstream>
#include <iterator>
#include <cmath>

#define DATASET_IN "b.in"
#define DATASET_OUT "b.out"
#define DATASET_OUT_NEW "b.out_new"


using namespace std;

struct Pizza {
    int idx, n_ingredients;
    vector<string> ingredients;

    Pizza(int idx_, vector<string> &ingredients_){
        idx = idx_;
        ingredients = ingredients_;
        n_ingredients = ingredients.size();
    }
};


struct Delivery {
    int team_size, n_ingredients;
    vector<int> pizzas_ids;

    Delivery(vector<Pizza> &pizzas_){
        team_size = pizzas_.size();
        set<string> ingredients;
        for(auto pizza: pizzas_){
            pizzas_ids.push_back(pizza.idx);
            for (auto ingredient: pizza.ingredients){
                ingredients.insert(ingredient);
            }
        }
        n_ingredients = ingredients.size();
    }
};

class Submission {
    vector<Delivery> deliveries;

    public:
        Submission(vector<Delivery> &deliveries_){
            deliveries = deliveries_;
        }

        void create_submission_file() {
            int score = 0;

            freopen(DATASET_OUT_NEW, "w", stdout);
            printf("%d\n", (int) deliveries.size());
            for (auto delivery: deliveries){
                int team_size = delivery.pizzas_ids.size();

                ostringstream oss;
                copy(delivery.pizzas_ids.begin(), delivery.pizzas_ids.end() - 1, ostream_iterator<int>(oss, " "));
                oss << delivery.pizzas_ids.back();
                string pizzas_ids_str = oss.str();

                printf("%d %s\n", team_size, pizzas_ids_str.c_str());
                score += pow(delivery.n_ingredients, 2);
            }
            printf("Score: %d\n", score);
        }
};


int main() {
    auto starttime = chrono::high_resolution_clock::now();

    freopen(DATASET_IN, "r", stdin);

    int n_pizzas, n_teams_of_2, n_teams_of_3, n_teams_of_4;
    cin >> n_pizzas >> n_teams_of_2 >> n_teams_of_3 >> n_teams_of_4;

    vector<Pizza> pizzas_all;
    for (int pizza_idx = 0; pizza_idx < n_pizzas; ++pizza_idx) {
        int n_ingredients;
        cin >> n_ingredients;
        vector<string> ingredients;
        string ingredient;
        for (int i = 0; i < n_ingredients; ++i) {
            cin >> ingredient;
            ingredients.push_back(ingredient);
        }
        pizzas_all.push_back(Pizza(pizza_idx, ingredients));
    }

    freopen(DATASET_OUT, "r", stdin);

    int n_deliveries;
    cin >> n_deliveries;

    vector<Delivery> deliveries;
    for (int delivery_idx = 0; delivery_idx < n_deliveries; ++delivery_idx){
        int n_pizzas;  // also corresponds to team size
        cin >> n_pizzas;
        vector<Pizza> pizzas;
        int pizza_id;
        for (int i = 0; i < n_pizzas; ++i){
            cin >> pizza_id;
            pizzas.push_back(pizzas_all[pizza_id]);
        }
        deliveries.push_back(Delivery(pizzas));
    }

    for (int i = 0; i < 10; ++i){
        for (int j = 0; j < n_deliveries; ++j){
            if(i==j){
                continue;
            }

            vector<int> pizzas_ids_ij;
            pizzas_ids_ij.insert(pizzas_ids_ij.end(), deliveries[i].pizzas_ids.begin(), deliveries[i].pizzas_ids.end());
            pizzas_ids_ij.insert(pizzas_ids_ij.end(), deliveries[j].pizzas_ids.begin(), deliveries[j].pizzas_ids.end());
            sort(pizzas_ids_ij.begin(), pizzas_ids_ij.end());

            do {
                vector<int> new_pizzas_ids_i(pizzas_ids_ij.cbegin(), pizzas_ids_ij.cbegin() + deliveries[i].team_size);
                vector<int> new_pizzas_ids_j(pizzas_ids_ij.cbegin() + deliveries[i].team_size , pizzas_ids_ij.cend());

                vector<Pizza> new_pizzas_i;
                for (auto pizza_idx: new_pizzas_ids_i){
                    new_pizzas_i.push_back(pizzas_all[pizza_idx]);
                }
                auto new_delivery_i = Delivery(new_pizzas_i);

                vector<Pizza> new_pizzas_j;
                for (auto pizza_idx: new_pizzas_ids_j){
                    new_pizzas_j.push_back(pizzas_all[pizza_idx]);
                }
                auto new_delivery_j = Delivery(new_pizzas_j);

                int current_score_ij = pow(deliveries[i].n_ingredients, 2) + pow(deliveries[j].n_ingredients, 2);
                int new_score_ij = pow(new_delivery_i.n_ingredients, 2) + pow(new_delivery_j.n_ingredients, 2);

                if(new_score_ij > current_score_ij){
                    deliveries[i], deliveries[j] = new_delivery_i, new_delivery_j;
                }
            } while (next_permutation(pizzas_ids_ij.begin(), pizzas_ids_ij.end()));
        }
    }

    auto submission = Submission(deliveries);
    submission.create_submission_file();

    auto endtime = chrono::high_resolution_clock::now();
    chrono::duration<double> elapsed_seconds = endtime - starttime;
    cout << "Execution time in seconds: " << elapsed_seconds.count() << endl;
}
