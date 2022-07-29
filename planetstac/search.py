import os
import requests
from requests.auth import HTTPBasicAuth
from typing import Union, List
from dataclasses import dataclass
import pprint

from item_types import AVAILABLE_ITEM_TYPES


@dataclass
class ItemIds:
    item_type: str
    ids: List[str]

    def __str__(self) -> str:
        return pprint.pformat(
            {
                "item_type": self.item_type,
                "ids": self.ids,
                "count": len(self.ids),
            },
            depth=1,
            sort_dicts=False,
        )


class Search:
    def __init__(self, item_type, api_key) -> None:
        self._item_type = item_type
        self._api_key = api_key
        assert self.__validate_item_type() == True, "Invalid item type"
        pass

    def get(self, filter=None) -> ItemIds:
        req = self.__construct_request(filter)
        response = requests.post(
            "https://api.planet.com/data/v1/quick-search",
            auth=HTTPBasicAuth(os.getenv("PL_API_KEY"), ""),
            json=req,
        )
        assert response.ok == True, response.text
        self._response = response
        self._ids = [feature["id"] for feature in response.json()["features"]]
        print(response.json()["features"][1])
        return ItemIds(self._item_type, self._ids)

    def __validate_item_type(self) -> bool:
        if self._item_type not in AVAILABLE_ITEM_TYPES:
            return False
        return True

    def __construct_request(self, filter) -> dict:
        search_request = {
            "item_types": [self._item_type],
        }
        if filter is not None:
            search_request["filter"] = filter

        return search_request

    @property
    def ids(self) -> Union[None, List[str]]:
        return self._ids

    @property
    def response(self):
        return self._response

    @property
    def item_type(self):
        return self._item_type