def get_word_indices(lst: list) -> dict:
    d = {}
    for i in range(len(lst)):
        for w in lst[i].lower().split():
            d[w] = d.get(w, []) + [i]
    return d


print(get_word_indices(['Look at my horse', 'my horse', 'is amazing']))
print(get_word_indices(['Avada Kedavra', 'avada kedavra', 'AVADA KEDAVRA']))
print(get_word_indices(['This is a string', 'test String', 'test', 'string']))

# {'look': [0], 'at': [0], 'my': [0, 1], 'horse': [0, 1], 'is': [2], 'amazing': [2]}
# {'avada': [0, 1, 2],'kedavra': [0, 1, 2]}
# {'this': [0], 'is': [0], 'a': [0], 'string': [0, 1, 3], 'test': [1, 2]}
