---
layout: post
title: An Overview of Equity Valuation
date: 2020-09-01
tags: finance
summary: Some samples of my financial analysis work. I used to work as an investment analyst for an asset management firm back in Vietnam. I was in team managing a small fund of $3M USD. My responsiblities were to find opportunities in public stocks of the Plastics industry, analyze those stocks to find their appropriate value, figure out whether this is a good investment and pitch my recommendation to the portfolio managers.

image: /assets/equity.JPG

---

### Overview
I used to work as an investment analyst for an asset management firm back in Vietnam. I was in team managing a small fund of $3M USD. My responsiblities were to find opportunities in public stocks of the Plastics industry, analyze those stocks to find their appropriate value, figure out whether this is a good investment and pitch my recommendation to the portfolio managers. 

<p align="center">
	<img align="center" src="/assets/equity.JPG" >
</p>

### Equity Valuation Samples
This is the samples of my financial analysis work. You can download it by clicking on these links.

[MSFT 05/03/2020](https://drive.google.com/file/d/1JVACo-lfvI9EMP0c8RZCmJByUMLUbOcs/view?usp=sharing)

[TXN 11/26/2019](https://drive.google.com/file/d/1MBhZ71mA1huIfQ4Fqo7UjHVzzNXqjGml/view?usp=sharing)

BMP 06/2019: [Overview](https://drive.google.com/file/d/1DIMFU2Ed_nGqNKoMw_DOBO4XbwvyznzS/view?usp=sharing) + [WACC](https://drive.google.com/file/d/1dUd0Z3n6QXI45znfRjVL3dWtstM9Tj_Z/view?usp=sharing) + [Valuation](https://drive.google.com/file/d/1fpb_TqEeMMDLbLQI7JfsOazu_q4GnsoQ/view?usp=sharing)

### How to Analyze

It took around 2 weeks to analyze a stock. First, I look at the industry from a bird-eye view. I find companies who had relatively cheap P/E, good overall financial health. For example, BMP, a leading firm in plastic pipe manufacturing, has P/E of 10 comparing to 14 of the industry, and they have **NO DEBT**. Then I research on what  their business model (how they make money), their financial statements, their competitors, the industry are. I also research intensively on the industry for their inputs and outputs. For example, inputs for BMP would be plastic pellets, which are highly dependent on oil. Therefore, the change in oil prices affect significantly the bottom line of BMP. 

After getting all the information and having a firm grasp of the firm, the industry and the trends, I start building a pro-forma financial statments. I usually start with Sales, by predicting upcoming sales of a company for 5 to 10 years. In the BMP example, I used average of the last five YoY growth, and the predicted YoY growth of Real Estate Industry, from the industry report of another analyst. Since BMP products are used in residential and civil infrastructures, it is intuitive to use Real Estate as an anchor for BMP Sales. 

Next, I use Sales to predict the rest of the Income Statement items. I can make assumptions like the COGS are going to be equal to 40% of Sales, because that's the average of COGS/Sales in the last 5 years. Average of the last 5 years and most recent number are most common assumptions. The rest of the items in Balance Sheet and Income Statements are forecasted in the same manner. 

<figure align="center">
	<img align="center" src="/assets/balance-sheet.JPG" >
	<figcaption> 
  		Pro-Forma Balance Sheet
	</figcaption>
</figure>

After getting all the pro forma financial Statements, we will find WACC of the firm. This is the Weighted Average Cost of Capital, or the average cost to get money for the firm. With WACC found, I try to calculate the Equity Value, by choosing one or multiple methods, like DCF, Dividends Growth Models and Comparables/Multiples. DCF is the most common method. It works by having the analyst find the forecasted Free Cash Flow of the firm. Let's refresh our memory. 

<div class="message">
  Free Cash Flow = EBIT(1-Tax Rate) + Depreciation - Capital Expenditures - Net changes in Working Capital 
</div>

<figure align="center">
	<img align="center" src="/assets/dcf.JPG" >
	<figcaption> 
  		Discounted Cash Flow
	</figcaption>
</figure>

Then we discounted all the free cash flow back to today, sum them up with a Terminal Value, to arrive at the Enterprise Value. Terminal Value is the number representing the firm's present value from the time point where the analyst finding the Terminal Value until forever. It uses growth rate and WACC as inputs. With the Enterprise Value available, we subtracts debt and cash from it to arrive at Equity Value. This is the intrinsic value of the firm. And by dividing it by the number of shares, we arrive at average price per share, or the price we believe the stock should be at. This is the DCF (Discounted Cash Flow) approach. The other two common approach are Dividends Growth Model, and Multiples. DGM use dividends and WACC as the inputs, and multiples use other similar firms as inputs. These two approaches are much simpler than DCF. I usually triangulate the results of different methods out, to find a range of stocks that makes sense. Then I build a slide deck to communicate this information to portfolio managers, so that they can decide to buy this stock or not. 

<figure align="center">
	<img align="center" src="/assets/sensitivity.JPG" >
	<figcaption> 
  		Sensitivity Analysis - Prices versus WACC, Price versus Growth
	</figcaption>
</figure>

There are other analysis you can do at this point. This is an example of sensitivity analysis, where we find the stock price at different levels of growth rate and WACC rate. This is important because growth rate and WACC affects the stock price significantly. By doing this type of analysis, we can see the range of prices that the stock can fall into. Additionally, in this example, we can see that for every one percent change in long term growth rate, the price of stocks goes up by 10 dollars, approximately. 

The process I just describe are quite common and used widely by funds to pick stocks for their portfolio. I hope you had a good read. 