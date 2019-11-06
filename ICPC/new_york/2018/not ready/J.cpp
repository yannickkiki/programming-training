#include <bits/stdc++.h>
using namespace std;
typedef pair<int, int> square;

int main() {
    const int N = 10;
    ifstream cin("J.in");

    int p=0;
    cin >> p;
    
    for(int test_idx=0; test_idx<p; test_idx++){
        int k=0;
        cin >> k;

        int board[N][N], is_blank_square[N][N];
        vector<square> blank_squares;
        
        for(int i=0; i<N; i++){
            for(int j=0; j<N; j++){
                cin >> board[i][j];
                bool is_blank_square_ = board[i][j]==-1;
                if(is_blank_square_){
                    blank_squares.push_back(make_pair(i, j));
                    board[i][j] = 0;
                }
                is_blank_square[i][j] = is_blank_square_;
            }
        }

        int cursor_idx = 0;
        
        int comp = 0;
        while (cursor_idx != blank_squares.size()){
            //if(comp++==50000) break;
            int i = blank_squares[cursor_idx].first;
            int j = blank_squares[cursor_idx].second;
            //cout << "Square: " << i << " " << j << "\n";
            if (board[i][j]==3){
                // reset and go to the previous square
                board[i][j] = 0;
                if (cursor_idx >= 1) cursor_idx -= 1;
                continue;
            }
            board[i][j] += 1;
            //cout << "Square value: " << board[i][j] << "\n";

            bool is_validated = true;

            for(int r=-1; r<=1; r++){
                for(int c=-1; c<=1; c++){
                    int current_i = i+r, current_j = j+c;
                    if ((r==0 && c==0) || current_i < 0 || current_i >= N || current_j < 0 || current_j >=N){
                        continue;
                    }
                    if(!is_blank_square[current_i][current_j]){
                        // cout << "Not blank neighbour: " << current_i << " " << current_j;
                        int val = board[current_i][current_j];
                        // cout << " ,Value " << val << "\n";
                        int number_of_remaining_blank_squares = 0;
                        int current_number_of_strokes_around = 0;
                        for (int dr=-1; dr<=1; dr++){
                            for (int dc=-1; dc<=1; dc++){
                                int dcurrent_i = current_i+dr, dcurrent_j = current_j+dc;
                                if ((dr==0 && dc==0) || dcurrent_i < 0 || dcurrent_i >= N || dcurrent_j < 0 ||       dcurrent_j >=N){
                                    continue;
                                }
                                if(is_blank_square[dcurrent_i][dcurrent_j]){
                                    if(board[dcurrent_i][dcurrent_j]==0){
                                        number_of_remaining_blank_squares += 1;
                                    }
                                    current_number_of_strokes_around += board[dcurrent_i][dcurrent_j];
                                }
                            }
                        }
                        int number_of_strokes_to_add = val - current_number_of_strokes_around;
                        // cout << "Number of strokes to add " << number_of_strokes_to_add << "\n";
                        if(number_of_strokes_to_add<number_of_remaining_blank_squares || number_of_strokes_to_add>3*number_of_remaining_blank_squares){
                            is_validated = false;
                            break;
                        }
                    }
                }
                if(not is_validated){
                    break;
                }
            }

            if(not is_validated){
                //cout << "Return at c1" << "\n";
                continue;
            }

            int number_of_remaining_blank_squares = 0, current_number_of_strokes = 0;
            for(int c=0; c<N; c++){
                if(is_blank_square[i][c] && c!=j){
                    if(board[i][c]==0){
                        number_of_remaining_blank_squares += 1;
                    }
                    current_number_of_strokes += board[i][c];
                }
            }
            
            int number_of_strokes_to_add = N - board[i][j] - current_number_of_strokes;
            is_validated = (number_of_strokes_to_add >= number_of_remaining_blank_squares) && (number_of_strokes_to_add <= 3*number_of_remaining_blank_squares);

            if(not is_validated){
            	//cout << "C2: Number of strokes to add: " << number_of_strokes_to_add << "\n";
                //cout << "Return at c2" << "\n";
                continue;
            }

            number_of_remaining_blank_squares = 0;
            current_number_of_strokes = 0;
            for(int r=0; r<N; r++){
                if(is_blank_square[r][j] && r!=i){
                    if(board[r][j]==0){
                        number_of_remaining_blank_squares += 1;
                    }
                    current_number_of_strokes += board[r][j];
                }
            }
            
            number_of_strokes_to_add = N - board[i][j] - current_number_of_strokes;
            is_validated = (number_of_strokes_to_add >= number_of_remaining_blank_squares) && (number_of_strokes_to_add <= 3*number_of_remaining_blank_squares);

            if(not is_validated){
                // cout << "C3: Number of strokes to add: " << number_of_strokes_to_add << "\n";
                //cout << "Return at c3" << "\n";
                continue;
            }

            cursor_idx += 1;
        }

        //cout << "End \n";
        
        cout << k << "\n";
        for (int i=0; i<N; i++){
            for (int j=0; j<=N-2; j++){
	            cout << board[i][j] << " ";
            }
            cout << board[i][N-1] << "\n";
        }
    }
}
