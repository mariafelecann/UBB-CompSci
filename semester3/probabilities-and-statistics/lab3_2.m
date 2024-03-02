#two randm variables are the same if they have the same PDF

p = input("please enter p(0.05<=p<=0.96) --> ");

# to simulate infinity: we jump to larger and larger values

for n = 1:3:100
  x = 0:n;
  y = binopdf(x,n,p);
  plot(x,y)
  pause(0.5)
endfor

