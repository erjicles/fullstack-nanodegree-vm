# Project: Logs Analysis

Author: Erik Johnson  
Date: August 8, 2018  
Course: Udacity Full Stack Web Developer Nanodegree

## Objective

The objective of this project is to create a Python program that runs SQL
statements against a PostgreSQL database containing news articles to answer
several questions about the data.

## Preparing Your Environment

The Python program is written using Python 3.7.0. 

It assumes you have installed a virtual machine (VM) using VirtualBox and 
Vagrant, as described by the course 
<a href="https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/5475ecd6-cfdb-4418-85a2-f2583074c08d/concepts/14c72fe3-e3fe-4959-9c4b-467cf5b7c3a0" target="_blank">here</a>.

It also assumes that you have set up the project **news** PostgreSQL database, 
provided by the course
<a href="https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91" target="_blank">here</a>.
The program only relies on the original database objects;
there are no database customizations such as views.

Once your VM and database are set up,
drop the **news.py** file in your **vagrant** directory.

## Running The Program

SSH into your VM, cd to the vagrant directory
(or wherever you dropped **news.py**),
and run one of the following 
commands from the command line
(depending on how your python is set up):

```
python news.py
or
python3 news.py
```

The program will output the answers to the three project questions below. The
results are provided in the **results.txt** file.

## Questions

### 1. What are the most popular three articles of all time? 
Which articles have been accessed the most? 
Present this information as a sorted list with the most popular article at the 
top.

**Example:**

"Princess Shellfish Marries Prince Handsome" — 1201 views  
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views  
"Political Scandal Ends In Political Scandal" — 553 views

### 2. Who are the most popular article authors of all time? 
That is, when you sum up all of the articles each author has written, which 
authors get the most page views? Present this as a sorted list with the most 
popular author at the top.

**Example:**

Ursula La Multa — 2304 views  
Rudolf von Treppenwitz — 1985 views  
Markoff Chaney — 1723 views  
Anonymous Contributor — 1023 views

### 3. On which days did more than 1% of requests lead to errors?
The log table includes a column status that indicates the HTTP status code that
the news site sent to the user's browser. (Refer to this lesson for more 
information about the idea of HTTP status codes.)

**Example:**

July 29, 2016 — 2.5% errors