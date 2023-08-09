"""Script for initializing ascent database."""


import argparse
import sqlite3
import sys
from pathlib import Path


parser = argparse.ArgumentParser()
parser.add_argument("database", type=Path)
args = parser.parse_args()


if args.database.exists():
    sys.exit(f"Error: {args.database} already exists")


# Generate data for grade info table

grades = []

for number in range(16):
    if number < 10:
        grades.append((f"5.{number}", number, None))
    else:
        for letter in "abcd":
            grades.append((f"5.{number}{letter}", number, letter))


# Create tables

connection = sqlite3.connect(args.database)

try:
    cursor = connection.cursor()

    cursor.executescript(
        """
        CREATE TABLE ascents(
            route TEXT NOT NULL,
            grade TEXT NOT NULL,
            crag TEXT NOT NULL,
            date TEXT NOT NULL,
            PRIMARY KEY(route, grade, crag)
        );

        CREATE TABLE grade_info(
            grade TEXT PRIMARY KEY,
            grade_number INTEGER NOT NULL,
            grade_letter TEXT
        );
        """
    )

    cursor.executemany(
        """
        INSERT INTO grade_info
        VALUES(?, ?, ?)
        """,
        grades,
    )

    connection.commit()
finally:
    connection.close()