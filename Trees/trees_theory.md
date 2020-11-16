# **Tree Data Structures** <br>
A tree DS has a root, branches, and leaves. All the children of one node are independent of of the children of another node. Each leaf node is unique. In a file system, directories or folders are structured as trees.

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

**Representation of a tree in linked lists:** (Fig.1)

![memory_repr_BT.png](data:image/png;base64,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)Source: OpenGenus IQ <br><br>

### **Important points to note:**
1. If a tree has n nodes, there will be (n-1) edges.
2. Trees are acyclic.
3. Applications of trees:<br>
    1. Store hierarchical data, like folder structure, organizational structre, XML/HTML data.
    2. Binary search trees allow fast search, insertion, deletion on sorted data. They also help find the closest item to a given item.
    3. Heap is a tree DS which is implemented using arrays and used to implement priority queues.
4. Trees are recursive data structures where a child node is another tree on itself.

## **Binary Trees:**
A binary tree is a tree in which each node can have atmost 2 children (so, it can have 0, or 1, or 2 children).

### **Properties of a binary tree:**
1. At level 0 in a binary tree, the maximum nodes possible are 1. At level 1, the maximum nodes possible are 2. At level 2, 4 are possible. So, the maximum number of nodes present in level (i) = 2^i.
2. Maximum number of nodes present at height (h) = 2^(h+1)-1
3. Minimum number of nodes present at height (h) = h+1
4. Maximum height with n nodes, h = n-1
5. Minimum height with n nodes, h = log(n+1)1

### **Types of Binary Trees:**
1. Full or, Proper or, Strict Binary Tree
2. Complete Binary Tree
3. Perfect Binary Tree
4. Degenerate Binary Tree

#### **Full Binary Tree:** 
Each node has either 0 or 2 child nodes. A full binary tree is a binary tree in which all nodes except leaf nodes have 2 children.
In a full binary tree, number of lead nodes is one greater than the number of internal nodes. So, if l is the number of leaf nodes and i is the number of internal nodes, l = i+1

**Properties of a full binary tree:**
1. Maximum number of nodes with height (h), n = 2^(h+1)-1 (this is the same as the maximum nodes for a basic binary tree 0).
2. Minimum number of nodes whith height (h), n = 2h+1
3. Minimum height, h = log(n+1)-1
4. Maximum height, h = (n-1)/2 where n is the number of nodes.

#### **Complete Binary Tree:**
A binary tree is a complete binary tree if all the levels arae completely filled except possibly the last level and the last level has all nodes as *left* as possible.
Tip: Fill the nodes from left to right. Only if all the left positions are complete/occupied, go right.

***All full binary trees are complete binary trees, but not all complete binary trees are full.***

**Properties of complete binary trees:**
1. Maximum nodes of height (h) = 2^(h+1)-1
2. Minimum nodes of height (h) = 2^h
3. Minimum height = log(n+1)-1
4. Maximum height = log(n)

#### **Perfect Binary Tree:**
If all internal nodes have 2 child nodes each and all leaves are at the same level, then the binary tree is called a perfect binary tree.
 
***Every perfect binary tree can be a full and a complete binary tree. But the other way isn't true.***

#### **Degenerate Binary Tree:**
A binary tree in which all internal nodes have one child each is called a degenerate tree. It could be either left-skewed binary tree or a right-skewed binary tree.

## **Binary Tree Traversals**
1. Pre-order
2. In-order
3. Post-order

Consider the following binary tree: (Fig.2)
![traversal.png](data:image/png;base64,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)

### **Pre-order Traversal:**
**Traversal Order**: Root -> Left -> Right
1. Check if the current node is empty/null.
2. Display the data part of the root or the current node.
3. Traversethe left subtree by recursiverly calling the pre-order function.
4. Traverse the right subtree by recursively calling the pre-order function.

**Pre-order traversal for Fig.2:** A B D E G H C F I

### **In-order Traversal:**
**Traversal Order**: Left -> Root -> Right
1. Check if the current node is empty/null.
2. Traversethe left subtree by recursiverly calling the pre-order function.
3. Display the data part of the root or the current node. 
4. Traverse the right subtree by recursively calling the pre-order function.

**Pre-order traversal for Fig.2:** D B G E H A C F I

### **Post-order Traversal:**
**Traversal Order**: Left -> Right -> Root
1. Check if the current node is empty/null.
2. Traversethe left subtree by recursiverly calling the pre-order function.
3. Traverse the right subtree by recursively calling the pre-order function.
4. Display the data part of the root or the current node. 

**Pre-order traversal for Fig.2:** D G H B E I F C A
