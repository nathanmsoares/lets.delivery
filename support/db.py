import databases
import sqlalchemy
# SQLAlchemy specific code, as with any other app
# DATABASE_URL = "sqlite:///./test.db"
DATABASE_URL = "postgresql://user:password@postgresserver/db"

database = databases.Database(DATABASE_URL)

metadata = sqlalchemy.MetaData()

notes = sqlalchemy.Table(
    "notes",
    metadata,
    sqlalchemy.Column("id", sqlalchemy.Integer, primary_key=True),
    sqlalchemy.Column("Name", sqlalchemy.String),
    sqlalchemy.Column("Breed", sqlalchemy.String),
    sqlalchemy.Column("Location_Of_Origin", sqlalchemy.String),
    sqlalchemy.Column("Coat_Length", sqlalchemy.Float),
    sqlalchemy.Column("Body_Type", sqlalchemy.String),
    sqlalchemy.Column("Pattern", sqlalchemy.String),
)


engine = sqlalchemy.create_engine(
    DATABASE_URL, connect_args={"check_same_thread": False}
)
metadata.create_all(engine)
