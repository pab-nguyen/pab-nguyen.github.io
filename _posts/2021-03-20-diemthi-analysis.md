---
title: Vietnam College Entrance Exam 2020
date: 2020-12-24 
layout: post
tags: data-analytics data-visualization
topics: data analytics
summary: "In Vietnam, education is taken very seriously. Parents and students prepare three years of high school for one exam, that in many people's opinions determine your future. Before 2015, students has to take two exams: one deciding whether they graduate high school, and the other is the college entrance exam. These two exams now became one, therefore it is extremely stressful for students in their last year of high school. </br></br>

In this project, I scraped 74,000 exam takers scores in 2020 from the official Government website, analyzed it to find insights about this exam. I then visualized in with Tableau to give the audience insights on this exam. "
image: /assets/images/collegeexam2020/thumbnail.jpg
---
## Introduction  
In Vietnam, high school graduates need to take a standardized college entrance exam to get considered for higher education. They need to take five subject tests: Maths, Literature, English, Social Sciences and Natural Sciences. Parents and students prepare three years of high school for this one exam, that in many people's opinions determine your future. Before 2015, students has to take two exams: one deciding whether they graduate high school, and the other is the college entrance exam. These two exams now became one, therefore it is extremely stressful for students in their last year of high school.  

I was interested to see the results of the students. In this project, I scraped 74,000 exam takers scores in 2020 from the official Government website, analyzed it to find insights about this exam. I then visualized in with Tableau to give the audience insights on this exam.  

## Ask    
There are some few questions I was curious beforehand:  
1. What is the age of the test takers?  
2. How well did the students do, score-wise?  
3. What is the score distribution among age and subjects?  
4. Are there any student that took more than five subjects?  
5. Is Nguyen still the most common last name? :D    

## Process and Process
First we will go to [http://diemthi.hcm.edu.vn/Home](http://diemthi.hcm.edu.vn/Home). There is a search box available. Students will put their candidate ID in here, press search (Xem điểm), and the site will give their results, as of below.

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/site.jpg">
</figure>

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/site2.jpg" >
	<figcaption>
		Website for scraping
	</figcaption>
</figure>

There are total 74,719 participants in this exams. From my understanding, the ID takes the form of eights digits. They start from 02000001 and end with 02074719. In this project, I created a simple Python file to crawl the data from the website, by opening the website, input in the IDs, and save the entire html code into a .txt file for all 74,719 participants. Here is how the code looks like.  

<pre>
import subprocess
result = subprocess.check_output('curl -F "sobaodanh=02000145" diemthi.hcm.edu.vn/Home/Show')
print(result)

f = open("sobaodanh.txt","r+")
f.truncate(0)
f.close()

for i in range(2000001,2074719):
    with open("sobaodanh.txt","a") as f:
        subprocess.run('curl -F "sobaodanh=0'+str(i)+'" diemthi.hcm.edu.vn/Home/Show,stdout=f)
        f.close()
        print(i-2000000)
</pre>

This code snippet will run through all 74,719 exam takers' ID, and input the html site into the text file, as explained above. It took me around 3 hours to scrape this data, and I believe there is a more time-efficient way to do this. The text file is approximately 170 MB in size.  

After scrapping process, we need to clean the file so that it allows us to see the students' name, DOB, and their scores in table format. I use another Python file to do it, however it was quite manual to look for what to delete and what to keep. You can download this cleaning python file [here](assets/images/collegeexam2020/csv_sbd.py).  

Here is how the clean csv looks like 
<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/csv.jpg">
</figure>

The headers are ID, Name, DOB and the subjects . Every row is a candidate, and their respective scores for each subjects. -1 means the candidate did not take that particular subject. 

After having a clean .csv file, I push it into Tableau Public, pivoted it, and created this visualization.
<iframe src="https://public.tableau.com/views/VietnamCollegeEntranceExamScore2020/Dashboard1?:embed=true&:showVizHome=no" height="755" width="1080"></iframe>

## Analysis
The total participants in my viz is 74,451, instead of 74,719. Approximately 300 records were missing, which I am not sure the cause of. 

Some 

