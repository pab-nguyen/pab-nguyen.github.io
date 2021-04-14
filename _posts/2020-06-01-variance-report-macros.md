--- 
layout: post
title: Variance Reports Full Automation
tags: excel-vba
date: 2020-06-01
image: /assets/variance.JPG
summary: There is a common process in drug manufacturing, where after they sold their products to customers, they reimburse them. Customers will usually send in an invoice, claiming they should get a reimbursement based on the percentage written in the contract. Manufacturers will analyze these claims, and then issue a report to state whether the claim is valid, and then issue a reimbursement. This is called Variance Reporting.</br></br>This reporting process often takes 2 - 3 days from the day they receive the claims, depends on the client size and the quantities of brands they bought. I have built a VBA script to automate this reporting process, reducing it to 30 minutes on average. </br></br> One of my biggest Excel VBA scripts written to date. ​



<p align="center">
	<video muted autoplay controls loop width="560">
    	<source src="{{ site.media_path }}/variance.mp4" type="video/mp4">
	</video>
</p>

### Overview 
One of my biggest Excel VBA scripts written to date. ​

There is a common process in drug manufacturing, where after they sold their products to customers, they reimburse them. Customers will usually send in an invoice, claiming they should get a reimbursement based on the percentage written in the contract. Manufacturers will analyze these claims, and then issue a report to state whether the claim is valid, and then issue a reimbursement. This is called Variance Reporting.

This reporting process often takes 2 - 3 days from the day they receive the claims, depends on the client size and the quantities of brands they bought. I have built a VBA script to automate this reporting process, reducing it to 30 minutes on average.  

### How it works  
This macro works by imitating the workflow of human analysts. It create two pivot tables using the data given. One contains the valid claims, and the other contains invalid claims. Then the macro will iterate through each product, find the appropriate number and plug it into individual reports and exclusion report. After that, it will loop through these individual report Worksheet and sum them up to get the Variance Report.

### Download 

You can download the macro and other files below.

[Macro](https://drive.google.com/file/d/1tNfYE2xwUEqsVwPspBiKobMcqOQUefTv/view?usp=sharing)

[Data file example](https://drive.google.com/file/d/17vi6YcvymiNXZ60MJ6ldUMDKe_w8ezGK/view?usp=sharing)

[Instructions](https://drive.google.com/file/d/1dKkPqG6Wjx5n8GEFURgIPNhEmlsyNd4i/view?usp=sharing)