import numpy as np
from collections import Counter

class CountVectorizer():
    """ """
    def __init__(self):
        self.get_feature_names_list = []
        self.cnt_all = []

    def get_feature_names(self):
        return self.get_feature_names_list

    def fit_transform(self, corp):
        for i, el in enumerate(corp):
            cnt = Counter()
            for word in el.split():
                word = word.lower()
                cnt[word] += 1
                if not (word in self.get_feature_names_list):
                    self.get_feature_names_list.append(word)    #Узнаем список уникальных слов
            self.cnt_all.append(dict(cnt))                      #Список Counter'ов

        #создаем итоговую матрицу
        _result = np.zeros((len(corpus), len(self.get_feature_names_list)), dtype='int')

        for i, w in enumerate(self.get_feature_names()):
            for j, cnt in enumerate(self.cnt_all):
                if w in cnt.keys():
                    _result[j][i] = cnt[w]
        return _result

corpus = [
    'Crock Pot Pasta Never boil pasta again',
    'Pasta Pomodoro Fresh ingredients Parmesan to taste'
]
vectorizer = CountVectorizer()
count_matrix = vectorizer.fit_transform(corpus)

print(vectorizer.get_feature_names())
print(count_matrix)