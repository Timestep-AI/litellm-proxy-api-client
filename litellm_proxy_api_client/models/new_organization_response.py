import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.new_organization_response_metadata_type_0 import NewOrganizationResponseMetadataType0


T = TypeVar("T", bound="NewOrganizationResponse")


@_attrs_define
class NewOrganizationResponse:
    """
    Attributes:
        organization_id (str):
        budget_id (str):
        models (List[str]):
        created_by (str):
        updated_by (str):
        created_at (datetime.datetime):
        updated_at (datetime.datetime):
        organization_alias (Union[None, Unset, str]):
        metadata (Union['NewOrganizationResponseMetadataType0', None, Unset]):
    """

    organization_id: str
    budget_id: str
    models: List[str]
    created_by: str
    updated_by: str
    created_at: datetime.datetime
    updated_at: datetime.datetime
    organization_alias: Union[None, Unset, str] = UNSET
    metadata: Union["NewOrganizationResponseMetadataType0", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.new_organization_response_metadata_type_0 import NewOrganizationResponseMetadataType0

        organization_id = self.organization_id

        budget_id = self.budget_id

        models = self.models

        created_by = self.created_by

        updated_by = self.updated_by

        created_at = self.created_at.isoformat()

        updated_at = self.updated_at.isoformat()

        organization_alias: Union[None, Unset, str]
        if isinstance(self.organization_alias, Unset):
            organization_alias = UNSET
        else:
            organization_alias = self.organization_alias

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, NewOrganizationResponseMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "organization_id": organization_id,
                "budget_id": budget_id,
                "models": models,
                "created_by": created_by,
                "updated_by": updated_by,
                "created_at": created_at,
                "updated_at": updated_at,
            }
        )
        if organization_alias is not UNSET:
            field_dict["organization_alias"] = organization_alias
        if metadata is not UNSET:
            field_dict["metadata"] = metadata

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.new_organization_response_metadata_type_0 import NewOrganizationResponseMetadataType0

        d = src_dict.copy()
        organization_id = d.pop("organization_id")

        budget_id = d.pop("budget_id")

        models = cast(List[str], d.pop("models"))

        created_by = d.pop("created_by")

        updated_by = d.pop("updated_by")

        created_at = isoparse(d.pop("created_at"))

        updated_at = isoparse(d.pop("updated_at"))

        def _parse_organization_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_alias = _parse_organization_alias(d.pop("organization_alias", UNSET))

        def _parse_metadata(data: object) -> Union["NewOrganizationResponseMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = NewOrganizationResponseMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["NewOrganizationResponseMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        new_organization_response = cls(
            organization_id=organization_id,
            budget_id=budget_id,
            models=models,
            created_by=created_by,
            updated_by=updated_by,
            created_at=created_at,
            updated_at=updated_at,
            organization_alias=organization_alias,
            metadata=metadata,
        )

        new_organization_response.additional_properties = d
        return new_organization_response

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
