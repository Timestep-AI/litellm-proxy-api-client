from http import HTTPStatus
from typing import Any, Dict, List, Optional, Union

import httpx

from ... import errors
from ...client import AuthenticatedClient, Client
from ...models.get_global_spend_report_global_spend_report_get_group_by_type_0 import (
    GetGlobalSpendReportGlobalSpendReportGetGroupByType0,
)
from ...models.http_validation_error import HTTPValidationError
from ...models.lite_llm_spend_logs import LiteLLMSpendLogs
from ...types import UNSET, Response, Unset


def _get_kwargs(
    *,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
    group_by: Union[
        GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset
    ] = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
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

    json_group_by: Union[None, Unset, str]
    if isinstance(group_by, Unset):
        json_group_by = UNSET
    elif isinstance(group_by, GetGlobalSpendReportGlobalSpendReportGetGroupByType0):
        json_group_by = group_by.value
    else:
        json_group_by = group_by
    params["group_by"] = json_group_by

    params = {k: v for k, v in params.items() if v is not UNSET and v is not None}

    _kwargs: Dict[str, Any] = {
        "method": "get",
        "url": "/global/spend/report",
        "params": params,
    }

    return _kwargs


def _parse_response(
    *, client: Union[AuthenticatedClient, Client], response: httpx.Response
) -> Optional[Union[HTTPValidationError, List["LiteLLMSpendLogs"]]]:
    if response.status_code == HTTPStatus.OK:
        response_200 = []
        _response_200 = response.json()
        for response_200_item_data in _response_200:
            response_200_item = LiteLLMSpendLogs.from_dict(response_200_item_data)

            response_200.append(response_200_item)

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
) -> Response[Union[HTTPValidationError, List["LiteLLMSpendLogs"]]]:
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
    group_by: Union[
        GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset
    ] = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
) -> Response[Union[HTTPValidationError, List["LiteLLMSpendLogs"]]]:
    r"""Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend
        group_by (Union[GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset]): Group
            spend by internal team or customer Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['LiteLLMSpendLogs']]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        group_by=group_by,
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
    group_by: Union[
        GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset
    ] = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
) -> Optional[Union[HTTPValidationError, List["LiteLLMSpendLogs"]]]:
    r"""Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend
        group_by (Union[GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset]): Group
            spend by internal team or customer Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['LiteLLMSpendLogs']]
    """

    return sync_detailed(
        client=client,
        start_date=start_date,
        end_date=end_date,
        group_by=group_by,
    ).parsed


async def asyncio_detailed(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
    group_by: Union[
        GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset
    ] = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
) -> Response[Union[HTTPValidationError, List["LiteLLMSpendLogs"]]]:
    r"""Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend
        group_by (Union[GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset]): Group
            spend by internal team or customer Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Response[Union[HTTPValidationError, List['LiteLLMSpendLogs']]]
    """

    kwargs = _get_kwargs(
        start_date=start_date,
        end_date=end_date,
        group_by=group_by,
    )

    response = await client.get_async_httpx_client().request(**kwargs)

    return _build_response(client=client, response=response)


async def asyncio(
    *,
    client: AuthenticatedClient,
    start_date: Union[None, Unset, str] = UNSET,
    end_date: Union[None, Unset, str] = UNSET,
    group_by: Union[
        GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset
    ] = GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM,
) -> Optional[Union[HTTPValidationError, List["LiteLLMSpendLogs"]]]:
    r"""Get Global Spend Report

     Get Daily Spend per Team, based on specific startTime and endTime. Per team, view usage by each key,
    model
    [
        {
            \"group-by-day\": \"2024-05-10\",
            \"teams\": [
                {
                    \"team_name\": \"team-1\"
                    \"spend\": 10,
                    \"keys\": [
                        \"key\": \"1213\",
                        \"usage\": {
                            \"model-1\": {
                                    \"cost\": 12.50,
                                    \"input_tokens\": 1000,
                                    \"output_tokens\": 5000,
                                    \"requests\": 100
                                },
                                \"audio-modelname1\": {
                                \"cost\": 25.50,
                                \"seconds\": 25,
                                \"requests\": 50
                        },
                        }
                    }
            ]
        ]
    }

    Args:
        start_date (Union[None, Unset, str]): Time from which to start viewing spend
        end_date (Union[None, Unset, str]): Time till which to view spend
        group_by (Union[GetGlobalSpendReportGlobalSpendReportGetGroupByType0, None, Unset]): Group
            spend by internal team or customer Default:
            GetGlobalSpendReportGlobalSpendReportGetGroupByType0.TEAM.

    Raises:
        errors.UnexpectedStatus: If the server returns an undocumented status code and Client.raise_on_unexpected_status is True.
        httpx.TimeoutException: If the request takes longer than Client.timeout.

    Returns:
        Union[HTTPValidationError, List['LiteLLMSpendLogs']]
    """

    return (
        await asyncio_detailed(
            client=client,
            start_date=start_date,
            end_date=end_date,
            group_by=group_by,
        )
    ).parsed
