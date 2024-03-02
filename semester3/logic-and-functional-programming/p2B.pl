merge_sublists(L, R) :-
    merge_sublists_aux(L, [], Res),
    remove_repetitive(Res, R1),
    sort(R1,R).
merge_sublists_aux([], Merged, Merged).
merge_sublists_aux([H|T], Acc, Merged) :-
    is_list(H),
    removeDoubles(H, Acc, NewH),
    merge_sublists_aux(T, NewH, Merged).
merge_sublists_aux([H|T], Acc, Merged) :-
    \+ is_list(H),
    merge_sublists_aux(T, [H|Acc], Merged).

removeDoubles([], Merged, Merged).
removeDoubles([H|T], Merged, Result) :-
    member(H, Merged),
    !,
    removeDoubles(T, Merged, Result).
removeDoubles([H|T], Merged, [H|Result]) :-
    removeDoubles(T, Merged, Result).
remove_repetitive([], []).
remove_repetitive([H | T], R) :-
    \+ member(H, T),
    remove_repetitive(T, TResult),
    R = [H | TResult].

remove_repetitive([H | T], R) :-
    member(H, T),
    remove_all(H, T, TailWithoutX),
    remove_repetitive(TailWithoutX, R).
remove_all(_, [], []).
remove_all(X, [X | Tail], R) :- remove_all(X, Tail, R).
remove_all(X, [Y | Tail], [Y | Result]) :- X \= Y, remove_all(X, Tail, Result).
