from dataclasses import dataclass


class Chunk:
  def __init__(self, header, data):
    self.is_header = header
    self.data = data


@dataclass
class Authenticator:
  password: str

  @staticmethod
  def authenticate():
    print("Authenticated!")


def run_command(command):
  if not isinstance(command, tuple) or len(command) < 2:
    print("Malformed command")
  else:
    opcode = command[0]
    if opcode == "connect":
      if len(command) != 2:
        print("Malformed command")
      else:
        channel = command[1]
        print(f"Connecting to channel {channel}")
    elif not command[1]:
      print(f"Unable to execute {opcode}: connection not established")
    elif opcode == "synchronise":
      if len(command) != 3:
        print("Malformed command")
      else:
        timestamp = command[2]
        if timestamp >= 0:
          print(f"Synchronising to timestamp {timestamp}")
        else:
          print("Invalid timestamp")
    elif opcode == "authenticate":
      if len(command) != 3:
        print("Malformed command")
      else:
        connection = command[2]
        if connection.password == "correct-horse-battery-staple":
          connection.authenticate()
        else:
          print("Couldn't authenticate connection")
    elif opcode == "send":
      if len(command) != 3:
        print("Malformed command")
      chunks = None
      if isinstance(command[2], list):
        chunks = command[2]
      elif isinstance(command[2], dict) and "data" in command[2] and isinstance(command[2]["data"], list):
        chunks = command[2]["data"]
      else:
        print("Malformed command")
      if chunks is not None:
        if len(chunks) >= 1 and chunks[0].is_header:
          chunks = chunks[1:]
        print("".join(chunk.data for chunk in chunks))
    else:
      print("Malformed command")


run_command(("connect", "Two"))
run_command(("synchronise", False, 10))
run_command(("synchronise", True, -10))
run_command(("synchronise", True, 20))
run_command(("authenticate", False, Authenticator(
    "correct-horse-battery-staple")))
run_command(("authenticate", True, Authenticator(
    "incorrect-donkey-generator-glue")))
run_command(("authenticate", True, Authenticator(
    "correct-horse-battery-staple")))
advanced_authenticator = Authenticator("correct-horse-battery-staple")
advanced_authenticator.authenticate = lambda: print(
    "Authenticated with advanced security")
run_command(("authenticate", True, advanced_authenticator))
run_command(("send", False, [Chunk(False, "households")]))
run_command(("send", True, [Chunk(True, "both"), Chunk(False, "alike")]))
run_command(("send", True, [Chunk(False, "in"),
            Chunk(False, "dignity"), Chunk(False, "in")]))
run_command(
    (
        "send", True, {
            "data": [
                Chunk(
                    True, "fair"), Chunk(
                    False, "Verona"), Chunk(
                    False, "where")]}))
run_command(
    ("send", True, {"data": [Chunk(False, "we"), Chunk(False, "lay")], "count": 2}))
run_command(("send", True, []))
run_command("restart")
run_command(tuple())
run_command(("disconnect", "Two"))
run_command(("connect",))
run_command(("synchronise", True, 4, "our"))
run_command(("send", True, Chunk(False, "scene")))
