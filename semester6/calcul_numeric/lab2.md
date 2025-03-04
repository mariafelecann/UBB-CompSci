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

f = exp(x)
syms x
f = exp(x)
T1 = taylor(f, x, 0, 'Order', 2)
fplot(f, [-3, 3])
T2 = taylor(f, x, 'Order', 3);
T3 = taylor(f, x, 'Order', 4); 
T4 = taylor(f, x, 'Order', 5);
fplot(T2, [-3, 3], '--g');
hold on
fplot(T3, [-3, 3], '--b')
fplot(T4, [-3, 3], '--m')
fplot(T1, [-3, 3]);
hold off
subs(f,x,1)
e_approx = vpa(exp(1), 7)

f2 = sin(x)
T32 = taylor(f2, x, 'Order', 4); 
T5 = taylor(f2, x, 'Order', 6);
fplot(f2, [-pi, pi])
hold on
fplot(T32, [-3, 3], '--m')
fplot(T5, [-3, 3], '--b')
hold off
sin_aprox = vpa(sin(pi/5), 5)

f3 = log10(1 + x)
T32 = taylor(f3, x, 'Order', 3);
T35 = taylor(f3, x, 'Order', 6);
fplot(f3, [-0.9, 1])
hold on
fplot(T32, [-0.9, 1], '--m')
fplot(T5, [-0.9, 1], '--b')
hold off

vpa(log(2), 7)


for i=200:1500
    vpa((subs(taylor(log(x+1), x, 'Order', i+1), x, 1)),7)
end

%T3c = taylor(log10(1-x), x, 'Order', 6)

%T3d = taylor(log10(1+x), x, 'Order', 6)

%T3d - T3c

