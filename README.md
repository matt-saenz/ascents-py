# ascents-py :climbing_man:

## Overview

Command line app for logging rock climbing ascents. Ascents are logged in a SQLite database table with the following fields:

1. `route`: Name of the route.
2. `grade`: Grade of the route in terms of the Yosemite Decimal System (YDS).
3. `crag`: Name of the crag, or general climbing area, where the route is located.
4. `date`: Date of first recorded ascent.

An ascent is defined as a redpoint ascent (i.e., successfully leading the route with no falls or takes).

## Example Usage

```
$ ascents -h
usage: ascents [-h] {init,log,drop,analyze} database
```

Initialize ascent database:

```
$ ascents init ascent.db
Initializing ascent database: ascent.db
Successfully initialized database
```

Log an ascent:

```
$ ascents log ascent.db
Enter the name of the route: Slither
Enter the grade of the route: 5.7
Enter the name of the crag where the route is located: Reimers Ranch
Enter the date of the ascent in YYYY-MM-DD format (or 't' for today or 'y' for yesterday): 2022-06-27
Ascent to be logged: Slither 5.7 at Reimers Ranch on 2022-06-27
Log the above ascent in ascent.db (y/n)? y
Successfully logged the above ascent
```

Confirm its existence:

```
$ sqlite3 --markdown ascent.db 'select * from ascents'
```

|  route  | grade |     crag      |    date    |
|---------|-------|---------------|------------|
| Slither | 5.7   | Reimers Ranch | 2022-06-27 |

Analyze the database:

```
$ ascents analyze ascent.db
Analysis of ascents in ascent.db
Generated on Fri May 24 2024 09:37:25 AM

Total number of ascents: 1

Count of ascents by year:
   1  2022

Count of ascents by crag:
   1  Reimers Ranch

Count of ascents by grade:
   1  5.7
```
