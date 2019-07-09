# subscription-tracker
Users add or remove subscriptions and print important data about the subscription.
Subscription is the base class and it contains information such as name, cost and renewal date.
Monthly is a inherited class that has specific methods for a monthly renewal date.
Yearly is a inherited class that has specific methods for a yearly renewal date.
The inventory class is used to keep track of all the subsciptions. It lets us add and remove subscriptions. If a subscription has already been added then we won't add it again. If we try to remove a subscription that does not exist in our inventory then we say so by returning false. The print_subs method allows for us to display the subscriptions name, cost and renewal date.
