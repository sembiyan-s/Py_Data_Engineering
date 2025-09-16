#   returns a function as an output

def email_builder(domain):
    def build_email(username):
        return(f'{username}@{domain}')
    return build_email

# create a builder function //      pre-bound logic /context bound
gmail=email_builder("gmail.com")  # build_email("sembiyan")
yahoo=email_builder("yahoo.com")
hotmail=email_builder("hotmail.com")
outlook=email_builder("outlook.com")

print(gmail("sembiyan"))
print(yahoo("sivadharshan"))
print(hotmail("Thanjai"))
print(outlook("SingaTamilan"))

