file_handle = open("pelican.txt", "a")
# append the line to te file using the write method
with open("pelican.txt", "a") as file_handle:
    file_handle.write("A wonderful bird is the pelican\n")
    file_handle.write("His bill holds more than his belican\n")

my_list = ["He can take in his beak,\n", "Enough food for a week, \n",
           "But im damned if i see how the Helican. \n"]
with open("pelican.txt", "a") as file_handle:
    file_handle.writelines(my_list)
file_handle.close()