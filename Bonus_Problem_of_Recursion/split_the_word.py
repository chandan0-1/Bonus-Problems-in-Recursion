def split_the_word(s,l,output):
	for x in l:
		if s.startswith(x):
			output.append(x)
			split_the_word(s[len(x):],l,output)
	return output
print(split_the_word("themanran",["the","man","ran"],[]))  #Test case 1
print(split_the_word("ilovedogsJohn",["i","am","a","dogs","loved","ogs","ohn","John"],[]))   #Test case 2
print(split_the_word("themanran",["clown","man","ran"],[]))  #Test case 3