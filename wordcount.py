from sys import argv
script, filename = argv

# open file and return as a string we can work with
f = open(filename)
text = f.read()
f.close()

# create a list of strings from text document
#replaced = ['!', '?']
#for replacements in replaced:
#	text = text.replace(replaced," ")
#print text

list_of_strings = new_text.split()
for string in list_of_strings:
	string.strip()

# build empty dictionary for key:word, value:occurances
word_dict = {}

# initialize key values to 0
key_val = 0

# read each word 
for item in list_of_strings:
	word_dict.setdefault(item, key_val) 
	value = word_dict[item]
	word_dict[item] = value + 1

print word_dict




