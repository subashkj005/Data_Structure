class Node:
    # defining a node for tree
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


class binary_tree:
    def __init__(self):
        self.root = None

    def insertion(self, value):
        new_node = Node(value)
        # In case of empty tree
        if self.root is None:
            self.root = new_node
            return True
        # Incase of tree have an element
        temp = self.root
        # while loops runs until it gets false
        while True:
            # if the inserting value has already on the tree
            if new_node.value == temp.value:
                return False
            # if the inserting value is less than the temp value, it moves to left
            if new_node.value < temp.value:
                if temp.left is None:
                    temp.left = new_node
                    return True
                # if the left of the node is not none, moves to the left node
                temp = temp.left
            # if the inserting value is greater than the temp value, it moves to right
            else:
                if temp.right is None:
                    temp.right = new_node
                    return True
                # if the right of the node is not none, moves to the right node
                temp = temp.right

    def contains(self, value):
        temp = self.root
        # Loop runs until temp become None
        while temp is not None:
            # if value less than temp.value
            if value < temp.value:
                temp = temp.left
            # if value greater than temp.value
            elif value > temp.value:
                temp = temp.right
            # In else case, if its not greater nor lesser then it will be equal. So in
            # else case checks whether it is equal
            else:
                return True
        # Incase if value not found, temp becomes None and get out of the loop. Here it return as False.
        return False

    def min_value(self, current_node):
        while current_node.left is not None:
            current_node = current_node.left
        return current_node.value


    def delete_node(self,current_node, value):
        # if the tree is empty
        if current_node == None:
            return None
        # if the value is in the left part, recrusively goes to the left until it reaches the value
        if value < current_node.value:
            current_node.left = self.delete_node(current_node.left, value)
        # if the value is in the right part, recrusively goes to the right until it reaches the value
        elif value > current_node.value:
            current_node.right = self.delete_node(current_node.right, value)
        # In else case, value is not less or greater means its equal or found the correct node
        else:
            # if the node doesn't have any leaf nodes
            if current_node.left is None and current_node.right is None:
                return None
            # if the node have a leaf node in left, not right
            elif current_node.left is None:
                current_node = current_node.right
            # if the node have a leaf node in right, not left
            elif current_node.right is None:
                current_node = current_node.left
            # in else case, if the node have both right and left leaf nodes
            else:
                # calls the min valu function and get the minimum value
                sub_tree_min = self.min_value(current_node.right)
                # change the current node value to the minimum value
                current_node.value = sub_tree_min
                # deleteing the node that found
                current_node.right = self.delete_node(current_node.right, sub_tree_min)
        return current_node

    def main_del_node(self,value):
        self.delete_node(self.root,value)



#     -------------Traversal--------------

# I. Bredth First Search
    def bredth_first_search(self):
        current_node = self.root
        result = []
        queue = []
        # Adding the first root node to the queue
        queue.append(current_node)
        while len(queue) > 0:
            # After adding the root element from queue
            current_node = queue.pop(0)
            # "pop(0)" popping the first element of queue the result
            result.append(current_node.value)
            # after first element move to left and add that to queue
            if current_node.left is not None:
                queue.append(current_node.left)
            # After adding the left one add the right one to the queue
            if current_node.right is not None:
                queue.append(current_node.right)
            #By adding the left and right to queue, while loop again runs and this time pops the left one first and right
            #After that balance elements enter the queue as left and right order and pops to the result in the same order
        return result

# II.Depth First Order
#------------ 1. Pre-Order--------------

    def pre_order(self):
        # pre-order traversal, first appends the root value and travers to to the bottom left until its
        # node.left is none, from there it return back to the last point, from there goes to bottom right
        # until its node.right is none, and finally return back to self.root and run same way on the right side.
        result = []
        def traversal(current_node):
            # First append the value
            result.append(current_node.value)
            # Travers through bottom left
            if current_node.left is not None:
                traversal(current_node.left)
            # if left is none then goes to right
            if current_node.right is not None:
                traversal(current_node.right)

        traversal(self.root)
        return result

#------------ 2. Post-Order--------------
    def post_oder(self):
        result = []
        # Travers to the bottom left upto where node.left and node.right is none and then
        # append the value, return back to last top point and look for right and do the same
        # thing and goes to right and bottom left, repeats the same pattern and finally appends
        # the self.root

        def traversal(current_node):
            # traverse to bottom right
            if current_node.left is not None:
                traversal(current_node.left)
            #traverse to right when left is none
            if current_node.right is not None:
                traversal(current_node.right)
            # Finally appends the node.value
            result.append(current_node.value)
        traversal(self.root)
        return result

#------------ 3. In-Order--------------

    def in_order(self):
        result = []
        def traverse(current_node):
            if current_node.left is not None:
                traverse(current_node.left)
            result.append(current_node.value)
            if current_node.right is not None:
                traverse(current_node.right)
        traverse(self.root)
        return result



# s = binary_tree()
# s.insertion(47)
# s.insertion(21)
# s.insertion(76)
# s.insertion(18)
# s.insertion(27)
# s.insertion(52)
# s.insertion(82)

s = binary_tree()
s.insertion(80)
s.insertion(50)
s.insertion(90)
s.insertion(40)
s.insertion(60)
s.insertion(85)
s.insertion(100)
s.insertion(30)
s.insertion(42)
s.insertion(55)
s.insertion(62)
s.insertion(83)
s.insertion(86)
s.insertion(92)
s.insertion(105)

print(s.bredth_first_search())
s.main_del_node(90)
print(s.bredth_first_search())

















