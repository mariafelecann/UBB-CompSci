% candidate(L : list, E: the element to be chosen)
%flow model: (i, o)
candidate([E|_],E).
candidate([_|T],E) :-
candidate(T,E).

%generate_numbers(N: the number, L: the list with numbers from 1 to N)
%flow model: (i,o)
generate_numbers(1, [1]).
generate_numbers(N, [N|Rest]) :-
    N > 1,
    Prev is N - 1,
    generate_numbers(Prev, Rest).

% solution(N: the number given, Rez: the list of numbers that added=N)
% flow model: (i,i,o)
solution(N, Rez) :-
   generate_numbers(N,L),
   candidate(L, E),
   E =< N,
   solution_aux(L, N, Rez, [E], E).
% solution_aux(L: list of nr from 1 to N, N, NewL: the
% solution ,PartL: partial list with candidates, S: the sum of the
% elems from PartL)
%flow model:(i,i,o,i,i)
solution_aux(_, N, Rez, Rez, N) :- !.
solution_aux(L, N, Rez, [H | Col], S) :-
    candidate(L, E),
    E < H,
    S1 is S+E,
    S1 =< N,
solution_aux(L, N, Rez, [E, H | Col], S1).
