Taylor's Series Formula
f(x)=f(a)+ 1!f ′(a) (x–a)+ 2!f”(a) (x–a) 2+ 3!f” ′(a)(x–a) 3 +⋯+ Remainder
1.
a)
> syms x
>> f = exp(x)
>> T1 = taylor(f, x, 0, 'Order', 2)
0 is x0, the center
2 = degree + 1
MacLauren formula:
ex = 1+x+x2/2! +...+ xn/n! + xn+1/(n +1)! eξx,
>> fplot(f, [-3,3])
>> grid on
>> T2 = taylor(f, x, 1, 'Order', 3)
