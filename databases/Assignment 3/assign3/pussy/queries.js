//Question 1

use training
db.scores.find( { score: { $lt: 65 }} ).forEach(function (f){print(tojson(f, '', true));})

// Question 2

use training
db.scores.find({},{score : 1}).sort({score : -1}).limit(1);
db.scores.find({},{score : 1}).sort({score : 1}).limit(1);

// Question 3

use digg
db.stories.find({"shorturl.view_count": {$gt: 1000}}).forEach(function (f){print(tojson(f, '', true));})

// Question 4

db.stories.find({$or : [{"topic.name" : "Television"}, {"media" : "videos"}]}).skip(5).limit(10).pretty();

// Question 5

db.stories.find({"topic.name": "Comedy", $or: [ { "media": "news" }, { "media" : "images" } ]}).forEach(function (f){print(tojson(f, '', true));})

//Exercise 2
//Question 1

use training
db.scores.update({ score: {$gte: 90} }, { $set:{grade: "A"}}, false, true )
db.scores.update({ score: { $gte : 80, $lt: 90 } }, { $set: { grade : "B" }}, false, true )
db.scores.update({ score: { $gte : 70, $lt: 80 } }, { $set: { grade : "C" }}, false, true )
db.scores.update({ score: { $gte : 50, $lt: 70 } }, { $set: { grade : "D" }}, false, true )
db.scores.update({ score: { $gte : 35, $lt: 50 } }, { $set: { grade : "E" }}, false, true )
db.scores.update({ score: { $lt: 35 } }, { $set: { grade : "F" }}, false, true )

//Question 2

db.scores.update({'score': {"$lte": 60}, 'name' : 'exam'},{'$inc': {score: 10}},false, true);