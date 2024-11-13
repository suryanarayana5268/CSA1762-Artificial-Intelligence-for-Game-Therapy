
hostile_nation(country_a).
american(robert).
sold_weapons(robert, country_a, missiles).
crime(X) :- american(X), hostile_nation(Y), sold_weapons(X, Y, _).

