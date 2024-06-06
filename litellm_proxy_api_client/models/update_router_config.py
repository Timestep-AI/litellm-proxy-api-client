from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.update_router_config_context_window_fallbacks_type_0_item import (
        UpdateRouterConfigContextWindowFallbacksType0Item,
    )
    from ..models.update_router_config_fallbacks_type_0_item import UpdateRouterConfigFallbacksType0Item
    from ..models.update_router_config_model_group_retry_policy_type_0 import (
        UpdateRouterConfigModelGroupRetryPolicyType0,
    )
    from ..models.update_router_config_routing_strategy_args_type_0 import UpdateRouterConfigRoutingStrategyArgsType0


T = TypeVar("T", bound="UpdateRouterConfig")


@_attrs_define
class UpdateRouterConfig:
    """Set of params that you can modify via `router.update_settings()`.

    Attributes:
        routing_strategy_args (Union['UpdateRouterConfigRoutingStrategyArgsType0', None, Unset]):
        routing_strategy (Union[None, Unset, str]):
        model_group_retry_policy (Union['UpdateRouterConfigModelGroupRetryPolicyType0', None, Unset]):
        allowed_fails (Union[None, Unset, int]):
        cooldown_time (Union[None, Unset, float]):
        num_retries (Union[None, Unset, int]):
        timeout (Union[None, Unset, float]):
        max_retries (Union[None, Unset, int]):
        retry_after (Union[None, Unset, float]):
        fallbacks (Union[List['UpdateRouterConfigFallbacksType0Item'], None, Unset]):
        context_window_fallbacks (Union[List['UpdateRouterConfigContextWindowFallbacksType0Item'], None, Unset]):
    """

    routing_strategy_args: Union["UpdateRouterConfigRoutingStrategyArgsType0", None, Unset] = UNSET
    routing_strategy: Union[None, Unset, str] = UNSET
    model_group_retry_policy: Union["UpdateRouterConfigModelGroupRetryPolicyType0", None, Unset] = UNSET
    allowed_fails: Union[None, Unset, int] = UNSET
    cooldown_time: Union[None, Unset, float] = UNSET
    num_retries: Union[None, Unset, int] = UNSET
    timeout: Union[None, Unset, float] = UNSET
    max_retries: Union[None, Unset, int] = UNSET
    retry_after: Union[None, Unset, float] = UNSET
    fallbacks: Union[List["UpdateRouterConfigFallbacksType0Item"], None, Unset] = UNSET
    context_window_fallbacks: Union[List["UpdateRouterConfigContextWindowFallbacksType0Item"], None, Unset] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        from ..models.update_router_config_model_group_retry_policy_type_0 import (
            UpdateRouterConfigModelGroupRetryPolicyType0,
        )
        from ..models.update_router_config_routing_strategy_args_type_0 import (
            UpdateRouterConfigRoutingStrategyArgsType0,
        )

        routing_strategy_args: Union[Dict[str, Any], None, Unset]
        if isinstance(self.routing_strategy_args, Unset):
            routing_strategy_args = UNSET
        elif isinstance(self.routing_strategy_args, UpdateRouterConfigRoutingStrategyArgsType0):
            routing_strategy_args = self.routing_strategy_args.to_dict()
        else:
            routing_strategy_args = self.routing_strategy_args

        routing_strategy: Union[None, Unset, str]
        if isinstance(self.routing_strategy, Unset):
            routing_strategy = UNSET
        else:
            routing_strategy = self.routing_strategy

        model_group_retry_policy: Union[Dict[str, Any], None, Unset]
        if isinstance(self.model_group_retry_policy, Unset):
            model_group_retry_policy = UNSET
        elif isinstance(self.model_group_retry_policy, UpdateRouterConfigModelGroupRetryPolicyType0):
            model_group_retry_policy = self.model_group_retry_policy.to_dict()
        else:
            model_group_retry_policy = self.model_group_retry_policy

        allowed_fails: Union[None, Unset, int]
        if isinstance(self.allowed_fails, Unset):
            allowed_fails = UNSET
        else:
            allowed_fails = self.allowed_fails

        cooldown_time: Union[None, Unset, float]
        if isinstance(self.cooldown_time, Unset):
            cooldown_time = UNSET
        else:
            cooldown_time = self.cooldown_time

        num_retries: Union[None, Unset, int]
        if isinstance(self.num_retries, Unset):
            num_retries = UNSET
        else:
            num_retries = self.num_retries

        timeout: Union[None, Unset, float]
        if isinstance(self.timeout, Unset):
            timeout = UNSET
        else:
            timeout = self.timeout

        max_retries: Union[None, Unset, int]
        if isinstance(self.max_retries, Unset):
            max_retries = UNSET
        else:
            max_retries = self.max_retries

        retry_after: Union[None, Unset, float]
        if isinstance(self.retry_after, Unset):
            retry_after = UNSET
        else:
            retry_after = self.retry_after

        fallbacks: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.fallbacks, Unset):
            fallbacks = UNSET
        elif isinstance(self.fallbacks, list):
            fallbacks = []
            for fallbacks_type_0_item_data in self.fallbacks:
                fallbacks_type_0_item = fallbacks_type_0_item_data.to_dict()
                fallbacks.append(fallbacks_type_0_item)

        else:
            fallbacks = self.fallbacks

        context_window_fallbacks: Union[List[Dict[str, Any]], None, Unset]
        if isinstance(self.context_window_fallbacks, Unset):
            context_window_fallbacks = UNSET
        elif isinstance(self.context_window_fallbacks, list):
            context_window_fallbacks = []
            for context_window_fallbacks_type_0_item_data in self.context_window_fallbacks:
                context_window_fallbacks_type_0_item = context_window_fallbacks_type_0_item_data.to_dict()
                context_window_fallbacks.append(context_window_fallbacks_type_0_item)

        else:
            context_window_fallbacks = self.context_window_fallbacks

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if routing_strategy_args is not UNSET:
            field_dict["routing_strategy_args"] = routing_strategy_args
        if routing_strategy is not UNSET:
            field_dict["routing_strategy"] = routing_strategy
        if model_group_retry_policy is not UNSET:
            field_dict["model_group_retry_policy"] = model_group_retry_policy
        if allowed_fails is not UNSET:
            field_dict["allowed_fails"] = allowed_fails
        if cooldown_time is not UNSET:
            field_dict["cooldown_time"] = cooldown_time
        if num_retries is not UNSET:
            field_dict["num_retries"] = num_retries
        if timeout is not UNSET:
            field_dict["timeout"] = timeout
        if max_retries is not UNSET:
            field_dict["max_retries"] = max_retries
        if retry_after is not UNSET:
            field_dict["retry_after"] = retry_after
        if fallbacks is not UNSET:
            field_dict["fallbacks"] = fallbacks
        if context_window_fallbacks is not UNSET:
            field_dict["context_window_fallbacks"] = context_window_fallbacks

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.update_router_config_context_window_fallbacks_type_0_item import (
            UpdateRouterConfigContextWindowFallbacksType0Item,
        )
        from ..models.update_router_config_fallbacks_type_0_item import UpdateRouterConfigFallbacksType0Item
        from ..models.update_router_config_model_group_retry_policy_type_0 import (
            UpdateRouterConfigModelGroupRetryPolicyType0,
        )
        from ..models.update_router_config_routing_strategy_args_type_0 import (
            UpdateRouterConfigRoutingStrategyArgsType0,
        )

        d = src_dict.copy()

        def _parse_routing_strategy_args(
            data: object,
        ) -> Union["UpdateRouterConfigRoutingStrategyArgsType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                routing_strategy_args_type_0 = UpdateRouterConfigRoutingStrategyArgsType0.from_dict(data)

                return routing_strategy_args_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateRouterConfigRoutingStrategyArgsType0", None, Unset], data)

        routing_strategy_args = _parse_routing_strategy_args(d.pop("routing_strategy_args", UNSET))

        def _parse_routing_strategy(data: object) -> Union[None, Unset, str]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, str], data)

        routing_strategy = _parse_routing_strategy(d.pop("routing_strategy", UNSET))

        def _parse_model_group_retry_policy(
            data: object,
        ) -> Union["UpdateRouterConfigModelGroupRetryPolicyType0", None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, dict):
                    raise TypeError()
                model_group_retry_policy_type_0 = UpdateRouterConfigModelGroupRetryPolicyType0.from_dict(data)

                return model_group_retry_policy_type_0
            except:  # noqa: E722
                pass
            return cast(Union["UpdateRouterConfigModelGroupRetryPolicyType0", None, Unset], data)

        model_group_retry_policy = _parse_model_group_retry_policy(d.pop("model_group_retry_policy", UNSET))

        def _parse_allowed_fails(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        allowed_fails = _parse_allowed_fails(d.pop("allowed_fails", UNSET))

        def _parse_cooldown_time(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        cooldown_time = _parse_cooldown_time(d.pop("cooldown_time", UNSET))

        def _parse_num_retries(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        num_retries = _parse_num_retries(d.pop("num_retries", UNSET))

        def _parse_timeout(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        timeout = _parse_timeout(d.pop("timeout", UNSET))

        def _parse_max_retries(data: object) -> Union[None, Unset, int]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, int], data)

        max_retries = _parse_max_retries(d.pop("max_retries", UNSET))

        def _parse_retry_after(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        retry_after = _parse_retry_after(d.pop("retry_after", UNSET))

        def _parse_fallbacks(data: object) -> Union[List["UpdateRouterConfigFallbacksType0Item"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                fallbacks_type_0 = []
                _fallbacks_type_0 = data
                for fallbacks_type_0_item_data in _fallbacks_type_0:
                    fallbacks_type_0_item = UpdateRouterConfigFallbacksType0Item.from_dict(fallbacks_type_0_item_data)

                    fallbacks_type_0.append(fallbacks_type_0_item)

                return fallbacks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["UpdateRouterConfigFallbacksType0Item"], None, Unset], data)

        fallbacks = _parse_fallbacks(d.pop("fallbacks", UNSET))

        def _parse_context_window_fallbacks(
            data: object,
        ) -> Union[List["UpdateRouterConfigContextWindowFallbacksType0Item"], None, Unset]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            try:
                if not isinstance(data, list):
                    raise TypeError()
                context_window_fallbacks_type_0 = []
                _context_window_fallbacks_type_0 = data
                for context_window_fallbacks_type_0_item_data in _context_window_fallbacks_type_0:
                    context_window_fallbacks_type_0_item = UpdateRouterConfigContextWindowFallbacksType0Item.from_dict(
                        context_window_fallbacks_type_0_item_data
                    )

                    context_window_fallbacks_type_0.append(context_window_fallbacks_type_0_item)

                return context_window_fallbacks_type_0
            except:  # noqa: E722
                pass
            return cast(Union[List["UpdateRouterConfigContextWindowFallbacksType0Item"], None, Unset], data)

        context_window_fallbacks = _parse_context_window_fallbacks(d.pop("context_window_fallbacks", UNSET))

        update_router_config = cls(
            routing_strategy_args=routing_strategy_args,
            routing_strategy=routing_strategy,
            model_group_retry_policy=model_group_retry_policy,
            allowed_fails=allowed_fails,
            cooldown_time=cooldown_time,
            num_retries=num_retries,
            timeout=timeout,
            max_retries=max_retries,
            retry_after=retry_after,
            fallbacks=fallbacks,
            context_window_fallbacks=context_window_fallbacks,
        )

        update_router_config.additional_properties = d
        return update_router_config

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
