def group_by_rhyme(words):
    rhymes = {}
    for word in words:
        rhyme = word[-2:]
        if rhyme in rhymes:
            rhymes[rhyme].append(word)
        else:
            rhymes[rhyme] = [word]
    return list(rhymes.values())


words = ['ana', 'banana', 'carte', 'arme', 'parte']
result = group_by_rhyme(words)
print(result)