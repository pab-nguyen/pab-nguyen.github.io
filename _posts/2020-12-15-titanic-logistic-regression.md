---
layout: post
title: Simple Logistic Regression on Titanic
---

# Predicting Survivor Rate of Titanic


Hello, welcome to my first attempt at cracking this competition. 
I am new at data science, therefore any comments would be highly appreciated.

## Importing Libraries
These are the libraries I found neccessary to perform this model building exercise. 
```{r, echo=TRUE,results='hide',message=FALSE}
library(tidyverse)# metapackage of all tidyverse packages
library('plyr') # data manipulation
library('dplyr')
```

## First look at the data
First, I'm going to pull in the data from Kaggle. There are two data sets, train and test. 
```{r}
train <- read.csv("../input/titanic/train.csv")
test <- read.csv ("../input/titanic/test.csv")
dim(train)
dim(test)
```
The train data set has 891 rows, each row represents a passenger and the test set has 418 rows.
Let's look at the first few rows of the data.

```{r}
head(train,n=5)
```
These are the 12 variables in the train data set. The test data set doesn't contain Survived.

Variable Name | Description
--------------|-------------
Survived      | Survived (1) or died (0)
Pclass        | Passenger's class
Name          | Passenger's name
Sex           | Passenger's sex
Age           | Passenger's age
SibSp         | Number of siblings/spouses aboard
Parch         | Number of parents/children aboard
Ticket        | Ticket number
Fare          | Fare
Cabin         | Cabin
Embarked      | Port of embarkation

***

Right off the bat, I am speculating that sex and age will be significant in detecting the Survivor Rate. 
Passenger ID, Name and Ticket are not relevant in my opinion. 

For this exercise, I am going to fit a logistic model. 

However, first, we are going to remove missing data from the train data set.
```{r}
a <- nrow(train)
train <- na.omit(train)
a - nrow(train)


plyr::count(train$Survived)
```
We removed 177 observations due to missing data.
Among the 714 passengers, 424 died and 290 survived.

## Fitting the model
 
Let's fit the a logistic model with all the variables, except for PassengerId, Name and Ticket

```{r}
titanic.lr <- glm(formula=as.factor(Survived)~.-PassengerId-Name-Ticket,data=train,family='binomial')
summary(titanic.lr)
```
Among all these variables, only Ticket Class, Sex, Age, SibSp are significant.

These variables, in my opnion, make logical sense for survival rate.
Sex would be a great factor, since men back then is more likely to know how to swim. 
Age plays an important part too, since younger people might have higher chance to survive, due to increased physical strength and agility.
Having traveled with siblings and spouses traveling with might improve survival rate, since passenger has someone to help them.

The only problem I have is with ticket class. My guess is people with higher ticket class might have a higher social status, thus being prioritized. 
Or it might be the ticket class reflects access to lifeboats.

Let's fit the model one more time with these variables
```{r}
titanic.lr <- glm(formula=as.factor(Survived)~as.factor(Pclass)+as.factor(Sex)+Age+SibSp,data=train,family='binomial')
summary(titanic.lr)
```
All the variables have low p-value, with high significance values. I believe this is the best model for logistic regression.

## Prediction
Let's push the test data through this model
``` {r}
prob <- predict(titanic.lr,newdata=test,type="response")
prediction <- rep(0,nrow(test))
prediction[prob>0.5] <- 1
solution <- data.frame(PassengerID = test$PassengerId, Survived = prediction)
```
And write it into a submission file
```{r}
write.csv(solution, file = 'solution.csv', row.names = F)
head(solution)
```

** Thank you for reading my report on Logistic Regression to predict Titanic Survivals !!! **