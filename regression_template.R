# Regression Template in R

#Importing the dataset
dataset = read.csv('')

#Splitting the dataset
install.packages('caTools')
library(caTools)
set.seed(123)
split = sample.split(dataset$, SplitRatio = 2/3)
training_set = subset(dataset, split = TRUE)
test_set = subset(dataset, split = FALSE)

#Feature Scalling
# training_set = scale(training_set)
# test_set = scale(test_set)

# Fitting the regression model to the dataset
#Create your regressor

# Predicting a new result with Regression
y_pred = predict(regressor, data.frame(Level = 6.5))

# Visualising the Regression result
library(ggplot2)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = dataset$Level, y = predict(regressor, newdata = dataset)),
            color = 'blue') +
  ggtitle('Truth or Bluff(Regression Model)') +
  xlab('Level') + 
  ylab('Salary')

# Visualising the Regression result (smoother)
library(ggplot2)
x_grid = seq(min(dataset$Level), max(dataset$Level), 0.01)
ggplot() +
  geom_point(aes(x = dataset$Level, y = dataset$Salary),
             color = 'red') + 
  geom_line(aes(x = x_grid, y = predict(regressor, newdata = data.frame(Level = x_grid))),
            color = 'blue') +
  ggtitle('Truth or Bluff(Regression Model)') +
  xlab('Level') + 
  ylab('Salary')

