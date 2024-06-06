from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.lite_llm_end_user_table_allowed_model_region_type_0 import LiteLLMEndUserTableAllowedModelRegionType0
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.lite_llm_budget_table import LiteLLMBudgetTable


T = TypeVar("T", bound="LiteLLMEndUserTable")


@_attrs_define
class LiteLLMEndUserTable:
    """
    Attributes:
        user_id (str):
        blocked (bool):
        alias (Union[None, Unset, str]):
        spend (Union[Unset, float]):  Default: 0.0.
        allowed_model_region (Union[LiteLLMEndUserTableAllowedModelRegionType0, None, Unset]):
        default_model (Union[None, Unset, str]):
        litellm_budget_table (Union['LiteLLMBudgetTable', None, Unset]):
    """

    user_id: str
    blocked: bool
    alias: Union[None, Unset, str] = UNSET
    spend: Union[Unset, float] = 0.0
    allowed_model_region: Union[LiteLLMEndUserTableAllowedModelRegionType0, None, Unset] = UNSET
    default_model: Union[None, Unset, str] = UNSET
    litellm_budget_table: Union["LiteLLMBudgetTable", None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable

        user_id = self.user_id

        blocked = self.blocked

        alias: Union[None, Unset, str]
        if isinstance(self.alias, Unset):
            alias = UNSET
        else:
            alias = self.alias

        spend = self.spend

        allowed_model_region: Union[None, Unset, str]
        if isinstance(self.allowed_model_region, Unset):
            allowed_model_region = UNSET
        elif isinstance(self.allowed_model_region, LiteLLMEndUserTableAllowedModelRegionType0):
            allowed_model_region = self.allowed_model_region.value
        else:
            allowed_model_region = self.allowed_model_region

        default_model: Union[None, Unset, str]
        if isinstance(self.default_model, Unset):
            default_model = UNSET
        else:
            default_model = self.default_model

        litellm_budget_table: Union[Dict[str, Any], None, Unset]
        if isinstance(self.litellm_budget_table, Unset):
            litellm_budget_table = UNSET
        elif isinstance(self.litellm_budget_table, LiteLLMBudgetTable):
            litellm_budget_table = self.litellm_budget_table.to_dict()
        else:
            litellm_budget_table = self.litellm_budget_table

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "user_id": user_id,
                "blocked": blocked,
            }
        )
        if alias is not UNSET:
            field_dict["alias"] = alias
        if spend is not UNSET:
            field_dict["spend"] = spend
        if allowed_model_region is not UNSET:
            field_dict["allowed_model_region"] = allowed_model_region
        if default_model is not UNSET:
            field_dict["default_model"] = default_model
        if litellm_budget_table is not UNSET:
            field_dict["litellm_budget_table"] = litellm_budget_table

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.lite_llm_budget_table import LiteLLMBudgetTable

        d = src_dict.copy()
        user_id = d.pop("user_id")

        blocked = d.pop("blocked")

        def _parse_alias(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        alias = _parse_alias(d.pop("alias", UNSET))

        spend = d.pop("spend", UNSET)

        def _parse_allowed_model_region(data: object) -> Union[LiteLLMEndUserTableAllowedModelRegionType0, None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, str):
                    raise TypeError()
                allowed_model_region_type_0 = LiteLLMEndUserTableAllowedModelRegionType0(data)

                return allowed_model_region_type_0
            except:  # noqa: E722
                pass
            return cast(Union[LiteLLMEndUserTableAllowedModelRegionType0, None, Unset], data)

        allowed_model_region = _parse_allowed_model_region(d.pop("allowed_model_region", UNSET))

        def _parse_default_model(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        default_model = _parse_default_model(d.pop("default_model", UNSET))

        def _parse_litellm_budget_table(data: object) -> Union["LiteLLMBudgetTable", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                litellm_budget_table_type_0 = LiteLLMBudgetTable.from_dict(data)

                return litellm_budget_table_type_0
            except:  # noqa: E722
                pass
            return cast(Union["LiteLLMBudgetTable", None, Unset], data)

        litellm_budget_table = _parse_litellm_budget_table(d.pop("litellm_budget_table", UNSET))

        lite_llm_end_user_table = cls(
            user_id=user_id,
            blocked=blocked,
            alias=alias,
            spend=spend,
            allowed_model_region=allowed_model_region,
            default_model=default_model,
            litellm_budget_table=litellm_budget_table,
        )

        lite_llm_end_user_table.additional_properties = d
        return lite_llm_end_user_table

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
