# hof rules 1 ----------> can take one function as a argument
# hof rules 2 ----------> returns a function as an output

#   uses ----> code reusability , cannot any changes in code ,dynamic ,flexible

def gmail_email(username,domain="gmail.com"):
    return{f'{username}@{domain}'}

def ymail_email(username,domain="ymail.com"):
    return{f'{username}@{domain}'}

def hotmail_email(username,domain="hotmail.com"):
    return{f'{username}@{domain}'}


def build_mail(username,email_func):
    return email_func(username)     # gmail_email("sembiyan")

print(build_mail("sembiyan" ,gmail_email))
print(build_mail("sivadharshan",ymail_email))
print(build_mail("Thanjai",hotmail_email))
