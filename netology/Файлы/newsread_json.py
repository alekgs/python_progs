import json
from collections import Counter


def read_json(file, max_len_word=6, top_words=10):
    with open(file, encoding='utf-8') as news_file:
        descripion_words = []
        news = json.load(news_file)
        for item in news['rss']['channel']['items']:
            description = [word for word in item['description'].split(' ') if len(word) > max_len_word]
            descripion_words.extend(description)
        counter_words = Counter(descripion_words)
        print(counter_words.most_common(top_words))


read_json('newsafr.json')
