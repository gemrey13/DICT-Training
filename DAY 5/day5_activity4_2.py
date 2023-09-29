from day5_activity4 import BankAccount

acc1 = BankAccount("Gem Rey", 20)
acc2 = BankAccount("Menard")

acc1.deposit(20)
acc2.deposit(32)

acc1.withdraw(21)
acc2.withdraw(30)

acc1.check_balance()
acc2.check_balance()