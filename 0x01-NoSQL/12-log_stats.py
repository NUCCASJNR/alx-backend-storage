#!/usr/bin/env python3

"""This module contains a function that lists nginx stats"""


from pymongo import MongoClient

if __name__ == "__main__":
    # Establish the connection
    client = MongoClient(host="localhost", port=27017)
    # Select the database
    db = client["logs"]
    # Select the collection
    collection = db.nginx
    total_logs = collection.count_documents({})
    print(f"{total_logs} logs")
    status = collection.count_documents({"path": "/status"})
    # get_log = collection.count_documents({"method": "GET"})
    # post_log = collection.count_documents({"method": "POST"})
    # put_log = collection.count_documents({"method": "PUT"})
    # patch_log = collection.count_documents({"method": "PATCH"})
    # delete_log = collection.count_documents({"method": "DELETE"})

    # logs_dict = {"method GET": get_log, "method POST": post_log,
    #              "method PUT": put_log, "method PATCH": patch_log,
    #              "method DELETE": delete_log}
    # for key, value in logs_dict.items():
    #     print(f"\t{key}: {value}")
    print("Methods:")
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\t{method}: {method_count}")
    print(f"{status} status check")
