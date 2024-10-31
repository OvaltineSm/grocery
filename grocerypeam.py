grocery = [
    {
        "name": "Meat",
        "productName": [
            {"partName": "Ramb","price": 800},
            {"partName": "Chicken", "price": 400},
            {"partName": "Turkey", "price": 600},
        ],
    },
    {
        "name": "Grain",
        "productName": [
            {"partName": "Rice", "price": 200},
            {"partName": "Wheat-Bread", "price": 300},
            {"partName": "Pasta", "price": 20},
        ],
    },
]

basket = []
while True:
    print("Welcome to my grocery shop:Type 0 to exit")
    for i in range(len(grocery)):
        print(f"{i+1})"+ grocery[i]["name"])
    answer = int(input("Type your answer:"))
    if answer == 0:
        break
    getitem = grocery[answer - 1]
    
    for i in range(len(getitem["productName"])):
        print(f"{i+1})"+ getitem["productName"][i]["partName"])
    answer = int(input("Type your answer:")) - 1 
    basket.append(getitem["productName"][i])
print("\n\n================")
total_price = sum(part["price"] for part in basket)

print("Receipt")
print("--------")

for part in basket:
    print(f"{part['partName']:10} - ${part['price']}")

print("--------")
print(f"Total: ${total_price}")



















