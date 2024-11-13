% Declare holding/1 as dynamic
:- dynamic holding/1.

% Facts
at(monkey, ground).
at(banana, ceiling).
at(chair, ground).
at(stick, ground).
holding(none).

% Actions
move(Object) :- at(monkey, ground), at(Object, ground), write('Monkey moves to '), write(Object), nl.
pick(Object) :- move(Object), holding(none), retract(holding(none)), assert(holding(Object)), write('Monkey picks up the '), write(Object), nl.
climb :- holding(stick), write('Monkey climbs on chair'), nl.
knock :- climb, write('Monkey knocks the bananas down'), nl.

% Goal
get_bananas :- pick(stick), climb, knock.
