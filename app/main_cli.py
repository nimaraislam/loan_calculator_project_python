from app.schemas.loan_schema import Loan
from app.services.file_service import read_db, write_db
from app.services.loan_service import *

def main():
    loans = read_db()
    print("**********Welcome to Loan Calculator**********")
    print("Please select an option:")
    while True:
        print("Press C for calculate loan interest.")
        print("Press L for see the list of loans.")
        print("Press D for see the details of a loan.")
        print("Press S for see the summary of loan.")
        print("Press Q for quit.")
        input_option=input("> ").strip().upper()
        if input_option == "C":
            input_principal_amount= input("Enter the desired loan amount (Kr.): ").strip()
            input_interest_rate= input("Enter the interest rate (%): ").strip()
            input_term= input("Enter the term: ").strip()
            try:
                principal=float(input_principal_amount)
                interest_rate=float(input_interest_rate)
                term=int(input_term)
                month_or_year=input("Month or Year?[M/Y]: ").strip().upper()
                loan=Loan(principal,interest_rate,term,month_or_year)
                loan.calculate_loan_interest()
                loan.calculate_final_amount()
                print(f"Interest amount:{loan.calculate_loan_interest():.2f} kr.")
                print(f"Final Amount to be Paid:{loan.calculate_final_amount():.2f} kr")
                input_save=input("Do you want to save data?[Y/N]: ").strip().upper()
                if input_save=="Y":
                    loan.id = len(loans) + 1
                    loans.append(loan.to_dict())
                    write_db(loans)
                    print("Data hase been saved successfully.")
                elif input_save=="N":
                    print("Data has not saved.") 
                else:
                     print(f"Invalid input: '{input_save}'. Data was neither saved nor discarded. Calculation complete.")
                     
            except ValueError as e:
                print(f"Error: {e}")
        elif input_option == "L":
             if len(loans) == 0:
                    print("No loan has been calculated yet!")
             else:
                header=["Id","Principal Amount","Interest Rate","Term","M/Y","Interest","Final Amount"]
                print(f"{header[0]:<5}{header[1]:<18}{header[2]:<15}{header[3]:<5}{header[4]:<5}{header[5]:<15}{header[6]:<18}")
                print("-"*80)
                for i in loans:
                        #values=[i['id'],i['principal_amount'],i['interest_rate'],i['term'],i['month_or_year'],i['total_interest'],i['final_amount']]
                    principal_formatted=f"{i['principal_amount']:.2f} kr."
                    interest_rate_formatted=f"{i['interest_rate']:.2f} %"
                    total_interest_formatted=f"{i['total_interest']:.2f} kr."
                    final_amount_formatted=f"{i['final_amount']:.2f} kr."
                    print(f"{i['id']:<5}{principal_formatted:<18}{interest_rate_formatted:<15}{i['term']:<5}{i['month_or_year']:<5}{total_interest_formatted:<15}{final_amount_formatted:<18}")
                print("-"*80)
        elif input_option == "D":
             if len(loans) == 0:
                    print("No loan has been calculated yet!")
             else:
                print("Id","Principal Amount",sep="\t")
                for i in loans:
                    id = i['id']
                    principal_amt=f"{i['principal_amount']} kr."
                    print(id,principal_amt,sep="\t")
                print("Select id to check the loan details")
                try:
                    input_id=input(">").strip()
                    input_id_int=int(input_id)
                    print("-------------Details--------------")
                    
                    for i in loans:
                        if i['id']==input_id_int:
                             print(f"Id: {i['id']}\n"
                                   f"Princpal Amount: {i['principal_amount']:.2f} kr.\n"
                                   f"PInterest Rate: {i['interest_rate']:.2f} %\n"
                                   f"Term: {i['term']} {'Month' if {i['month_or_year']}=='M' else 'Year'}\n"
                                   f"Total Interest Amount: {i['total_interest']:.2f} kr.\n"
                                   f"Final Amount: {i['final_amount']:.2f} kr." ) 
                    print(f"Monthly Installment: {calculate_monthly_installment(input_id_int):.2f} kr.")
                    print("-"*30)                
                except ValueError:
                     print("Invalid Id")
                except TypeError:
                     print("Invalid Id")
        elif input_option == "Q":
                break
        else:
             print("Invalid selection!Press again a correct option.")       

if __name__=="__main__":
    main()