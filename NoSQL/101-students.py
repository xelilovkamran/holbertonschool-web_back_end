#!/usr/bin/env python3
"""students
"""

import pymongo


def top_students(mongo_collection):
    """returns all students sorted by average score
    """

    top_students = mongo_collection.aggregate([
        {
            "$project": {
                "name": "$name",
                "averageScore": {"$avg": "$topics.score"}
            }
        },
        {"$sort": {"averageScore": -1}}
    ])

    return top_students
