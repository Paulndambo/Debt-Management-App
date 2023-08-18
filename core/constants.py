MONTHS_LIST = (
    ("January", "January"),
    ("February", "February"),
    ("March", "March"),
    ("April", "April"),
    ("May", "May"),
    ("June", "June"),
    ("July", "July"),
    ("August", "August"),
    ("September", "September"),
    ("October", "October"),
    ("November", "November"),
    ("December", "December"),
)

LOAN_STATUS_CHOICES = (
    ("Paid", "Paid"),
    ("Defaulted", "Defaulted"),
    ("Paying", "Paying"),
    ("Reviewing", "Reviewing"),
)

YEARS_CHOICE_LIST = (
    ("2023", "2023"),
    ("2024", "2024"),
    ("2025", "2025"),
    ("2026", "2026"),
    ("2027", "2027"),
    ("2028", "2028"),
    ("2029", "2029"),
)

def get_loan_status(amount_borrowed, amount_paid):
    loan_status = ''
    if amount_borrowed == amount_paid:
        loan_status = 'Paid'
    elif amount_borrowed > amount_paid:
        loan_status = 'Paying'

    return loan_status