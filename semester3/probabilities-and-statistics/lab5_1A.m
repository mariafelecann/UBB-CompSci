#LAB 6 !!

alpha = input("please provide the significance level:(between 0 and 1) --> ");
X =[ 7 7 4 5 9 9 4 12 8 1 8 7 3 13 2 1 17 7 12 5 6 2 1 13 14 10 2 4 9 11 3 5 12 6 10 7];
n = length(X);
#niu reffers the mean
#the null hypotheses is h0: niu = 8.5  (it is together
#with niu > 8.5 ) , and the interpretation is,
#in this case, the efficiency standard is met

#the alternative hypotheses h1: niu < 8.5 (the efficiency
#standard is not met)

#this is a left tailed test for niu
#this is a left tailed test for the mean when sigma
# is known

sigma = 5;
m0 = 8.5;
[h,p,ci,zval] = ztest(X, m0, sigma, "alpha", alpha, "tail", "left");

z = norminv(alpha,0,1);
RR = [-inf z];

printf("value of h : %d\n", h);
if h==1
  printf("the null hypotesis is REJECTED !! >:(\n");
  printf("the data suggests that the standard is not met...lame\n");
else
  printf("the null hypotesis is not rejected :D\n");
  printf("the data suggests the standard IS met!!!\n");
endif

printf("the rejections is (%4.4f , %4.4f) \n", RR);
printf("procetage of the statistics is %4.4f \n", zval);
printf("the pvalue of teh test is %4.4f \n", p);

