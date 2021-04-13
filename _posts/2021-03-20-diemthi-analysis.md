---
title: Vietnam College Entrance Exam 2020
date: 2020-12-24 
layout: post
tags: data-analytics data-visualization
topics: data analytics
summary: "In Vietnam, Education is taken very seriously. Parents and students prepare three years of high school for one exam, that in many people's opinions determine someone's future. Before 2015, students has to take two exams: one deciding whether they graduate high school, and the other is the college entrance exam. These two exams now became one, therefore it is extremely stressful for students in their last year of high school. </br></br>

In this project, I scraped 74,000 exam takers scores in 2020 from the official Government website, analyzed it to find insights about this exam. I then visualized in with Tableau to give the audience insights on this exam. "
image: /assets/images/collegeexam2020/thumbnail.jpg
---


First we will go to [http://diemthi.hcm.edu.vn/Home](http://diemthi.hcm.edu.vn/Home). There is a search box available. Students will look put their candidate ID in here, press search, and the site will give their results, as of below.

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/site.jpg" >
</figure>

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/site1.jpg" >
</figure>

There are total 74719 participants in this exams. The ID starts from 02000001 to 02074719. I will create a simple Python file to crawl the data from 