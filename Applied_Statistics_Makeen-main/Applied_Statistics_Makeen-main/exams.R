
summary(exams_n_100)
str(exams_n_100)

#to divide the many boxplot
par(mfrow=c(1,2))
boxplot(math_score ~ gender,horizontal = TRUE, col ="lightpink")
par(mfrow=c(1,2))
boxplot(reading_score ~ gender ,horizontal = TRUE, col ="lightblue")
attach(s_data)
boxplot(s_data$`reading score`~s_data$gender ,horizontal = TRUE, col =c("lightblue", "gray"))
boxplot(s_data$`math score`~s_data$gender,horizontal = TRUE, col =c("lightpink","Orange"))



#The relationship among reading score and math score
s_data$RS = s_data$`reading score`
s_data$MS = s_data$`math score`
attach(s_data)

plot(RS,MS)
cor(RS,MS)

model01=lm(s_data$RS~s_data$MS)
summary(model01)

abline(model01, col="red")


#The relationship among reading score and writing score

new_s_data=exams_n_100[,c(1,5,6,7,8)]
View(new_s_data)
new_s_data$RS = new_s_data$`reading score`
new_s_data$MS = new_s_data$`math score`
new_s_data$WS = new_s_data$`writing score`
attach(new_s_data)

plot(RS,WS)
cor(RS,WS)

model02=lm(new_s_data$RS~new_s_data$WS)
summary(model02)

abline(model02, col="red")

table(gender)

MaleDataset=new_s_data[new_s_data$gender=='male',]
View(MaleDataset)

plot(MaleDataset$RS,MaleDataset$WS)
cor(MaleDataset$RS,MaleDataset$WS)


femaleDataset=new_s_data[new_s_data$gender=='female',]
View(femaleDataset)

plot(femaleDataset$RS,femaleDataset$WS)
cor(femaleDataset$RS,femaleDataset$WS)


