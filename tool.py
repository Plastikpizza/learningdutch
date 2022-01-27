import json
import word2word
# import numpy as np
# from sklearn.linear_model import LinearRegression

avg = lambda x : sum(x)/len(x)

translate = word2word.Word2word("nl", "en")

with open("vocab.json", "r") as file:
    voc = json.loads(file.read())
    print(f"average of {avg(list(map(len, voc)))} unknown words per page.")
    
    # pageNumber = np.array(range(len(voc)))
    # newWords = np.array(list(map(len, voc)))
    
    # model = LinearRegression().fit(pageNumber.reshape(-1, 1), newWords.reshape(-1, 1))
    
    # print(f"[model]: you'll see {model.coef_} new words each page. {model.intercept_}")
    
    for i, page in enumerate(voc):

        # some stats:

        # print(f"page {i+1}, {len(page)} words")
        
        # The following block is great for Anki:
        # it automatically translates the words you do not know,
        # and puts them into a CSV file that Anki can parse and make
        # flash cards from for you!

        for word in page:
            try:
                a,b,c = translate(word)[:3]
                print(f"{word}\t{a}, {b}, {c}")
            except KeyError:
                print(f"{word} ... Maybe look online: https://de.pons.com/%C3%BCbersetzung/niederl%C3%A4ndisch-deutsch/{word}")