import os
class Calc(object):
    def __init__(self):
        while True:
            try:
                os.system('cls')
                self.rental = float(input("What are your total monthly rent earnings?\n"))
                print(f'${self.rental}0')
                self.laundry = self.rental + float(input("What are your total monthly laundry earnings?\n"))
                print(f'${self.laundry}0')
                self.storage = self.laundry + float(input("What are your total monthly storage earnings?\n"))
                print(f'${self.storage}0')
                self.miscellaneous = self.storage + float(input("What are your total monthly other/miscellaneous earnings?\n"))
                print(f'${self.miscellaneous}0')
                self.expenses()
                break
            except Exception as e:
                print(e)

    def expenses(self):
        while True:
            try:
                os.system('cls')
                print("\n-----------------------------------------------------")
                print(f'TOTAL EARNINGS: ${self.miscellaneous}0')
                print("\n-----------------------------------------------------")
                print("\nNow let's take a look at your expected expenses:")
                self.taxes = float(input("What are your total monthly tax expenses?\n"))
                print(f'${self.taxes}0')
                self.insurance = self.taxes + float(input("What are your total monthly insurance expenses?\n"))
                print(f'${self.insurance}0')
                self.utilities = self.insurance + float(input("What are your total monthly utility expenses?\n"))
                print(f'${self.utilities}0')
                self.property = self.utilities + float(input("What are your total monthly property management expenses?\n"))
                print(f'${self.property}0')
                self.hoa = self.property + float(input("What are your total monthly H.O.A. expenses?\n"))
                print(f'${self.hoa}0')
                self.lawn = self.hoa + float(input("What are your total monthly lawn expenses?\n"))
                print(f'${self.lawn}0')
                self.mortgage = self.lawn + float(input("What are your total monthly mortgage expenses?"))
                print(f'${self.mortgage}0')
                self.vacancy = self.mortgage + float(input("What are your total monthly vacancy expenses?\n"))
                print(f'${self.vacancy}0')
                self.repairs = self.vacancy + float(input("What are your total monthly repair expenses?\n"))
                print(f'${self.repairs}0')
                self.capital = self.repairs + float(input("What are your total monthly expenses in capital expenses?\n"))
                print(f'${self.capital}0')
                self.various = self.capital + float(input("What are your total monthly other/miscellaneous expenses?\n"))
                print(f'${self.various}0')
                self.investments()
                break
            except Exception as e:
                print(e)
        
    def investments(self):
        while True:
            try:
                print("\n-----------------------------------------------------")
                print(f'TOTAL EXPENSES: ${self.various}0')
                print("\n-----------------------------------------------------")
                print("\n\tCALCULATING CASH FLOW...")
                print("\n-----------------------------------------------------")
                print(f"\nTOTAL EARNINGS: ${self.miscellaneous}0 -" + f'\nTOTAL EXPENSES: ${self.various}0 =')
                self.flow = self.miscellaneous - self.various
                print(f'TOTAL MONTHLY CASH FLOW: ${self.flow}0')
                print("\nWe have one more step. Let's take a look at your investments:")
                self.down = float(input("How much did you invest in total for your downpayment?\n"))
                print(f'${self.down}0')
                self.closing = self.down + float(input("How much did you invest in total for closing costs?\n"))
                print(f'${self.closing}0')
                self.rehab = self.closing + float(input("How much did you invest in total for rehab/repairs?\n"))
                print(f'${self.rehab}0')
                self.other = self.rehab + float(input("How much did you invest in total for other/miscellaneous expenses?\n"))
                print(f'${self.other}0')
                self.cocroi()
                break
            except Exception as e:
                print(e)

    def cocroi(self):

           
        os.system('cls')
        print("\n-----------------------------------------------------")
        print(f'TOTAL INVESTMENTS: ${self.other}0')
        print("\n-----------------------------------------------------")
        print("\nCALCULATING CASH ON CASH RETURN ON INVESTMENT")
        print("\n---------------------------------------------------------------------------------------------")
        acf = self.flow * 12
        roi = acf/self.other*100
        print(f"\nTOTAL CASHFLOW: ${self.flow}0 × 12 (MONTHS PER YEAR) = ANNUAL CASH FLOW: ${acf}0")
        print(f"\nANNUAL CASH FLOW: ${acf}0 ÷ TOTAL INVESTMENTS: ${self.other}0 × 100 ={roi}")
        print("\n---------------------------------------------------------------------------------------------")
        print("\n\tYOUR CASH ON CASH RETURN ON INVESTMENT" + f'\n\t\t\t {roi}%')


     





Calc()
