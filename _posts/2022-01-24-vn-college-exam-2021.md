---
title: Vietnam College Exam 2021
date: 2020-12-24 
layout: post
tags: data-visualization
topics: data analytics
summary: "In Vietnam, education is taken very seriously. Parents and students prepare three years of high school for one exam, that in many people's opinions determine your future. Before 2015, students has to take two exams: one deciding whether they graduate high school, and the other is the college entrance exam. These two exams now became one, therefore it is extremely stressful for students in their last year of high school. </br></br>

In this project, I scraped 74,000 exam takers scores in 2020 from the official Government website of Ho Chi Minh City, analyzed it then visualized in with Tableau to give the audience insights on this exam. "
image: /assets/images/collegeexam2021/thumbnail.png
---
## Introduction  
For those of you who are not familiar with the education system in Vietnam, there is an important national exam held every year during the summer, which will determine whether a person can get into college or not. And as I am writing this post in 2022, college is still regarded to be a big decision that set your life course. Personally, I don't believe that's true, yet I am interested to see how Vietnamese students did against this extremely hard exam.  

Last year, I scraped exam scores for 74,000 exam takers in Ho Chi Minh city. This year, I am more ambitious, and decided to scrape almost a million exam takers' results. My process is scraping, cleaning and then visualizing in Tableau.  

## Collect and Process
The first step to data collection is to figure how to access website and set up a scraper. 
The website we are accessing is https://thanhnien.vn/giao-duc/tuyen-sinh/2021/tra-cuu-diem-thi-thpt-quoc-gia.html

The scraping file is available [here](https://pab-nguyen.github.io/assets/file/scraping.py)
## Visualization

After having a clean .csv file, I push it into Tableau Public, pivoted it, and created this visualization.
<iframe src="https://public.tableau.com/views/VietnameseCollegeTest2021/VietnamCollegeExam2021?:embed=true&:showVizHome=no" height="755" width="1150"></iframe>


If you have anything to suggest, please email me. I would love to hear from you! 