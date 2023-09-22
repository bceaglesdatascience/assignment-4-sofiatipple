n=int(input("Number of purchases: "))
sales_tax=float(input("Sales tax: "))


customer_list=[]
item_cost=[]

for x in range(n):
    customer=input("Customer: ")
    cost=int(input("Cost: "))
    item_cost.append(cost)
    customer_list.append(customer)


def add_tax (item_cost,sales_tax):
    total_cost_list=[]
    for cost in item_cost:
        total_tax = sales_tax*cost
        total_cost_list.append(cost+total_tax)
    return total_cost_list

final_cost=add_tax(item_cost,sales_tax)

customer_cost={}

for x,customer in enumerate(customer_list):
    if customer in customer_cost:
        customer_cost[customer_list]+=final_cost[x]
    else:
        customer_cost[customer_list]=final_cost[x]



print(customer_cost)


