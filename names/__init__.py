import time
from names.bst import BinarySearchTree

start_time = time.time()
# Open Names_1
f = open('names_1.txt', 'r')
names_1 = f.read().split('\n')
f.close()
# OPen Names_2
f = open('names_2.txt', 'r')
names_2 = f.read().split('\n')
f.close()
# Initialize holder for duplicate names
duplications = []
# Create initial BST with first name in names_1
bst = BinarySearchTree(names_1[0])
# Add all names into the BST
# Skipping the 0th index
# O(n)
for name in names_1[1:]:
    bst.insert(name)
# Iterate through names_2
# Check if exist's in BST
# Add to duplicates list if found
# O(n)
for name in names_2:
    if bst.contains(name):
        duplications.append(name)
# O(n2)
# for name_1 in names_1:
#     for name_2 in names_2:
#         if name_1 == name_2:
#             duplicates.append(name_1)
end_time = time.time()
print(f"{len(duplications)} duplicates:\n\n{', '.join(duplications)}\n\n")
print(f"runtime: {end_time - start_time} seconds")
