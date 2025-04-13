
""" 
Function to get book text given a url path.
"""
def get_book_text(path_to_file):
    file_contents= ""
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

"""
Function to get number of words given a URL path.  
"""
def get_num_words(content):
     return len(content.split())
    # content_count = len(get_book_text(path_to_file).split)
    # print(content_count)
    # return content_count

""" 
Function to get character occurences.
"""
def get_char_occurences(content):
    occur = {}
    for c in content:
        lowered = c.lower()
        val = occur.get(lowered)
        if val == None:
            occur[lowered] = 1
        else:
            occur[lowered] += 1

    return occur

"""
Function to get character occurence
Takes in a dictionary of content as arg
Returns a sorted list of dictionary
"""
def get_charOnly_Occurence(contentDict):
    char_sorted = []
    for i in contentDict.items():
         if (i[0].isalpha()):
            char_sorted.append({"char" : i[0], "num" : i[1]})
    char_sorted.sort(reverse=True, key=sort_on)
    return char_sorted

""" 
Function to return the number value of the dict
"""            
def sort_on(dict):
    return dict["num"]            


# for testing only 
if __name__ == "__main__":
    get_charOnly_Occurence({"b":1, "c": 2})
    seq = [1, 2, 3]