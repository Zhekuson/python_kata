# Hash tables  

## Complexity
|        | Average | Worst  |
| ---    | :---:   | :---:  |
| Space  | `O(n)`  | `O(n)` |
| Search | `O(1)`  | `O(n)` |
| Insert | `O(1)`  | `O(n)` |
| Delete | `O(1)`  | `O(n)` |
---  
## When to use 

- You don't care about sorted structure and about iterating many times over it
- Your data is not complex and easy hashable 

## Theory
Hash table is an associative array (maps keys to values)  

A hash table uses a hash function to compute an index, also called a hash code, into an array of buckets or slots,
from which the desired value can be found. During lookup, the key is hashed and the resulting hash indicates where the corresponding value is stored

The efficiency actually depends on **hash function**   
Perfect hash function has 2 properties: 
1) computed fast 
2) has low rate of **collisions**    

That's why function should provide uniform distribution  
**Load factor** - property of hash table that shows loading coefficient
<img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\bg_white&space;\inline&space;\alpha&space;=&space;n/k"/>
  
where **n** is the number of entries occupied in the hash table
and **k** is the number of possible outputs (buckets) of hash function

Load factor should not approach 1, because then performance becomes much worse.  
For example, search takes <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\bg_white&space;\inline&space;\Theta(1&plus;\alpha)"/>

Collision problem is usually solved via **chaining** (linked lists of elements with the same hash value)








## Tricky moments, Python features and fun facts
Implementation of Hash table is available in standart library via `dict`
By default, Python is using open hashing based on a primitive polynomial over <img src="https://latex.codecogs.com/png.image?\dpi{150}&space;\bg_white&space;\inline&space;\mathbb{Z}_{2}"/>


A hash table is a contiguous vector of records, whose slots come in three
flavors:

1. Slots with key+value pairs.  Call these **citizens**.
2. Not-yet-used slots.  Call these **virgins**.
3. Slots that were once citizens, but whose key got deleted, and where
   another key+value pair hasn't yet overwritten the slot.  Call these
   **turds**.
  

Python resizes the table when the number of **virgins** falls **below a third** of
the total number of slots (doubling size)

_**1,073,741,824**_ - is the maximum number of elements by now in dict

To avoid thrashing when a mix of additions and deletions are made when the
table is near a resize threshold, Python doesn't actually check the # of
virgins after a delete (in effect, it assumes you'll soon be replacing the
turds with citizens again).  So, curiously enough, deleting a key *never*
shrinks the table.  A long sequence of deletes followed by an add may shrink
it, though.  A **way to force possible shrinkage** without adding a key is:

```python
dict = dict.copy()
```

`dict.copy()` always returns a **turd-free** dictionary, of the smallest
power-of-2 size that leaves at least a third of the slots virgin.
