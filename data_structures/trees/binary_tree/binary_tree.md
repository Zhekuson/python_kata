# Binary (search) tree

## Complexity
|        |  Average   | Worst  |
|--------|:----------:|:------:|
| Space  |   `O(n)`   | `O(n)` |
| Search | `O(log n)` | `O(n)` |
| Insert | `O(log n)` | `O(n)` |
| Delete | `O(log n)` | `O(n)` |
| Access | `O(log n)` | `O(n)` |
---  
## When to use 
The main goal - you want to build easy data structure and: 
- You want to keep your values **sorted** and **easily accessible** (log n) 

Easy to create, hard to support non-degenerate structure  
So don't use them, if you already have structures like AVL or RBTree 

## Theory
Summary:
- Rooted binary tree
- Each node contains value
- Left subtree always contains elements **less or equal**
- Right subtree always contains elements **greater**

## Tricky moments, Python features and fun facts

In Python, package _binarytree_ contains simple BST implementation.

The worst thing about BST is its degenerate form. If you keep inserting increasing sequence into BST, 
it will grow one big subtree with large depth, so accessing it (and other operations) will become **O(n)** instead **O(log n)**

