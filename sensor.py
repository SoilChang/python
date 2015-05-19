def censor(text_string, word_string):
    text = []
    for i in text_string:
        text.append(i)
    word = []
    for i in word_string:
        word.append(i)
    
    for i in range(len(text)):
        #anchor at the first letter 
        if text[i] == word[0] and  i+len(word) <= len(text): # out of bound
            
            found = True
            for j in range(1,len(word)):  
                if text[i+j] != word[j]:
                    found = False
                    break
            if found:
                for k in range(len(word)):
                    text[i+k] = "*"
    return "".join(text)
            
text1 = "hey hey hey"
word1 = "hey"
print censor(text1, word1)
