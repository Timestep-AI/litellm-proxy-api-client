from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_team_table import LiteLLMTeamTable
from ...models.new_team_request import NewTeamRequest
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    body: NewTeamRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}
    if not isinstance(litellm_changed_by, Unset):
        headers["litellm-changed-by"] = litellm_changed_by

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/team/new",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, LiteLLMTeamTable]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = LiteLLMTeamTable.from_dict(response.json())

        return response_200
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[Union[HTTPValidationError, LiteLLMTeamTable]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewTeamRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, LiteLLMTeamTable]]:
    r"""New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'

    ```

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, LiteLLMTeamTable]]
    """

    kwargs = _get_kwargs(
        body=body,
        litellm_changed_by=litellm_changed_by,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: NewTeamRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, LiteLLMTeamTable]]:
    r"""New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'

    ```

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, LiteLLMTeamTable]
    """

    return sync_detailed(
        client=client,
        body=body,
        litellm_changed_by=litellm_changed_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewTeamRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Response[Union[HTTPValidationError, LiteLLMTeamTable]]:
    r"""New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'

    ```

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, LiteLLMTeamTable]]
    """

    kwargs = _get_kwargs(
        body=body,
        litellm_changed_by=litellm_changed_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewTeamRequest,
    litellm_changed_by: Union[None, Unset, str] = UNSET,
) -> Optional[Union[HTTPValidationError, LiteLLMTeamTable]]:
    r"""New Team

     Allow users to create a new team. Apply user permissions to their team.

    👉 [Detailed Doc on setting team budgets](https://docs.litellm.ai/docs/proxy/team_budgets)


    Parameters:
    - team_alias: Optional[str] - User defined team alias
    - team_id: Optional[str] - The team id of the user. If none passed, we'll generate it.
    - members_with_roles: List[{\"role\": \"admin\" or \"user\", \"user_id\": \"<user-id>\"}] - A list
    of users and their roles in the team. Get user_id when making a new user via `/user/new`.
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"extra_info\": \"some info\"}
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - budget_duration: Optional[str] - The duration of the budget for the team. Doc
    [here](https://docs.litellm.ai/docs/proxy/team_budgets)
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Returns:
    - team_id: (str) Unique team id - used for tracking spend across multiple keys for same team id.

    _deprecated_params:
    - admins: list - A list of user_id's for the admin role
    - users: list - A list of user_id's for the user role

    Example Request:
    ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
      \"team_alias\": \"my-new-team_2\",
      \"members_with_roles\": [{\"role\": \"admin\", \"user_id\": \"user-1234\"},
        {\"role\": \"user\", \"user_id\": \"user-2434\"}]
    }'

    ```

     ```
    curl --location 'http://0.0.0.0:4000/team/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
                \"team_alias\": \"QA Prod Bot\",
                \"max_budget\": 0.000000001,
                \"budget_duration\": \"1d\"
            }'

    ```

    Args:
        litellm_changed_by (Union[None, Unset, str]): The litellm-changed-by header enables
            tracking of actions performed by authorized users on behalf of other users, providing an
            audit trail for accountability
        body (NewTeamRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, LiteLLMTeamTable]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
            litellm_changed_by=litellm_changed_by,
        )
    ).parsed
