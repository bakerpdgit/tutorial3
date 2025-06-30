from abc import ABC, abstractmethod
from typing import Optional

# logger service interface
class LoggerService(______):
    """Logger Service"""

    @___________
    def _log(self, message: str) -> None:
        """Log the given message"""

# database service interface
class DatabaseService(______):
    """Database Service"""

    @____________
    def save(self, item: str) -> str:
        """persist to storage"""

    @abstractmethod
    def get(self, item_id: str) -> Optional[str]:
        """get item from storage"""
        pass

# inherits from database service
class MongoDatabaseService(__________):
    """Mongo Database Service"""

    def save(self, item: str) -> str:
        # some logic
        return item

    def get(self, item_id: str) -> Optional[str]:
        return None

# inherits from database service
class PostgreSQLDatabaseService(____________):
    """PostgreSQL Database Service"""

    def save(self, item: str) -> str:
        # some logic
        return item

    def get(self, item_id: str) -> Optional[str]:
        return None

# inherits from logger service
class Application(___________):
    """
        Application is a logger that has a database
        
        Args:
            db (DatabaseService): A general database service to be used
    """
    def __init__(self, db: DatabaseService) -> None:
        self.__log: list[str] = []
        self.__db: DatabaseService = _____

    # implements the _log method from the LoggerService interface
    def _log(self, message: str) -> None:
        self.__log.append(message)

    def save_item(self, item: str) -> str:
        """Method to save an item"""
        # some logic
        saved_item = self.__db.save(item)
        self._log("saved an item")
        # more logic
        return saved_item

    @property
    def log(self) -> list[str]:
        return self.__log

# make a new application using a Mongo Database Service
# we can put in any database service because of interface polymorphism
app: Application = Application(______________())
print(app.save_item("hello world"))
print(app.log)

    



    
