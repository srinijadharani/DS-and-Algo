# **Tree Data Structures** <br>
A tree DS has a root, branches, and leaves. All the children of one node are independent of of the children of another node.Each leaf node is unique. In a file system, directories or folders are structured as trees.

Trees are non-linear data structures. A non-linear data structure has multiple layers, in a hierarchical order. Trees are unidirectional (top to bottom).

### **Terminology:**<br>
1. Node: It is a fundamental part of a tree. Nodes store information. 
2. Edge: An edge connects two nodes to show that there is a relation between them. Every node is connected by exactly one incoming edge from another node, except the root node which has none. But each node may have sevearl outgoing edges.
3. Root: It is the only node in the tree that has no incoming edges. It has no parent node.
4. Path: A path is an ordered list of nodes that are connected by edges. It's a sequence of consecutive edges from source node to the destination node. 
5. Children: The node below a given node connected by its edges downwards is called its child node. These have incoming edges, and maybe outgoing edges.
6. Siblings: Children of the same parent node are said to be siblings.
7. Subtree: A set of nodes and edges comprised of a parent node and all descendants of that parent is called a subtree.
8. Leaf Node: Leaf node is a node that has no children. These are also called external nodes.
9. Non-Leaf Node: Non-Leaf nodes have at least one child node. These are also called internal nodes.
10. Traversing: Passing through nodes in a sequential order is called traversing the tree.
11. Ancestor: Any predecessor node on the path from root node to that particular node is called the ancestor node to that node.
12. Descendant: Any successor node on the path from that particular node to the leaf node is called the descendant node to that node.
13. Degree: Degree of a node is the number of children to that node. Degree of a tree is the maximum degree among all nodes.
14. Depth: Depth of a node is the length of path from root to that node. Depth of root node is always 0.
15. Height: Height of a node is the number of edges in the longest path from that node to a leaf. Height is the opposite of depth. The height and depth of a node may or may not be same.<br>
    ```Height of a tree = Height of its root node.```
16. Level: The number of edges from root to the given node is called level.<br>
    ```Level of the tree = Height of the tree```<br>
    ```Level of a node ≠ Height of a node```<br>
    ```Level of a tree = Depth of a node```<br>

### **Important points to note:**
1. If a tree has n nodes, there will be (n-1) edges.
2. Trees are acyclic.
3. Applications of trees:<br>
    1. Store hierarchical data, like folder structure, organizational structre, XML/HTML data.
    2. Binary search trees allow fast search, insertion, deletion on sorted data. They also help find the closest item to a given item.
    3. Heap is a tree DS which is implemented using arrays and used to implement priority queues.
4. Trees are recursive data structures where a child node is another tree on itself.
