import pytest

from planetstac.search import Search, ItemIds
from .helpers import search_filter


@pytest.fixture
def item_types():
    return {
        "FAIL": "BAD",
        "PASS": "PSScene",
    }


@pytest.fixture
def valid_items():
    return ItemIds("PSScene", ["20180831_152918_1033", "20180830_153042_0f52"])


def test_item_type(item_types):
    with pytest.raises(ValueError) as _:
        Search(item_types["FAIL"])


def test_search(search_filter, item_types, valid_items):
    search = Search(item_types["PASS"])
    items = search.get(search_filter)
    assert items == valid_items
