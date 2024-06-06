from enum import Enum


class ModelInfoBaseModelType0(str, Enum):
    GPT_3_5_TURBO = "gpt-3.5-turbo"
    GPT_3_5_TURBO_16K = "gpt-3.5-turbo-16k"
    GPT_4 = "gpt-4"
    GPT_4_1106_PREVIEW = "gpt-4-1106-preview"
    GPT_4_32K = "gpt-4-32k"
    TEXT_EMBEDDING_ADA_002 = "text-embedding-ada-002"

    def __str__(self) -> str:
        return str(self.value)
