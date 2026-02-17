has_account = True
email_verified = False
email = 'g@exmaple.com'
user_age = 17

can_login = has_account and email_verified
is_email_valid = '@' in email
is_age_valid = user_age >= 18 
can_login_final = has_account and email_verified and is_email_valid and is_age_valid

print(f'''\nLogin possible: {can_login}
User age valid: {is_age_valid}
User email valid: {is_email_valid}
User can login: {can_login_final}''')

print(f"\nUser has an account: {has_account == True}\n")