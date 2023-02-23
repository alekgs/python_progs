import xml.etree.ElementTree as ET
from collections import Counter


def read_xml(file, max_len_word=6, top_words=10):
    with open(file, encoding='utf-8') as news_file:
        descr_words = []
        tree = ET.parse(news_file).getroot()
        for elem in tree.findall('channel/item/description'):
            descr_words.extend([word for word in elem.text.split(' ') if len(word) > max_len_word])
        counter_words = Counter(descr_words)
        print(counter_words.most_common(top_words))


read_xml('newsafr.xml')
