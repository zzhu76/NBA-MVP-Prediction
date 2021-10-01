# NBA-MVP-Prediction

## Historical Data Analysis

## Data Selection
#### There are many features that affect MVP evaluation, we decided to use Random Forest Regression and Heatmaps to indentify which features that are important to our prediction model。

#### This is the workbook ![Data Selection Workbook](https://github.com/zzhu76/NBA-MVP-Prediction/blob/main/MVP_Feature_Selection_.ipynb)

#### Random Forest Regression
![Random Forest Regression](https://user-images.githubusercontent.com/89670129/135665300-428f22db-47ba-4ea4-8f7c-9ad99c065815.jpg)

#### Heatmaps
![Heatmaps](https://user-images.githubusercontent.com/89670129/135664857-d556adb7-a4c9-44af-b94d-048f90d29934.jpg)

#### Combine the result from our previous models, our final feature selection is the following: points, assist,  total rebound, win shares, block, game played, minute played, and steals. (each feature is per-game based)


## Prediction 
The MVP prediction model consists of four parts. 

  - Data Preparation
  - Regression 
  - Classification 
  - Accuracy

#### Data Preparation
We used data from season 1980 to last season, season 2020. We handled filled data with mean, and label encoded categorical features, team, for example. Also, we selected features that best describes a players performance. 

#### Regression
The MVP prediction model predicts the MVP after the season starts. It takes the player's stats of the current season as input, and outputs the predicted vote share, which is the number of votes won by the player over the total votes. We used linear regression model to predict the vote share based on the player's stats, 

#### Classification
After we assign each player a predicted vote share, we pick the player with the highest predicted vote share each season to be the MVP. 

#### Accuracy
We trained the model using data from 1980 to 2007, and tested the model's performance on season 2008 to 2020. We implemented the 5 fold cross validation with mean squared error to test the accuracy of regression and classification. The classification model has an accuracy 63.5. The accuracy for 2008-2015 is 75%, and it dropped significantly to 40% for the remain five year. What’s the problem? The problem is James Harden. Our model predicted him to be the MVP 5 times, while he only won MVP only once in 2017. Why our model loves him this much? The answer lies in the data set. As you can see, WS is a high level feature we used in the model, it stands for win share. it measures the contribution of a player’s individual performance to the win of team. In the past 27 out of 40 seasons, the selected mvp is the player with the highest WS that season. That is why our linear model treat WS as priority. However, take season 2016 as an example, JH had a WS higher than the Russel Westbrooke, while Russel was the actual MVP winner. 

#### Future Work
We could add more features, team performance and popularity for example. There are very few players in the history of NBA who won an MVP award with his team not being able to make to the playoff. Consequently, team performance is definitely a considerably important feature to add to our model. We also could scrape a player's popularity from the internet. Instaram followers, Tweeter comments, used frequency on NBA 2K and etc. We also could add weight to the features since features dont share the same important. We could alos implement different models and test their performances, like KNN, where we form a cluster of players based on their feature, and hopefully, the mvp group could form a small and dense one. 
