from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.update_team_request import UpdateTeamRequest
from ...types import Response


def _get_kwargs(
    *,
    body: UpdateTeamRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/team/update",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[Any, HTTPValidationError]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = response.json()
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
) -> Response[Union[Any, HTTPValidationError]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Example - update team TPM Limit

    ```
    curl --location 'http://0.0.0.0:8000/team/update'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"team_id\": \"litellm-test-client-id-new\",
        \"tpm_limit\": 100
    }'
    ```

    Args:
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Example - update team TPM Limit

    ```
    curl --location 'http://0.0.0.0:8000/team/update'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"team_id\": \"litellm-test-client-id-new\",
        \"tpm_limit\": 100
    }'
    ```

    Args:
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Example - update team TPM Limit

    ```
    curl --location 'http://0.0.0.0:8000/team/update'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"team_id\": \"litellm-test-client-id-new\",
        \"tpm_limit\": 100
    }'
    ```

    Args:
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[Any, HTTPValidationError]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: UpdateTeamRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Update Team

     Use `/team/member_add` AND `/team/member/delete` to add/remove new team members

    You can now update team budget / rate limits via /team/update

    Parameters:
    - team_id: str - The team id of the user. Required param.
    - team_alias: Optional[str] - User defined team alias
    - metadata: Optional[dict] - Metadata for team, store information for team. Example metadata =
    {\"team\": \"core-infra\", \"app\": \"app2\", \"email\": \"ishaan@berri.ai\" }
    - tpm_limit: Optional[int] - The TPM (Tokens Per Minute) limit for this team - all keys with this
    team_id will have at max this TPM limit
    - rpm_limit: Optional[int] - The RPM (Requests Per Minute) limit for this team - all keys associated
    with this team_id will have at max this RPM limit
    - max_budget: Optional[float] - The maximum budget allocated to the team - all keys for this team_id
    will have at max this max_budget
    - models: Optional[list] - A list of models associated with the team - all keys for this team_id
    will have at most, these models. If empty, assumes all models are allowed.
    - blocked: bool - Flag indicating if the team is blocked or not - will stop all calls from keys with
    this team_id.

    Example - update team TPM Limit

    ```
    curl --location 'http://0.0.0.0:8000/team/update'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data-raw '{
        \"team_id\": \"litellm-test-client-id-new\",
        \"tpm_limit\": 100
    }'
    ```

    Args:
        body (UpdateTeamRequest): UpdateTeamRequest, used by /team/update when you need to update
            a team

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

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[Any, HTTPValidationError]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
