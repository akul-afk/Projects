#Creating a function to count the number of frequencies of letter in a string in decreasing order
#1 creating a blank dictionary
#2 creating a for loop to check for letter in the input
#3 storing each letter as a key
#4 creating an if statement to check number of occurrence of key(letters) in the input
#5 if letter repeats it adds 1 and if doesn't repeat it stays 1
#6 finally printing the result
def most_frequent(word):
    dict ={}
    for l in word:
        keys = dict.keys()
        if l in keys:
            dict[l] += 1
        else:
            dict[l] = 1
    return dict
word=input("Please enter a string:\n")
print("Number of frequencies of letters in word \"" +word+ "\" is: \n" +str(most_frequent(word)))



