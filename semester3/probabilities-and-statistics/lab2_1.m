# we are solving the ex 2
# we plot the pdf and the cdf of the binaominal distribution

n = input("give number of trials n = ");  #n = natural number
p = input("give the probabbility of success p = "); #p is between 0 and 1
x = 0:1:n; #this is the number of success in n trials

px = binopdf(x,n,p);
plot(x, px, '*r')

xx = 0:0.01:n;
cx=binocdf(xx,n,p);
plot(xx,cx,'g')
