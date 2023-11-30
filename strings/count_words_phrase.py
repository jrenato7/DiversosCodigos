'''
Given a phrase, return a list of the most frequent words according to the k

def frequent_words(phrase: str, k: int) -> list[str]:
    pass

phrase = 'once twice thrice twice thrice thrice'

frequent_words(phrase, 2) = ['thrice', 'twice']

$u9anoWroChoxIdrLdLsweswi9ugosor

'''

# Duas formas de implementar: 1) só com comandos padrões 2) com collections:

# forma 1

def frequent_words_v1(phrase: str, k: int) -> list[str]:
    """
    O(n log n) tempo e O(n) espaço
    Sendo n a quantidade de palavras contidas em phrase
    """
    word_map = {}
    for word in phrase.split(" "):  # O(n)
        if word in word_map:
            word_map[word] += 1
        else:
            word_map[word] = 1

    output = [(word, count) for word, count in word_map.items()]
    # vai ordenar usando como chave o segundo elemento da tupla: lambda item: item[1]
    # reverte a ordenação para que o elemento mais freqnte seja o primeiro da lista
    output = sorted(output, key=lambda item: item[1], reverse=True)  # O(n log n)
    output = [word for word, _ in output if word]
    return output[:k]


# forma 2
from collections import Counter


def frequent_words_v2(phrase: str, k: int) -> list[str]:
    """
    O(n) tempo e O(n) espaço
    Sendo n a quantidade de palavras contidas em phrase
    """
    words = [word for word in phrase.split(" ") if word]
    c = Counter(words)
    return [word for word, _ in c.most_common(k)]


# Testes
import unittest


class FrequentWordsBase:
# class FrequentWordsBase(unittest.TestCase):
    def test_empty_spaces(self):
        """
        Deve retornar uma lista vazia caso receba uma frase so com espaços.
        """
        resp = self.func("     ", 3)
        self.assertListEqual([], resp)

    def test_empty_phrase(self):
        """
        Deve retornar uma lista vazia caso receba uma frase sem nada.
        """
        resp = self.func("", 2)
        self.assertListEqual([], resp)

    def test_empty_k_0(self):
        """
        Deve retornar uma lista vazia caso receba k=0.
        """
        resp = self.func(self.phrase, 0)
        self.assertListEqual([], resp)

    def test_most_frequent_k2(self):
        """
        Deve retornar uma lista com ['thrice', 'twice'].
        """
        expected = ['thrice', 'twice']
        resp = self.func(self.phrase, 2)
        self.assertListEqual(expected, resp)

    def test_most_frequent_k1(self):
        """
        Deve retornar uma lista com ['thrice'].
        """
        expected = ['thrice']
        resp = self.func(self.phrase, 1)
        self.assertListEqual(expected, resp)

    def test_most_frequent_k5(self):
        """
        Deve retornar uma lista com ['thrice', 'twice', 'once'].
        """
        expected = ['thrice', 'twice', 'once']
        resp = self.func(self.phrase, 5)
        self.assertListEqual(expected, resp)


class FrequentWordsV1Test(unittest.TestCase, FrequentWordsBase):
    def setUp(self):
        self.phrase = 'once twice thrice twice thrice thrice'
        self.func = frequent_words_v1


class FrequentWordsV2Test(unittest.TestCase, FrequentWordsBase):
    def setUp(self):
        self.phrase = 'once twice thrice twice thrice thrice'
        self.func = frequent_words_v2


if __name__ == '__main__':
    unittest.main()
