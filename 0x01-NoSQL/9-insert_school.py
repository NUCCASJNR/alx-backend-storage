#!/usr/bin/env python3

"""This module inserts into a document"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a doc in a collection
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
