from enum import Enum


class NewCustomerRequestAllowedModelRegionType0(str, Enum):
    EU = "eu"

    def __str__(self) -> str:
        return str(self.value)
