---
layout: post
title: Client Calendar Log
date: 2020-06-01
tags: excel-vba
image: /assets/calendar-log.JPG
summary: The sales department usually keep a document to record meetings with clients, which they update on a weekly basis. They used Outlook, WebEx to set up the meetings, then update it manually into this document. The manual update will take around a half hour every week. </br></br> I have built a VBA script to automate this process. It allows users to extract the calendar from Outlook, under a .csv file, then extract the data from this .csv file into a template. This script reduces the process to only five minutes. You can watch the video to understand how it works.

---

### Overview
This macro is used to automate the client meetings logs recording process. I wrote this Excel VBA Script during one of my internships. The sales department usually keep a document to record meetings with clients, which they update on a weekly basis. They used Outlook, WebEx to set up the meetings, then update it manually into this document. The manual update will take around a half hour every week. 

I have built a VBA script to automate this process. It allows users to extract the calendar from Outlook, under a .csv file, then extract the data from this .csv file into a template. This script reduces the process to only five minutes. You can watch the video to understand how it works. 

### How it works  
User takes the calendar CSV file from outlook, then open the file along with the macro file. The macro will iterate through each rows in the CSV file, and input it into the template. A written instructions is available below.


<p align="center">
	<video muted autoplay controls loop width="560">
    	<source src="{{ site.media_path }}/calendar.mp4" type="video/mp4">
	</video>
</p>

### Download
You can download the macro and the calendar file below.

[Macro](https://drive.google.com/file/d/1TOeSl4KmvTY3jcV-nnfoyeT91QMNFDGU/view?usp=sharing)

[Calendar file example (.csv)](https://drive.google.com/file/d/1KNztb087SWLPrngjaNlQJe_eSZOuSc9l/view?usp=sharing)

[Instructions](https://drive.google.com/file/d/18-_Fd9yXTxATUOXfBLPnisGs6Nw4XDQj/view?usp=sharing) 