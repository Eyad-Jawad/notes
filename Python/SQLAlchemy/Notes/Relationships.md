The most basic form of a relationship in `SQLAlchemy` is a `ForeignKey`, where it is used as a reference for `join` queries and the sort, but you can go a step further and put the whole other object in it:

```Python

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Table(Base):
    __tablename__ = "table"

    table2_id: Mapped[int] = mapped_column(ForeignKey("table2.id"))

    table2: Mapped[Table2] = relationship(
        back_populates="table2",
    )

```

and in Table2:

```Python

from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship

class Table2(Base):
    __tablename__ = "table2"

    table_id: Mapped[int] = mapped_column(ForeignKey("table.id"))

    table: Mapped[Table] = relationship(
        back_populates="table",
    )

```

If you have a type checker on it'll show an error at `Mapped[]`, this [[mypy#Some Errors]] should solve it.
If the relationship above has an owner, you can do something like:

```
table2: Mapped[Table2] = relationship(
    back_populates="table2",
    cascade="all, delete",
)

```

Which will wipe out all of the other objects where this object is referenced, be careful where you write this, because it will delete everything.

In this kind of situation, sometimes calling `select` alone won't let you be able to access the other objects, due to optimizations and the sort, so you should call it like this:

```Python

from sqlalchemy import select
from sqlalchemy.orm import selectinload

stmt = (
    select(Table)
    .options(selectinload(Table.table2))
)

```