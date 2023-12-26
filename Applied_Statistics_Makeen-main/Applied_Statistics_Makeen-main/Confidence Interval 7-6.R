a =c(1,4,4,4,5,5,5,8)
a_m=mean(a)
a_m
a_s=sd(a)
a_s

a_boxplot=boxplot(a)
a_boxplot

b=c(1,2,3,4,5,6,7,8)
b_m=mean(b)
b_m
b_s=sd(b)
b_s

b_boxplot=boxplot(b)
b_boxplot


ab_boxplot=boxplot(a,b, horizontal = TRUE, col =c("red","blue"))

#to divide the many boxplot
set.seed(123)
var1=rnorm(20,50,3)
fivenum(var1)
summary(var1)

par(mfrow=c(2,4))
boxplot(var1,horizontal = TRUE, col ="lightpink")

par(mfrow=c(2,4))
boxplot(var1,horizontal = TRUE, col ="lightblue")

par(mfrow=c(2,4))
boxplot(var1,horizontal = TRUE, col ="orange")

par(mfrow=c(2,4))
boxplot(var1,horizontal = TRUE, col ="gray")

par(mfrow=c(2,4))
boxplot(var1,horizontal = TRUE, col ="black")

par(mfrow=c(2,4))
boxplot(var1,horizontal = TRUE, col ="red")