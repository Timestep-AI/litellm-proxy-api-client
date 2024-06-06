import datetime
from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

T = TypeVar("T", bound="InvitationModel")


@_attrs_define
class InvitationModel:
    """
    Attributes:
        id (str):
        user_id (str):
        is_accepted (bool):
        accepted_at (Union[None, datetime.datetime]):
        expires_at (datetime.datetime):
        created_at (datetime.datetime):
        created_by (str):
        updated_at (datetime.datetime):
        updated_by (str):
    """

    id: str
    user_id: str
    is_accepted: bool
    accepted_at: Union[None, datetime.datetime]
    expires_at: datetime.datetime
    created_at: datetime.datetime
    created_by: str
    updated_at: datetime.datetime
    updated_by: str
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        id = self.id

        user_id = self.user_id

        is_accepted = self.is_accepted

        accepted_at: Union[None, str]
        if isinstance(self.accepted_at, datetime.datetime):
            accepted_at = self.accepted_at.isoformat()
        else:
            accepted_at = self.accepted_at

        expires_at = self.expires_at.isoformat()

        created_at = self.created_at.isoformat()

        created_by = self.created_by

        updated_at = self.updated_at.isoformat()

        updated_by = self.updated_by

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "id": id,
                "user_id": user_id,
                "is_accepted": is_accepted,
                "accepted_at": accepted_at,
                "expires_at": expires_at,
                "created_at": created_at,
                "created_by": created_by,
                "updated_at": updated_at,
                "updated_by": updated_by,
            }
        )

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        id = d.pop("id")

        user_id = d.pop("user_id")

        is_accepted = d.pop("is_accepted")

        def _parse_accepted_at(data: object) -> Union[None, datetime.datetime]:
            if data is None:
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                accepted_at_type_0 = isoparse(data)

                return accepted_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, datetime.datetime], data)

        accepted_at = _parse_accepted_at(d.pop("accepted_at"))

        expires_at = isoparse(d.pop("expires_at"))

        created_at = isoparse(d.pop("created_at"))

        created_by = d.pop("created_by")

        updated_at = isoparse(d.pop("updated_at"))

        updated_by = d.pop("updated_by")

        invitation_model = cls(
            id=id,
            user_id=user_id,
            is_accepted=is_accepted,
            accepted_at=accepted_at,
            expires_at=expires_at,
            created_at=created_at,
            created_by=created_by,
            updated_at=updated_at,
            updated_by=updated_by,
        )

        invitation_model.additional_properties = d
        return invitation_model

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
