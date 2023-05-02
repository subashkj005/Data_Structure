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

    # to find the minimum value in a node tree
    def min_value(self):
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

    # finding the closest value to the specific value
    def closest_value(self,target):
        current = self.root
        closest = current.value
        while current is not None:
            # if it get the lesser closest value than before, change the closest with current.value
            if abs(current.value - target) < abs(closest - target):
                closest = current.value
            # if target is greater, then moves to right
            if target > current.value:
                current = current.right
            # if target is lesser, then moves to left
            else:
                current = current.left
        print('\nClosest value :', closest)






s = binary_tree()
s.insertion(47)
s.insertion(21)
s.insertion(76)
s.insertion(18)
s.insertion(27)
s.insertion(52)
s.insertion(82)
# print(s.in_order())
# s.main_del_node(18)
# print(s.in_order())
# s.closest_value(50)
s.closest_value(19)




