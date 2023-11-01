from typing import Any


class BaseLLM:
    def __init__(self):
        pass

    def get_media_encoding(self, data: Any):
        raise NotImplementedError

    def get_text_encoding(self, query: str):
        raise NotImplementedError
