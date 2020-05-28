income = int(input())
if income <= 15527:
    percent = 0
elif 15528 <= income <= 42707:
    percent = 15
elif 42708 <= income <= 132406:
    percent = 25
else:
    percent = 28
calculated_tax = income * percent / 100
print('The tax for {} is {}%. That is {:.0f} dollars!'.format(income, percent, calculated_tax))