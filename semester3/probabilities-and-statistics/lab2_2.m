#solving the final application
#x follows the binomial that has paramteters 3 and 0.5

x = 0:1:3
px = binopdf(x,3,0.5)
plot(x, px, '*r')
cx=binocdf(x,3,0.5)
plot(x,cx,'g')

#P(x=0) represents the probability of having 0 heads:
binopdf(0,3,0.5)
printf("probability of having 0 heads: %f\n",
 binopdf(0,3,0.5))

#P(x!=1) is the probability of having anything other than 1 head:
printf("probability of having anything other than 1 head: %f\n",
 1 - binopdf(1,3,0.5))


#P(x<=2) - probability of having anything under 2 heads:
printf("probability of having anything under 2 heads: %f\n",
 1 - binocdf(2,3,0.5))

 #P(x>1) - probability of having a larger number of heads that 1:
 printf("probability of having a larger number of heads that 1: %f\n",
 1 - binocdf(1,3,0.5))








