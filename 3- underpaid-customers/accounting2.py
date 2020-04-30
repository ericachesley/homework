MELON_COST = 1.00

def check_payments(file_name):
    """Check for underpayments

    Parses order log and compares each payment to the expected cost (melons*melon_cost)
    """
    
    log_file = open(file_name)
    
    for line in log_file:
        line = line.rstrip()
        data = line.split("|")
        
        name = data[1]
        first_name = name.split(" ")[0]
        melons = int(data[2])
        paid = float(data[3])

        expected = melons * MELON_COST
        if expected != paid:
            payment_status = "overpaid" if paid > expected else "underpaid"
            print(f"{name} paid ${paid:.2f},",
                  f"expected ${expected:.2f}",
                  f"--> {first_name} {payment_status}"
                  )
            

check_payments("customer-orders.txt")