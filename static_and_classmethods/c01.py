from enum import Enum

class Skin(Enum):
    """Enum to store player skins and demonstrate static attributes"""
    DEFAULT = "._."
    SKIN0 = "(^ω^)"
    SKIN1 = "(●´ω｀●)"
    SKIN2 = "ᕦ(ò_óˇ)ᕤ"

    # we use a static method as Skin is not instantiated - it is used as a class
    @staticmethod
    def allowed_skins() -> dict[str, str]:
        """
            Method to get a dictionary of allowed skins
        """
        return {skin.name : skin.value for skin in Skin}

class User:
    """
        A user has a username, age and skin avatar
    """
    def __init__(self, username: str, age: int) -> None:
        self.__username = username
        self.__age: int = age
        self.__skin: Skin = Skin.DEFAULT

    @property
    def username(self) -> str:
        return self.__username

    @property
    def age(self) -> int:
        return self.__age

    def upgrade_skin(self, skin: Skin) -> None:
        self.__skin = skin

    def __repr__(self) -> str:
        return self.__skin.value

# make a new user and set its skin
user: User = User("admin", 21)
user.upgrade_skin(Skin.SKIN2)
print(user)
print(Skin.allowed_skins())

