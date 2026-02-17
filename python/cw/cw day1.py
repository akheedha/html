import random

apple = 15.5
orange = 20
grape = 10.25

tot_vol = apple + orange + grape
print(tot_vol)

tot_vol = int(tot_vol)
print(tot_vol)

tot_vol = str(tot_vol)
print("Total volume sold: " + tot_vol)

random_num = random.randrange(5,10)

tot_vol_final = int(tot_vol) + random_num 
print("Final total after bonus: ",tot_vol_final)