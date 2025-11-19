from pydantic import BaseModel, Field

class User(BaseModel):
    name: str = Field(min_length=3)
    age: int = Field(ge=0)
    email: str = Field(min_length=5)


if __name__ == "__main__":
 
    tests = [
        {"name": "Alice", "age": 25, "email": "alice@example.com"},
        {"name": "Al", "age": 25, "email": "alice@example.com"},
        {"name": "Bob", "age": -5, "email": "bob@example.com"},
        {"name": "Charlie", "age": 30, "email": "c@b"},
        {"name": "Charliead", "age": 30, "email": "c@b"},

    ]

    for test in tests:
        print("----------------------------\n")
        try:
            user = User(**test)
            print(f"Erfolgreich erstellt: \n{user}")
        except Exception as e:
            print(f"Fehler bei der Erstellung von \n{test}: \n{e}")
   

