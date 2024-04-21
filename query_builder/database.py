from dataclasses import dataclass, asdict


@dataclass(frozen=True)
class DBConnectionParams:
    user: str
    password: str
    host: str
    port: int
    database: str  # name

    @property
    def connection_uri(self):
        return f"mysql+mysqlconnector://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"

    def asdict(self):
        return asdict(self)


class InvalidDBCredentials(Exception):
    pass
