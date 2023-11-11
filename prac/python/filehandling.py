print("File handling")

# only write the file and override the existing content of the file 
# f = open("test.txt","w")
# f.write("test")
# this content adding in the new line of the file and not override the file 
# f = open("test.txt","a")
# f.write("This is the new text\n")

# file open to the with block and the y will handle file file and self close the file 

with open("test.txt") as f:
    # return the all file line in the list format 
    a= f.readlines()
    print(a)

