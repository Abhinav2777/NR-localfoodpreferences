import csv
from pymongo import MongoClient

mongoClient = MongoClient() 
db = mongoClient.flask_db
#recipes=db.recipes    
db.segment.drop()
#header=[ "name", "section", "roll"]
header = [ "name", "id", "minutes","contributor_id","submitted","tags","nutrition","n_steps","steps","description","ingredients","n_ingredients","food type","cal"]
csvfile = open('../RAW_recipes.csv', 'r')
reader = csv.DictReader( csvfile )

for each in reader:
    row={}
    for field in header:
        row[field]=each[field]
        
    #print (row)
    db.segment.insert_one(row)
segment=db.segment