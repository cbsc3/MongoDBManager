import pymongo
from pymongo import MongoClient
import colorama
from colorama import Fore, Back, Style

colorama.init()

print(Fore.MAGENTA + "The following is a console application to manage your mongodb database")
session_name = input(Fore.WHITE + "What is the name of your session: ")



action = input("What do you want to do? delete, add, view:")



def insert():
    api_key = input("Please insert your MongoDB API Token: ")
    cluster = MongoClient(api_key)
    cluster_name = input("What is the cluster name?: ")
    coll_name = input("What is the following collection name?: ")
    db = cluster[cluster_name]
    collection = db[coll_name]
    bson_obj_nameOne = input(Fore.MAGENTA + "What is the BSON obj name one?: ")
    bson_obj_nameTwo = input(Fore.GREEN + "What is the BSON obj name two?: ")
    insertOne = input("Insert one?: ")
    insertTwo = input("Insert two?: ")
    insert_dict = {bson_obj_nameOne:insertOne, bson_obj_nameTwo:insertTwo}
    print(Fore.MAGENTA + "Currently inserting data")
    collection.insert_one(insert_dict)
    repeat = input("Would you like to preform this action again?: ")
    if repeat == "n":
        exit()
    if repeat == "y":
        while True:
            insert()

def delete():
    api_key = input("Please insert your MongoDB API Token: ")
    cluster = MongoClient(api_key)
    coll_name = input("What is the following collection name?: ")
    db = cluster[cluster_name]
    collection = db[coll_name]
    bson_obj_nameOne = input("What is the BSON obj name one?: ")
    bson_obj_nameTwo = input("What is the BSON obj name two?: ")
    insertOne = input("Delete one?: ")
    insertTwo = input("Delete two?: ")
    insert_dict = {bson_obj_nameOne:insertOne, bson_obj_nameTwo:insertTwo}
    print(Fore.MAGENTA + "Currently deleting data")
    collection.delete_one(insert_dict)
    repeat = input("Would you like to preform this action again?: ")
    if repeat == "n":
        exit()
    if repeat == "y":
        while True:
            delete()

def view():
    api_key = input("Please insert your MongoDB API Token: ")
    cluster = MongoClient(api_key)
    coll_name = input("What is the following collection name?: ")
    db = cluster[cluster_name]
    collection = db[coll_name]
    results = collection.find()
    for result in results:
        print(Fore.CYAN + f"Current entries in: {coll_name}")
        print(result)
    repeat = input("Would you like to preform this action again?: ")
    if repeat == "n":
        exit()
    if repeat == "y":
        while True:
            view()



if action == "add":
    insert()
if action == "delete":
    delete()
if action == "view":
    view()
