#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
# Logs Analysis Project
# Udacity Full Stack Web Developer Nanodegree
# Author: Erik Johnson

import datetime
import psycopg2

# 1. What are the most popular three articles of all time?
#    Which articles have been accessed the most?
#    Present this information as a sorted list with the most popular article
#    at the top.
#    Example:
#    "Princess Shellfish Marries Prince Handsome" — 1201 views
#    "Baltimore Ravens Defeat Rhode Island Shoggoths" — 915 views
#    "Political Scandal Ends In Political Scandal" — 553 views
QUERY1 = """
select a.title, count(l.id) as views
from log l
inner join articles a
    on l.path = '/article/' || a.slug
where l.status like '200%'
group by a.title
order by views desc
limit 3;
"""


def do_question1():
    """Show the top 3 most popular three articles of all time"""
    # Connect to the database
    db = psycopg2.connect("dbname=news")

    # Execute the query and retrieve the results
    c = db.cursor()
    c.execute(QUERY1)
    rows = c.fetchall()

    # Close the db connection
    db.close()

    # Show the results
    print "=============================="
    print "Question 1:"
    print "Top 3 most popular articles of all time:"
    for row in rows:
        print '"{0}" - {1} views'.format(row[0], row[1])
    print ""


# 2. Who are the most popular article authors of all time?
#    That is, when you sum up all of the articles each author has written,
#    which authors get the most page views? Present this as a sorted list with
#    the most popular author at the top.
#    Example:
#    Ursula La Multa — 2304 views
#    Rudolf von Treppenwitz — 1985 views
#    Markoff Chaney — 1723 views
#    Anonymous Contributor — 1023 views
QUERY2 = """
select auth.name, count(l.id) as views
from log l
inner join articles art
    on l.path = '/article/' || art.slug
inner join authors auth
    on art.author = auth.id
where l.status like '200%'
group by auth.name
order by views desc;
"""


def do_question2():
    """Show the most popular article authors of all time"""
    # Connect to the database
    db = psycopg2.connect("dbname=news")

    # Execute the query and retrieve the results
    c = db.cursor()
    c.execute(QUERY2)
    rows = c.fetchall()

    # Close the db connection
    db.close()

    # Show the results
    print "=============================="
    print "Question 2:"
    print "Most popular article authors of all time:"
    for row in rows:
        print '{0} - {1} views'.format(row[0], row[1])
    print ""


# 3. On which days did more than 1% of requests lead to errors?
#    The log table includes a column status that indicates the HTTP status code
#    that the news site sent to the user's browser. (Refer to this lesson for
#    more information about the idea of HTTP status codes.)
#    Example:
#    July 29, 2016 — 2.5% errors
QUERY3 = """
select requests.dt, (errors.N::float / requests.N::float) as error_percent
from
(
    select l.time::date as dt, count(l.id) as N
    from log l
    group by l.time::date
) as requests
inner join (
    select l.time::date as dt, count(l.id) as N
    from log l
    where l.status like '4%'
    group by l.time::date
) as errors
    on requests.dt = errors.dt
where (errors.N::float / requests.N::float) > 0.01
order by error_percent desc;
"""


def do_question3():
    """Show which days more than 1% of requests led to errors"""
    # Connect to the database
    db = psycopg2.connect("dbname=news")

    # Execute the query and retrieve the results
    c = db.cursor()
    c.execute(QUERY3)
    rows = c.fetchall()

    # Close the db connection
    db.close()

    # Show the results
    print "=============================="
    print "Question 3:"
    print "Days with more than 1% of requests leading to errors:"
    for row in rows:
        print '{0:%B %d, %Y} - {1:.2%} errors'.format(row[0], row[1])
    print ""


if __name__ == '__main__':
    do_question1()
    do_question2()
    do_question3()
