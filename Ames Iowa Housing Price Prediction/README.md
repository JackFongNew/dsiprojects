## Project 2: Housing Price Prediction in Ames, Iowa

## Executive Summary

### Problem Statement
My problem statement is: How might I better estimate housing prices in Ames, Iowa so that I can manage potential buyers' expectations?

### Approach
My approach of this project is to study the historical housing prices in Ames and the housing dataset features provided by Ames, Iowa Assessor's Office. I will build a linear regression model, and will be evaluating its performance using the Root Mean Squared Error (RMSE) metric. The processes involved data preparation, data massage, data visualization, regularization and recursive feature elimination.  

### Stakeholder
I am a freelance data analyst building a housing price prediction model and my prime stakeholders are property agents/agencies who will use the model to manage their potential buyers' expectations.

Other potential stackholders include local banks and Ames Housing Authority.

### Data source
The housing data set provides historical housing prices from 206 to 2010, and 80 other features related to the property, locations and sales processes.
- [Ames, Iowa Housing Dataset](https://www.kaggle.com/c/dsi-us-6-project-2-regression-challenge/data)

### Data Dictionary
|No.|Feature| Type | Description
|:--|---:|:--:|---:
|1.	|ID |integer |Observation number
|2.	|PID |object |Parcel identification number - can be used with city web site for parcel review. 
|3.	|MS SubClass |object |Identifies the type of dwelling involved in the sale.	
|4.	|MS Zoning |object |Identifies the general zoning classification of the sale.
|5.	|Lot Frontage |float |Linear feet of street connected to property
|6.	|Lot Area |integer |Lot size in square feet
|7.	|Street |object |Type of road access to property
|8.	|Alley |object |Type of alley access to property
|9.	|Lot Shape |object |General shape of property
|10.|Land Contour |object |Flatness of the property
|11.|Utilities |object |Type of utilities available
|12.|Lot Config |object |Lot configuration
|13.|Land Slope |object |Slope of property
|14.|Neighborhood |object |Physical locations within Ames city limits (map available)
|15.|Condition 1 |object |Proximity to various conditions
|16.|Condition 2 |object |Proximity to various conditions (if more than one is present)
|17.|Bldg Type |object |Type of dwelling
|18.|House Style |object |Style of dwelling
|19.|Overall Qual |integer |Rates the overall material and finish of the house
|20.|Overall Cond |integer |Rates the overall condition of the house
|21.|Year Built |integer |Original construction date
|22.|Year Remod/Add |integer |Remodel date (same as construction date if no remodeling or additions)
|23.|Roof Style |object |Type of roof
|24.|Roof Matl |object |Roof material
|25.|Exterior 1st |object |Exterior covering on house
|26.|Exterior 2nd |object |Exterior covering on house (if more than one material)
|27.|Mas Vnr Type |object |Masonry veneer type
|28.|Mas Vnr Area |float |Masonry veneer area in square feet
|29.|Exter Qual |object |Evaluates the quality of the material on the exterior 
|30.|Exter Cond |object |Evaluates the present condition of the material on the exterior
|31.|Foundation |object |Type of foundation
|32.|Bsmt Qual |object |Evaluates the height of the basement
|33.|Bsmt Cond |object |Evaluates the general condition of the basement
|34.|Bsmt Exposure |object |Refers to walkout or garden level walls
|35.|BsmtFin Type 1	|object |Rating of basement finished area
|36.|BsmtFin SF 1 |float |Type 1 finished square feet
|37.|BsmtFin Type 2	|object |Rating of basement finished area (if multiple types)
|38.|BsmtFin SF 2 |float |Type 2 finished square feet
|39.|Bsmt Unf SF |float |Unfinished square feet of basement area
|40.|Total Bsmt SF |float |Total square feet of basement area
|41.|Heating |object |Type of heating
|42.|Heating QC |object |Heating quality and condition
|43.|Central Air |object |Central air conditioning
|44.|Electrical |object |Electrical system
|45.|1st Flr SF |integer |First Floor square feet
|46.|2nd Flr SF |integer |Second floor square feet
|47.|Low Qual Fin SF |integer |Low quality finished square feet (all floors)
|48.|Gr Liv Area |integer |Above grade (ground) living area square feet
|49.|Bsmt Full Bath |float |Basement full bathrooms
|50.|Bsmt Half Bath |float |Basement half bathrooms
|51.|Full Bath |integer |Full bathrooms above grade
|52.|Half Bath |integer |Half baths above grade
|53.|Bedroom AbvGrd	 |integer |Bedrooms above grade (does NOT include basement bedrooms)
|54.|Kitchen |integer |Kitchens above grade
|55.|Kitchen Qual |object |Kitchen quality
|56.|TotRms AbvGrd	|integer |Total rooms above grade (does not include bathrooms)
|57.|Functional |object |Home functionality (Assume typical unless deductions are warranted)
|58.|Fireplaces |integer |Number of fireplaces
|59.|Fireplace Qu |object |Fireplace quality
|60.|Garage Type |object |Garage location
|61.|Garage Yr Blt |float |Year garage was built
|62.|Garage Finish |object |Interior finish of the garage
|63.|Garage Cars |float |Size of garage in car capacity
|64.|Garage Area |float |Size of garage in square feet
|65.|Garage Qual |object |Garage quality
|66.|Garage Cond |object |Garage condition
|67.|Paved Drive |object | Paved driveway
|68.|Wood Deck SF |integer |Wood deck area in square feet
|69.|Open Porch SF |integer |Open porch area in square feet
|70.|Enclosed Porch |integer |Enclosed porch area in square feet
|71.|3ssn Porch |integer |Three season porch area in square feet
|72.|Screen Porch |integer |Screen porch area in square feet
|73.|Pool Area |integer |Pool area in square feet
|74.|Pool QC |object |Pool quality
|75.|Fence |object |Fence quality
|76.|Misc Feature |object |Miscellaneous feature not covered in other categories
|77.|Misc Val |integer |$Value of miscellaneous feature
|78.|Mo Sold |integer |Month Sold (MM)
|79.|Yr Sold |integer |Year Sold (YYYY)
|80.|Sale Type |object |Type of sale
|81.|SalePrice |integer |Sale price $$


## Conclusion
From my analysis of the 80 features, I have created 28 new features (7 from the actual features, 6 new combined features and 15 dummy features). In the end, I have achieved the best results using the ElasticNEt regression.

Of the top 5 features out of the 28 features in terms of price predictability based on the Lasso bar chart, 4 of them relate to the housing profile and only 1 (#4 neighborhood) relates to location.
1. above ground living area
2. overall (combination of overall quality and overall condition)
3. total basement area
4. neighborhood
5. quality (quality rating of various features)

However, the top 3 features that hurt the value most are:
1. overall age(age of the house with/ or without remodeling)
2. ms_subclass_30
3. ms_subclass_160

From my knowledge of housing prices and the property industry in general, it surprises me that location does not rate higher as the predictor. Moving forward, I should consider to include more location related features to improve my prediction. The aging of the house will obviously reduce the housing price.

## Conclusion
From my analysis of the 80 features, I have created 28 new features (7 from the actual features, 6 new combined features and 15 dummy features). In the end, I have achieved the best results using the ElasticNEt regression and the model is good for price prediction.

Of the top 5 features out of the 28 features in terms of price predictability based on the ElasticNet bar chart, 4 of them relate to the housing profile and only 1 (#4 neighborhood) relates to location.
1. above ground living area
2. overall (combination of overall quality and overall condition)
3. total basement area
4. neighborhood
5. quality (quality rating of various features)

However, the top 3 features that hurt the value most are:
1. overall age(age of the house with/ or without remodeling)
2. ms_subclass_30
3. ms_subclass_160

## Recommendations
### Value Impact Business Recommendations
The owner of the house can do a number of remodeling improvement to increase the value of the house but these would need to be cost justified. Example include expansion of the masonry veneer area, increasing size of garage, changing garage style or house style.

Based of the correlation between the neighborhoods and saleprice, the neighborhoods worth investing in are Timberland, College Creek, Somerset, Stone Brook, Northridge Heights, Veenker and Northridge.

The model is constructed based of the Ames, Iowa dataset and will not generalize well to other cities since it includes specific neighbourhoods by name. The basic predictability of the model is still applicable but it has to be customized based on the other cities features which involve changes.

### Data Massage
When running data massage routine, we must ensure our actions maintain data integrity, e.g. determining the percentage of allowable data to eliminate, imputation of the missing data or the consideration of the outlier(s). All these decisions will affect the prediction outcome.

### Feature Engineering Process
Feature engineering process requires lots of research, relevant domain knowledge and thorough EDA skills. A data analyst needs to acquire sufficient experience and domain knowledge to assist the efficient feature engineering process.

### Regression Model Selection
It is always good to apply various model to perform the regularization to get the better outcome. For my selected features, Ridge regression has computed lesser root mean squared error (RMSE) compare to the other regression model.


## Further Recommendation
From my knowledge of housing prices and the property industry in general, it surprises me that location does not rate higher as the predictor. I should consider to include more location related features to improve my prediction.

From my perspective, we have to include all the factors capable of impacting housing prices such as economy crisis and changes in state government housing policies. Doing so, we can have a better prediction of the housing price.

In addition, it is recommended that the model has to be revisited and updated with new information to ensure the model is improved.

Further research should be carried out on how to improve the feature engineering, further experiment with other models and start different polynomial features transform to improve the price prediction model.