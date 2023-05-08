import secrets
import string


def password_generator(
  length: int = 16,
  uppercase: bool = True,
  lowercase: bool = True,
  numbers: bool = True,
  symbols: bool = True,
) -> str:
  """
  Generate a random password based on the given parameters.
  """

  characters: list[str] = []

  if uppercase:
    frequency = 4
    characters += string.ascii_uppercase * frequency

  if lowercase:
    frequency = 4
    characters += string.ascii_lowercase * frequency

  if numbers:
    frequency = 3
    characters += string.digits * frequency

  if symbols:
    frequency = 2
    characters += string.punctuation * frequency

  password = ""
  password = password.join(secrets.choice(characters) for _ in range(32 if length > 32 else length))
    
  return password

