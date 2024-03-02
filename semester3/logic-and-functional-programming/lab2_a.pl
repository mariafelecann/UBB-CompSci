% L - list, R - Final result
% flow model(i,o)
remove_repetitive([], []).
remove_repetitive([H | T], R) :-
    \+ member(H, T),
    remove_repetitive(T, TResult),
    R = [H | TResult].

remove_repetitive([H | T], R) :-
    member(H, T),
    remove_all(H, T, TailWithoutX),
    remove_repetitive(TailWithoutX, R).
%X - element to remove, L - initial list, R- final list
%flow model(i,i,o)
remove_all(_, [], []).
remove_all(X, [X | Tail], R) :- remove_all(X, Tail, R).
remove_all(X, [Y | Tail], [Y | Result]) :- X \= Y, remove_all(X, Tail, Result).
