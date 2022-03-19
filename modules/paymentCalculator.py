from  modules import payment_conditions

def processHours(hours):
    """ This function will calculate the final price that must be paid to an employee.

    Args:
        hours (string): This is a string with the days and hours that must be processed.

    Returns:
        int: This is the result in USD.
    """
    earned_money=0
    days=hours.split(',')
    for d in days:
        day=d[:2]
        starting_hour=d[2:4]
        finishing_hour=d[8:10]
        total_hours=int(finishing_hour)-int(starting_hour)
        if day in payment_conditions.regular_days:
            b=int(starting_hour)+1
            for i in range(total_hours):
                if b+i in payment_conditions.day_hours:
                    earned_money+=15
                elif b+i  in payment_conditions.nigth_hours:
                    earned_money+=20
                elif b+i  in payment_conditions.dawn_hours:
                    earned_money+=25  
        elif day in payment_conditions.weekends:
            b=int(starting_hour)+1
            for i in range(total_hours):
                if b+i in payment_conditions.day_hours:
                    earned_money+=20
                elif b+i  in payment_conditions.nigth_hours:
                    earned_money+=25
                elif b+i  in payment_conditions.dawn_hours:
                    earned_money+=30 
        else:
            return ("Can't read the days in file")
    return earned_money
    

def calculate(employees):
    """This is the function that receives the data from all the employees, iterate it and calculates the values (by calling hours processor)
     and returns the result in the asked format.

    Args:
        employees (array): List of employees with their worked hours

    Returns:
        array: A list with the results of all the employees
    """
    results=[]
    for e in employees:
        employee = e.split('=')
        name = employee[0]
        hours= employee[1]
        result = processHours(hours)
        results.append(f'The amount to pay {name} is: {str(result)} USD')
    return results   