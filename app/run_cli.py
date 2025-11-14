from app.services.file_service import read_db,DB_PATH
from app.services.loan_service import Loan
from app.services.database import Database

def main():
    #loans = read_db()
    database=Database()
    print("**********Welcome to the Loan Calculator**********")
    print("Please select an option:")
    while True:
        print("Press A for add a new loan.")
        print("Press D for delete a loan.")
        print("Press L for view all loans.")
        print("Press E for view details of a loan.")
        print("Press S for summarize total principal, interest, and final amounts.")
        print("Press Q for quit.")
        input_option=input("> ").strip().upper()
        if input_option == "A":
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
                print("-"*25)
                print(f"Interest amount:{loan.calculate_loan_interest():.2f} kr.")
                print(f"Final Amount to be Paid:{loan.calculate_final_amount():.2f} kr")
                print("-"*25)
                input_save=input("Do you want to save data?[Y/N]: ").strip().upper()
                print("")
                if input_save=="Y":
                    database.save_loan(loan)
                    print("Data has been saved successfully.\n")
                elif input_save=="N":
                    print("Data has not saved.") 
                else:
                     print(f"Invalid input: '{input_save}'. Data was neither saved nor discarded. Calculation complete.\n")
                     
            except ValueError as e:
                print(f"Error: {e}")
        elif input_option == "D":
             loans = print_loan_list()
             if loans == None:
                 print("No loan has been calculated yet!")
                 print("-"*25)
             else:
                 print("-"*25)
                 print("Select id to delete the loan.")
                 try:
                    input_id=input(">").strip()
                    input_id_int=int(input_id)
                    print("-------------Details--------------")
                    print_loan_details_by_id(input_id_int)
                    print("")
                    input_delete=input("Do you want to delete data?[Y/N]: ").strip().upper()
                    print("")
                    if input_delete=="Y":
                        deleted_loans=database.delete_loan_by_id(input_id_int)
                        if deleted_loans is None:
                            print(f"Loan with ID {input_delete} not found.")
                        print(f"Loan with id {input_delete} has been deleted.")
                    #loans=read_db()
                    elif input_delete=="N":
                        print("Loan has not deleted.") 
                    else:
                        print(f"Invalid input: '{input_delete}'.Invalid input\n")
                 except ValueError:
                    print("Invalid Id")
                 except TypeError:
                        print("Invalid Id")
                
        elif input_option == "L":
             loans = database.get_all_loans()
             if len(loans) == 0:
                    print("No loan has been calculated yet!\n")
                    print("-"*25)
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
        elif input_option == "E":
            loans = print_loan_list()
            if loans is None:
                 print("No loan has been calculated yet!")
                 print("-"*25)
            else:
                 print("-"*25)
                 print("Select id to check the loan details")
                 try:
                    input_id=input(">").strip()
                    input_id_int=int(input_id)
                    print("-------------Details--------------")
                    print_loan_details_by_id(input_id_int)
                    print("-"*30)  

                 except ValueError:
                        print("Invalid Id")
                 except TypeError:
                        print("Invalid Id")

        elif input_option == "S":
             if database.get_total_loan_number() == 0:
                print("No loan has been calculated yet!\n")
                print("-"*25)
             else:
                print("--------------Summary--------------")
                print(f"Total loan: {database.get_total_loan_number()} \n"
                    f"Sum of Princpal Amount: {database.get_sum_of_principal_amount():.2f} kr. \n"
                    f"Sum of Interest Amount: {database.get_sum_of_interest_amount():.2f} kr. \n"
                    f"Sum of Final Amount: {database.get_sum_of_final_amount():.2f} kr.")
                print("-"*35)
        elif input_option == "Q":
                break
        else:
             print("Invalid selection!Press again a correct option.")

def print_loan_list():
      database = Database()
      loans = database.get_all_loans()
      if len(loans) == 0:
            return None          
      else:
           print("Id","Principal Amount",sep="\t")
           for i in loans:
             id = i['id']
             principal_amt=f"{i['principal_amount']} kr."
             print(id,principal_amt,sep="\t")
      return loans

def print_loan_details_by_id(input_id_int):
      database = Database()
      loan=database.get_loan_details_by_id(input_id_int)
      print( f"Id: {loan['id']}\n"
             f"Princpal Amount: {loan['principal_amount']:.2f} kr.\n"
             f"Interest Rate: {loan['interest_rate']:.2f} %\n"
             f"Term: {loan['term']} {'Month' if {loan['month_or_year']}=='M' else 'Year'}\n"
             f"Total Interest Amount: {loan['total_interest']:.2f} kr.\n"
             f"Final Amount: {loan['final_amount']:.2f} kr." ) 
      print(f"Monthly Installment: {database.calculate_monthly_installment(input_id_int):.2f} kr.")
      return loan
           

if __name__=="__main__":
    main()