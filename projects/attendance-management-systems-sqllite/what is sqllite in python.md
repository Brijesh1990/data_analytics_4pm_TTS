# SQLite in Python

## What is SQLite?

SQLite is a small, serverless relational database engine. It stores a database in a file (or in memory) and reads and writes it directly from the application. Unlike PostgreSQL or MySQL, it does not require a separate database server process, account, or network connection.

Python includes the `sqlite3` module in its standard library, so most Python installations can use SQLite without installing anything:

```python
import sqlite3
```

The database file contains tables, indexes, and the data itself. SQLite is useful for local applications, prototypes, tests, scripts, small websites, and embedded devices. It supports SQL, transactions, indexes, constraints, and joins.

## When to use it

SQLite is a good fit when:

- Your application needs a local, easy-to-deploy database.
- A single application (or a small number of processes) mostly reads and writes the data.
- You want a database for development, testing, or a command-line tool.

Consider a server database such as PostgreSQL when you need many concurrent writers, centralized multi-user access over a network, fine-grained database user permissions, or advanced server operations. SQLite permits concurrent readers but serializes writes: only one writer can write to a database at a time.

## Connecting to a database

`sqlite3.connect()` opens a database, creating the file if it does not already exist. Use a path to persist data:

```python
import sqlite3

connection = sqlite3.connect("attendance.db")
try:
    # Use the connection here.
    ...
finally:
    connection.close()
```

Special connection options:

```python
sqlite3.connect(":memory:")  # A temporary database held in memory.
sqlite3.connect("file:temporary?mode=memory&cache=shared", uri=True)
```

An in-memory database usually belongs to one connection and disappears when that connection closes. A shared-memory URI has different lifetime and sharing behavior; use it only when multiple connections in the same process need to share that database.

Always close connections when finished. A connection used as a context manager handles transaction commit or rollback, but **does not close the connection**:

```python
with sqlite3.connect("attendance.db") as connection:
    # Successful exit commits; an exception rolls back.
    ...
# Close explicitly when it is no longer needed.
connection.close()
```

## Creating a table

Use `CREATE TABLE` to define a table. SQLite uses flexible type affinity rather than rigid column types, but choosing meaningful types and constraints is still important.

```python
import sqlite3

connection = sqlite3.connect("attendance.db")
connection.execute("""
    CREATE TABLE IF NOT EXISTS attendance (
        id INTEGER PRIMARY KEY,
        student_name TEXT NOT NULL,
        attendance_date TEXT NOT NULL,
        present INTEGER NOT NULL CHECK (present IN (0, 1)),
        UNIQUE (student_name, attendance_date)
    )
""")
connection.commit()
connection.close()
```

Common SQLite storage classes are `NULL`, `INTEGER`, `REAL`, `TEXT`, and `BLOB`. Common declared types include `INTEGER`, `REAL`, `TEXT`, and `BLOB`. Dates and times are commonly stored as ISO 8601 text (for example, `2026-10-24`) or as Unix timestamps; SQLite has date/time functions but no dedicated date storage class.

`INTEGER PRIMARY KEY` is a special alias for the rowid in an ordinary SQLite table. Add constraints such as `NOT NULL`, `UNIQUE`, `CHECK`, and `FOREIGN KEY` to have the database help protect data integrity.

## Adding, reading, changing, and deleting rows

Use a cursor or the connection's `execute()` method to run SQL. Use `?` placeholders and pass values separately. **Never build SQL by inserting user input into the SQL string.**

```python
with sqlite3.connect("attendance.db") as connection:
    connection.execute(
        """
        INSERT INTO attendance (student_name, attendance_date, present)
        VALUES (?, ?, ?)
        """,
        ("Asha", "2026-10-24", 1),
    )

    rows = connection.execute(
        """
        SELECT id, student_name, attendance_date, present
        FROM attendance
        WHERE attendance_date = ?
        ORDER BY student_name
        """,
        ("2026-10-24",),
    ).fetchall()

    for row in rows:
        print(row)
```

For a single result, use `fetchone()`; for all remaining results, use `fetchall()` or iterate over the cursor. For large result sets, iterate rather than loading every row into memory:

```python
cursor = connection.execute(
    "SELECT student_name FROM attendance WHERE present = ?",
    (1,),
)
for (name,) in cursor:
    print(name)
```

Update or delete rows with parameterized statements:

```python
connection.execute(
    "UPDATE attendance SET present = ? WHERE id = ?",
    (0, 12),
)
connection.execute(
    "DELETE FROM attendance WHERE id = ?",
    (12,),
)
```

Each parameter value must be supplied separately. A one-item parameter tuple needs a trailing comma: `(value,)`. Parameters are for values, not SQL identifiers such as table or column names; identifiers should be selected from trusted, fixed choices and quoted appropriately.

For many rows, `executemany()` avoids repeatedly writing the same statement:

```python
records = [
    ("Asha", "2026-10-24", 1),
    ("Ravi", "2026-10-24", 0),
]
connection.executemany(
    """
    INSERT INTO attendance (student_name, attendance_date, present)
    VALUES (?, ?, ?)
    """,
    records,
)
```

## Returning named columns

By default, query rows are tuples. Set `row_factory` to `sqlite3.Row` to access values by column name:

```python
connection = sqlite3.connect("attendance.db")
connection.row_factory = sqlite3.Row

row = connection.execute(
    "SELECT student_name, present FROM attendance WHERE id = ?",
    (1,),
).fetchone()

if row is not None:
    print(row["student_name"], row["present"])

connection.close()
```

## Transactions and error handling

A transaction makes a group of changes atomic: they all commit together, or they can be rolled back together. The connection context manager commits on normal exit and rolls back if an exception escapes the block:

```python
try:
    with sqlite3.connect("attendance.db") as connection:
        connection.execute(
            "UPDATE attendance SET present = ? WHERE id = ?",
            (1, 1),
        )
        connection.execute(
            "INSERT INTO attendance (student_name, attendance_date, present) "
            "VALUES (?, ?, ?)",
            ("Mina", "2026-10-24", 1),
        )
except sqlite3.Error as error:
    print(f"Database operation failed: {error}")
```

Catch database errors where the application can meaningfully report or handle them. Do not suppress errors that indicate a failed write. `sqlite3.IntegrityError` is a more specific exception for constraint violations.

## Foreign keys

Foreign-key constraints are not enforced unless enabled for the connection. Turn them on when connecting, before beginning a transaction:

```python
connection = sqlite3.connect("attendance.db")
connection.execute("PRAGMA foreign_keys = ON")
```

For example:

```sql
CREATE TABLE students (
    id INTEGER PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE attendance (
    id INTEGER PRIMARY KEY,
    student_id INTEGER NOT NULL REFERENCES students(id),
    attendance_date TEXT NOT NULL,
    present INTEGER NOT NULL CHECK (present IN (0, 1))
);
```

SQLite checks a foreign key only when foreign-key enforcement is enabled on that connection.

## Useful practices

- Keep the database file in a deliberate location; a relative path is resolved from the process's current working directory.
- Use `?` placeholders for all external values to prevent SQL injection and quoting bugs.
- Use constraints and transactions to protect data consistency.
- Use indexes for columns frequently used in filtering, joining, or sorting, and verify their value with realistic queries.
- Keep write transactions short. SQLite allows many readers, but writes contend with each other.
- For a read-heavy workload with concurrent readers, write-ahead logging can help:

  ```python
  connection.execute("PRAGMA journal_mode = WAL")
  ```

  WAL creates associated `-wal` and `-shm` files while in use. Keep the database and its WAL files together and use SQLite's backup support rather than copying a live database file blindly.
- If using a connection from multiple threads, understand the `check_same_thread` default. By default, a connection may only be used in the thread that created it. Disabling the check does not make concurrent use automatically safe; coordinate access or use separate connections.
- Back up important databases. Python's `sqlite3` connection provides a `backup()` method:

  ```python
  source = sqlite3.connect("attendance.db")
  backup = sqlite3.connect("attendance-backup.db")
  source.backup(backup)
  backup.close()
  source.close()
  ```

## Common mistakes

1. **Using the wrong module name:** import `sqlite3`, not `sqlite`.
2. **Forgetting to commit:** writes outside a committing transaction may not be saved as expected. Use the connection context manager or explicitly call `commit()`.
3. **Assuming `with connection` closes it:** it manages the transaction, not the connection lifetime. Call `close()` when done.
4. **Concatenating input into SQL:** use placeholders for values.
5. **Forgetting foreign-key enforcement:** enable `PRAGMA foreign_keys = ON` for each connection.
6. **Expecting many simultaneous writers:** SQLite serializes writes; use a server database if write concurrency is a central requirement.
7. **Assuming a database path is relative to the Python file:** relative paths are based on the current working directory.

