
## Using CLI

```
```

- Create new DB

```
> use books
switched to db books
```

> Though above will initiate a DB, but you need to add document to collection to initiate it.

- Insert document

```
> db.fiction.insertOne({"name": "Harry Poter", "author": "JK Rowling"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("62cafae86629fd3e176d107e")
}
> show dbs
admin   0.000GB
books   0.000GB
config  0.000GB
local   0.000GB
> db.getCollectionNames()
[ "fiction" ]

```

- Show Collection in DB

```commandline
> show collections
comments
movies
sessions
theaters
users

```

- Fetch all document

```
> db.fiction.insertOne({"name": "Feluda", "author": "Styajit Ray"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("62cafd136629fd3e176d107f")
}
> db.fiction.insertOne({"name": "Byomkesh", "author": "Saradindu"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("62cafd246629fd3e176d1080")
}
> db.fiction.find({})
{ "_id" : ObjectId("62cafae86629fd3e176d107e"), "name" : "Harry Poter", "author" : "JK Rowling" }
{ "_id" : ObjectId("62cafd136629fd3e176d107f"), "name" : "Feluda", "author" : "Styajit Ray" }
{ "_id" : ObjectId("62cafd246629fd3e176d1080"), "name" : "Byomkesh", "author" : "Saradindu" }
> db.fiction.find({"name": "Feluda"})
{ "_id" : ObjectId("62cafd136629fd3e176d107f"), "name" : "Feluda", "author" : "Styajit Ray" }
```

> Note the MongoDB will insert a unique id to all documents

- Update

```
> db.fiction.updateOne({"name": "Feluda"}, {$set: {"name": "Feluda", "author": "Satyajit"}})
{ "acknowledged" : true, "matchedCount" : 1, "modifiedCount" : 1 }
> db.fiction.find({"name": "Feluda"})
{ "_id" : ObjectId("62cafd136629fd3e176d107f"), "name" : "Feluda", "author" : "Satyajit" }

```

> Note the `acknowledged` for all operation, also for insert it returns unique `id` while for update returns how many modified

- Delete

```
> db.fiction.insertOne({"name": "Discovery of India", "author": "Nehru"})
{
        "acknowledged" : true,
        "insertedId" : ObjectId("62cafe9e6629fd3e176d1081")
}
> db.fiction.find({})
{ "_id" : ObjectId("62cafae86629fd3e176d107e"), "name" : "Harry Poter", "author" : "JK Rowling" }
{ "_id" : ObjectId("62cafd136629fd3e176d107f"), "name" : "Feluda", "author" : "Satyajit" }
{ "_id" : ObjectId("62cafd246629fd3e176d1080"), "name" : "Byomkesh", "author" : "Saradindu" }
{ "_id" : ObjectId("62cafe9e6629fd3e176d1081"), "name" : "Discovery of India", "author" : "Nehru" }
> db.fiction.deleteOne({"author" : "Nehru" })
{ "acknowledged" : true, "deletedCount" : 1 }
> db.fiction.find({})
{ "_id" : ObjectId("62cafae86629fd3e176d107e"), "name" : "Harry Poter", "author" : "JK Rowling" }
{ "_id" : ObjectId("62cafd136629fd3e176d107f"), "name" : "Feluda", "author" : "Satyajit" }
{ "_id" : ObjectId("62cafd246629fd3e176d1080"), "name" : "Byomkesh", "author" : "Saradindu" }
```

- Show 1 Record

```commandline
> db.movies.find().limit(1).pretty()
{
        "_id" : ObjectId("573a1390f29313caabcd4135"),
        "plot" : "Three men hammer on an anvil and pass a bottle of beer around.",
        "genres" : [
                "Short"
        ],
        "runtime" : 1,
        "cast" : [
                "Charles Kayser",
                "John Ott"
        ],
        "num_mflix_comments" : 1,
        "title" : "Blacksmith Scene",
        "fullplot" : "A stationary camera looks at a large anvil with a blacksmith behind it and one on either side. The smith in the middle draws a heated metal rod from the fire, places it on the anvil, and all three begin a rhythmic hammering. After several blows, the metal goes back in the fire. One smith pulls out a bottle of beer, and they each take a swig. Then, out comes the glowing metal and the hammering resumes.",
        "countries" : [
                "USA"
        ],
        "released" : ISODate("1893-05-09T00:00:00Z"),
        "directors" : [
                "William K.L. Dickson"
        ],
        "rated" : "UNRATED",
        "awards" : {
                "wins" : 1,
                "nominations" : 0,
                "text" : "1 win."
        },
        "lastupdated" : "2015-08-26 00:03:50.133000000",
        "year" : 1893,
        "imdb" : {
                "rating" : 6.2,
                "votes" : 1189,
                "id" : 5
        },
        "type" : "movie",
        "tomatoes" : {
                "viewer" : {
                        "rating" : 3,
                        "numReviews" : 184,
                        "meter" : 32
                },
                "lastUpdated" : ISODate("2015-06-28T18:34:09Z")
        }
}
```

