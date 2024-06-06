from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.team_member_add_request import TeamMemberAddRequest
from ...types import Response


def _get_kwargs(
    *,
    body: TeamMemberAddRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/team/member_add",
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
    body: TeamMemberAddRequest,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Team Member Add

     [BETA]

    Add new members (either via user_email or user_id) to a team

    If user doesn't exist, new user row will also be added to User Table

    ```

    curl -X POST 'http://0.0.0.0:4000/team/member_add'     -H 'Authorization: Bearer sk-1234'     -H
    'Content-Type: application/json'     -d '{\"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
    \"member\": {\"role\": \"user\", \"user_id\": \"krrish247652@berri.ai\"}}'

    ```

    Args:
        body (TeamMemberAddRequest):

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
    body: TeamMemberAddRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Team Member Add

     [BETA]

    Add new members (either via user_email or user_id) to a team

    If user doesn't exist, new user row will also be added to User Table

    ```

    curl -X POST 'http://0.0.0.0:4000/team/member_add'     -H 'Authorization: Bearer sk-1234'     -H
    'Content-Type: application/json'     -d '{\"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
    \"member\": {\"role\": \"user\", \"user_id\": \"krrish247652@berri.ai\"}}'

    ```

    Args:
        body (TeamMemberAddRequest):

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
    body: TeamMemberAddRequest,
) -> Response[Union[Any, HTTPValidationError]]:
    r"""Team Member Add

     [BETA]

    Add new members (either via user_email or user_id) to a team

    If user doesn't exist, new user row will also be added to User Table

    ```

    curl -X POST 'http://0.0.0.0:4000/team/member_add'     -H 'Authorization: Bearer sk-1234'     -H
    'Content-Type: application/json'     -d '{\"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
    \"member\": {\"role\": \"user\", \"user_id\": \"krrish247652@berri.ai\"}}'

    ```

    Args:
        body (TeamMemberAddRequest):

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
    body: TeamMemberAddRequest,
) -> Optional[Union[Any, HTTPValidationError]]:
    r"""Team Member Add

     [BETA]

    Add new members (either via user_email or user_id) to a team

    If user doesn't exist, new user row will also be added to User Table

    ```

    curl -X POST 'http://0.0.0.0:4000/team/member_add'     -H 'Authorization: Bearer sk-1234'     -H
    'Content-Type: application/json'     -d '{\"team_id\": \"45e3e396-ee08-4a61-a88e-16b3ce7e0849\",
    \"member\": {\"role\": \"user\", \"user_id\": \"krrish247652@berri.ai\"}}'

    ```

    Args:
        body (TeamMemberAddRequest):

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
