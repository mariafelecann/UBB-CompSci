#for the final:  the pdf of a law: f(x) = P(X=x) - the probability of X that takes a value x
                # the cdf of a law: F(x) = P(X<=x) - the prob of X to be less or equal than x

N = input("freedon of degree: ");

#x>0:
1 - tcdf(0,N)  #because P(x>=0) = 1 - P(X<0)

# we work with continuous distributions
# cdf = P(X<=x) = integral de la -inf la x (f(t)dt)

# -1<=x<=1 :
tcdf(1, N) - tcdf(-1, N)

# x<=0 :
tcdf(0,N)

# x<=-1 U x>=1:
1 - tcdf(1,N) - tcdf(-1,N)

a = input("please give alpha: (0<alpha<1)");
b = input("please give beta: (0<beta<1)");
#c.)

tinv(a,N)

#d.)

1 - tinv(b,N)

