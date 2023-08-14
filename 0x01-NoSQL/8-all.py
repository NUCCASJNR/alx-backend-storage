#!/usr/bin/env python3

"""
a Python function that lists all documents in a collection
"""


def list_all(mongo_collection):
    """
    List all docs in a collection
    """

    docs = []
    for doc in mongo_collection.find():
        docs.append(doc)
    return docs
