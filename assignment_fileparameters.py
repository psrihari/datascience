# Example4:
# Open and Append at last
f = open("C:/example/bank.txt",mode='a')
f.write(" Added this line by opening the file in append mode ")

# Opening the file again to read
f = open("C:/example/bank.txt", "r")
print(f.read())
f.close()