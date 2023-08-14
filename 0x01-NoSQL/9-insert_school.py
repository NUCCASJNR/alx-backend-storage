#!/usr/bin/env python3

"""This module inserts into a document"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a doc in a collection
    Args:
        mongo_collection: pymongo collection object
        kwargs: documents to be inserted
    """

    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
