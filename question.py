# given a list of words, group them into sets of anagrams
# example ["eat","tea","tan","ate","nat","bat"] to [["eat", "tea","ate"],["tan","nat"],["bat"]]


names = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(names)

result_dict = {} 

for new in names:

    new_words = "".join(sorted(new)) 
    key = new_words 
    word = new 

    if key not in result_dict: 
        result_dict[key] = []

    result_dict[key].append(word)
    
ang = list(result_dict.values()) 
print(ang)