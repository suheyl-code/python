# Write a function to seperate names from emails of a tuple in a list, i.e [("alex@example.com", "Alex Johnson")...]
def seperate(people):
    result = []
    for email, name in people:
        result.append(f"{name} <{email}>")
    return result


people = [("alex@example.com", "Alex Johnson"),
          ("john@gmail.com", "John james")]
print(seperate(people))
