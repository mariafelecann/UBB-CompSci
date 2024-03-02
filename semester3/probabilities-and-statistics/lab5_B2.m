Premium = [22.4 21.7 24.5 23.4 21.6 23.3 22.4 21.6 24.8 20.0]
Regular = [17.7 14.8 19.6 19.6  12.1 14.8 15.4 12.6 14.0 12.2]

n1 = length(Premium);
n2 = length(Regular);

conf_level = 0.95;
alpha = 1 - conf_level;

sp = sqrt(((n1-1)*var(Premium) + (n2-1)*var(Regular))/(n1+n2));

m1 = mean(Premium) - mean(Regular) - tinv((1-alpha)/2, n1+n2-2) * sp * sqrt(1/n1 + 1/n2);
m2 = mean(Premium) - mean(Regular) - tinv(alpha/2, n1+n2-2) * sp * sqrt(1/n1 + 1/n2);

printf("the CI for the theoretical mean when sigma is unknown...(%4.3f, %4.3f)\n", m1,m2);
