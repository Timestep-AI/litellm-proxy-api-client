from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lite_llm_budget_table_model_max_budget_type_0 import LiteLLMBudgetTableModelMaxBudgetType0


T = TypeVar("T", bound="LiteLLMBudgetTable")


@_attrs_define
class LiteLLMBudgetTable:
    """Represents user-controllable params for a LiteLLM_BudgetTable record

    Attributes:
        soft_budget (Union[None, Unset, float]):
        max_budget (Union[None, Unset, float]):
        max_parallel_requests (Union[None, Unset, int]):
        tpm_limit (Union[None, Unset, int]):
        rpm_limit (Union[None, Unset, int]):
        model_max_budget (Union['LiteLLMBudgetTableModelMaxBudgetType0', None, Unset]):
        budget_duration (Union[None, Unset, str]):
    """

    soft_budget: Union[None, Unset, float] = UNSET
    max_budget: Union[None, Unset, float] = UNSET
    max_parallel_requests: Union[None, Unset, int] = UNSET
    tpm_limit: Union[None, Unset, int] = UNSET
    rpm_limit: Union[None, Unset, int] = UNSET
    model_max_budget: Union["LiteLLMBudgetTableModelMaxBudgetType0", None, Unset] = UNSET
    budget_duration: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.lite_llm_budget_table_model_max_budget_type_0 import LiteLLMBudgetTableModelMaxBudgetType0

        soft_budget: Union[None, Unset, float]
        if isinstance(self.soft_budget, Unset):
            soft_budget = UNSET
        else:
            soft_budget = self.soft_budget

        max_budget: Union[None, Unset, float]
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

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

        model_max_budget: Union[Dict[str, Any], None, Unset]
        if isinstance(self.model_max_budget, Unset):
            model_max_budget = UNSET
        elif isinstance(self.model_max_budget, LiteLLMBudgetTableModelMaxBudgetType0):
            model_max_budget = self.model_max_budget.to_dict()
        else:
            model_max_budget = self.model_max_budget

        budget_duration: Union[None, Unset, str]
        if isinstance(self.budget_duration, Unset):
            budget_duration = UNSET
        else:
            budget_duration = self.budget_duration

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if soft_budget is not UNSET:
            field_dict["soft_budget"] = soft_budget
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if max_parallel_requests is not UNSET:
            field_dict["max_parallel_requests"] = max_parallel_requests
        if tpm_limit is not UNSET:
            field_dict["tpm_limit"] = tpm_limit
        if rpm_limit is not UNSET:
            field_dict["rpm_limit"] = rpm_limit
        if model_max_budget is not UNSET:
            field_dict["model_max_budget"] = model_max_budget
        if budget_duration is not UNSET:
            field_dict["budget_duration"] = budget_duration

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lite_llm_budget_table_model_max_budget_type_0 import LiteLLMBudgetTableModelMaxBudgetType0

        d = src_dict.copy()

        def _parse_soft_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        soft_budget = _parse_soft_budget(d.pop("soft_budget", UNSET))

        def _parse_max_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))

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

        def _parse_model_max_budget(data: object) -> Union["LiteLLMBudgetTableModelMaxBudgetType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_max_budget_type_0 = LiteLLMBudgetTableModelMaxBudgetType0.from_dict(data)

                return model_max_budget_type_0
            except:  # noqa: E722
                pass
            return cast(Union["LiteLLMBudgetTableModelMaxBudgetType0", None, Unset], data)

        model_max_budget = _parse_model_max_budget(d.pop("model_max_budget", UNSET))

        def _parse_budget_duration(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_duration = _parse_budget_duration(d.pop("budget_duration", UNSET))

        lite_llm_budget_table = cls(
            soft_budget=soft_budget,
            max_budget=max_budget,
            max_parallel_requests=max_parallel_requests,
            tpm_limit=tpm_limit,
            rpm_limit=rpm_limit,
            model_max_budget=model_max_budget,
            budget_duration=budget_duration,
        )

        lite_llm_budget_table.additional_properties = d
        return lite_llm_budget_table

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
