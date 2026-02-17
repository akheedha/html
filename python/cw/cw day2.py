receipt = '''The customer bought 2 items:\n
Book Title: "{0}" – ₹{1}
Book Title: "{2}" – ₹{3}
\nTotal bill amount: \t{4}'''

print("\tMASHUP STACK\n")

book1 = 450
book2 = 600
ttl_amt = book1 + book2

bill = receipt.format('Python basics', book1, 'Data Science Intro', book2, ttl_amt)
print(bill.upper())

print('\nThank'.upper() +  '-You\n'.upper())