N = input("enter the number of simulations: ");
#here we count the succeses until we find the first success
p = input("probability 0<p<1 : ");
#we must simulate the nr of trials
X=zeros(1,N);

for(i=1:N)
  X(i) = 0;
  while rand() >= p
    X(i) = X(i)+1; #as long as we get failures we increase the nr of fails for each trial
  endwhile
endfor

k = 0:20;
y = geopdf(k,p);
u_x = unique(X);
n_x = hist(X, length(u_x));
rel_freq = n_x/N
plot(u_x, rel_freq,'*',y, 'o');
