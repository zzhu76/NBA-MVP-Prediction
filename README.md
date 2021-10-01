# NBA-MVP-Prediction

## Historical Data Analysis

#### (Grace's section)

According to the list of NBA MVP Winners from 1956 to 2021, we can get basic information of the MVPs. I analyzed the original data with Python.
The total number of MVPs is 66, average age is 27，the Youngest MVP is 22 and the oldest is 35.

![Age Distribution](https://user-images.githubusercontent.com/89670129/135693723-02fec89e-7033-4f89-b543-b3ce9a754007.png)
From this Age Distribution, initial conclusion can be drawn from the average age and the minium age —— The age of MVP tends to be players’twenties.
But is not convincible enough with partial analysis，so the deeper analysis is necessary.

The max age of the MVP is 35 and there are some MVP Winners who over age of 30.
From this Age Distribution chart, the age of MVPs can be divided into three parts： 22-24,25-29,30-35
The tendency is raising form part 1，reach the peak in part 2 and start to descend in part 3.
![Age Distribution2](https://user-images.githubusercontent.com/89670129/135693863-c7190e3e-061b-4d9b-b603-32a179e8ef77.png)

So the general conclusion is —— The age of MVP tends to be players’twenties and the older the player the possibility to win MVP is smaller.

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
