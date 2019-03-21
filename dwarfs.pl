inFrontOf(X,Y) :- behind(Y,X).

front(grumpy,dopey).
front(doc,droopy).
front(doc,happy).
front(happy,sleepy).
front(happy,smelly).
front(happy,bashful).
front(sneezy,dopey).
front(smelly,grumpy).
front(smelly,stumpy).
front(smelly,sneezy).
front(dopey,droopy).
front(sleepy,grumpy).
front(sleepy,bashful).
front(stumpy,dopey).

behind(X,Y) :- inFrontOf(Y,X).

behind(stumpy,sneezy).
behind(stumpy,doc).
behind(sleepy,stumpy).
behind(sleepy,smelly).
behind(sleepy,happy).
behind(bashful,smelly).
behind(bashful,droopy).
behind(bashful,sleepy).
behind(dopey,sneezy).
behind(dopey,doc).
behind(dopey,sleepy).
behind(smelly,doc).

start() :- .....