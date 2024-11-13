bird(eagle).
bird(sparrow).
bird(penguin).
fly(penguin) :- !, fail.
fly(X) :- bird(X).
can_fly(Bird) :-
    fly(Bird),
    write(Bird), write(' can fly.'), nl.
can_fly(Bird) :-
    \+ fly(Bird),
    write(Bird), write(' cannot fly.'), nl.
