# Polynomial Regression

# Data Reprocessing----

#Importing dataset
dataset = read.csv("Position_Salaries.csv")
dataseset = dataset[, 2:3 ]

#Splitting dataset into Training Set and Test Set
#Not splitting, because the dataset is small

#Feature Scalling
#training_set[, 2:3] = scale(training_set[, 2:3])
#test_set[, 2:3] = scale(test_set[,2:3])

# Fitting the linear regression model to the dataset
lin_reg = lm(formula = Salary ~ Level,
             data=dataset)

# Fitiing the polynomial regression model to the dataset
dataset$Level2 = dataset$Level^2
dataset$Level3 = dataset$Level^3
dataset$Level4 = dataset$Level^4
pol_reg = lm(formula = Salary ~ .,
             data=dataset)

# Visualising the Linear Regression result
#install.packages('ggplot2')
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(lin_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff(Linear Regeression)') +
  xlab('Level') + 
  ylab('Salary')
  
# Visualising the Polynomial Regression result
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(pol_reg, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff(Polynomial Regeression)') +
  xlab('Level') + 
  ylab('Salary')

# Prediciting a new result with Linear Regression
y_pred = predict(lin_reg, data.frame(Level = 6.5))

# Predicting a new result with Polynomial Regression
y_pred = predict(pol_reg, data.frame(Level = 6.5, 
                                     Level2 = 6.5^2, 
                                     Level3 = 6.5^3,
                                     Level4 = 6.5^4))
