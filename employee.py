"""Employee pay calculator."""

class Employee:

    def __init__(self, name, wage, monthlyHours, numOfContracts, contractRate):
        self.name = name
        self.wage = wage
        self.monthlyHours = monthlyHours
        self.numOfContracts = numOfContracts
        self.contractRate = contractRate

    def get_pay(self):
        hours = self.monthlyHours
        contracts = self.numOfContracts

        if self.monthlyHours < 0:
            hours = 1
        if self.numOfContracts <= 0:
            contracts = 1
        return (self.wage * hours) + (contracts * self.contractRate)

    def __str__(self):
        pay = ""

        if(self.monthlyHours < 0):
            pay += self.name + " works on a monthly salary of " + str(self.wage)
        else:
            pay += self.name + " works on a contract of " + str(self.monthlyHours) + " hours at " + str(self.wage) +"/hour"

        if(self.numOfContracts == 0 and self.contractRate > 0):
            pay += " and receives a bonus commission of " + str(self.contractRate)
        elif(self.numOfContracts > 1):
            pay += " and receives a commission for " + str(self.numOfContracts) + " contract(s) at " + str(self.contractRate) + "/contract"

        pay += ".  Their total pay is " + str(self.get_pay()) + "."
        
        return pay

# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', 4000, -1, 0, 0)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', 25, 100, 0, 0)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', 3000, -1, 4, 200)

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', 25, 150, 3, 220)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', 2000, -1, 0, 1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', 30, 120, 0, 600)
