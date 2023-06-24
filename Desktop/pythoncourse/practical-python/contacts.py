contacts = {
    "number":4,
    "students":
    [
        {"name":"Bryan Beck", "email":"bryan@example.com"},
        {"name":"Harry Potter", "email":"harry@example.com"},
        {"name":"Ron Weasley", "email":"ron@example.com"},
        {"name":"Hermione Granger", "email":"hermione@example.com"}
    ]
}

for student in contacts["students"]:
    print(student["email"])