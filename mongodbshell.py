import pymongo
from pymongo import MongoClient
import colorama
from colorama import Fore, Back, Style
import datetime

colorama.init()

print(Fore.MAGENTA + "The following is a console application to manage your mongodb database")
session_name = input(Fore.WHITE + "What is the name of your session: ")

with open("log.txt", "w") as f:
    f.writelines(session_name + ":" + " " + str(datetime.datetime.now()))

action = input("What do you want to do? delete, add, view:")



def insert():
    cluster = MongoClient('mongodb+srv://admin:password12345@cluster0.gsfkl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
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
    cluster = MongoClient('mongodb+srv://admin:password12345@cluster0.gsfkl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    cluster_name = input("What is the cluster name?: ")
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
    cluster = MongoClient('mongodb+srv://admin:password12345@cluster0.gsfkl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority')
    cluster_name = input("What is the cluster name?: ")
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