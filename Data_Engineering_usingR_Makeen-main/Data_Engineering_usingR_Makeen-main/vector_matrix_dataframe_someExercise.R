#Vector 
a <- c(25, 36, 78, 55, 22, 99)
a

# Vector with numerical values in a sequence
numbers <- 1:10

numbers
#Access Vectors

a[2]
# Access the first and third item
a[c(1,3)]

# Access all items except for the first item
a[c(-1)]

#Change an Item
a[1] <- "100"
a


# Create matrix 
a <- seq(10,120, by =10)
dim(a)<- c(3,4)
a
# Methods for creating a matrix 
# creating a matrix using Matrix function 
#with defualt value of columns and byrow that is false
mtrx <- matrix(1:12, nrow = 3)
mtrx
#with defualt value of rows
mtrx <- matrix(1:12, ncol = 4)
mtrx
# with the byrow value is TRUE
mtrx <- matrix(1:12, ncol = 4, byrow = TRUE)
mtrx
# When we use the matrix will be able to decide the way our data is organized into a matrix 

# creating a matrix using C bind, it stands for column bin
usa <- c(1.3, 1.5, 1.2, 1.4, 1.5)
usa

de <- c(0.2, 0.4, 0.7, 0.8, 0.8)
de

ngo <- cbind(usa, de)
ngo

# names the rows 
rownames(ngo) <- c("2013", "2014", "2015", "2016", "2017")
ngo
#Orientation of data through transposes 
ngo <- t(ngo)
ngo
# creating a matrix using R bind, it stands for raw bind 
ind <- c(2, 2.2, 2.4, 2.5, 2.6)
ngo <- rbind(ngo, ind)
ngo
_________________________
# create matix in one line 
gdp <- matrix(c(47.9, 41.2, 41.9, 54.6, 56.2, 57.5, 1.6, 1.6,1.7),
                   nrow =3, byrow = TRUE,
                    dimnames = list(c("de", "usa", "ind"),
                                    c("2014", "2015", "2016" )))
gdp

________________________________
# Indexing an element from a matrix
gross <- c(381, 1340, 318, 975, 396, 960, 292, 940, 302, 934, 290, 897, 262, 879, 249,797)
hp.mat <- matrix(gross, nrow = 8, byrow =T)
hp.mat

#calling specific value 
hp.mat[6,2]

# calling an singal value, by select the order of the value 
hp.mat[6] 

#calling the entire row
hp.mat[6,]

#calling the entire rows of specific column
hp.mat[,2]

#Slicing a matrix
# In vector; vector[c("A","B", "D")]
#selecting multiple rows in matrix 
hp.mat[c(1,3,7), ]

colnames(hp.mat) <- c("USA","worldwide")
rownames(hp.mat) <- c("Hallows part 2", "Sorcerer's Stone", "Hallows part 1", 
                      "Order", "Price","Goblet", "Chamber", "Prisoner")
hp.mat

hp.mat["Goblet",]

_______________________________

#Matrix arithmetic

b.office <- c(171.5, 292, 281.6, 460.6, 139.3, 288)
matrix.mat <- matrix(b.office, nrow = 3, byrow = T, 
                     dimnames = list(c("The Matrix", "Reloaded", "Revolutions"),
                       c("us", "Worldwide")))
matrix.mat

#Convert the millions into billions use scaling
matrix.scaled <- matrix.mat/1000
matrix.scaled

#The average matgin for each matrix movie
avg.margin <- matrix.mat -121
avg.margin

#Subtracting two matrix 
budget <- matrix(c(63, 150, 150), nrow = 3, ncol = 2)
budget

margin <- matrix.mat - budget
margin

#Subtracting a vector from matrix 
matrix.mat - c(63, 150, 150)

#Matrix multiplication
v <- matrix(1:6, nrow = 3)
v
matrix.multiplied <- matrix.mat*v
matrix.multiplied

#inner multiplication we need to use %*%
# outer multiplication we need to use %o%

#Matrix operations
b.office <- c(171.5, 292, 281.6, 460.6, 139.3, 288)
matrix.mat <- matrix(b.office, nrow = 3, byrow = T, 
                     dimnames = list(c("The Matrix", "Reloaded", "Revolutions"),
                                     c("us", "Worldwide")))

matrix.mat
#how much did the matrix make
total <- colSums(matrix.mat)
rowSums(matrix.mat)
# average 
avg <- colMeans(matrix.mat)
rowMeans(matrix.mat)
# saving preliminary results and adding them to data structure
matrix.prelim <- rbind(matrix.mat, avg, total)
matrix.prelim

# data Frame 
# Create a data frame
Data_Frame <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame

#Summarize the Data
summary(Data_Frame)

# Access Items

Data_Frame[1]

Data_Frame[["Training"]]

Data_Frame$Training

#Add Rows
New_row_DF <- rbind(Data_Frame, c("Strength", 110, 110))
New_row_DF

#Add Columns
New_col_DF <- cbind(Data_Frame, Steps = c(1000, 6000, 2000))
New_col_DF

#Remove Rows and Columns
# Remove the first row and column
Data_Frame_New <- Data_Frame[-c(1), -c(1)]
Data_Frame_New

#Amount of Rows and Columns
dim(Data_Frame)
#Data Frame Length
length(Data_Frame)

#Combining Data Frames
Data_Frame1 <- data.frame (
  Training = c("Strength", "Stamina", "Other"),
  Pulse = c(100, 150, 120),
  Duration = c(60, 30, 45)
)

Data_Frame2 <- data.frame (
  Training = c("Stamina", "Stamina", "Strength"),
  Pulse = c(140, 150, 160),
  Duration = c(30, 30, 20)
)

New_Data_Frame <- rbind(Data_Frame1, Data_Frame2)
New_Data_Frame

