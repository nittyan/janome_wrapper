from enum import Enum
from typing import List

from janome.tokenizer import Token
from janome.tokenizer import Tokenizer


class PartOfSpeech(Enum):
    """ 品詞 """

    NOUN = '名詞,'
    VERB = '動詞,'

    def is_this(self, text: str) -> bool:
        return text.startswith(self.value)


class TokenizerWrapper:

    def __init__(self):
        self._tokenizer: Tokenizer = Tokenizer()

    def tokenize(self, text: str, part_of_speeches: List[PartOfSpeech], stop_words: List[str]=[]) -> List[Token]:
        return [token for token in self._tokenizer.tokenize(text)
                if self._start_with(token, part_of_speeches) and not self._is_stop_word(token, stop_words)]

    def _start_with(self, token: Token, part_of_speeches: List[PartOfSpeech]) -> bool:
        for entry in part_of_speeches:
            if entry.is_this(token.part_of_speech):
                return True
        return False

    def _is_stop_word(self, token: Token, stop_words: List[str]):
        return token.surface in stop_words


def main():
    tokenizer = TokenizerWrapper()
    tokens: List[Token] = tokenizer.tokenize('隣の客はよく柿食う客だ', [PartOfSpeech.VERB, PartOfSpeech.NOUN], ['隣'])
    for token in tokens:
        print(token.surface)


if __name__ == '__main__':
    main()