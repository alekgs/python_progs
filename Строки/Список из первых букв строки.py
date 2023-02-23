"""
st = 'Create a list of the first letters of every word in this string'
print([i[0] for i in st.split()])
"""

phrase = 'Take only the words that start with t in this sentence'
print([words for words in phrase.split() if words[0].lower() == 't'])



