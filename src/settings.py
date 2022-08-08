class JWT_Settings:
    SECRET_KEY = 'palyanyza'
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 30


class Settings:
    database_username = 'postgres'
    database_password = 'postgres'
    database_host = '127.0.0.1'
    database_port = 5432

    database_name = 'test_fastapi'


settings = Settings()
