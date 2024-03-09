class Bank:

    def __init__(self, balance: List[int]):
        self.account = balance

        

    def transfer(self, account1: int, account2: int, money: int) -> bool:
        if account1 > len(self.account) or account2 > len(self.account) or self.account[account1-1] < money:
            return False
        
        self.account[account1-1] -=money
        self.account[account2 -1] += money

        return True
        

    def deposit(self, account: int, money: int) -> bool:
            if account > len(self.account):
                return False
            
            self.account[account -1] += money

            return True
        

    def withdraw(self, account: int, money: int) -> bool:
        if account > len(self.account):
            return False
        check = self.account[account -1] - money
        if check < 0:
            return False
        
        self.account[account -1] -= money 
        return True
        


# Your Bank object will be instantiated and called as such:
# obj = Bank(balance)
# param_1 = obj.transfer(account1,account2,money)
# param_2 = obj.deposit(account,money)
# param_3 = obj.withdraw(account,money)