# Given a singly linked list and an integer k, remove the kth last 
# element from the list. k is guaranteed to be smaller than the 
# length of the list.

# The list is very long, so making more than one pass is prohibitively 
# expensive.

# Do this in constant space and in one pass.

#Traverse the whole list. Assign index-val pairs to a hash map, constantly
#increment the length variable by 1.

#Once you have the length (self.next = None), subtract k + 1 to get the preceding
#node, and k to get the node to remove.
# set k+1.next to k-1, and k.next to None.