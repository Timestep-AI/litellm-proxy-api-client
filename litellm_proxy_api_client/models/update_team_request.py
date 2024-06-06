from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_team_request_metadata_type_0 import UpdateTeamRequestMetadataType0


T = TypeVar("T", bound="UpdateTeamRequest")


@_attrs_define
class UpdateTeamRequest:
    """UpdateTeamRequest, used by /team/update when you need to update a team

    team_id: str
    team_alias: Optional[str] = None
    organization_id: Optional[str] = None
    metadata: Optional[dict] = None
    tpm_limit: Optional[int] = None
    rpm_limit: Optional[int] = None
    max_budget: Optional[float] = None
    models: Optional[list] = None
    blocked: Optional[bool] = None
    budget_duration: Optional[str] = None

        Attributes:
            team_id (str):
            team_alias (Union[None, Unset, str]):
            organization_id (Union[None, Unset, str]):
            metadata (Union['UpdateTeamRequestMetadataType0', None, Unset]):
            tpm_limit (Union[None, Unset, int]):
            rpm_limit (Union[None, Unset, int]):
            max_budget (Union[None, Unset, float]):
            models (Union[List[Any], None, Unset]):
            blocked (Union[None, Unset, bool]):
            budget_duration (Union[None, Unset, str]):
    """

    team_id: str
    team_alias: Union[None, Unset, str] = UNSET
    organization_id: Union[None, Unset, str] = UNSET
    metadata: Union["UpdateTeamRequestMetadataType0", None, Unset] = UNSET
    tpm_limit: Union[None, Unset, int] = UNSET
    rpm_limit: Union[None, Unset, int] = UNSET
    max_budget: Union[None, Unset, float] = UNSET
    models: Union[List[Any], None, Unset] = UNSET
    blocked: Union[None, Unset, bool] = UNSET
    budget_duration: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.update_team_request_metadata_type_0 import UpdateTeamRequestMetadataType0

        team_id = self.team_id

        team_alias: Union[None, Unset, str]
        if isinstance(self.team_alias, Unset):
            team_alias = UNSET
        else:
            team_alias = self.team_alias

        organization_id: Union[None, Unset, str]
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, UpdateTeamRequestMetadataType0):
            metadata = self.metadata.to_dict()
        else:
            metadata = self.metadata

        tpm_limit: Union[None, Unset, int]
        if isinstance(self.tpm_limit, Unset):
            tpm_limit = UNSET
        else:
            tpm_limit = self.tpm_limit

        rpm_limit: Union[None, Unset, int]
        if isinstance(self.rpm_limit, Unset):
            rpm_limit = UNSET
        else:
            rpm_limit = self.rpm_limit

        max_budget: Union[None, Unset, float]
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        models: Union[List[Any], None, Unset]
        if isinstance(self.models, Unset):
            models = UNSET
        elif isinstance(self.models, list):
            models = self.models

        else:
            models = self.models

        blocked: Union[None, Unset, bool]
        if isinstance(self.blocked, Unset):
            blocked = UNSET
        else:
            blocked = self.blocked

        budget_duration: Union[None, Unset, str]
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
            }
        )
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if models is not UNSET:
            field_dict["models"] = models
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_team_request_metadata_type_0 import UpdateTeamRequestMetadataType0

        d = src_dict.copy()
        team_id = d.pop("team_id")

        def _parse_team_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team_alias = _parse_team_alias(d.pop("team_alias", UNSET))

        def _parse_organization_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        def _parse_metadata(data: object) -> Union["UpdateTeamRequestMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = UpdateTeamRequestMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateTeamRequestMetadataType0", None, Unset], data)

        metadata = _parse_metadata(d.pop("metadata", UNSET))

        def _parse_tpm_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        tpm_limit = _parse_tpm_limit(d.pop("tpm_limit", UNSET))

        def _parse_rpm_limit(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        rpm_limit = _parse_rpm_limit(d.pop("rpm_limit", UNSET))

        def _parse_max_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))

        def _parse_models(data: object) -> Union[List[Any], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                models_type_0 = cast(List[Any], data)

                return models_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List[Any], None, Unset], data)

        models = _parse_models(d.pop("models", UNSET))

        def _parse_blocked(data: object) -> Union[None, Unset, bool]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, bool], data)

        blocked = _parse_blocked(d.pop("blocked", UNSET))

        def _parse_budget_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))

        update_team_request = cls(
            team_id=team_id,
            team_alias=team_alias,
            organization_id=organization_id,
            metadata=metadata,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            max_budget=max_budget,
            models=models,
            blocked=blocked,
            budget_duration=budget_duration,
        )

        update_team_request.additional_properties = d
        return update_team_request

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
