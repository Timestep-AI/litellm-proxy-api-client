from enum import Enum


class DynamoDBArgsBillingMode(str, Enum):
    PAY_PER_REQUEST = "PAY_PER_REQUEST"
    PROVISIONED_THROUGHPUT = "PROVISIONED_THROUGHPUT"

    def __str__(self) -> str:
        return str(self.value)
