N = input("please enter the nr of simulations --> ");
n = input("please enter the nr of trials --> ");
p = input("please enter the probability: (0<p<1) --> ");

# a simulation means that we keep the same parameters

#each simulation has n chestii idk

U = rand(n,N); #bc its like we have a matrix and each column has n stuff and there
                #there are N columns sau ceva de genu
#the binomail is interested in how many successes we have in n trials
#so if we have a vector full of 0 and 1s the successes are the number of 1s
X = sum(U < p)
#for binopdf:
#first arg: list of values, the succeses we can find, the send=cond arg: nr of trials
#3 arg: the propbability of succes
K = 0:n;
P_K = binopdf(K, n, p)
U_X = unique(X)
n_X = hist(X, length(U_X));
rel_freq = n_X/N

plot(U_X, rel_freq, '*', P_K, 'o')
