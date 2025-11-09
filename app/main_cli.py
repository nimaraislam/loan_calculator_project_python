from app.schemas.loan_schema import Loan

def main():
    print("**********Welcome to Loan Calculator**********")
    while True:
        print("Please select an option:")
        print("Press C for calculate loan interest.")
        print("Press Q for quit.")
        input_option=input("> ").strip().upper()
        if input_option == "C":
            input_principal_amount= input("Enter the desired loan amount (Kr.): ").strip()
            input_interest_rate= input("Enter the interest rate: ").strip()
            input_term= input("Enter the term: ").strip()
            try:
                principal=float(input_principal_amount)
                interest_rate=float(input_interest_rate)
                term=int(input_term)
                input_duration=input("Month or Year? [M/Y]: ").strip().upper()
                loan=Loan(principal,interest_rate,term)
                loan.calculate_loan_interest(input_duration)
                loan.calculate_final_amount()
                print(f"Interest amount:{loan.calculate_loan_interest(input_duration):.2f} kr.")
                print(f"Final Amount to be Paid:{loan.calculate_final_amount():.2f} kr")
                print(loan.to_dict())
            except ValueError as e:
                print(f"Error: {e}")
        elif input_option == "Q":
                break
        else:
             print("Invalid selection!Press again a correct option.")       

if __name__=="__main__":
    main()