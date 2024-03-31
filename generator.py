import random
import datetime
from faker import Faker

fake = Faker()


def generate(fake, random, cursor, db): 
    for _ in range(150):
        username = fake.user_name()
        email = fake.email()
        password = fake.password(length=10)
        address = fake.address()
        phone_number = fake.phone_number()[:10]
        registration_date = fake.date_this_decade()
        cursor.execute("INSERT INTO Users (Username, Email, Password, Address, PhoneNumber, RegistrationDate) VALUES (%s, %s, %s, %s, %s, %s)",
                    (username, email, password, address, phone_number, registration_date))
        db.commit()

        # Generate 150 random stores
    for _ in range(150):
        store_name = fake.company()
        owner_id = random.randint(1, 150)
        description = fake.text()
        location = fake.address()
        creation_date = fake.date_this_decade()
        cursor.execute("INSERT INTO Stores (StoreName, OwnerID, Description, Location, CreationDate) VALUES (%s, %s, %s, %s, %s)",
                    (store_name, owner_id, description, location, creation_date))
        db.commit()

    # Generate 150 random products
    for _ in range(150):
        store_id = random.randint(1, 150)
        product_name = fake.word()
        category = fake.word()
        description = fake.text()
        price = round(random.uniform(1, 1000), 2)
        stock_quantity = random.randint(1, 100)
        cursor.execute("INSERT INTO Products (StoreID, ProductName, Category, Description, Price, StockQuantity) VALUES (%s, %s, %s, %s, %s, %s)",
                    (store_id, product_name, category, description, price, stock_quantity))
        db.commit()

    # Generate 150 random orders
    for _ in range(150):
        user_id = random.randint(1, 150)
        order_date = fake.date_between(start_date='-1y', end_date='today')
        total_amount = round(random.uniform(10, 1000), 2)
        cursor.execute("INSERT INTO Orders (UserID, OrderDate, TotalAmount) VALUES (%s, %s, %s)",
                    (user_id, order_date, total_amount))
        db.commit()

    # Generate 150 random order details
    for _ in range(150):
        order_id = random.randint(1, 150)
        product_id = random.randint(1, 150)
        quantity = random.randint(1, 10)
        subtotal = round(random.uniform(10, 1000), 2)
        payment_method = random.choice(['Credit Card', 'Debit Card', 'PayPal'])
        cursor.execute("INSERT INTO OrderDetails (OrderID, ProductID, Quantity, Subtotal, PaymentMethod) VALUES (%s, %s, %s, %s, %s)",
                    (order_id, product_id, quantity, subtotal, payment_method))
        db.commit()

def test(): 
    print('hello world')
    
def input_to_contacts(random, cursor, db):
    # Generate and insert random 10-digit numbers into the Contacts column
    for _ in range(150):
        random_number = ''.join(random.choices('0123456789', k=10))  # Generate a random 10-digit number
        sql = f"UPDATE stores SET Contacts = '{random_number}' WHERE Contacts IS NULL LIMIT 1"  # Update only rows where Contacts is NULL
        cursor.execute(sql)
        db.commit()
