from enum import Enum


class KeyManagementSystem(str, Enum):
    AWS_SECRET_MANAGER = "aws_secret_manager"
    AZURE_KEY_VAULT = "azure_key_vault"
    GOOGLE_KMS = "google_kms"
    LOCAL = "local"

    def __str__(self) -> str:
        return str(self.value)
