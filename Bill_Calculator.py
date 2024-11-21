def totalCalc(bill , tip_perc):

 total = bill*(1 + 0.01* tip_perc)
 total = round(total , 2)
 print("Please pay: " , total)


totalCalc(180,35)
