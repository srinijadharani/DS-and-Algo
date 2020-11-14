class TreeNode:
  def __init__(self, data):
    self.data = data
    self.children = []
    self.parent = None # this stores the parent of TreeNode.
  
  def add_child(self, child):
    child.parent = self # child is an instance of TreeNode class and now self will become the parent of this child object
    self.children.append(child) # add the child element into children list
  
  def build_product_tree():
    root = TreeNode("Electronics")

    laptop = TreeNode("Laptop")
    laptop.add_child(TreeNode("Asus"))
    laptop.add_child(TreeNode("Lenovo"))
    laptop.add_child(TreeNode("MacBook"))

    cell = TreeNode("Cell Phone")
    cell.add_child(TreeNode("Redmi"))
    cell.add_child(TreeNode("Samsung"))
    cell.add_child(TreeNode("iPhone"))

    tv = TreeNode("Television")
    tv.add_child(TreeNode("LG"))
    tv.add_child(TreeNode("Sony"))

    root.add_child(laptop)
    root.add_child(cell)
    root.add_child(tv)

    return root