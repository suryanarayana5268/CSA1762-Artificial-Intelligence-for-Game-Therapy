sum(0,0).
sum(N,Sum):- N>0,N1 is N-1,sum(N1,S),Sum is N+S.
