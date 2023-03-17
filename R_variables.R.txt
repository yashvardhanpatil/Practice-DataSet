######Variables#####
#Variables are containers for storing the data values.
#Variable are used to allocate a memory location to a specific
#value that we want to store.
#A variable must start with a letter.
#It can contain underscore,letters and numbers.
#It cannot contain - and all other special characters,
#like #,@,!,$,%,^,&,*,etc.
#In R we can use both (= and <-) as a assignment operator, but
#mostly <- operator is preffered over =.

x = 10+5
x

y <- x+5

x = 50
!a = 100



#Data types in R:
#1.Integer
#2.Float
#3.String/character
#4.Logical/Boolean

a = 10
class(a)
b = 10.5
class(b)

a = 100L
class(a)

strr = 'Python'
class(strr)
bool = TRUE
class(bool)

a = F
class(a)
a = '100'
class(a)


#Data structures in R
#Vector and Data Frame, Lists

marks <- c(89,87,88,90)
y = c(10,TRUE,'Python')
y
marks


#Accessing elements from a vector
marks[3]
marks[4]
marks[1:3]
marks[3:4]
marks[c(1,4)]


#Assigning or replacing values in a vector
marks[4] <- 95
marks

#List Creation
lst <- list(100,TRUE,'Python')
lst

#Accessing and replacing elements from list

lst[3]
lst[2] <- FALSE
lst


#Data Frame Creation
df <- data.frame(Age = c(52,56,54,20,52),
                 City = c('Pune',"HYD",'MUmbai','Delhi','Chennai'),
                 Marks = c(10,12,10,11,15) )
View(df)

#Accessing elements from a data frame
df[1,1]
df[1:3,1]
df[c(2,4),1:2]
df[4,c(1,3)]


#Replacing values from a data frame.
df[4,1] <- 23

getwd()
rm(cars)


data <- read.csv(file.choose())


data <- read.csv('Salaries.csv')
View(data)
a
#In-class activity
#1. Perform basic arithmetic operations
#2. Create variables and store various values and their data type.
#3. Create atomic vector,lists,data frame
#4. Perform indexing/slicing on list
#5. Create a data frame with 3 columns and 5 records.
#6. Perform 5 slicing operations on data frames.
#7. Replace some values from data frame



mean(var = c(10,20,20,22))
mean(var <- c(10,12,14,15))
