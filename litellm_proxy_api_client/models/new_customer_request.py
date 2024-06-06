from typing import Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.new_customer_request_allowed_model_region_type_0 import NewCustomerRequestAllowedModelRegionType0
from ..types import UNSET, Unset

T = TypeVar("T", bound="NewCustomerRequest")


@_attrs_define
class NewCustomerRequest:
    """Create a new customer, allocate a budget to them

    Attributes:
        user_id (str):
        alias (Union[None, Unset, str]):
        blocked (Union[Unset, bool]):  Default: False.
        max_budget (Union[None, Unset, float]):
        budget_id (Union[None, Unset, str]):
        allowed_model_region (Union[NewCustomerRequestAllowedModelRegionType0, None, Unset]):
        default_model (Union[None, Unset, str]):
    """

    user_id: str
    alias: Union[None, Unset, str] = UNSET
    blocked: Union[Unset, bool] = False
    max_budget: Union[None, Unset, float] = UNSET
    budget_id: Union[None, Unset, str] = UNSET
    allowed_model_region: Union[NewCustomerRequestAllowedModelRegionType0, None, Unset] = UNSET
    default_model: Union[None, Unset, str] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        user_id = self.user_id

        alias: Union[None, Unset, str]
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        blocked = self.blocked

        max_budget: Union[None, Unset, float]
        if isinstance(self.max_budget, Unset):
            max_budget = UNSET
        else:
            max_budget = self.max_budget

        budget_id: Union[None, Unset, str]
        if isinstance(self.budget_id, Unset):
            budget_id = UNSET
        else:
            budget_id = self.budget_id

        allowed_model_region: Union[None, Unset, str]
        if isinstance(self.allowed_model_region, Unset):
            allowed_model_region = UNSET
        elif isinstance(self.allowed_model_region, NewCustomerRequestAllowedModelRegionType0):
            allowed_model_region = self.allowed_model_region.value
        else:
            allowed_model_region = self.allowed_model_region

        default_model: Union[None, Unset, str]
        if isinstance(self.default_model, Unset):
            default_model = UNSET
        else:
            default_model = self.default_model

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if blocked is not UNSET:
            field_dict["blocked"] = blocked
        if max_budget is not UNSET:
            field_dict["max_budget"] = max_budget
        if budget_id is not UNSET:
            field_dict["budget_id"] = budget_id
        if allowed_model_region is not UNSET:
            field_dict["allowed_model_region"] = allowed_model_region
        if default_model is not UNSET:
            field_dict["default_model"] = default_model

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        d = src_dict.copy()
        user_id = d.pop("user_id")

        def _parse_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alias = _parse_alias(d.pop("alias", UNSET))

        blocked = d.pop("blocked", UNSET)

        def _parse_max_budget(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_budget = _parse_max_budget(d.pop("max_budget", UNSET))

        def _parse_budget_id(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        budget_id = _parse_budget_id(d.pop("budget_id", UNSET))

        def _parse_allowed_model_region(data: object) -> Union[NewCustomerRequestAllowedModelRegionType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allowed_model_region_type_0 = NewCustomerRequestAllowedModelRegionType0(data)

                return allowed_model_region_type_0
            except:  # noqa: E722
                pass
            return cast(Union[NewCustomerRequestAllowedModelRegionType0, None, Unset], data)

        allowed_model_region = _parse_allowed_model_region(d.pop("allowed_model_region", UNSET))

        def _parse_default_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_model = _parse_default_model(d.pop("default_model", UNSET))

        new_customer_request = cls(
            user_id=user_id,
            alias=alias,
            blocked=blocked,
            max_budget=max_budget,
            budget_id=budget_id,
            allowed_model_region=allowed_model_region,
            default_model=default_model,
        )

        new_customer_request.additional_properties = d
        return new_customer_request

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
