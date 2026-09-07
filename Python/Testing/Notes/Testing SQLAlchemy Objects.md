For some reason, in `SQLAlchemy` when you pass an orm object, you can't use the object you've passed to to assersion tests, you have to request a new object and check with that.


```Python

# An actual test from the todo app:

@pytest.mark.asyncio
@patch("todo_app.db.queries.uuid4")
async def test_set_token_empty(mock_uuid, mock_session):
    mock_uuid.return_value = "token"

    user = User(
        username="Noice",
        hash="Anything",
    )
    mock_session.add(user)
    await mock_session.commit()

    assert await set_token(mock_session, user) == "token"

    stmt = select(User)
    result = await mock_session.execute(stmt)
    user = result.scalar_one()

    assert user.username == "Noice"
    assert user.hash == "Anything"
    assert user.access_token == "token"

```