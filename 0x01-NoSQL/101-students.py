#!/usr/bin/env python3

"""
This module contains a function that sorts average score in desc order
"""

from pymongo import MongoClient


def top_students(mongo_collection):
    """
    Returns all students sorted by average score
    Args:
        mongo_collection: pymongo collection object
    """

    pipeline = mongo_collection.aggregate([
    {
        "$group": {
            "_id": None,
            "averageScore": {"$avg": "$score"}
        }
    },
    {
        '$sort': {'averageScore': -1}
    }
])
    return pipeline