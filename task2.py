budgets = {
   "name": "John", "age": 21, "budget": 23000,
   "name1": "Steve",  "age1": 32, "budget1": 40000,
   "name2": "Martin",  "age2": 16, "budget2": 2700,
}
y = budgets.get("budget")
u = budgets.get("budget1")
s = budgets.get("budget2")
f = y + u + s
print(f)