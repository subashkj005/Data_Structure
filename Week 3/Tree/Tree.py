class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None

    def add_child(self, child):
        child.parent = self
        self.children.append(child)

    def print_tree(self):
        print(self.data)
        for child in self.children:
            child.print_tree()

    def get_level(self):
        level = 0
        p = self.parent
        while p:
            level +=1
            p = p.parent
        return level

def build_tree():
    root = TreeNode("----Vehicles----")

    car = TreeNode("--Car--")
    car.add_child(TreeNode("* Toyoto"))
    car.add_child(TreeNode("* Nissan"))
    car.add_child(TreeNode("* Lamborghini"))

    bike = TreeNode("--Bike--")
    bike.add_child(TreeNode("* Aprila"))
    bike.add_child(TreeNode("* KTM"))
    bike.add_child(TreeNode("* Ducati"))

    root.add_child(car)
    root.add_child(bike)


    root.print_tree()





build_tree()

