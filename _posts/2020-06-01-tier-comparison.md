---
title: Tier Comparison Macro
date: 2020-08-01
layout: post
tags: excel-vba
summary: I wrote this Excel VBA Macro during one of my internships. This script allows user to compare two drug formulary tier to see whether the brand my company owns underperform or overperform competitor's brand, in terms of drug formulary. You can download the macro and the calendar file below.
image: /assets/tier-comparison.JPG
---
<p align="center">
	<iframe width="560" height="315" src="https://www.youtube.com/embed/ZHWA5N7iJtc?rel=0?version=3&autoplay=1&controls=0&&showinfo=0&loop=1" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>
</p>

### Overview
I wrote this Excel VBA Macro during one of my internships. This script allows user to compare two drug formulary tier to see whether the brand my company owns underperform or overperform competitor's brand, in terms of drug formulary. 

You can download the macro and the calendar file [here](https://drive.google.com/file/d/1gYL3Oc3gx_kOCbYjGzYOX9zyiUgWe4f5/view?usp=sharing)

### Full Macro
<pre>
Sub compare_tier()
'***********************************************
'Purpose: compare two product tier and returns whether Sunovion product is at advantage, parity or disadvantage compare to competitors'
'The Tier Rank is below
'***********************************************
    Dim tierlist As Variant
    tierlist = Array("T1", "T1R", "T2", "T2R", "T3", "T3R", "T4", "T4R", "T5", "T5R", "On", "Of", "NC")
    
    lastrow = ActiveSheet.Cells(Rows.Count, 1).End(xlUp).Row
    For i = 1 To lastrow - 1
        a = ActiveCell.Offset(0, -3).Value
        b = ActiveCell.Offset(0, -2).Value
        
        If InStr(a, "R") <> 0 Then
            a = Left(a, 2) & "R"
            Debug.Print a
        ElseIf Left(a, 2) = "NA" Then
            ActiveCell.Value = "NA"
            GoTo a
        Else
            a = Left(a, 2)
        End If
        
        If InStr(b, "R") <> 0 Then
            b = Left(b, 2) & "R"
        ElseIf Left(b, 2) = "NA" Then
            ActiveCell.Value = "NA"
            GoTo a
        Else
            b = Left(b, 2)
        End If
         
        If Application.Match(a, tierlist, False) < Application.Match(b, tierlist, False) Then
            ActiveCell.Value = "Advantaged"
        ElseIf Application.Match(a, tierlist, False) = Application.Match(b, tierlist, False) Then
            ActiveCell.Value = "Parity"
        ElseIf Application.Match(a, tierlist, False) > Application.Match(b, tierlist, False) Then
            ActiveCell.Value = "Disadvantaged"
        End If
a:
        ActiveCell.Offset(1, 0).Select

    Next i
        
End Sub
</pre>

### Explanation

I created an array of the tier (tierlist), better to worse from left to right. While going through each row, my macro will find compare two brands by finding their position in the array, then compare them. Whichever brand got a lower number for position, has advantage over the other. The macro will the input either Advantaged, Disadvantaged, or Parity accordingly