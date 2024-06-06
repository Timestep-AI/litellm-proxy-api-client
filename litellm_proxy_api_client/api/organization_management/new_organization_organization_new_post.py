from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...models.new_organization_request import NewOrganizationRequest
from ...models.new_organization_response import NewOrganizationResponse
from ...types import Response


def _get_kwargs(
    *,
    body: NewOrganizationRequest,
) -> Dict[str, Any]:
    headers: Dict[str, Any] = {}

    _kwargs: Dict[str, Any] = {
        "method": "post",
        "url": "/organization/new",
    }

    _body = body.to_dict()

    _kwargs["json"] = _body
    headers["Content-Type"] = "application/json"

    _kwargs["headers"] = headers
    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, NewOrganizationResponse]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = NewOrganizationResponse.from_dict(response.json())

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
) -> Response[Union[HTTPValidationError, NewOrganizationResponse]]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    body: NewOrganizationRequest,
) -> Response[Union[HTTPValidationError, NewOrganizationResponse]]:
    r"""New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - `organization_alias`: *str* = The name of the organization.
    - `models`: *List* = The models the organization has access to.
    - `budget_id`: *Optional[str]* = The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - `max_budget`: *Optional[float]* = Max budget for org
    - `tpm_limit`: *Optional[int]* = Max tpm limit for org
    - `rpm_limit`: *Optional[int]* = Max rpm limit for org
    - `model_max_budget`: *Optional[dict]* = Max budget for a specific model
    - `budget_duration`: *Optional[str]* = Frequency of reseting org budget

    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, NewOrganizationResponse]]
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
    body: NewOrganizationRequest,
) -> Optional[Union[HTTPValidationError, NewOrganizationResponse]]:
    r"""New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - `organization_alias`: *str* = The name of the organization.
    - `models`: *List* = The models the organization has access to.
    - `budget_id`: *Optional[str]* = The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - `max_budget`: *Optional[float]* = Max budget for org
    - `tpm_limit`: *Optional[int]* = Max tpm limit for org
    - `rpm_limit`: *Optional[int]* = Max rpm limit for org
    - `model_max_budget`: *Optional[dict]* = Max budget for a specific model
    - `budget_duration`: *Optional[str]* = Frequency of reseting org budget

    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, NewOrganizationResponse]
    """

    return sync_detailed(
        client=client,
        body=body,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    body: NewOrganizationRequest,
) -> Response[Union[HTTPValidationError, NewOrganizationResponse]]:
    r"""New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - `organization_alias`: *str* = The name of the organization.
    - `models`: *List* = The models the organization has access to.
    - `budget_id`: *Optional[str]* = The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - `max_budget`: *Optional[float]* = Max budget for org
    - `tpm_limit`: *Optional[int]* = Max tpm limit for org
    - `rpm_limit`: *Optional[int]* = Max rpm limit for org
    - `model_max_budget`: *Optional[dict]* = Max budget for a specific model
    - `budget_duration`: *Optional[str]* = Frequency of reseting org budget

    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, NewOrganizationResponse]]
    """

    kwargs = _get_kwargs(
        body=body,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    body: NewOrganizationRequest,
) -> Optional[Union[HTTPValidationError, NewOrganizationResponse]]:
    r"""New Organization

     Allow orgs to own teams

    Set org level budgets + model access.

    Only admins can create orgs.

    # Parameters

    - `organization_alias`: *str* = The name of the organization.
    - `models`: *List* = The models the organization has access to.
    - `budget_id`: *Optional[str]* = The id for a budget (tpm/rpm/max budget) for the organization.
    ### IF NO BUDGET ID - CREATE ONE WITH THESE PARAMS ###
    - `max_budget`: *Optional[float]* = Max budget for org
    - `tpm_limit`: *Optional[int]* = Max tpm limit for org
    - `rpm_limit`: *Optional[int]* = Max rpm limit for org
    - `model_max_budget`: *Optional[dict]* = Max budget for a specific model
    - `budget_duration`: *Optional[str]* = Frequency of reseting org budget

    Case 1: Create new org **without** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"max_budget\": 100
    }'


    ```

    Case 2: Create new org **with** a budget_id

    ```bash
    curl --location 'http://0.0.0.0:4000/organization/new'
    --header 'Authorization: Bearer sk-1234'
    --header 'Content-Type: application/json'
    --data '{
        \"organization_alias\": \"my-secret-org\",
        \"models\": [\"model1\", \"model2\"],
        \"budget_id\": \"428eeaa8-f3ac-4e85-a8fb-7dc8d7aa8689\"
    }'
    ```

    Args:
        body (NewOrganizationRequest):

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, NewOrganizationResponse]
    """

    return (
        await asyncio_detailed(
            client=client,
            body=body,
        )
    ).parsed
