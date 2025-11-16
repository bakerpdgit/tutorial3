class User:
  """
      Class for a user that has a username and email
  """

  def __init__(self, username: str, email: str):
    self._username: str = username  # protected attribute
    self._email: str = email  # protected attribute

  @property
  def username(self):
    return self._username

  @property
  def email(self):
    return self._email

  def view_dashboard(self):
    print("viewing dashboard")

  def __repr__(self):
    return f"User({self._username})"


class Moderator(User):
  """
      Moderator can ban users
  """

  def __init__(self, username: str, email: str):
    super().__init__(username, email)

  def ban_user(self, user: User):
    print(f"banned {user}")


class Admin(Moderator):
  """
      Admin can ban and delete users
  """

  def delete_user(self, user: User):
    print(f"deleted {user}")


# make new user, moderator and admin
user = User("johndoe", "john@example.com")
mod = Moderator("mod_jane", "jane@example.com")
admin = Admin("admin_bob", "bob@example.com")

# methods are inherited
user.view_dashboard()
mod.view_dashboard()
mod.ban_user(user)
admin.view_dashboard()
admin.ban_user(user)
admin.delete_user(user)
