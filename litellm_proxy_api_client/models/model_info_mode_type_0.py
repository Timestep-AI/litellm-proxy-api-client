from enum import Enum


class ModelInfoModeType0(str, Enum):
    CHAT = "chat"
    COMPLETION = "completion"
    EMBEDDING = "embedding"

    def __str__(self) -> str:
        return str(self.value)
