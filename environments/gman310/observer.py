#!/user/bin/env python
"""
Simple implematation of the Ovserver Desing Pattern
"""

class BusinessCustomer:
    """
      This is a type of observer , which is a business customer. when they fall behind 
      on payments, the progrma should automaticaly robocall their finace department.
    """

    def __init__(self, acct_id, money_owed) :
        """
           Constructor to store accoutn ID and current amount of money owed.
           Used to build a new object 
        """
        self.acct_id = acct_id
        self.money_owed = money_owed

    def update(self) :
        """
          When the accounting system (the subject or publisher)need to notify 
          all oveservers(subscribers) about some event this is the method that will be invoked
        """          
        if self.money_owed > 0:
            print (f"{self.acct_id}: Call the company's finace department")
        else:
            print (f"{self.acct_id}: Crporate balance paid")

class  ConsumerCustomer:
    """
        This is antother type of observer, not corp we will send an email instead of a call
    """   
    def __init__(self, acct_id, money_owed):
        """
        """
        self.acct_id = acct_id
        self.money_owed = money_owed    
    def update(self):
        """
        """
        if self.money_owed > 0:
            print  (f"{self.acct_id}: Send an email to the individual")
        else: 
            print (f"{self.acct_id}: Individual is all payd ")
class AccountingSystem:
    """ 
      This is the subject (or Publisher) that maintains a list of observers(subscribers)
      and is capable of notifying them. There could  be a mix of diffrent observes  too
      as we have  both business and consumer
    """
    def __init__(self):
        """
        Construct create a new empty  accounting system with 
          an empty set of customers (obeservers/subscribers)
        """            
        self.customers = set ()

    def register(self, customer):

        """
         A new customer has singed up so add them to the set
        """
        self.customers.add(customer)
         
    def unregister(self, customer):
        """
        An existing customer has closed their account . 
        rmeove them from the set
        """        
        self.customers.remove(customer)

    def notify(self):
        """
         Notify all current  customers about some event. 
         This iteratively steps threugh the set and invokes the update () method 
         on each type of customer.
        """
        for customer in self.customers:
             customer.update()

def main():
    """
    Execution starts here
    """
    # Create a mix of  buisness and Consumer 
    cust1 = BusinessCustomer("ACCT100",10)
    cust2 = BusinessCustomer("ACCT200",0) 
    cust3 = ConsumerCustomer("ACCT300",-10)
    cust4 = ConsumerCustomer("ACCT400",20)
    #create the account systems (subject/Publisher) and register 
    accounting_sys = AccountingSystem() 
    accounting_sys.register(cust1)
    accounting_sys.register(cust2)
    accounting_sys.register(cust3)
    accounting_sys.register(cust4)

    # Some event occurred; notify all subscribers about theri bills
    accounting_sys.notify()
    
    #Once a customer has cancelled their account unregister them 
    print (f"Customer:{cust2.acct_id} has closed thier accoutn")
    accounting_sys.unregister(cust2)

    #Event occured again and notice how cust isn't displayed
    accounting_sys.notify()
if __name__ == "__main__":
    main()
