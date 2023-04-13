from databases import Database
from user_storage.models.user import User, UserResponse


class UserDB:
    def __init__(self, dsn: str) -> None:
        self._conn = Database(dsn)

    async def startup(self) -> None:
        await self._conn.connect()

    async def shutdown(self) -> None:
        await self._conn.disconnect()

    async def insert_user(self, user: User) -> int:
        query: str = """
            INSERT INTO "user" (user_name, first_name, last_name, email, phone)
            VALUES (:user_name, :first_name, :last_name, :email, :phone)
            RETURNING id
        """
        values: dict = dict(
            user_name=user.user_name,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
        )

        return await self._conn.fetch_val(query=query, values=values)

    async def read_user(self, user_id: int) -> UserResponse:
        query: str = """SELECT * FROM "user" WHERE id = :user_id"""
        values: dict = dict(user_id=user_id)
        record = await self._conn.fetch_one(query, values)
        if record:
            return UserResponse(
                user_id=record["id"],
                user_name=record["user_name"],
                first_name=record["first_name"],
                last_name=record["last_name"],
                email=record["email"],
                phone=record["phone"],
            )
        else:
            # ToDo Raise Error
            ...

    async def del_user(self, user_id: int) -> None:
        query: str = """DELETE FROM "user" WHERE id = :user_id"""
        values: dict = dict(user_id=user_id)
        await self._conn.execute(query, values)

    async def update_user(self, user_id: int, user: User) -> int:
        query: str = """
            UPDATE "user"
            SET user_name = :user_name, 
            first_name = :first_name,
            last_name = :last_name,
            email = :email,
            phone = :phone
             WHERE id = :user_id
        """
        values: dict = dict(
            user_id=user_id,
            user_name=user.user_name,
            first_name=user.first_name,
            last_name=user.last_name,
            email=user.email,
            phone=user.phone,
        )

        return await self._conn.execute(query=query, values=values)