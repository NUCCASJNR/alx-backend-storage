#!/usr/bin/env python3

"""Contains a cache class"""

from typing import Union, Callable
from uuid import uuid4
from functools import wraps

import redis


def count_calls(method: Callable) -> Callable:
    """
    Decorator function that takes in a callable
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """increment count"""
        if isinstance(self._redis, redis.Redis):
            self._redis.incr(method.__qualname__)
        return method(self, *args, **kwargs)
    return wrapper


def call_history(method: Callable) -> Callable:
    """
    Decorator function to store the history of inputs
      and outputs for a function
    """
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Store inputs and outputs in Redis lists"""
        if isinstance(self._redis, redis.Redis):
            inputs_key = f"{method.__qualname__}:inputs"
            outputs_key = f"{method.__qualname__}:outputs"

            # Store input arguments
            self._redis.rpush(inputs_key, str(args))

            # Call the original method and get the output
            result = method(self, *args, **kwargs)

            # Store the output
            self._redis.rpush(outputs_key, str(result))

            return result
        return method(self, *args, **kwargs)
    return wrapper


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
        self._redis = redis.Redis()
        self._redis.flushdb()

    @call_history
    @count_calls
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """
        Generate random id, stes it as the key and use the data
        passed to the function as the value
        """
        key: str = str(uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> [int, bytes, float, str]:
        """
        convert to any desired format
        """

        data = self._redis.get(key)
        if fn is not None:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        """
        REtrieves a string from redis using the provided key and
        returns it as a sring
        Args:
            key: str retrieved from redis
        Return:
                str
        """
        return self.get(key, fn=lambda x: x.decode("utf-8"))

    def get_int(self, key: int) -> int:
        """
           REtrieves a int from redis using the provided key and
        returns it as an integer
        Args:
            key: int retrieved from redis
        Return:
                int
        """

        return self.get(key, fn=lambda x: int(x))
