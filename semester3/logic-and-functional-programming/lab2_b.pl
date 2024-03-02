%L - the original list, R- Result List, Max- maximum
remove_max([],_,[]).
remove_max([H|T], Max, R):-
    H=:=Max,
    remove_max(T, Max, R).
remove_max([H|T], Max,[H|R]):-
    H=\=Max,
    remove_max(T, Max, R).

%L-the original list, M- the maximum

find_max([M],M).
find_max([H|T], M):-
    find_max(T, M2),
    M is max(H, M2).

%List - the original list, Res- the final result
remove_all_maximum(List, Res):-
    find_max(List, Maxim),
    remove_max(List, Maxim,Res).

