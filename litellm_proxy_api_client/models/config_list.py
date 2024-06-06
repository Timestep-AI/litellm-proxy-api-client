from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="ConfigList")


@_attrs_define
class ConfigList:
    """
    Attributes:
        field_name (str):
        field_type (str):
        field_description (str):
        field_value (Any):
        stored_in_db (Union[None, bool]):
        field_default_value (Any):
        premium_field (Union[Unset, bool]):  Default: False.
    """

    field_name: str
    field_type: str
    field_description: str
    field_value: Any
    stored_in_db: Union[None, bool]
    field_default_value: Any
    premium_field: Union[Unset, bool] = False
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        field_name = self.field_name

        field_type = self.field_type

        field_description = self.field_description

        field_value = self.field_value

        stored_in_db: Union[None, bool]
        stored_in_db = self.stored_in_db

        field_default_value = self.field_default_value

        premium_field = self.premium_field

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "field_name": field_name,
                "field_type": field_type,
                "field_description": field_description,
                "field_value": field_value,
                "stored_in_db": stored_in_db,
                "field_default_value": field_default_value,
            }
        )
        if premium_field is not UNSET:
            field_dict["premium_field"] = premium_field

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        field_name = d.pop("field_name")

        field_type = d.pop("field_type")

        field_description = d.pop("field_description")

        field_value = d.pop("field_value")

        def _parse_stored_in_db(data: object) -> Union[None, bool]:
            if data is None:
                return data
            return cast(Union[None, bool], data)

        stored_in_db = _parse_stored_in_db(d.pop("stored_in_db"))

        field_default_value = d.pop("field_default_value")

        premium_field = d.pop("premium_field", UNSET)

        config_list = cls(
            field_name=field_name,
            field_type=field_type,
            field_description=field_description,
            field_value=field_value,
            stored_in_db=stored_in_db,
            field_default_value=field_default_value,
            premium_field=premium_field,
        )

        config_list.additional_properties = d
        return config_list

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
