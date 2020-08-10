#project1(mycaptain)
#Task1
num1 =input("Enter radius of the cirlce:")
print(22/7*float(num1)**2)

#task2
print("File extensions available:\"py\",\"java\",\"txt\",\"jp\",\"jpeg\"")
Fexten ={"py":"python","java":"java","txt":"text","jp":"jpeg","html":"HTML"}
filename =input("Enter filename: ")
files =filename.split(".")[-1]
print("The extension for the file is:",Fexten.get(files))





