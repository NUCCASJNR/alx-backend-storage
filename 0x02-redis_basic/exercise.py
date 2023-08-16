#!/usr/bin/env python3

"""Contains a cache class"""

from uuid import uuid4
from redis import Redis
from typing import Union


class Cache:
    """
    A cache class
    """
    def __init__(self):
        """
        Initializes the cache class
        Args:
            redis: Instance of the redis class
        """
        self.__redis = Redis(host="127.0.0.1", port=6379)
        self.__redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate random id, stes it as the key and use the data
        passed to the function as the value
        """
        key: str = str(uuid4())
        self.__redis.set(key, data)
        return key