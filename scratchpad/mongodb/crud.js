// add a single document
db.users.insertOne (
    {
        name: "user 2",
        field: "general",
        car: "none"
    }
)

// add multiple documents
db.docs.insertMany (
    [
        { name: "doc 1", type: 1 },
        { name: "doc 2", type: 1 },
        { name: "doc 1", type: 2 },
        { name: "doc 2", type: 2 },
    ]
)

// get all documents in a collection
db.docs.find()
// limit number of documents
db.docs.find().limit(2)
// filter documents
db.docs.find( { type: { $gt: 1 } })
db.docs.find( { name: 'doc 1', type: 2})

// update documents
db.docs.updateOne ( { name: "doc 1", type: 1 }, {$set: { group: 1 } })
db.docs.updateMany ( { type: 2 }, {$set: { group: 2 } })
db.docs.replaceOne ( { name: "doc 2", type: 1 }, { name: "doc 3", type: 3, group: 3 })
db.docs.find()  // check

// delete documents
db.docs.deleteOne ( { name: "doc 1", type: 1 } )
db.docs.find()  // check
db.docs.deleteMany ( { type: 2 } )
db.docs.find()  // check

// bulk writes
try {
    db.docs.find()
    db.docs.deleteOne ( { name: "doc 3" } )
    db.docs.find()
    db.docs.insertOne ( { name: "doc 4", type: 4, group: 4 } )
    db.docs.insertOne ( { name: "doc 4", type: 5, group: 4 } )
    db.docs.insertOne ( { name: "doc 4", type: 6, group: 4 } )
    db.docs.insertOne ( { name: "doc 4", type: 7, group: 4 } )
    db.docs.insertOne ( { name: "doc 4", type: 8, group: 4 } )
    db.docs.insertOne ( { name: "doc 4", type: 9, group: 4 } )
    db.docs.insertOne ( { name: "doc 4", type: 10, group: 4 } )
    db.docs.find()
    db.docs.deleteMany ( { type: { $lt: 8, $gt: 5 } } )
    db.docs.find()
    db.docs.updateMany ( { type: { $lt: 8} },{ $set: { group: "a" } } )
    db.docs.replaceOne ( { type: 9 }, { note: "deleted" } )
    db.docs.find()
} catch( error ) {
    print( error )
}

// delete collection
db.docs.deleteMany ( { } )

