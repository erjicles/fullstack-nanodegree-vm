# Project: Logs Analysis
Author: Erik Johnson
Date: August 8, 2018
Course: Udacity Full Stack Web Developer Nanodegree

## Objective
The objective of this project is to create a Python program that runs SQL
statements against a PostgreSQL database containing news articles to answer
several questions about the data.

## Running the Program
The Python program is written in Python 3.7.0. 

It assumes you have set up your environment as described by the course [here](https://classroom.udacity.com/nanodegrees/nd004/parts/51200cee-6bb3-4b55-b469-7d4dd9ad7765/modules/c57b57d4-29a8-4c5f-9bb8-5d53df3e48f4/lessons/bc938915-0f7e-4550-a48f-82241ab649e3/concepts/a9cf98c8-0325-4c68-b972-58d5957f1a91)
and that you are utilizing the *news* PostgreSQL database, also described at
that link.

To run the program, drop the *news.py* file in your *vagrant* directory, and use
the following command from the command line:

```
python news.py
```
or
```
python3 news.py
```

The program will output the answers to the three project questions, as described
below.

## Questions
1. What are the most popular three articles of all time? 
Which articles have been accessed the most? 
Present this information as a sorted list with the most popular article at the 
top.

Example:

"Princess Shellfish Marries Prince Handsome" — 1201 views
"Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
"Political Scandal Ends In Political Scandal" — 553 views

2. Who are the most popular article authors of all time? 
That is, when you sum up all of the articles each author has written, which 
authors get the most page views? Present this as a sorted list with the most 
popular author at the top.

Example:

Ursula La Multa — 2304 views
Rudolf von Treppenwitz — 1985 views
Markoff Chaney — 1723 views
Anonymous Contributor — 1023 views

3. On which days did more than 1% of requests lead to errors? The log table includes a column status that indicates the HTTP status code that the news site sent to the user's browser. (Refer to this lesson for more information about the idea of HTTP status codes.)

Example:

July 29, 2016 — 2.5% errors