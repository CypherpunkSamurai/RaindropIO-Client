# RaindropIO Client using cookies
# @author: CypherpunkSamurai
import json
from typing import List

import requests

__version__ = 1


class RaindropIO(object):

    def __init__(self, cookie: str, check=True):
        """
            RaindropIO Init with cookies
            @params:
                - cookie:   login cookie
                - check:    check login
            @return:
                - RaindropIO()
        """
        self.cookie = cookie
        self.headers = {
            "User-Agent": "RaindropClient (WinNT)",
            "Cookie": cookie,
        }
        # Checks
        assert "email" in self.get_user()

    def get_user(self):
        """
            Gets user info
        """
        url = "https://api.raindrop.io/v1/user"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception("invalid auth. please refresh cookies")
        return json.loads(r.text)

    def get_collections(self):
        url = "https://api.raindrop.io/v1/collections/all"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot fetch collections. {r.status_code}")
        return json.loads(r.text)

    def get_collection(
            self,
            collection_id: int,
            sort: str = "sort",
            perpage: int = 40):
        """
            Gets a collection list by id
        """
        url = f"https://api.raindrop.io/v1/raindrops/{collection_id}?sort={sort}&perpage={perpage}&version=2"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot fetch collection. {r.status_code}")
        return json.loads(r.text)

    def get_tags(self, perpage: int = 40):
        """
            Get tags
        """
        url = f"https://api.raindrop.io/v1/filters/0?perpage={perpage}&version=2&tagsSort=_id"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot fetch tags. {r.status_code}")
        return json.loads(r.text)

    def get_stats(self):
        """
            Get user stats
        """
        url = "https://api.raindrop.io/v1/user/stats"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot fetch user stats. {r.status_code}")
        return json.loads(r.text)

    def _parse(self, url):
        """
            Parse URL
        """
        url = f"https://api.raindrop.io/v1/import/url/parse?url={url}"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot fetch user stats. {r.status_code}")
        if "item" not in r.text:
            raise Exception(f"cannot parse url. {r.status_code}")
        return json.loads(r.text)["item"]

    def add_url(self, url, collection_id: int = 0):
        """
            Adds the url to the raindrops
        """
        url = "https://api.raindrop.io/v1/raindrop"
        # Data
        data = self._parse(url)
        data["collectionId"] = collection_id
        r = requests.post(url, headers=self.headers, data=data)
        # Check
        if r.status_code != 200:
            raise Exception(
                f"cannot add raindrop to collection {collection_id}. {r.status_code}")
        return json.loads(r.text)

    def trash_raindrops(self, raindrop_ids: List[int]):
        """
            Trash Raindrops
        """
        url = "https://api.raindrop.io/v1/raindrops/-1?sort=sort&perpage=40&version=2&dangerAll=true"
        # Data
        data = {
            "ids": raindrop_ids
        }
        r = requests.post(url, headers=self.headers, data=data)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot trash raindrop ids. {r.status_code}")
        return json.loads(r.text)

    def get_trash(self, perpage: int = 40):
        """
            Get Trash folder
        """
        url = f"https://api.raindrop.io/v1/raindrops/-99?sort=sort&perpage={perpage}&version=2"
        r = requests.get(url, headers=self.headers)
        # Check
        if r.status_code != 200:
            raise Exception(f"cannot get trash list. {r.status_code}")
        return json.loads(r.text)

    def trash_raindrop_permanent(self, raindrop_ids: List[int]):
        """
            Permanently removes raindrops
        """
        url = "https://api.raindrop.io/v1/raindrops/-99?sort=sort&perpage=40&version=2&dangerAll=true"
        # Data
        data = {
            "ids": raindrop_ids
        }
        r = requests.post(url, headers=self.headers, data=data)
        # Check
        if r.status_code != 200:
            raise Exception(
                f"cannot permanently trash raindrop ids. {r.status_code}")
        return json.loads(r.text)
