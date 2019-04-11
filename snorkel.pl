beat(garry, barry). % (2)

beat(X, Y) :- (X \= garry -> wearred(X), wearblue(Y); wearblue(Y)). %(7)

wearred(X) :- write(X), write(" wears red."), nl.

wearblue(X) :- write(X), write(" wears blue."), nl.

weargreen(X) :- place(X, 2), number(X, 3), write(X), write(" wears green."), nl.

wearyellow(barry). % (7)

wearyellow(X) :- beat(larry, X), write(X), write(" wears yellow."), nl. % (3)