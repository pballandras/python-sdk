# -*- coding: utf-8 -*-
"""
Test suite for the community-developed Python SDK for interacting with Lacework APIs.
"""

import pytest

from datetime import datetime, timedelta, timezone

from laceworksdk.api.cloud_activities import CloudActivitiesAPI

# Build start/end times
current_time = datetime.now(timezone.utc)
start_time = current_time - timedelta(days=1)
start_time = start_time.strftime("%Y-%m-%dT%H:%M:%SZ")
end_time = current_time.strftime("%Y-%m-%dT%H:%M:%SZ")


# Tests

def test_cloud_activities_api_object_creation(api):
    assert isinstance(api.cloud_activities, CloudActivitiesAPI)


def test_cloud_activities_api_env_object_creation(api_env):
    assert isinstance(api_env.cloud_activities, CloudActivitiesAPI)


@pytest.mark.ci_exempt
def test_cloud_activities_api_get(api):
    response = api.cloud_activities.get()
    assert "data" in response.keys()


def test_cloud_activities_api_get_by_date(api):
    response = api.cloud_activities.get(start_time=start_time, end_time=end_time)
    assert "data" in response.keys()


def test_cloud_activities_api_search(api):
    response = api.cloud_activities.search(query_data={
        "timeFilter": {
            "startTime": start_time,
            "endTime": end_time
        },
        "filters": [
            {
                "expression": "eq",
                "field": "eventModel",
                "value": "CloudTrailCep"
            }
        ],
        "returns": [
            "eventType",
            "eventActor"
        ]
    })
    assert "data" in response.keys()
