# Write your code here :-)
def commacode(words):
    words = list(map(str, words))
    if words == []:
        return ','
    return ' ,'.join(words[:-1]) + ', and ' + words[-1]


result = commacode(['apples', 'bananas', 'tofu', 'cats'])
print(result)
