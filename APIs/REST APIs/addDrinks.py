from app import app, db, Drink

def get_drink_input():
    drinks = []
    while True:
        drink_name = input("Enter the name of a drink, or enter 'done' to end it : ")
        if drink_name.lower() == 'done':
            break
        drink_description = input("Enter the description of the drink : ")
        drinks.append(Drink(name=drink_name, description=drink_description))
    return drinks

def add_drinks_to_db(drinks):
    with app.app_context():
        for drink in drinks:
            db.session.add(drink)
        db.session.commit()
        print(f"{len(drinks)} drinks added to the database")
        
if __name__ == '__main__':
    drinks = get_drink_input()
    if drinks:
        add_drinks_to_db(drinks=drinks)
    else:
        print("No drinks added to the database")
    print("The elements currently in the database : ")
    Drink.query.all()