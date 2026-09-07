SQL commands are not case-sensitive, but it's conventional to capitalize them for readability. You can also use new lines and white space as you like to format the command for readability. Most database systems require you to end a query with a semicolon (';')
A SQL query can contain:
- SQL keywords (like the ​SELECT​ and ​FROM​)
- Column names (like the ​name​ column)
- Table names (like the ​person​ table)
- Wildcard characters (such as ​`%`)
- Functions
- Specific filtering criteria
- etc.

```sql
SELECT * 
FROM dbTable
WHERE something = 'idk what'
LIMIT 5;
```


```sql
SELECT DISTINCT columnName -- this will literally return distinct elements
FROM dbTable;
```

we have `AND` and `OR` in SQL

When you place a `%` wildcard in a query string, the SQL system will return results that match the rest of the string exactly, and have anything (or nothing) where the wildcard is. For example, `'Ca%a'` matches `Canada` and `California`.
The other, less commonly used wildcard, is `_`. This one means 'match the rest of the text, as long as there's exactly one character in exactly the position of the `_`, no matter what it is. So, `'B_b'` would match `'Bob'` and `'Bub'` but not `'Babe'` or `'Bb'`.

SQL also supports numeric comparisons like `<` (less than) and `>` (greater than). You can also use the keywords `BETWEEN` and `AND` -- and all of those work with words as well as numbers.

the data stored in the data base is case sensitive, so we have the functions UPPER() and LOWER():
```sql
SELECT *
FROM dbTable
WHERE LOWER(column) = 'idk what';
```

Here are a few useful aggregate functions SQL provides:
MAX: finds the maximum value
MIN: finds the minimum value
SUM: calculates the sum of the specified column values
AVG: calculates the average of the specified column values
COUNT​: counts the number of specified column values

we also have ORDER BY something ASC -- or DESC
you could do:
```SQL
SELECT * 
FROM table1
JOIN table2
  ON  something = something
LIMIT 10;
```
you could also do :
```SQL
SELECT Name as n, age as a
FROM table1;
```


Sometimes, you'd interacte with a database using a layer of abstraction in what's called an ORM, most common example is [[SQLAlchemy Table|SQLAlchemy]]
