#Python django:-
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| article_id    | int     |
| author_id     | int     |
| viewer_id     | int     |
| view_date     | date    |
+---------------+---------+
There is no primary key (column with unique values) for this table, the table may have duplicate rows.
Each row of this table indicates that some viewer viewed an article (written by some author) on some date. 
Note that equal author_id and viewer_id indicate the same person.

Write a solution to find all the authors that viewed at least one of their own articles.
Return the result table sorted by id in ascending order.
The result format is in the following example.
Example 1:
Input: 
Views table:
+------------+-----------+-----------+------------+
| article_id | author_id | viewer_id | view_date  |
+------------+-----------+-----------+------------+
| 1          | 3         | 5         | 2019-08-01 |
| 1          | 3         | 6         | 2019-08-02 |
| 2          | 7         | 7         | 2019-08-01 |
| 2          | 7         | 6         | 2019-08-02 |
| 4          | 7         | 1         | 2019-07-22 |
| 3          | 4         | 4         | 2019-07-21 |
| 3          | 4         | 4         | 2019-07-21 |
+------------+-----------+-----------+------------+
Output: 
+------+
| id   |
+------+
| 4    |
| 7    |
+------+
# python django:-
from .models import Views
from django.db.models import F
data = Views.objects.filter(author_id=F('viewer_id')).values('author_id').distinct().order_by('author_id')

#Problema 2 
Table: Tweets

+----------------+---------+
| Column Name    | Type    |
+----------------+---------+
| tweet_id       | int     |
| content        | varchar |
+----------------+---------+
tweet_id is the primary key (column with unique values) for this table.
This table contains all the tweets in a social media app.
Write a solution to find the IDs of the invalid tweets. The tweet is invalid if the number of characters used in the content of the tweet is strictly greater than 15.

Return the result table in any order.

The result format is in the following example.
Example 1:

Input: 
Tweets table:
+----------+----------------------------------+
| tweet_id | content                          |
+----------+----------------------------------+
| 1        | Vote for Biden                   |
| 2        | Let us make America great again! |
+----------+----------------------------------+
Output: 
+----------+
| tweet_id |
+----------+
| 2        |
+----------+
Explanation: 
Tweet 1 has length = 14. It is a valid tweet.
Tweet 2 has length = 32. It is an invalid tweet.

 from .models import Tweets
 from django.db.models import F, Func, IntegerField

 class Length(Func):
     function = 'LENGTH'
     output_field = IntegerField()
 data = Tweets.objects.annotate(content_length=Length(F('content'))).filter(content_length__gt=15).values('tweet_id')




# Python Django:
Table: Employees
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| name          | varchar |
+---------------+---------+
id is the primary key (column with unique values) for this table.
Each row of this table contains the id and the name of an employee in a company.
Table: EmployeeUNI
+---------------+---------+
| Column Name   | Type    |
+---------------+---------+
| id            | int     |
| unique_id     | int     |
+---------------+---------+
(id, unique_id) is the primary key (combination of columns with unique values) for this table.
Each row of this table contains the id and the corresponding unique id of an employee in the company.

Write a solution to show the unique ID of each user, If a user does not have a unique ID replace just show null.
Return the result table in any order.
The result format is in the following example.
# models.py:-
 class EmployeeUNI(models.Model):
     id = models.IntegerField(primary_key=True)
     unique_id = models.IntegerField()
 class Employees(models.Model):
     id = models.IntegerField(primary_key=True)
     name = models.CharField(max_length=50)    
 #views.py:
 from django.shortcuts import render
 from .models import Employees, EmployeeUNI
 from django.db.models import OuterRef, Subquery
 # Create your views here.
 def index(request):
     subquery = EmployeeUNI.objects.filter(id=OuterRef('id')).values('unique_id')[:1]

     result = Employees.objects.annotate(unique_id=Subquery(subquery)).values('id', 'unique_id', 'name')
     print(result)
     return render(request, 'home.html', {'data':result})






