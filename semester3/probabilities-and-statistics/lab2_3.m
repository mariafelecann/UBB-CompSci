#simulating 3 coin tosses

N = input("give the number of simulations N = ");

#we are going to form a matrix with 3 rows and N column with numbers between 0 and 1

U = rand(3,N);
Y = (U<0.5);
X = sum(Y);
clf
hist(X)
