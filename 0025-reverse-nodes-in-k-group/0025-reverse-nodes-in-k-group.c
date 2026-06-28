/**
 * Definition for singly-linked list.
 * struct ListNode {
 *     int val;
 *     struct ListNode *next;
 * };
 */
struct ListNode* reverseKGroup(struct ListNode* head, int k) {
    struct ListNode dummy;
    dummy.next = head;
    struct ListNode *prevGroup = &dummy;

    while (1) {
        // Check if there are at least k nodes left
        struct ListNode *kth = prevGroup;
        for (int i = 0; i < k; i++) {
            kth = kth->next;
            if (!kth)
                return dummy.next;
        }

        struct ListNode *groupNext = kth->next;

        // Reverse the group
        struct ListNode *prev = groupNext;
        struct ListNode *curr = prevGroup->next;

        while (curr != groupNext) {
            struct ListNode *temp = curr->next;
            curr->next = prev;
            prev = curr;
            curr = temp;
        }

        // Reconnect the reversed group
        struct ListNode *temp = prevGroup->next;
        prevGroup->next = kth;
        prevGroup = temp;
    }

    return dummy.next;
}