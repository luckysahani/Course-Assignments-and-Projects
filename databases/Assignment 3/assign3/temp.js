use training
db.scores.update({'score': {"$lte": 60}, 'name' : 'exam'},{'$inc': {score: 10}},false, true);