class Subscription:
    def __init__(self, name, cost, renewal_date):
        self.name = name
        self.cost = cost
        self.renewal_date = renewal_date

    def get_name(self):
        return self.name
    def get_cost(self):
        return self.cost
    def get_renewal_date(self):
        return self.renewal_date
    def change_renewal_date(self, new_renewal_date):
        self.renewal_date = new_renewal_date
    def change_cost(self, new_cost):
        self.cost = new_cost

class Monthly(Subscription):
    def __init__(self, name, cost, renewal_date):
        Subscription.__init__(self, name, cost, renewal_date)
    def get_yearly_cost(self):
        return self.cost * 12

class Yearly(Subscription):
    def __init__(self, name, cost, renewal_date):
        Subscription.__init__(self, name, cost, renewal_date)
    def get_monthly_cost(self):
        return self.cost / 12

class Inventory:
    items = []

    def add(self, user_sub):
        for sub in self.items:
            if sub.get_name() == user_sub.get_name():
                return False
        self.items.append(user_sub)
        return True

    def get_total_cost(self):
        ot_cost = 0
        monthly_cost = 0
        yearly_cost = 0
        for sub in self.items:
            if isinstance(sub, Monthly):
                monthly_cost += sub.get_cost()
            elif isinstance(sub, Yearly):
                yearly_cost += sub.get_cost()
            else:
                ot_cost += sub.get_cost()
        print("You have paid $%s for one time subscriptions" % ot_cost)
        print("You are paying $%s for monthly subscriptions" % monthly_cost)
        print("You are paying $%s for yearly subscriptions" % yearly_cost)
        total_cost = monthly_cost*12 + yearly_cost
        print("Your total yearly cost for subscriptions is $%s" % total_cost)

    def print_subs(self):
        print("Printing all subscriptions....")
        for sub in self.items:
            name = sub.get_name()
            cost = sub.get_cost()
            print("Name: %s   Cost: $%s" % (name, cost))
            if isinstance(sub, Monthly):
                print("Yearly Cost is: %s" % sub.get_yearly_cost())
            elif isinstance(sub, Yearly):
                print("Monthly cost is: %s" % sub.get_monthly_cost())
        if len(self.items) == 0:
            print("You have no subscriptions")

    def remove(self, name):
        for sub in self.items:
            if sub.get_name() == name:
                self.items.remove(sub)
                return True
        return False

# my_subs = Inventory()
# netflix = Subscription("Netflix", 13, "July 20 2019")
# hulu = Subscription("Hulu", 8, "July 10 2019")
# hbo = Subscription("HBO", 15, "August 2 2019")
# my_subs.add_sub(netflix)
# my_subs.add_sub(hulu)
# my_subs.add_sub(hbo)
# my_subs.print_subs()
# my_subs.get_total_cost()
# my_subs.remove_sub("Hulu")
# my_subs.remove_sub("HBO")
# my_subs.print_subs()