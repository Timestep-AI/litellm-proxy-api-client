from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union, cast

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.member import Member


T = TypeVar("T", bound="TeamMemberAddRequest")


@_attrs_define
class TeamMemberAddRequest:
    """
    Attributes:
        team_id (str):
        member (Union['Member', List['Member']]):
        max_budget_in_team (Union[None, Unset, float]):
    """

    team_id: str
    member: Union["Member", List["Member"]]
    max_budget_in_team: Union[None, Unset, float] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        team_id = self.team_id

        member: Union[Dict[str, Any], List[Dict[str, Any]]]
        if isinstance(self.member, list):
            member = []
            for member_type_0_item_data in self.member:
                member_type_0_item = member_type_0_item_data.to_dict()
                member.append(member_type_0_item)

        else:
            member = self.member.to_dict()

        max_budget_in_team: Union[None, Unset, float]
        if isinstance(self.max_budget_in_team, Unset):
            max_budget_in_team = UNSET
        else:
            max_budget_in_team = self.max_budget_in_team

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update(
            {
                "team_id": team_id,
                "member": member,
            }
        )
        if max_budget_in_team is not UNSET:
            field_dict["max_budget_in_team"] = max_budget_in_team

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.member import Member

        d = src_dict.copy()
        team_id = d.pop("team_id")

        def _parse_member(data: object) -> Union["Member", List["Member"]]:
            try:
                if not isinstance(data, list):
                    raise TypeError()
                member_type_0 = []
                _member_type_0 = data
                for member_type_0_item_data in _member_type_0:
                    member_type_0_item = Member.from_dict(member_type_0_item_data)

                    member_type_0.append(member_type_0_item)

                return member_type_0
            except:  # noqa: E722
                pass
            if not isinstance(data, dict):
                raise TypeError()
            member_type_1 = Member.from_dict(data)

            return member_type_1

        member = _parse_member(d.pop("member"))

        def _parse_max_budget_in_team(data: object) -> Union[None, Unset, float]:
            if data is None:
                return data
            if isinstance(data, Unset):
                return data
            return cast(Union[None, Unset, float], data)

        max_budget_in_team = _parse_max_budget_in_team(d.pop("max_budget_in_team", UNSET))

        team_member_add_request = cls(
            team_id=team_id,
            member=member,
            max_budget_in_team=max_budget_in_team,
        )

        team_member_add_request.additional_properties = d
        return team_member_add_request

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
