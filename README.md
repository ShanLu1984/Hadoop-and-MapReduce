# Udacity-Course-Projects-Intro-to-Hadoop-and-MapReduce
## Introduction
Class website: https://classroom.udacity.com/courses/ud617. Cited from the homepage: 
The The Apache™ Hadoop® project develops open-source software for reliable, scalable, distributed computing. Learn the fundamental principles behind it, and how you can use its power to make sense of your Big Data.

## What's inside:
### Lesson 6 Projects:
 #### Part One: 
  * Data: purchases.txt, Purchase records of different stores.
  * Code: mapper.py, reducer.py
  * Experiment resesults:
  
  |       Quiz        |    Reults       |
  |-------------------|-----------------|
  |Sales per Category |  Toys: 57463477.11, Consumer Electronics: 57452374.13 |
  | Highest Sale |Reno: 499.99, Toledo: 499.98, Chandler: 499.98|
  | Total Sales | Number of Sales: 4138476, Total Vale of Sales: 1034457953.26|
  
 #### Part Two: 
  * Data: access_log, Web server log file from a public relation company whose clients were DVD distributors.
  * Code: mapper.py, reducer.py
  * Experiment results:
  
  |       Quiz        |    Reults       |
  |-------------------|-----------------|
  | Hits to Page | /assets/js/the-associates.js: 2456  |
  | Hits from IP | 10.99.99.186: 6 |
  | Most Popular | File path: /assets/css/combined.css, Number of occurrences: 117352|

## Installation
* You can read instructions on how to download and run the virtual machines here https://docs.google.com/document/d/1v0zGBZ6EHap-Smsr3x3sGGpDW-54m82kDpPKC2M6uiY/pub.

* Information on how to transfer files back and forth to the virtual machine can be found here https://docs.google.com/document/d/1MZ_rNxJhR4HCU1qJ2-w7xlk2MTHVqa9lnl_uj-zRkzk/pub.

* For step-by-step instructions for how to load data into HDFS, please re-watch HDFS Demo https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3095085570923. For a reminder of how to run a mapreduce job, please re-watch Simplifying Things https://classroom.udacity.com/courses/ud617/lessons/308873795/concepts/3093825960923.

## Example Use
1. Download and run the virtual machine (includes datasets). The datasets are also available from:
* http://content.udacity-data.com/courses/ud617/access_log.gz
* http://content.udacity-data.com/courses/ud617/purchases.txt.gz
2. Upload dataset "access_log" into hadoop HDFS 
```
hadoop fs -put access_log myinput
```
3. Make corresponding changes to mapper.py and reducer.py according to the Quiz questions
4. To test your python code, make a small testfile
```
head 100 ../data/access_log > testfile
```
and using pipline to test
```
cat testfile | ./mapper.py | sort | ./reducer2.py
```
5. Run a mapreduce job, 
```
hs mapper.py reducer.py myinput myoutput
```
6. Read results directly from the output file
```
hadoop fs -cat myoutput/part-00000
```
7. If the file is too big to read, save outputfile
```
hadoop fs -get myoutput/part-00000 mylocalfile.txt
```
and search for the answer to the Quiz questions using "grep" commend
```
grep "/assets/js/the-associates.js" mylocalfile.txt
```
