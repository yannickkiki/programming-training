#include <iostream>

using namespace std;

struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    explicit ListNode(int x) : val(x), next(nullptr) {}
//    ListNode(int x, ListNode *next) : val(x), next(next) {}
};


// todo: review this, not working as expected (but the solution is working Solution.getDecimalValue)
ListNode* build_linked_list(int* arr, int n) {
    ListNode root;
    ListNode node;
    for (int i = 0; i < n; i++) {
        ListNode new_node (arr[i]);
        node.next = &new_node;
        if (i==0) {
            root.next = &new_node;
        }
        node = new_node;
    }
    return root.next;
}


class Solution {
    public:
        int getDecimalValue(ListNode* head) {
            int result = head->val;
            head = head->next;
            while(head) {
                result = result * 2 + head->val;
                head = head->next;
            }
            return result;
        }
};

int main() {
    Solution s;
    int arr[] = {1, 0, 1};
    ListNode* head = build_linked_list(arr, 3);
    int value = s.getDecimalValue(head);
    bool result = value == 5 ? "Success": "Failure";
    cout << result << endl;
}
