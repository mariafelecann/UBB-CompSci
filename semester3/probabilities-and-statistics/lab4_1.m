
problem 2a.)

N = input("input the number of simulations p --> ");

p = input("please enter the probability: (0<p<1) --> ");

U = rand(1,N);
X = (U<p);

U_x = [0 1];
n_X = hist(X, length(U_x)); #tells us how many 0 and how many 1s there are
rel_freq = n_X/N
K = 0:N;
P_K = binopdf(K,N,p)
U_x = unique(X)



