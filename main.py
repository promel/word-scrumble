import random

words = ['tweet','to','each','Shakespeare','named','as','think','of','William','by','try','sentence','a','a','sent','celebrity']

sentences = []
LIMIT = len(words)
for x in range(100000):
    picked = []
    random_words = []
    while(True):
       pick = random.randint(0,LIMIT - 1)
    #    print(pick)

       if pick not in picked:
        #    words[pick]
           picked.append(pick)
           random_words.append(words[pick])
        #    print('Picked word',)
           if len(picked) == LIMIT:
                break
    if random_words[1] == 'to':
        sentences.append(random_words)
    # print(sentences)


regular_sentences = [' '.join(sentence) for sentence in sentences]

for sentence in regular_sentences:
    if 'by William Shakespeare' in sentence:
        with open('file.txt', "a+") as f:
            f.write(sentence + '\n\n')
