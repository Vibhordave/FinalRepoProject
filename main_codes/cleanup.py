import re  # Required for pattern matching
import os
arr = []  # Array to store the lines of the file
# Open the file
current_dir = os.path.dirname(os.path.abspath(__file__))
sibling_dir = os.path.join(current_dir, "..", "Qdata")
txt_dir = os.path.join(current_dir, "..", "Text_files")
qu_compilation_path = os.path.join(txt_dir, "leetcode.txt")
qu_final_compilation=os.path.join(txt_dir, "leetcode_problemset.txt")
with open(qu_compilation_path, "r") as file:
    # Read each line one by one
    for line in file:
        # Process the line
        arr.append(line)  # You can perform any operation on the line here


def remove_elements_with_pattern(array, pattern):
    new_array = []
    for element in array:
        if pattern not in element:
            new_array.append(element)
        else:
            pass
    return new_array

def initials(array):
    new_array=[]
    for ele in array:
        ele = "https://leetcode.com" + ele
        new_array.append(ele)
    return new_array


arr = remove_elements_with_pattern(arr, "/solution")
arr=initials(arr)
print(len(arr))
arr = list(set(arr))

with open(qu_final_compilation, 'w') as f:
    # Iterate over each link in your final list
    for j in arr:
        # Write each link to the file, followed by a newline
        f.write(j)