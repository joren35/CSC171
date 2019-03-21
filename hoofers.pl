hoofer(tony).
hoofer(shikuo).
hoofer(ellen).

hoofer(X) :- skier(X) ; mountainclimber(X) ; skier(X), mountainclimber(X).

likes(tony, snow).
likes(tony, rain).

likes(tony, _) :- dislikes(ellen, _).
dislikes(ellen, _) :- likes(tony, _).

skier(X) :- likes(X, snow).
mountainclimber(X) :- dislikes(X, rain).

start() :- write("Is there a member of the Hoofers Club who is a mountain climber but not a skier?\n"),
	nl, write("Answer: "),query_climber([shikuo, tony, ellen]).

query_climber([H|T]) :- ( mountainclimber(H) -> query_skier([H|T]), nl ; query_climber(T) ).

query_skier([H|T]) :- ( skier(H) -> query_climber(T) ; write(H), nl ).