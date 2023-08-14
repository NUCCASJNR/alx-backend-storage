#!/usr/bin/env python3

"""This module inserts into a document"""


def insert_school(mongo_collection, **kwargs):
    """
    insert a doc in a collection
    """

    docs = [kwargs]
    mongo_collection.insert_many(docs)
    return (kwargs['_id'])
