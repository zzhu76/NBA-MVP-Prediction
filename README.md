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
