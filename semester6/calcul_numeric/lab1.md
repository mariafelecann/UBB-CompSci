## matrices

A = [1 2 3; 4 5 6; 7 8 10]
inv(A)
det(A)

## vectors
v = 1:2:19   - 2 is the step size => we get a raw vector
v = 1:100
v*v - we can do this because they are raw vectors
v.^2 - squares all the elements
v' - column vector
5*v - multiplies the vector with a number, so we dont need a dot

### exercises

1. p(x) = x^5 - 5x^4 -16x^3 + 16x^2 -17x + 21
  - plot the graph on [-4, 7.2]

x = -4:0.1:7.2; - the semicolon = the vector is not displayed
px  = x.^5 - 5*x.^4 - 16*x.^2 - 17*x + 21
plot(x,px) - plots the vector with x axis x and y axis px 

  - compute p(-2.5)
p = [1, -5, -16, 16, -17, 21]
( x^5, x^4, x^3, x^2, x, 1)

we can use the function `polyval`
polyval(p, -2.5)

  - find the roots of p
`The roots (sometimes called zeroes or solutions) of a polynomial 
P(x) are the values of x for which P(x) is equal to zero`

roots(p)

2. Plot the functions f,g,h : [0,2π] → R, f(x) = sinx,g(x) = sin2x,h(x) = sin3x, on the same figure,
 in three tiled positions, one on top of the other.
(gen 3 diagarame separate in acelasi chenar)

x = 0:0.1*pi:2*pi
f=sin(x);
g=sin(2*x);
h=sin(3*x);
subplot(3, 1, 1)
plot(x,f)
3 = rows. (we need 3 diagrams on a column)
1 = columns
1 = index(first diagram)
subplot(3,1,2)
2 = index (second diagram)
plot(x,g)
subplot(3,1,3)
3 = index
plot(x,h)

3.  For R,r ∈ R+, consider the epicycloid (also called hypercycloid), given by the parametric equations
 x(t) = (R+r)cost−rcos R
 r 
+1 t
 y(t) = (R+r)sint−rsin R
 r 
+1 t , t∈[0,10π].
 Plot its graph, for R = 3.8,r = 1

(for each t we get an x coordiante and a y coordinate)

t=0:0.01*pi:10*pi;
R=3.8;
r=1;
xt = (R+r)*cos(t)-r*cos((R/r+1)*t);
yt = (R+r)*sin(t)-r*sin((R/r+1)*t);
plot(xt,yt)


4. Plot the function of two variables f : [−2,2]×[0.5,4.5]→R, f(x,y)=sin(ex)cos(lny)(using both
 mesh and plot3)

[x,y] = meshgrid(-2:0.1:2, 0.5:0.1:4.5);
                      x          y
z = sin(exp(x)).*cos(log(y));
mesh(x,y,z)
plot3(x,y,z)

