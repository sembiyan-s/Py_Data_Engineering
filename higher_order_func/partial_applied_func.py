# partially can give only one argument ,another one is fixed 

from functools import partial
def email_builder (username,domain):
    return  f'your mail id is :{username}@{domain}'


# for  fixed domain  using partial function
gmail_fixed=partial(email_builder,domain="gmail.com")
ymail_fixed=partial(email_builder ,domain="yahoo.com")
hotmail_fixed=partial(email_builder ,domain="hotmail.com")

# give one argument without have any error
print(gmail_fixed("sembiyan"))
print(ymail_fixed("sivadharshan"))
print(hotmail_fixed("HipHopTamilan"))