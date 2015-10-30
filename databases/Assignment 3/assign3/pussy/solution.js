// Exercise Set 1
// Q#1
use training
db.scores.find( { score: { $lt: 65 }} ).forEach(function (f){print(tojson(f, '', true));})

// Q#2
db.scores.find({}, {score: 1, _id:0}).sort({score: 1}).limit(1)
db.scores.find({}, {score: 1, _id:0}).sort({score: -1}).limit(1)

use digg

// Q#3
db.stories.find({"shorturl.view_count": {$gt: 1000}}).forEach(function (f){print(tojson(f, '', true));})

// Q#4
db.stories.find({$or: [ { "topic.name": "Television" }, { "media" : "videos" } ]}, {"topic.name": 1, "media": 1}).skip(5).limit(10)

// Q#5
db.stories.find({"topic.name": "Comedy", $or: [ { "media": "news" }, { "media" : "images" } ]}).forEach(function (f){print(tojson(f, '', true));})

// Exercise Set 2
// Q#1
use training
db.scores.update({ score: {$gte: 90} }, { $set:{grade: "A"}}, false, true )
db.scores.update({ score: { $gte : 70, $lt: 90 } }, { $set: { grade : "B" }}, false, true )
db.scores.update({ score: { $gte : 50, $lt: 70 } }, { $set: { grade : "C" }}, false, true )
db.scores.update({ score: { $gte : 25, $lt: 50 } }, { $set: { grade : "D" }}, false, true )
db.scores.update({ score: { $lt: 25 } }, { $set: { grade : "F" }}, false, true )

// Q#2
db.scores.update( { score: {$lt: 60} },   { $inc: { score: 10} }, false ,true)