def change_domain(email, oldDomain, newDomain):
    if oldDomain in email:
        nEmail = email[:email.index('@')]
        nEmail = nEmail + '@' + newDomain
    return nEmail

newEmail = change_domain("saggs.frfjvs@gmail.com", "gmail.com", "yahoo.com")
print(newEmail)