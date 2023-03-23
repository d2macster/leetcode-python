from typing import Optional
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        new_head : Optional[ListNode] = None
        counter = 0
        first_node_in_sequence: Optional[ListNode] = None
        prev_node: Optional[ListNode] = None
        
        while head is not None:
            cur_head = head
            head = head.next

            if first_node_in_sequence is None:
                first_node_in_sequence = cur_head
                counter = 1
                continue
            
            if first_node_in_sequence.val == cur_head.val:
                counter += 1
                continue

            if counter == 1:
                if prev_node is None:
                    prev_node = first_node_in_sequence
                    new_head = first_node_in_sequence
                    first_node_in_sequence.next = None
                else:
                    prev_node.next = first_node_in_sequence
                    prev_node = first_node_in_sequence
                    first_node_in_sequence.next = None
            first_node_in_sequence = cur_head
            counter = 1

        if counter == 1:
            if prev_node is None:
                prev_node = first_node_in_sequence
                new_head = first_node_in_sequence
                first_node_in_sequence.next = None
            else:
                prev_node.next = first_node_in_sequence
                prev_node = first_node_in_sequence
                first_node_in_sequence.next = None

        return new_head