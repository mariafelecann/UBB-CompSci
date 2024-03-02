%merge(L1, L2, Res) : L1 - the first list, L2 - the second list, Res -
% the resulted list
% flow model: (i,i,o)
% base case: if one of the lists is empty, the solution is the other
% list
merge([], L, L).
merge(L, [], L).
% first case: if we have a duplicate element, we skip it and continue the
% merging
merge([H|T1], [H|T2], Res) :-
    merge(T1, T2, Res).
% second case: if the head of the first list(H1) is smaller than the
% head of the second list(H2),we add it to the result list and continue merging
merge([H1 | T1], [H2 | T2], [H1 | Res]) :-
    H1 < H2,
    merge(T1, [H2|T2], Res).
% thrid case: if the head of the second list(H2) is smaller than the
% head of the first list(H1), we add it to the result list and continue
% merging
merge([H1|T1], [H2|T2], [H2|Res]) :-
    H2 < H1,
    merge([H1|T1], T2, Res).
