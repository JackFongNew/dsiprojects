## Trend in SAT and ACT in 2017 & 2018

### Problem Statement

In the US, all high school students are required to take college entrance tests before they submit their application to any college. The SAT and ACT are the most popular college entrance test administered in the US.

The question is how might we increase the participation rate among high school students in the United States in taking the SAT test for college admissions so that I can make recommendation to the College Board that administers the SAT test.

### Executive Summary

In this project, I will be examing the data for SAT and ACT in 2017 and 2018. The data includes participation rates, mean score of each subject, and total/composite scores which are organized at the state level in alphabet order.

Throughout this data analysis exploration, I will perform data preparation, data visualization and analyzing the SAT and ACT participation rates as well as the scoring across the state in the US. Then, I will identify trend in the data and combine with my research to develop potential solutions to the problem statement.

__Data source:__
- [SAT 2017 Data](https://blog.collegevine.com/here-are-the-average-sat-scores-by-state/)
- [ACT 2017 Data](https://www.act.org/content/dam/act/unsecured/documents/cccr2017/ACT_2017-Average_Scores_by_State.pdf)
- [SAT 2018 Data](https://reports.collegeboard.org/archive/sat-suite-program-results/2018/state-results)
- [ACT 2018 Data](https://nces.ed.gov/programs/digest/d18/tables/dt18_226.60.asp)

### Data Dictionary Entry:

|__Feature__|__Type__|__Dataset__|__Description__|
|---:|:---:|:---:|---:|
|us_state|*object*|SAT/ACT|51 states in the United States|
|sat_part_17|*float*|SAT|Statewide SAT participation rate by percentage in 2017|
|sat_erw_17|*integer*|SAT|SAT 2017 *Evidence-Based Reading and Writing* test mean score(200-800) of each state|
|sat_math_17|*integer*|SAT|SAT 2017 *Math* test mean score(200-800) of each state|
|sat_total_17|*integer*|SAT|SAT 2017 *Total* is the sum of both test mean score(400-1600) of each state|
|act_part_17|*float*|ACT|Statewide ACT participation rate by percentage in 2017|
|act_eng_17|*float*|ACT|ACT 2017 *English* test mean score(1-36) of each state|
|act_math_17|*float*|ACT|ACT 2017 *Math* test mean score(1-36) of each state|
|act_read_17|*float*|ACT|ACT 2017 *Reading* test mean score(1-36) of each state|
|act_sci_17|*float*|ACT|ACT 2017 *Science* test mean score(1-36) of each state|
|act_comp_17|*float*|ACT|ACT 2017 *Composite* is the mean score(1-36) of the 4 tests of each state|
|sat_part_18|*float*|SAT|Statewide SAT participation rate by percentage in 2018|
|sat_erw_18|*integer*|SAT|SAT 2018 *Evidence-Based Reading and Writing* test mean score(200-800) of each state|
|sat_math_18|*integer*|SAT|SAT 2018 *Math* test mean score(200-800) of each state|
|sat_total_18|*integer*|SAT|SAT 2018 *Total* is the sum of both test mean score(400-1600) of each state|
|act_part_18|*float*|ACT|Statewide ACT participation rate by percentage in 2018|
|act_eng_18|*float*|ACT|ACT 2018 *English* test mean score(1-36) of each state|
|act_math_18|*float*|ACT|ACT 2018 *Math* test mean score(1-36) of each state|
|act_read_18|*float*|ACT|ACT 2018 *Reading* test mean score(1-36) of each state|
|act_sci_18|*float*|ACT|ACT 2018 *Science* test mean score(1-36) of each state|
|act_comp_18|*float*|ACT|ACT 2018 *Composite* is the mean score(1-36) of the 4 tests of each state|

### Outside Research

I noticed many interesting changes in a number of states in terms of SAT and ACT participation rates. 2 states in particular caught my attention.

First we look at ACT particiation rate for __Colorado__ in 2017 and 2018. You can see the participation rate increased from 11% to 100%, which is 809% increment. While at the same time, the ACT participation rate has decreased from 100% to 30%. Such significant changes prompted me to search for an explanation. In 2017, the state authority switched from mandatory ACT to mandatory SAT testing which explained the changes. The core reason for the switch was that state officials deemed the SAT test to be more closely aligned to the state's academic standard.

Now we will look at participation rate for __Illinois__ in 2017 and 2018. The participation rate for the SAT has increased by 1,000%, which is a huge increment meanwhile the ACT decreased by 54%. I discovered that state switched from mandatory ACT to mandatory SAT test. The Illinois State Board of Education (ISBE) claimed that SAT test is better aligned with the state's academic standard. Thus, ISBE has made SAT test mandatory for high school graduates.

Another inconsistency I observed was in __Alaska__. Alaska shows different result of participation rate whereby the sum of SAT and ACT test participation rate in 2018 is only 76%, which is less than 100%. In 2017, the Alaska Legislature relaxed the previous requirement that required students to take only SAT or ACT and provided the option to take the workKeys test as well for admission evaluation. You can see the participation rate for ACT in 2018 has decreased by 49% while SAT increased by 13%.

__References:__
- [Testive: Colorado Changed to the SAT in 2017](https://www.testive.com/colorado-sat-change-2017/#:~:text=On%20April%2011th%2C%202017%20all,a%20new%20four%20hour%20exam.)
- [Chalkbeat](https://co.chalkbeat.org/2017/8/17/21100853/sat-scores-show-mixed-results-on-whether-colorado-juniors-are-on-track-for-college)
- [Illinois moves ahead with new testing plan, replacing ACT with SAT](https://www.chicagotribune.com/news/ct-illinois-chooses-sat-met-20160211-story.html)
- [Alaska high school students no longer need national tests to graduate](https://www.adn.com/alaska-news/education/2016/06/30/students-no-longer-need-national-tests-to-graduate/)

### Conclusions and Recommendations

Based on my data exploration and outside research, the participation on either of the test is mainly influenced by state authorities. A small portion of the participation rate is came from the individual preference. In the US, 18 states have mandated the ACT test and 11 states have mandated the SAT test while the rest of the states have no restriction on the choice of college entrance test.

Let's consider __Iowa__ as it only has less than 4% of the SAT participation rate in 2017 and 2018. Iowa has not made any test mandatory and all students can go with their preference. In order to the boost the SAT participation rate in Iowa, the College Board should consider to revamp and improve the SAT test so that it align with Iowa education standard and propose to state authority. 

There are 2 broad approaches to driving change- the __Carrot__ and the __Stick__. The Carrot relies on incentives while the Stick is more directive.

__Carrot:__ The College Board should consider providing additional subsidies to the state authority to help the state support the participants from low income families. Besides that, College Board should consider offering free tuition classes, either remotely or on campus to help the students prepare for the SAT test. This is beacuse the sudden switch of test might lead to large changes to average scores if the high schools curriculum is no aligned to the test or the students are not prepared for the SAT test. This happened in Colorado and Illinois.

__Stick:__ The Iowa Department of Education should consider making SAT test mandatory as the college admission requirement which provides benefits to the education system and the students. High schools will make sure all the subjects are covered and educate the students with the proper method and mindset to tackle SAT test. Besides that, the SAT test can be use to benchmark students and to analyse the high-school education system.

Overall, from my perspective, all state authorities should consider encouraging participants to take more than one test in order to give themselves more opportunities to apply for colleges in other states. Further research should be carried out on how to encourage the participants to take more than one test and show the participants the benefits of taking more than one test.

In conclusion, I hope I have demonstrated in a number of instances above that the states' participation rate is not the ideal benchmark for comparison due to the different number of participants in each state. The sample should be drawn from the population randomly to make the analysis more comparable. 

__References:__
- [Does your state require the SAT or ACT?](https://www.testive.com/state-sat-act/)