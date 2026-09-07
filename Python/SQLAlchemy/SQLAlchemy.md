## I think you should study SQL itself on w3schools, there are a lot of blind spots in your knowledge


SQLAlchemy is a library for manipulating dabases through a layer of abstraction with what's called : "Object Relational Mapping"

to connect to a SQLite database do:

```python

from sqlalchemy import create_engine

SQLALCHEMY_DATABASE_URL = "sqlite:///database_name.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL)
# and you can pass echo=True to the function if you want to
# get feedback on the operations that take place

```

you can also do:

```python

from sqlalchemy.orm import Session

session = Session(engine)

```

and treat session like a db

another way of doing it is:

```python

from sqlalchemy import create_engine, MetaData, Table, Column, Integer, Text, ...

engine = ...

meta = MetaData()

table = Table(
	"TableName",
	meta,
	Column("ColName", Integer, primary_key=True),
	.
	.
	.
)

meta.create_all(engine)

```

then you could manipulate it doing this:

```python

conn = engine.connect()

inserted_data = table.insert().values(ColName=3)

"""

you could also do this:

from sqlalchemy import insert

inserted_data = insert(table).values(ColName=3)

and you could do this with any other SQL method

"""

result = conn.execute(inserted_data)

conn.commit()

```

I'm not sure if the look of it is goofy because that's how it is, I'm uesd to other ways, or becuse of the guy doing the tutorial: [This Guy](https://www.youtube.com/watch?v=529LYDgRTgQ)

if you want to connect two columns between tables you'd use ForeignKey:

```python
from sqlalchemy import ..., ForeignKey

.
.
.

table2 = Table(
	"table2",
	meta,
	.
	.
	.
	Column("Something", Integer, ForeignKey("table1.id"))
)

```

if you want to insert many things at once do this:

```python

inserted_data = table.insert().values([
	{"val1": 1},
	{"val2": 2},
	.
	.
	.
])

conn.execute(inserted_data)
conn.commit()

```

an error will occurr if you have two connected tables and the table that refers to the other table is executed before the other one is committed

look at this join query:

```python

join_query = table1.join(table2, table1.c.id == table2.c.id)
select_query = table1.select().with_only_columns(table1.c.name, table2.c.name).select_from(join_query)

result = conn.execute(select_query)

for row in result.fetchall():
	print(row)
	
```

or you could use `outerjoin()` instead of `join()`, you can select things that are present in table1 only, as well as things that are present in both, since the normal `join()` selects those that are present in both tables only

you can also use functions:

```python

from sqlalchemy import func

...func.sum()
...func.count()
...func.max()
.
.
.

```


another way of doing things is:

```python

from sqlalchemy imoprt create_engine, Column, Integer, ...
from sqlalchemy.orm import declarative_base, sessoinmaker, relationship

engine = create_engine("sqlite:///database_name.db")

Base = declarative_base()

class Table(Base):
	__tablename__ = "table_name"
	
	id = Column(Integer, primary_key=True)
	.
	.
	.
	table2 = relationship("Table2", back_populates="table2_name")
	
class Table2(Base):
	.
	.
	.
	table = relationship("Table", back_populates="table_name")

Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

something = Table(id=10)

session.add(something)
session.commit()

```

the relationship variable is to access things in the other table from it

if you don't want to `commit()` but you want the other table to do something to the first table you can do `session.flush()` instead

you can do queries in a different way:

```python

result = session.query(Table.id).filter(Table.id > 1).all()
print(result)

result = session.query(Table).filter(Table.id == 1).delete()

result = session.query(Table).filter(Table.id == 5).update({"id" : 2})

result = session.query(Table.id, Table2.id).join(Table2).all()

# You can also use group_by() or having() and func

session.close()

```

you can also use panda's dataframes with sqlalchemy:

```python

df = pd.read_sql("SELECT * FROM table", con=engine)
df.to_sql("table", con=engine, if_exists="append", index=False)

```


another way of doing stuff:

```python

class Table(Base):
	__tablename__ = "table"
	
	id: Mapped[int] = mapped_column(primary_key=True)
	title: Mapped[str] = mapped_column

from sqlalchemy import select

stmt = select(Table).where(Table.id == 1)

result = session.execute(stmt)

query = result.one() # Returns a Row object
query = result.scalar() # Returns an object
.
.
.

```







