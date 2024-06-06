from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    json_start_date: Union[None, Unset, str]
    if isinstance(start_date, Unset):
        json_start_date = UNSET
    else:
        json_start_date = start_date
    params["start_date"] = json_start_date

    json_end_date: Union[None, Unset, str]
    if isinstance(end_date, Unset):
        json_end_date = UNSET
    else:
        json_end_date = end_date
    params["end_date"] = json_end_date

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/global/activity/model",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[HTTPValidationError]:
    if response.status_code == HTTPStatus.UNPROCESSABLE_ENTITY:
        response_422 = HTTPValidationError.from_dict(response.json())

        return response_422
    if client.raise_on_unexpected_status:
        raise errors.UnexpectedStatus(response.status_code, response.content)
    else:
        return None


def _build_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Response[HTTPValidationError]:
    return Response(
        status_code=HTTPStatus(response.status_code),
        content=response.content,
        headers=response.headers,
        parsed=_parse_response(client=client, response=response),
    )


def sync_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[HTTPValidationError]:
    r"""Get Global Activity Model

     Get number of API Requests, total tokens through proxy - Grouped by MODEL

    [
        {
            \"model\": \"gpt-4\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
        {
            \"model\": \"azure/gpt-4-turbo\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
    ]

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
    )

    response = client.get_httpx_client().request(
        **kwargs,
    )

    return _build_response(client=client, response=response)


def sync(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[HTTPValidationError]:
    r"""Get Global Activity Model

     Get number of API Requests, total tokens through proxy - Grouped by MODEL

    [
        {
            \"model\": \"gpt-4\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
        {
            \"model\": \"azure/gpt-4-turbo\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
    ]

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[HTTPValidationError]:
    r"""Get Global Activity Model

     Get number of API Requests, total tokens through proxy - Grouped by MODEL

    [
        {
            \"model\": \"gpt-4\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
        {
            \"model\": \"azure/gpt-4-turbo\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
    ]

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[HTTPValidationError]:
    r"""Get Global Activity Model

     Get number of API Requests, total tokens through proxy - Grouped by MODEL

    [
        {
            \"model\": \"gpt-4\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
        {
            \"model\": \"azure/gpt-4-turbo\",
            \"daily_data\": [
                    const chartdata = [
                    {
                    date: 'Jan 22',
                    api_requests: 10,
                    total_tokens: 2000
                    },
                    {
                    date: 'Jan 23',
                    api_requests: 10,
                    total_tokens: 12
                    },
            ],
            \"sum_api_requests\": 20,
            \"sum_total_tokens\": 2012

        },
    ]

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        HTTPValidationError
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
