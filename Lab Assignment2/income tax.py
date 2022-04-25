print('''Please adhere to the following instructions for calculating the Income Tax:
      • All taxpayers are charged a flat tax rate of 20%.
      • All taxpayers are allowed a $10,000 standard deduction.
      • For each dependent, a taxpayer is allowed an additional $3,000 deduction.
      • Gross income must be entered to the nearest penny.''')

tax_rate = 0.2
standarad_deduction = 10000
more_deduction = 3000
gross = int(input("Please enter your Gross Income:"))
dependents = int(input("Please enter no. of dependents:"))
taxable_Income = (int(gross) - int(standarad_deduction) - (int(more_deduction) * int(dependents)))
tax = (int(taxable_Income)*float(tax_rate))
print("Your Income Tax value is:", (tax), "$",'\n')
