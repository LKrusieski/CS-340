#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 24 18:58:49 2024

@author: larrykrusiesk_snhu
"""
from pymongo import MongoClient
from bson.objectid import ObjectId


class AnimalShelter(object):
    
    def __init__(self, USER, PASS, HOST, PORT, DB, COL):
        
        ##USER = 'aacuser'
        ##PASS = 'SNHU1234'
        ##HOST = 'nv-desktop-services.apporto.com'
        ##PORT = 34549
        ##DB = 'AAC'
        ##COL = 'animals'
        
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['%s' % (DB)]
        self.collection = self.database['%s' % (COL)]
        
        
        
    def create(self, data):
        
        # if there is data, create a document with it
        if data is not None:
            
            status = self.database.animals.insert_one(data)
            return status.acknowledged
        # if there is no data to create a document with, raise an exception
        else: 
            
            raise Exception("Nothing to save, because data parameter is empty")
        
    def read(self, data):
        
        # if data exists, use the data as input to the find method
        if data is not None:
            
            items = self.database.animals.find(data)
           
            return items
        
        # if data does not exist, return all documents in DB        
        else:
            
            items  = self.database.animals.find()
            
            return items
        
    def update(self,data, updateData):
        
        # check for the number documents that exist in the database that 
        # match the query
        numToUpdate = self.database.animals.count_documents(data)
        
        
        
        # if there is more then one document to be updated, use update_many()
        if numToUpdate > 1:
            
            result = self.database.animals.update_many(data, updateData)
            return result.modified_count
        
        # if there is one and only one document to be updated, use update_one()
        elif numToUpdate == 1:
            
            result = self.database.animals.update_one(data, updateData)
            return result.modified_count
        
        # raise Exception if matching documents not found
        else:
            raise Exception("No documents found to update")
            
    def delete(self, data):
        
       # check for the number documents that exist in the database that 
       # match the query
       numToDelete = self.database.animals.count_documents(data)
       
       
       
       # if there is more then one document to be updated, use update_many()
       if numToDelete > 1:
           
           result = self.database.animals.delete_many(data)
           return result.deleted_count
       
       # if there is one and only one document to be updated, use update_one()
       elif numToDelete == 1:
           
           result = self.database.animals.delete_one(data)
           return result.deleted_count
       
       # raise Exception if matching documents not found
       else:
           raise Exception("No documents found to delete")
           
