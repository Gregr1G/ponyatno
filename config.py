import os

import dotenv

dotenv.load_dotenv()

user = os.getenv("DATABASE_USERNAME")
password = os.getenv("DATABASE_PASSWORD")
host = os.getenv("DATABASE_IP")
port = os.getenv("DATABASE_PORT")
database = os.getenv("DATABASE_NAME")

url = f"postgresql+asyncpg://{user}:{password}@{host}/{database}"

