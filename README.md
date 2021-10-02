# NBA-MVP-Prediction

## Historical Data Analysis

#### Regional Analysis
![map](https://user-images.githubusercontent.com/89670129/135697451-be9649bb-fa51-4999-bb11-ab8e87c33ba2.png)

#### Age Distribution

According to the list of NBA MVP Winners from 1956 to 2021, we can get basic information of the MVPs. I analyzed the original data with Python.
The total number of MVPs is 66, average age is 27，the Youngest MVP is 22 and the oldest is 35.
![Age Distribution](https://user-images.githubusercontent.com/89670129/135693723-02fec89e-7033-4f89-b543-b3ce9a754007.png)
From this Age Distribution, initial conclusion can be drawn from the average age and the minium age —— The age of MVP tends to be players’twenties.
But is not convincible enough with partial analysis，so the deeper analysis is necessary.

The max age of the MVP is 35 and there are some MVP Winners who over age of 30.
From this Age Distribution chart, the age of MVPs can be divided into three parts： 22-24,25-29,30-35
The tendency is raising form part 1，reach the peak in part 2 and start to descend in part 3.
![Age Distribution 2](https://user-images.githubusercontent.com/89670129/135693863-c7190e3e-061b-4d9b-b603-32a179e8ef77.png)
So the general conclusion is —— The age of MVP tends to be players’twenties and the older the player the possibility to win MVP is smaller.


Position Distribution also demonstrate some rules. From the Position Distribution Chart we can see the number of three major positions: Center 27 > Forward 20 > Guard 19.
The numbers are almost the same, so the distribution of the MVP is very even.
Perhaps the difference in position will affect the player's posscession of the ball, but what is certain that being a MVP  must be both offensive and defensive.

#

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
