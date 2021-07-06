import json
import random
import spacy
nlp = spacy.load("en_core_web_lg")
f = open("google-large.txt", "r")
lines = f.readlines()

def overlap(w, word):
    if w in word: return True
    if word in w: return True
    return False

def my_similar(word, topn=5):
    word = nlp.vocab[word]

    queries = [
      nlp.vocab[w.strip()] for w in lines
    ]
    by_similarity = sorted(queries, key=lambda w: word.similarity(w), reverse=True)
    result = [w.lower_ for w in by_similarity[:topn+1] if not overlap(w.lower_, word.lower_)]

    return result

def lambda_handler():
    i = random.randint(0,len(lines))
    word = lines[i].strip()
    similar = my_similar(word)
    return {
        'statusCode': 200,
        'body': json.dumps({'word': word, 'similar': similar})
    }

if __name__ == "__main__":
    print(lambda_handler())