"""
 Reverse a linked list
 head could be None as well for empty list
 Node is defined as

 class Node(object):

   def __init__(self, data=None, next_node=None):
       self.data = data
       self.next = next_node

 return back the head of the linked list in the below method.
"""

def Reverse(head):
    if head==None or head.next==None: return head
    curr=head
    prev=None
    tail=curr.next
    curr.next=prev
    while tail.next!=None:
        prev=curr
        curr=tail
        tail=curr.next
        curr.next=prev
    head=tail
    head.next=curr
    return head


def Reverse(head):
    curr=head
    prev=None
    nextN=None
    while curr:
        nextN=curr.next
        curr.next=prev
        prev=curr
        curr=nextN
    return prev


def Reverse(head):
    if not head.next: return head
    else:
        new_head=Reverse(head.next)

    head.next.next=head
    head.next=None
    return new_head