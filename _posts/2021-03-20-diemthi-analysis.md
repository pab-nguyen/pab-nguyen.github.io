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


First we will go to [http://diemthi.hcm.edu.vn/Home](http://diemthi.hcm.edu.vn/Home). There is a search box available. Students will put their candidate ID in here, press search (Xem điểm), and the site will give their results, as of below.

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/site.jpg">
</figure>

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/site2.jpg" >
	<figcaption>
		Example
	</figcaption>
</figure>

There are total 74719 participants in this exams. The ID starts from 02000001 to 02074719. I will create a simple Python file to crawl the data from the website, and save it into a .txt file.

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

This code snippet will run through all 74,719 exam takers' ID, and input the html site into the text file. 
After scrapping process, we need to clean the text file so that it allows us to see the students' name, DOB, and their scores.  

I use another Python file to do it, however it was quite manual to look for what to delete and what to keep. You can download this cleaning python file [here](assets/images/collegeexam2020/csv_sbd.py).  

Here is how the clean csv looks like 

<figure align="center">
	<img align="center" src="/assets/images/collegeexam2020/csv.jpg">
</figure>

After that, I use this csv, transform it a bit, put it into Tableau Public, and created this visualizations.
<iframe src="https://public.tableau.com/views/VietnamCollegeEntranceExamScore2020/Dashboard1?:embed=true&:showVizHome=no"  width="645" height="955"></iframe>



<div class='tableauPlaceholder' id='viz1618342006735' width="750">
	<noscript>
		<a href='#'>
			<img alt='Vietnam College Entrance Exam 2020 Statistics ' src='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VietnamCollegeEntranceExamScore2020&#47;Dashboard1&#47;1_rss.png' style='border: none' />
		</a>
	</noscript>
	<object class='tableauViz'  style='display:none;' width="750">
		<param name='host_url' value='https%3A%2F%2Fpublic.tableau.com%2F' /> 
		<param name='embed_code_version' value='3' /> 
		<param name='site_root' value='' />
		<param name='name' value='VietnamCollegeEntranceExamScore2020&#47;Dashboard1' />
		<param name='tabs' value='no' />
		<param name='toolbar' value='yes' />
		<param name='static_image' value='https:&#47;&#47;public.tableau.com&#47;static&#47;images&#47;Vi&#47;VietnamCollegeEntranceExamScore2020&#47;Dashboard1&#47;1.png' /> 
		<param name='animate_transition' value='yes' />
		<param name='display_static_image' value='yes' />
		<param name='display_spinner' value='yes' />
		<param name='display_overlay' value='yes' />
		<param name='display_count' value='yes' />
		<param name='language' value='en' />
	</object>
</div>                

<script type='text/javascript'>
    var divElement = document.getElementById('viz1618342006735');                    
    var vizElement = divElement.getElementsByTagName('object')[0];                    
    if 
    	( divElement.offsetWidth > 800 ) { vizElement.style.width='1366px';vizElement.style.height='795px';} 
    else if 
    	( divElement.offsetWidth > 500 ) { vizElement.style.width='1366px';vizElement.style.height='795px'} 
	else 
		{ vizElement.style.width='100%';vizElement.style.height='2227px';}                     
	var scriptElement = document.createElement('script');                    
	scriptElement.src = 'https://public.tableau.com/javascripts/api/viz_v1.js';                    
	vizElement.parentNode.insertBefore(scriptElement, vizElement);                
</script>