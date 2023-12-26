set.seed(123)
m=rnorm(100, 5, 5)
m
boxplot(m, horizontal = TRUE, col ="blue" )

fivenum(m)
summary(m)

m[3]
m[3]=m[3]+40
m[3]
boxplot(m, horizontal = TRUE, col ="red" )

m[50]=m[50]-30
m[50]
boxplot(m, horizontal = TRUE, col ="yellow" )

#boxplot(m[-3], horizontal = TRUE, col ="yellow" )

boxplot(m[-c(3,50,72)], horizontal = TRUE, col ="yellow" )

