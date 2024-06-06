from http import HTTPStatus
from typing import Any, Dict, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.http_validation_error import HTTPValidationError
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    model_group: str,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Dict[str, Any]:
    params: Dict[str, Any] = {}

    params["model_group"] = model_group

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
        "url": "/global/activity/exceptions",
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
    model_group: str,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[HTTPValidationError]:
    r"""Get Global Activity Exceptions

     Get number of API Requests, total tokens through proxy

    {
        \"daily_data\": [
                const chartdata = [
                {
                date: 'Jan 22',
                num_rate_limit_exceptions: 10,
                },
                {
                date: 'Jan 23',
                num_rate_limit_exceptions: 10,
                },
        ],
        \"sum_api_exceptions\": 20,
    }

    Args:
        model_group (str): Filter by model group
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        model_group=model_group,
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
    model_group: str,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[HTTPValidationError]:
    r"""Get Global Activity Exceptions

     Get number of API Requests, total tokens through proxy

    {
        \"daily_data\": [
                const chartdata = [
                {
                date: 'Jan 22',
                num_rate_limit_exceptions: 10,
                },
                {
                date: 'Jan 23',
                num_rate_limit_exceptions: 10,
                },
        ],
        \"sum_api_exceptions\": 20,
    }

    Args:
        model_group (str): Filter by model group
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
        model_group=model_group,
        start_date=start_date,
        end_date=end_date,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    model_group: str,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Response[HTTPValidationError]:
    r"""Get Global Activity Exceptions

     Get number of API Requests, total tokens through proxy

    {
        \"daily_data\": [
                const chartdata = [
                {
                date: 'Jan 22',
                num_rate_limit_exceptions: 10,
                },
                {
                date: 'Jan 23',
                num_rate_limit_exceptions: 10,
                },
        ],
        \"sum_api_exceptions\": 20,
    }

    Args:
        model_group (str): Filter by model group
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[HTTPValidationError]
    """

    kwargs = _get_kwargs(
        model_group=model_group,
        start_date=start_date,
        end_date=end_date,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    model_group: str,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
) -> Optional[HTTPValidationError]:
    r"""Get Global Activity Exceptions

     Get number of API Requests, total tokens through proxy

    {
        \"daily_data\": [
                const chartdata = [
                {
                date: 'Jan 22',
                num_rate_limit_exceptions: 10,
                },
                {
                date: 'Jan 23',
                num_rate_limit_exceptions: 10,
                },
        ],
        \"sum_api_exceptions\": 20,
    }

    Args:
        model_group (str): Filter by model group
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
            model_group=model_group,
            start_date=start_date,
            end_date=end_date,
        )
    ).parsed
