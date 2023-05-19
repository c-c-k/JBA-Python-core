#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""pymongo usage reference and example

Based on the official pymongo tutorial
"""

import datetime
import os

from bson.objectid import ObjectId
from dotenv import load_dotenv
import pymongo

def get_client_by_uri():
    client = pymongo.MongoClient(os.environ['MONGODB_FULL_URI'])
    return client

def get_client_by_params():
    client = pymongo.MongoClient(
            host=os.environ['MONGODB_HOST'],
            port=int(os.environ['MONGODB_PORT']),
            authsource=os.environ['MONGODB_AUTH_DATABASE'],
            username=os.environ['MONGODB_USER'],
            password=os.environ['MONGODB_PASSWORD'],
            )
    return client

def get_db(client):
    db = client[os.environ['MONGODB_DATABASE']]
    return db

def clean_db(client, db):
    client.drop_database(db)
    # for collection in db.list_collection_names():
    #     db[collection].drop()

def create_single_document(collection):
    print('insert a single document with an '
          'automatically generated ObjectId _id into a collection')
    result = collection.insert_one({
        'type': 'special 1',
        'string': 'string value',
        'number_int': 1,
        'number_float': 1.1,
        'list': [1, 2, 3, 4],
        'dictionary': {'a': 1, 'b': 2},
        'date': datetime.datetime.now()
    })
    print('insert one result:')
    print(f'status: {result.acknowledged}, _id: {result.inserted_id},'
          f'   object: {result}')
    print('--------------------')
    return result.inserted_id

def create_single_document_custom_id(collection):
    print('insert a single document with a custom _id into a collection')
    result = collection.insert_one({
        '_id': 1,
        'type': 'special 2',
        'name': 'custom id object',
    })
    print('insert one result:')
    print(f'status: {result.acknowledged}, _id: {result.inserted_id},'
          f'   object: {result}')
    print('--------------------')
    return result.inserted_id

def bulk_insert(collection):
    print('bulk insert documents into a collection')
    documents = [
            {'name': f'doc {x}', 'type': x} 
            for x in range(17)]
    result = collection.insert_many(documents)
    print('bulk insert result:')
    print(f'status: {result.acknowledged}, _ids: {result.inserted_ids},'
          f'  object: {result}')
    print('--------------------')
    return result.inserted_ids

def query_single_top_document(collection):
    print('get the first document in a collection only')
    document = collection.find_one()
    print(document)
    print('--------------------')
    return document

def query_single_document_by_object_id(collection, _id):
    print('get a document by an automatically generated ObjectId _id')
    print('_id type: ', type(_id))
    print('_id str value: ', _id)
    print('_id repr value: ', repr(_id))
    document = collection.find_one({'_id': _id})
    print(document)
    print('--------------------')
    return document

def query_single_document_by_non_object_id(collection, _id):
    print('get a document by a custom non-ObjectId _id')
    print('_id type: ', type(_id))
    print('_id str value: ', _id)
    print('_id repr value: ', repr(_id))
    document = collection.find_one({'_id': _id})
    print('_id: ', _id)
    print(document)
    print('--------------------')
    return document

def query_single_document_by_field(collection):
    print('get an document by a non _id field')
    print('field: "name", value: "doc 2"')
    document = collection.find_one({'name': 'doc 3'})
    print(document)
    print('--------------------')
    return document

def query_multiple(collection):
    print('get multiple documents from a collection')
    print('field: "type", value: "3 < x < 9"')
    documents = collection.find({'type': {'$gt': 3, '$lt': 9}})
    print(*documents)
    print('--------------------')
    return documents

def count(collection):
    print('count the number of documents in a collection')
    print(f'total documents: {collection.count_documents({})}')
    doc_count = collection.count_documents(
            {'name': {'$regex': '^DOC.*', '$options': 'i'}})
    print(f'field: "name", value: "^doc.*", count: {doc_count}')
    print('--------------------')
    return doc_count

def create_index(collection):
    print('create an index')
    result = collection.create_index(
            [('type', pymongo.ASCENDING)], unique=True)
    print('create index result:')
    print('result type: ', type(result))
    print('result str value: ', result)
    print('result repr value: ', repr(result))
    print('--------------------')
    return result

def try_index_duplicate(collection):
    print('try to insert a new document with a duplicate value for'
          'a field that was declared to have a unique index')
    try:
        collection.insert_one({'type': 12})
    except (pymongo.errors.DuplicateKeyError) as e:
        print(e)

def list_collections(db):
    print('list all collections in the database')
    collections = []
    # can use dot notation
    collections.append(db.collection_1)
    # can use getattrib
    collections.append(getattr(db, 'collection_2', None))
    # can use dictionary access
    collections.append(db['collection-3'])
    # can not use get
    # collections.append(db.get('collection-4', None))  # raises TypeError
    for collection in collections:
        collection.drop()
    print('before', db.list_collection_names())
    for collection in collections:
        collection.insert_one({'test': 1})
    print('after', db.list_collection_names())
    print('--------------------')

def main():
    load_dotenv('.env')
    client = get_client_by_uri()
    # client = get_client_by_params()
    db = get_db(client)
    clean_db(client, db)
    list_collections(db)
    collection = db.test_collection
    object_id = create_single_document(collection)
    non_object_id = create_single_document_custom_id(collection)
    bulk_insert(collection)
    query_single_document_by_object_id(collection, object_id)
    query_single_document_by_non_object_id(collection, non_object_id)
    query_single_document_by_field(collection)
    query_multiple(collection)
    count(collection)
    create_index(collection)
    try_index_duplicate(collection)
    clean_db(client, db)


if __name__ == "__main__":
    main()
