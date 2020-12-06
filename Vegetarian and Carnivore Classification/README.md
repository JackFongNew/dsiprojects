## Project 3: Vegetarian and Carnivore Classification

### Executive Summary
Food is a uniquely important commodity, no one can avoid consuming it. At the same time, food is highly complex and includes a vast variety beyond that which we can directly grow or pick. Foods are composed of plethora of substances, some of these we need, some we should avoid, others we should limit. Different people have different needs for these substances, and different people have different tolerances for them.

### Problem Statement
How might I better understand what is important to customers and their needs so that I can assist my marketing team to develop relevant products and services to better meet those needs.

### Strategy
I am a data scientist working in a food industry company. My purpose of this project is to develop a classification model so that I can identify whether the user is a vegetarian or carnivore, as well as capturing the keywords of the conversations to determine trending topics.

Nowadays, marketing strategy has moved from B2C method (companies create and sell products that they think the customers needs) to the C2B method (observing customers' behavior, listening and reviewing customers' comments and co-create new products). The C2B approach evolved from the growth of popular consumer-generated media and content across different consumer online outlets, such as social networks, websites, blogs, podcasts or videos. To be able to better serve and achieve my customers' expectations, I would have to know the latest and hottest topics about food and the best place for me to get this information is through tracking trending topics on social media or blogs.

### Methodology
1. Set the problem statement.
2. Web scraping and data collection(Reddit).
3. Data massage and data preparation.
4. Exploratory data analysis.
5. Regularization and classification: Logistic Regression, Multinomial Naive Bayes, Random Forest.
6. Evaluation: Confusion Matrix and ROC curve with AUC.
7. Misclassification Analysis.
8. Conclusion and Recommendations.

### Stakeholder
My main stakeholder for this project will be my company's marketing team whereby they can utilize the information to make better decision for new products and services.

### Data Source
Reddit is an American social news aggregation, web content rating and discussion website. It is a network of communities based on people's interests. I will be using the posts from Reddit website for my project.

- [Reddit - Vegetarian](https://www.reddit.com/r/vegetarian/)
- [Reddit - Carnivore](https://www.reddit.com/r/zerocarb)

### Data Dictionary

|No.| Feature| Type | Description|
|:--|:---:|:--:|:---|
|1.| subreddit| object| Specific topic on the Reddit website|
|2.| text_feature| object| Contents of a post|
|3.| vegetarian| string| Binary variable for the specific topics. <br> 1: vegetarian </br> <br> 0: zerocarb/ carnivore </br>|

## Conclusion

In this project, I have used 3 different classifier models and completed a comparative study of their performance. 

From the analysis, Logistic Regression model has successfully solved my problem statement because it has the highest test accuracy (90.31%) of the prediction with lowest combination of false positive (29) and false negative (24) values. 

The accuracy of the model, low values of false positive and false negative are important to my analysis because I want to correctly interpret the customers' information so that my company can better serve their needs.

## Recommendation
1. __Classifier Model__ <br> Different classifiers can be used and their performance can be evaluated to find better predictions. Tuning of parameters would also help to get a better predictions. </br>


2. __NLP__ <br>Optimize the stop words and explore different NLP methods that generate the root form of the inflected words in order to improve the text classification accuracy. </br>


3. __Data__ <br>Scrape and collect more data for a better prediction, such as getting information from different blogs or social media instead of Reddit. </br>