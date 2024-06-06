from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

T = TypeVar("T", bound="BudgetNew")


@_attrs_define
class BudgetNew:
    """
    Attributes:
        budget_id (Union[Unset, str]): The unique budget id.
        max_budget (Union[None, Unset, float]): Requests will fail if this budget (in USD) is exceeded.
        soft_budget (Union[None, Unset, float]): Requests will NOT fail if this is exceeded. Will fire alerting though.
        max_parallel_requests (Union[None, Unset, int]): Max concurrent requests allowed for this budget id.
        tpm_limit (Union[None, Unset, int]): Max tokens per minute, allowed for this budget id.
        rpm_limit (Union[None, Unset, int]): Max requests per minute, allowed for this budget id.
        budget_duration (Union[None, Unset, str]): Max duration budget should be set for (e.g. '1hr', '1d', '28d')
    """

    budget_id: Union[Unset, str] = UNSET
    max_budget: Union[None, Unset, float] = UNSET
    soft_budget: Union[None, Unset, float] = UNSET
    max_parallel_requests: Union[None, Unset, int] = UNSET
    tpm_limit: Union[None, Unset, int] = UNSET
    rpm_limit: Union[None, Unset, int] = UNSET
    budget_duration: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        budget_id = self.budget_id

        max_budget: Union[None, Unset, float]
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        soft_budget: Union[None, Unset, float]
        if isinstance(self.soft_budget, Unset):
            soft_budget = UNSET
        else:
            soft_budget = self.soft_budget

        max_parallel_requests: Union[None, Unset, int]
        if isinstance(self.max_parallel_requests, Unset):
            max_parallel_requests = UNSET
        else:
            max_parallel_requests = self.max_parallel_requests

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

        budget_duration: Union[None, Unset, str]
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if soft_budget is not UNSET:
            field_dict["soft_budget"] = soft_budget
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        budget_id = d.pop("budget_id", UNSET)

        def _parse_max_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))

        def _parse_soft_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        soft_budget = _parse_soft_budget(d.pop("soft_budget", UNSET))

        def _parse_max_parallel_requests(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_parallel_requests = _parse_max_parallel_requests(d.pop("max_parallel_requests", UNSET))

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

        def _parse_budget_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))

        budget_new = cls(
            budget_id=budget_id,
            max_budget=max_budget,
            soft_budget=soft_budget,
            max_parallel_requests=max_parallel_requests,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            budget_duration=budget_duration,
        )

        budget_new.additional_properties = d
        return budget_new

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
