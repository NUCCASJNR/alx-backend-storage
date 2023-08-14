#!/usr/bin/env python3

"""This module contains a function that Updates
all school docs
"""


def update_topics(mongo_collection, name, topics):
    """
    changes all topics of a school document based on the name
    Args:
        mongo_collection: pymongo collection object
        name: name of the school to be updated
        topics: list of topics approached in the school
    """

    filter = {"name": name}
    update_operation = {"$set": {"topics": topics}}
    result = mongo_collection.update_many(filter, update_operation)
    return result
