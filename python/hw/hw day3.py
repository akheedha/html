is_logged_in = True 
is_subscribed = False

user_credits = 100
max_credits = 200
min_credits = 50

credit_valid = min_credits < user_credits <= max_credits
bonus_eligible = not (user_credits <= min_credits) or is_subscribed 

user_credits += 50
user_credits -= 20
user_credits *=  2
user_credits %= 150

power_result = user_credits ** 2

full_access = is_subscribed and is_logged_in
is_true_login = is_logged_in == True

access_result = is_logged_in or is_subscribed and False
print(f'''
{is_logged_in}
{is_subscribed}
{credit_valid}
{bonus_eligible}
{user_credits}
{power_result}
{full_access}
{is_true_login}
{access_result}
''')
