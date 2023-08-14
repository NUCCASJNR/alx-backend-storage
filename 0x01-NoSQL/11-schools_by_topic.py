#!/usr/bin/env python3

"""

This module contains a function that returns the list of school
having a specific topic
"""


def schools_by_topic(mongo_collection, topic):
    """
    returns the list of school having a specific topic
    Args:
        topic: topic been searched for
        mongo_collection: pymongo collection object
    """
    searching = ({"topics": topic})
    result = mongo_collection.find(searching)
    return result
