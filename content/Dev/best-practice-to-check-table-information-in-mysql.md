Title: Best Practice to Check Table Information in MySQL
Date: 2017-01-09 10:00
Modified: 2018-04-03 22:00
Tags: MySQL, MariaDB
Summary: There's a better way to check the table schema in MySQL.

I usually use `DESC` to check the columns of the table,
which is similar to `EXPLAIN`.
But it's not enough espeicially when I want to check indexes with columns.

Recently, I got introduced of `SHOW CREATE TABLE`.
It seems strange, but it shows the SQL for creating the table.
The result includes lot's of unnecessary lines, and you can clean them with `\G` in the end.
So, if you want to check columns and indexes of the table, you can use the following.

```sql
SHOW CREATE TABLE table\G
```
