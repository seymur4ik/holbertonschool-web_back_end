#!/usr/bin/env python3
"""
Function that changes all topics of a document based on a name
"""


def update_topics(mongo_collection, name, topics):
    """
    updates a document
    """
    return mongo_collection.update_many({'name': name},
                                        {'$set': {'topics': topics}},)
