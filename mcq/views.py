from django.shortcuts import render
#import spacy
import sys
#import re
import random
#from gensim.models import KeyedVectors
#import wikipedia
import json


"""# Create your views here.
def mcq(request):
    sys.stdout.reconfigure(encoding='utf-8')
    nlp = spacy.load("ja_core_news_sm")

    # Japanese sentence
    def read_txt_file(file_path):
        try:
            with open(file_path, 'r', encoding='utf-8') as file:
                return file.read()
        except FileNotFoundError:
            return None
    
    # Function to pick a random sentence
    def get_random_sentence(text):
        sentences = text.split("。") 
        sentences = [s.strip() for s in sentences if s.strip()] 
        return random.choice(sentences)

    # Function to extract verbs from a sentence
    def extract_verbs(sentence, nlp):
        doc = nlp(sentence)
        verbs = [token.text for token in doc if (token.pos_ == "VERB") and (len(token.text) > 1)]
        return verbs

    sentences = read_txt_file('mcq\\text.txt')
    word_vectors = KeyedVectors.load_word2vec_format("mcq\\vector\\cc.ja.300.vec", encoding='utf8', binary=False, limit = 10000)

    # Def chosen one:
    def choose(random_sentence, verbs):
        chosen_one  = verbs[random.randint(1,len(verbs))-1]
        q = random_sentence.replace(chosen_one, "____")
        return chosen_one, q

    # Function to get similar words for a target word
    def get_similar_words(target_word, num_similar=3, threshold=0.8):
        if target_word not in word_vectors:
            return None
        similar_words = [
            word for word, similarity in word_vectors.most_similar(target_word, topn=15) if similarity < threshold
        ]        
        # Ensure enough similar words are available
        if len(similar_words) < num_similar:
            return None
        # Pick three similar words
        chosen_similar_words = random.sample(similar_words, num_similar)
        chosen_similar_words += [target_word]
        random.shuffle(chosen_similar_words)
        return chosen_similar_words
    # Main logic
    while True: 
        random_sentence = get_random_sentence(sentences)
        if random_sentence:
            verbs = extract_verbs(random_sentence, nlp)
            if len(verbs) > 0:
                break
    target_verb, sen_sen = choose(random_sentence, verbs)
    simi = get_similar_words(target_verb, num_similar=3, threshold=0.7)

    return render(request, "mcq/index.html", {"sentence": random_sentence, "verbs": target_verb, "simi": simi, "sen_sen": sen_sen})


def index(request):
    random_number = random.randint(1, 100)  # Generate a random number between 1 and 100
    return render(request, 'mcq/index.html', {'random_number': random_number})


# Create your views here.
def mcq_wiki(request):
    sys.stdout.reconfigure(encoding='utf-8')
    nlp = spacy.load("ja_core_news_sm")
    wikipedia.set_lang("ja")
     
    # Function to pick a random sentence
    def get_random_sentence(text):
        sentences = text.split("。") 
        sentences = [s.strip() for s in sentences if s.strip()] 
        return random.choice(sentences)
    
    def getRandomWords(sentence):
        doc = nlp(sentence)
        tagging_list = ["NOUN", "VERB", "ADJ"] # , "SCONJ", "ADP"
        word = [token.text for token in doc if (token.pos_ in tagging_list) and (len(token.text) > 1)]
        return word

    wiki_page_title = ['日本', '東京', '東京大学', '日本の経済', 'ベトナム', '進撃の巨人', 'アメリカ合衆国']
    random_page = random.choice(wiki_page_title)
    print(f"Title: {random_page}")
    # Get a random sentence from the content
    sentences = wikipedia.WikipediaPage(random_page).content

    word_vectors = KeyedVectors.load_word2vec_format("mcq\\vector\\cc.ja.300.vec", encoding='utf8', binary=False, limit = 10000)

    # Def chosen one:
    def choose(random_sentence, verbs):
        chosen_one  = verbs[random.randint(1,len(verbs))-1]
        q = random_sentence.replace(chosen_one, "___")
        return chosen_one, q

    # Function to get similar words for a target word
    def get_similar_words(target_word, num_similar=3, threshold=0.8):
        if target_word not in word_vectors:
            return None
        similar_words = [
            word for word, similarity in word_vectors.most_similar(target_word, topn=15) if similarity < threshold
        ]        
        # Ensure enough similar words are available
        if len(similar_words) < num_similar:
            return None
        # Pick three similar words
        chosen_similar_words = random.sample(similar_words, num_similar)
        chosen_similar_words += [target_word]
        random.shuffle(chosen_similar_words)
        return chosen_similar_words
    # Main logic
    while True: 
        random_sentence = get_random_sentence(sentences)
        if random_sentence:
            words = getRandomWords(random_sentence)
            if len(words) > 0:
                break
    target_word, sen_sen = choose(random_sentence, words)
    simi = get_similar_words(target_word, num_similar=3, threshold=0.7)

    return render(request, "mcq/index.html", {"sentence": random_sentence, "target_word": target_word, "simi": simi, "sen_sen": sen_sen, "random_page": random_page})
"""
def mcq_fast(request):
    sys.stdout.reconfigure(encoding='utf-8')
    topic_names = ['日本', '東京', '東京大学', '日本の経済', 'ベトナム', '進撃の巨人', 'アメリカ合衆国']
    length = len(topic_names) -1
    random_topic = topic_names[random.randint(0, length)]
    with open(f"mcq/data/{random_topic}.json", "r", encoding="utf-8") as file:
        data = json.load(file)
        length = len(data)
        target_array = data[random.randint(0, length-1)][0]

        def sensen(sentence, word):
            q = sentence.replace(word, "___")
            return q

        topic = target_array.get("topic_name")
        sentence = target_array.get("sentence")
        target_word = target_array.get("word")
        simi = target_array.get("similar")
        sen_sen = sensen(sentence, target_word)
    
    return render(request, "mcq/index.html", {"target_word": target_word, "simi": simi, "sen_sen": sen_sen, "random_page": topic})
