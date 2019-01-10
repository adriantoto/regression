# SVR

#Importing the dataset
dataset = read.csv('Position_Salaries.csv')
dataset = dataset[2:3]

#Splitting the dataset
#install.packages('caTools')
#library(caTools)
#set.seed(123)
#split = sample.split(dataset$, SplitRatio = 2/3)
#training_set = subset(dataset, split = TRUE)
#test_set = subset(dataset, split = FALSE)

#Feature Scalling
#dataset = scale(dataset)

# Fitting the SVR model to the dataset
#install.packages('e1071')
library(e1071)
regressor = svm(formula=Salary ~ .,
                data=dataset,
                type='eps-regression')

# Predicting a new result with SVR
y_pred = predict(regressor, data.frame(Level = 6.5))

# Visualising the SVR result
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff(SVR Model)') +
  xlab('Level') + 
  ylab('Salary')

# Visualising the SVR result (smoother)
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.1)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff(SVR Model)') +
  xlab('Level') + 
  ylab('Salary')

