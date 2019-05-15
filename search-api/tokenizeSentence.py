from janome.tokenizer import Tokenizer
from janome.analyzer import Analyzer
from janome.tokenfilter import CompoundNounFilter
import re
import unicodedata

class TokenizerSentence(object):
    @staticmethod
    def extract_noun(text):
        t = Tokenizer()
        noun_list = []
        token_filters = [CompoundNounFilter()]
        analizer = Analyzer([], t, token_filters)
        for token in analizer.analyze(text):
            if token.part_of_speech.startswith("名詞,固有名詞") or token.part_of_speech.startswith("名詞,複合"):
                noun_list.append(token.base_form)
        return list(set(noun_list))
    @staticmethod
    def delete_tag(sentence):
        pattern1 = r'<.+?>'
        pattern2 = r'<.+?…'
        text = re.sub(pattern1, '', sentence)
        text = re.sub(pattern2, '', text)
        return text
    @staticmethod
    def is_japanese(sentence):
        for ch in sentence:
            try:
                name = unicodedata.name(ch) 
                if "HIRAGANA" in name or "KATAKANA" in name:
                    return True
            except:
                continue
        return False
