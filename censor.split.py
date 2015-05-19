def censor(text_string,word):
    text = text_string.split()
    for i in text:  #iterate through list
        if i == word:  #compare list
            idx = text.index(i)  #get index
            text.pop(idx)  #pop away element of that index
            text.insert(idx,"*"*len(word))   #insert **** in that index

    

    return " ".join(text)  #print each element with a space in between

text = "hey hey hey"
word = "hey"
print censor(text, word)
