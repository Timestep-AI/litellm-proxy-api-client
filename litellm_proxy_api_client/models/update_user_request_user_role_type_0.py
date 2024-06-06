from enum import Enum


class UpdateUserRequestUserRoleType0(str, Enum):
    CUSTOMER = "customer"
    INTERNAL_USER = "internal_user"
    INTERNAL_USER_VIEWER = "internal_user_viewer"
    PROXY_ADMIN = "proxy_admin"
    PROXY_ADMIN_VIEWER = "proxy_admin_viewer"
    TEAM = "team"

    def __str__(self) -> str:
        return str(self.value)
