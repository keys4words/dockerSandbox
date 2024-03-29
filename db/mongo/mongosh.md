# connect with authority
mongosh --host <hostname> -u <mongouser> -p <mongopass> --authenticationDatabase <dbname>

# intro
use <dbname>
show dbs/collections
db.createCollection("items")

# use validation schema
db.createCollection(<collection-name>, {
  validator: {
    $jsonSchema: {
      bsonType: "object",
      required: [
        "firstName", "lastName", "country", "isStudentActive",
        "email", "totalSpentInBooks", "gender"
      ],
      properties: {
        firstName: {
          bsonType: "string",
          description: "must be a string and is required",
        },
        lastName: {
          bsonType: "string",
          description: "must be a string and is required",
        },
        country: {
          bsonType: "string",
          description: "must be a string and is required",
        },
        isStudentActive: {
          bsonType: "bool",
          description: "must be a bool and is required"
        },
        gender: {
          enum: ["M", "F"],
          description: "can only be one of the enum values and is required",
        },
        favouriteSubjects: {
          bsonType: "array",
          description: "favourite subject is required",
        },
        totalSpentInBooks: {
          bsonType: "double",
          description: "must be a double if the field exists",
        },
        email: {
          bsonType : "string",
          pattern : "@amigoscode\.com$",
          description: "must be a string and match the regular expression pattern"
        },
      },
    },
  }
});
db.dropDatabase()

# put
db.items.insertOne({ name : "Mike Tyson", age: 56, reach: {"WBA": "gold belt", "WBC": "gold belt"}})
db.items.insertMany([])
# get
db.items.find().skip(1).sort({name: 1}).limit(2)
db.items.find({age: 56})
db.items.find( { name: { $in: ["James", "James"]}} )
db.items.find({ age: { $gte: 56} }, { name: 1})
db.items.find({ age: { $exists: false }})
# edit
db.items.updateOne({ age: 57}, {$set: {age: 44 } })
db.books.updateMany({})
# delete
db.books.deleteOne/deleteMany({ gender: 'M'})

# using js funcs inside
db.books.find().forEach(function(student) {print(student._id)})

# analyze queries
db.books.find().explain("executionStats") -> docsExamined

# play with indexes
db.books.getIndexes()
db.books.createIndex({firstName: 1/-1})
db.books.dropIndex({firstName: 1})