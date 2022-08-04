import pytest


@pytest.fixture
def search_filter():
    geom = {
        "type": "Polygon",
        "coordinates": [
            [
                [-78.67905020713806, 35.780212341409914],
                [-78.67378234863281, 35.780212341409914],
                [-78.67378234863281, 35.782684221280086],
                [-78.67905020713806, 35.782684221280086],
                [-78.67905020713806, 35.780212341409914],
            ]
        ],
    }

    geometry_filter = {
        "type": "GeometryFilter",
        "field_name": "geometry",
        "config": geom,
    }

    # filter images acquired in a certain date range
    date_range_filter = {
        "type": "DateRangeFilter",
        "field_name": "acquired",
        "config": {
            "gte": "2018-08-30T00:00:00.000Z",
            "lte": "2018-09-01T00:00:00.000Z",
        },
    }

    # filter any images which are more than 50% clouds
    cloud_cover_filter = {
        "type": "RangeFilter",
        "field_name": "cloud_cover",
        "config": {"lte": 0.5},
    }

    asset_filter = {"type": "AssetFilter", "config": ["ortho_analytic_4b_sr"]}

    # create a filter that combines our geo and date filters
    # could also use an "OrFilter"
    combined_filter = {
        "type": "AndFilter",
        "config": [
            geometry_filter,
            date_range_filter,
            cloud_cover_filter,
            asset_filter,
        ],
    }
    return combined_filter
