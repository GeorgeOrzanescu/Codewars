
def top_3_words(text):
    wrds = {}
    for p in r'!"#$%&()*+,./:;<=>?@[\]^_`{|}~-':
        # print(p)
        text = text.replace(p, ' ')
    for w in text.lower().split():
        if w.replace("'", '') != '':
            wrds[w] = wrds.get(w, 0) + 1
    return [y[0] for y in sorted(wrds.items(), key=lambda x: x[1], reverse=True)[:3]]



print(top_3_words("a a a  b  c c  d d d d  e e e e e")) #["e", "d", "a"]
print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"))
print(top_3_words("  //wont won_'t won_'t "))
print(top_3_words("  '  ' "))
print(top_3_words("""In a_ village of La Mancha, the name of which I have no desire to call to mind, there lived not long since one of those gentlemen that keep a lance
in the lance-rack, an old buckler, a_ lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a_ salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three_quarters of his income."""))