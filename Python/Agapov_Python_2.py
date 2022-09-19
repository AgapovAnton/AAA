import numpy as np
from collections import Counter


class CountVectorizer():
    """класс CountVectorizer:
    метод fit_transform принимает текстовый корпус
        возвращает терм-документную матрицу
    метод get_feature_names ничего не принимает возвращает
        список фичей (уникальных слов из корпуса)
    """
    def __init__(self):
        self.get_feature_names_list = []
        self.cnt_all = []

    def fit_transform(self, corp):
        for i, el in enumerate(corp):
            cnt = Counter()
            for word in el.split():
                word = word.lower()
                cnt[word] += 1
                # Создаем список уникальных слов
                if not (word in self.get_feature_names_list):
                    self.get_feature_names_list.append(word)

            # Список Counter'ов
            self.cnt_all.append(dict(cnt))

        # создаем итоговую матрицу
        result = np.zeros((len(corpus),
                           len(self.get_feature_names_list)), dtype='int')

        for i, w in enumerate(self.get_feature_names()):
            for j, cnt in enumerate(self.cnt_all):
                if w in cnt.keys():
                    result[j][i] = cnt[w]
        return result

    def get_feature_names(self):
        return self.get_feature_names_list


if __name__ == '__main__':
    corpus = [
        'Crock Pot Pasta Never boil pasta again',
        'Pasta Pomodoro Fresh ingredients Parmesan to taste'
    ]
    vectorizer = CountVectorizer()
    count_matrix = vectorizer.fit_transform(corpus)

    print(vectorizer.get_feature_names())
    print(count_matrix)
