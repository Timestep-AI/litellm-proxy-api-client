import datetime
from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field
from dateutil.parser import isoparse

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lite_llm_team_table_metadata_type_0 import LiteLLMTeamTableMetadataType0
    from ..models.member import Member


T = TypeVar("T", bound="LiteLLMTeamTable")


@_attrs_define
class LiteLLMTeamTable:
    """
    Attributes:
        team_alias (Union[None, Unset, str]):
        team_id (Union[None, Unset, str]):
        organization_id (Union[None, Unset, str]):
        admins (Union[Unset, List[Any]]):
        members (Union[Unset, List[Any]]):
        members_with_roles (Union[Unset, List['Member']]):
        metadata (Union['LiteLLMTeamTableMetadataType0', None, Unset]):
        tpm_limit (Union[None, Unset, int]):
        rpm_limit (Union[None, Unset, int]):
        max_budget (Union[None, Unset, float]):
        budget_duration (Union[None, Unset, str]):
        models (Union[Unset, List[Any]]):
        blocked (Union[Unset, bool]):  Default: False.
        spend (Union[None, Unset, float]):
        max_parallel_requests (Union[None, Unset, int]):
        budget_reset_at (Union[None, Unset, datetime.datetime]):
        model_id (Union[None, Unset, int]):
    """

    team_alias: Union[None, Unset, str] = UNSET
    team_id: Union[None, Unset, str] = UNSET
    organization_id: Union[None, Unset, str] = UNSET
    admins: Union[Unset, List[Any]] = UNSET
    members: Union[Unset, List[Any]] = UNSET
    members_with_roles: Union[Unset, List["Member"]] = UNSET
    metadata: Union["LiteLLMTeamTableMetadataType0", None, Unset] = UNSET
    tpm_limit: Union[None, Unset, int] = UNSET
    rpm_limit: Union[None, Unset, int] = UNSET
    max_budget: Union[None, Unset, float] = UNSET
    budget_duration: Union[None, Unset, str] = UNSET
    models: Union[Unset, List[Any]] = UNSET
    blocked: Union[Unset, bool] = False
    spend: Union[None, Unset, float] = UNSET
    max_parallel_requests: Union[None, Unset, int] = UNSET
    budget_reset_at: Union[None, Unset, datetime.datetime] = UNSET
    model_id: Union[None, Unset, int] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.lite_llm_team_table_metadata_type_0 import LiteLLMTeamTableMetadataType0

        team_alias: Union[None, Unset, str]
        if isinstance(self.team_alias, Unset):
            team_alias = UNSET
        else:
            team_alias = self.team_alias

        team_id: Union[None, Unset, str]
        if isinstance(self.team_id, Unset):
            team_id = UNSET
        else:
            team_id = self.team_id

        organization_id: Union[None, Unset, str]
        if isinstance(self.organization_id, Unset):
            organization_id = UNSET
        else:
            organization_id = self.organization_id

        admins: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.admins, Unset):
            admins = self.admins

        members: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.members, Unset):
            members = self.members

        members_with_roles: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.members_with_roles, Unset):
            members_with_roles = []
            for members_with_roles_item_data in self.members_with_roles:
                members_with_roles_item = members_with_roles_item_data.to_dict()
                members_with_roles.append(members_with_roles_item)

        metadata: Union[Dict[str, Any], None, Unset]
        if isinstance(self.metadata, Unset):
            metadata = UNSET
        elif isinstance(self.metadata, LiteLLMTeamTableMetadataType0):
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

        budget_duration: Union[None, Unset, str]
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        models: Union[Unset, List[Any]] = UNSET
        if not isinstance(self.models, Unset):
            models = self.models

        blocked = self.blocked

        spend: Union[None, Unset, float]
        if isinstance(self.spend, Unset):
            spend = UNSET
        else:
            spend = self.spend

        max_parallel_requests: Union[None, Unset, int]
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

        budget_reset_at: Union[None, Unset, str]
        if isinstance(self.budget_reset_at, Unset):
            budget_reset_at = UNSET
        elif isinstance(self.budget_reset_at, datetime.datetime):
            budget_reset_at = self.budget_reset_at.isoformat()
        else:
            budget_reset_at = self.budget_reset_at

        model_id: Union[None, Unset, int]
        if isinstance(self.model_id, Unset):
            model_id = UNSET
        else:
            model_id = self.model_id

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if team_alias is not UNSET:
            field_dict["team_alias"] = team_alias
        if team_id is not UNSET:
            field_dict["team_id"] = team_id
        if organization_id is not UNSET:
            field_dict["organization_id"] = organization_id
        if admins is not UNSET:
            field_dict["admins"] = admins
        if members is not UNSET:
            field_dict["members"] = members
        if members_with_roles is not UNSET:
            field_dict["members_with_roles"] = members_with_roles
        if metadata is not UNSET:
            field_dict["metadata"] = metadata
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration
        if models is not UNSET:
            field_dict["models"] = models
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if spend is not UNSET:
            field_dict["spend"] = spend
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if budget_reset_at is not UNSET:
            field_dict["budget_reset_at"] = budget_reset_at
        if model_id is not UNSET:
            field_dict["model_id"] = model_id

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lite_llm_team_table_metadata_type_0 import LiteLLMTeamTableMetadataType0
        from ..models.member import Member

        d = src_dict.copy()

        def _parse_team_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team_alias = _parse_team_alias(d.pop("team_alias", UNSET))

        def _parse_team_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        team_id = _parse_team_id(d.pop("team_id", UNSET))

        def _parse_organization_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        organization_id = _parse_organization_id(d.pop("organization_id", UNSET))

        admins = cast(List[Any], d.pop("admins", UNSET))

        members = cast(List[Any], d.pop("members", UNSET))

        members_with_roles = []
        _members_with_roles = d.pop("members_with_roles", UNSET)
        for members_with_roles_item_data in _members_with_roles or []:
            members_with_roles_item = Member.from_dict(members_with_roles_item_data)

            members_with_roles.append(members_with_roles_item)

        def _parse_metadata(data: object) -> Union["LiteLLMTeamTableMetadataType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                metadata_type_0 = LiteLLMTeamTableMetadataType0.from_dict(data)

                return metadata_type_0
            except:  # noqa: E722
                pass
            return cast(Union["LiteLLMTeamTableMetadataType0", None, Unset], data)

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

        def _parse_budget_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))

        models = cast(List[Any], d.pop("models", UNSET))

        blocked = d.pop("blocked", UNSET)

        def _parse_spend(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        spend = _parse_spend(d.pop("spend", UNSET))

        def _parse_max_parallel_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))

        def _parse_budget_reset_at(data: object) -> Union[None, Unset, datetime.datetime]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                budget_reset_at_type_0 = isoparse(data)

                return budget_reset_at_type_0
            except:  # noqa: E722
                pass
            return cast(Union[None, Unset, datetime.datetime], data)

        budget_reset_at = _parse_budget_reset_at(d.pop("budget_reset_at", UNSET))

        def _parse_model_id(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        model_id = _parse_model_id(d.pop("model_id", UNSET))

        lite_llm_team_table = cls(
            team_alias=team_alias,
            team_id=team_id,
            organization_id=organization_id,
            admins=admins,
            members=members,
            members_with_roles=members_with_roles,
            metadata=metadata,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            max_budget=max_budget,
            budget_duration=budget_duration,
            models=models,
            blocked=blocked,
            spend=spend,
            max_parallel_requests=max_parallel_requests,
            budget_reset_at=budget_reset_at,
            model_id=model_id,
        )

        lite_llm_team_table.additional_properties = d
        return lite_llm_team_table

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
