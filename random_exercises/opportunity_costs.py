# A program I made to compare my lifetime earnings in my current career, and
#after having taken a bootcamp, or going to college, taking into account
#cost of bootcamp/school and the time spent not making money.

current_age = float(input("How old are you? "))
retire_age = int(input("At what age do you expect to retire? ")) #The program
#could be further refined by having different retirement ages for different
#careers.

current_career = input("What is your current career? ")
current_income = int(input("What are the yearly earnings in your current"
    " career? "))

bootcamp_income = int(input("What salary would you earn after a coding"
    " bootcamp? "))
bootcamp_months = float(input("How many months does the bootcamp take? "))
bootcamp_years = bootcamp_months / 12 #Converts to years
bootcamp_cost = int(input("How much does the bootcamp cost? "))

college_income = int(input("What salary would you make after earning a"
    " degree? "))
college_years = int(input("How many years would you spend in college? "))
college_cost = int(input("What would tuition cost per year? "))
total_tuition = int(college_cost * college_years)

def tax_rate(salary, career): #Based on 2019 Brackets,
    if salary <= 39475: #determines effective tax rate and salary, filing 
        bracket1 = 9700 * 0.9 #singly, ignores deductions
        bracket2 = (salary - 9700) * 0.88
        after_tax = bracket1 + bracket2
        taxes = salary - after_tax
        eff_rate = taxes / salary
        print(f"Your income after taxes in {career} would be {after_tax}. "
        f"Your effective tax rate would be {eff_rate}.")
        return after_tax
    elif salary <= 84200:
        bracket1 = 9700 * 0.9
        bracket2 = (39475 - 9700) * 0.88
        bracket3 = (salary - 39475) * 0.78
        after_tax = bracket1 + bracket2 + bracket3
        taxes = salary - after_tax
        eff_rate = taxes / salary
        print(f"Your income after taxes in {career} would be {after_tax}. "
        f"Your effective tax rate would be {eff_rate}.")
        return after_tax
    elif salary <= 160725:
        bracket1 = 9700 * 0.9
        bracket2 = (39475 - 9700) * 0.88
        bracket3 = (84200 - 39475) * 0.78
        bracket4 = (salary - 84200) * 0.76
        after_tax = bracket1 + bracket2 + bracket3 + bracket4
        taxes = salary - after_tax
        eff_rate = taxes / salary
        print(f"Your income after taxes in {career} would be {after_tax}. "
        f"Your effective tax rate would be {eff_rate}.")
        return after_tax
    elif salary <= 204100:
        bracket1 = 9700 * 0.9
        bracket2 = (39475 - 9700) * 0.88
        bracket3 = (84200 - 39475) * 0.78
        bracket4 = (160725 - 84200) * 0.76
        bracket5 = (salary - 160725) * 0.68
        after_tax = bracket1 + bracket2 + bracket3 + bracket4 + bracket5
        taxes = salary - after_tax
        eff_rate = taxes / salary
        print(f"Your income after taxes in {career} would be {after_tax}. "
        f"Your effective tax rate would be {eff_rate}.")
        return after_tax
    elif salary <= 510300:
        bracket1 = 9700 * 0.9
        bracket2 = (39475 - 9700) * 0.88
        bracket3 = (84200 - 39475) * 0.78
        bracket4 = (160725 - 84200) * 0.76
        bracket5 = (204100 - 160725) * 0.68
        bracket6 = (salary - 204100) * 0.65
        after_tax = bracket1 + bracket2 + bracket3 + bracket4 + bracket5 + bracket6
        taxes = salary - after_tax
        eff_rate = taxes / salary
        print(f"Your income after taxes in {career} would be {after_tax}. "
        f"Your effective tax rate would be {eff_rate}.")
    elif salary > 510300:
        bracket1 = 9700 * 0.9
        bracket2 = (39475 - 9700) * 0.88
        bracket3 = (84200 - 39475) * 0.78
        bracket4 = (160725 - 84200) * 0.76
        bracket5 = (204100 - 160725) * 0.68
        bracket6 = (510300 - 204100) * 0.65
        bracket7 = (salary - 510300) * 0.63
        after_tax = bracket1 + bracket2 + bracket3 + bracket4 + bracket5 + bracket6 + bracket7
        taxes = salary - after_tax
        eff_rate = taxes / salary
        print(f"Your income after taxes in {career} would be {after_tax}. "
        f"Your effective tax rate would be {eff_rate}.")
        return after_tax

#Determines lifetime earnings before taxes
def before_tax_lifetime(salary, career, time_spent = 0, cost = 0): 
    lifetime_earnings = int((retire_age - current_age - time_spent) * salary)
    adjusted_for_learning = lifetime_earnings - cost
    print(f"\nBefore taxes, your lifetime earnings would be "
        f"{lifetime_earnings} in a career in {career}. Adjusted "
        f"for learning costs, this would be {adjusted_for_learning}.")

def after_tax_lifetime(salary, career, time_spent = 0, cost = 0): #Determines 
    after_tax_salary = tax_rate(salary, career) #lifetime earnings after taxes
    after_tax_lifetime_earnings = int((retire_age - current_age - time_spent)
     * after_tax_salary)
    adjusted_for_learning = after_tax_lifetime_earnings - cost
    print(f"After taxes, your lifetime earnings would be "
        f"{after_tax_lifetime_earnings} in a career in {career}. Adjusted "
        f"for learning costs, this would be {adjusted_for_learning}.")

before_tax_lifetime(bootcamp_income, "Software Development", bootcamp_years, 
bootcamp_cost)
after_tax_lifetime(bootcamp_income, "Software Development", bootcamp_years, 
bootcamp_cost)

before_tax_lifetime(college_income, "a college career", college_years,
college_cost)
after_tax_lifetime(college_income, "a college career", college_years, 
college_cost)

before_tax_lifetime(current_income, current_career)
after_tax_lifetime(current_income, current_career)
print("Please note that tax deductions are ignored here.")
#Add in a standard deduction