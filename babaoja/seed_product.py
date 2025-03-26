import os
import django
import random

# Set up Django settings before using any model
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "babaoja.settings")
django.setup()

from storeapp.models import Product, Category, Profile
from django.contrib.auth.models import User

# Create a user (replace with an existing user ID if needed)
user = User.objects.first()
if not user:
    user = User.objects.create_user(username="admin", password="adminpass")

# Create categories if they don't exist
category_names = ["Electronics", "Clothing", "Books", "Home & Kitchen"]
categories = {name: Category.objects.get_or_create(name=name)[0] for name in category_names}

# Seed products
usernames = [
    "john_doe", "jane_smith", "mike_tech", "linda_dsn", 
    "david_ai", "nora_cloud", "samuel_dev", "flora_uiux", 
    "tobi_crypto", "grace_robot"
]

users = {user.username: user for user in User.objects.filter(username__in=usernames)}

products = [
    {"user": random.choice(usernames), "name": "Laptop", "description": "A high-end gaming laptop", "price": 1200.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "T-Shirt", "description": "Comfortable cotton t-shirt", "price": 19.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Python Book", "description": "Learn Python the easy way", "price": 29.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Blender", "description": "High-power kitchen blender", "price": 49.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Smartphone", "description": "Latest model smartphone with AI features", "price": 899.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Jeans", "description": "Stylish denim jeans", "price": 39.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Django Guide", "description": "Master Django framework", "price": 35.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Microwave Oven", "description": "800W microwave oven with grill", "price": 89.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Smartwatch", "description": "Fitness tracker with heart rate monitor", "price": 199.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Sneakers", "description": "Comfortable sports sneakers", "price": 59.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "AI & Machine Learning Book", "description": "Deep dive into AI concepts", "price": 44.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Coffee Maker", "description": "Brew fresh coffee every morning", "price": 79.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Tablet", "description": "10-inch screen tablet", "price": 329.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Leather Jacket", "description": "Premium leather jacket", "price": 199.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Cybersecurity Book", "description": "Learn ethical hacking", "price": 55.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Vacuum Cleaner", "description": "Cordless powerful vacuum cleaner", "price": 149.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Headphones", "description": "Noise-cancelling over-ear headphones", "price": 249.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Sweatshirt", "description": "Cozy fleece sweatshirt", "price": 34.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Web Development Guide", "description": "Full-stack web development course", "price": 39.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Air Fryer", "description": "Healthy cooking with less oil", "price": 99.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Wireless Earbuds", "description": "True wireless earbuds with noise cancellation", "price": 129.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Running Shoes", "description": "Lightweight running shoes", "price": 69.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Blockchain Book", "description": "Understand the blockchain revolution", "price": 49.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Toaster", "description": "4-slice toaster with adjustable settings", "price": 39.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Gaming Mouse", "description": "High-precision wireless gaming mouse", "price": 79.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Winter Coat", "description": "Insulated winter coat for cold weather", "price": 129.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "JavaScript Mastery", "description": "Advanced JavaScript concepts", "price": 37.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Electric Kettle", "description": "1.5L electric kettle with fast boiling", "price": 24.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Gaming Keyboard", "description": "Mechanical RGB gaming keyboard", "price": 109.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Summer Dress", "description": "Floral print summer dress", "price": 49.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Data Science Book", "description": "Hands-on data science projects", "price": 59.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Dishwasher", "description": "Energy-efficient automatic dishwasher", "price": 499.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Monitor", "description": "27-inch 4K UHD monitor", "price": 329.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Joggers", "description": "Stylish cotton joggers", "price": 39.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "UX Design Book", "description": "Learn UI/UX best practices", "price": 45.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Rice Cooker", "description": "Automatic rice cooker with multiple settings", "price": 69.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Portable Speaker", "description": "Bluetooth speaker with deep bass", "price": 89.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Backpack", "description": "Waterproof laptop backpack", "price": 59.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Cybersecurity Mastery", "description": "Comprehensive guide to cybersecurity", "price": 65.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Refrigerator", "description": "Double-door refrigerator with inverter technology", "price": 799.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Drone", "description": "4K camera drone with GPS", "price": 599.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Formal Shirt", "description": "Classic formal shirt", "price": 29.99, "category": categories["Clothing"]},
    {"user": random.choice(usernames), "name": "Python for Beginners", "description": "Step-by-step Python learning", "price": 27.99, "category": categories["Books"]},
    {"user": random.choice(usernames), "name": "Hair Dryer", "description": "Ionic hair dryer for smooth hair", "price": 34.99, "category": categories["Home & Kitchen"]},
    {"user": random.choice(usernames), "name": "Smart TV", "description": "55-inch 4K UHD Smart TV", "price": 699.99, "category": categories["Electronics"]},
    {"user": random.choice(usernames), "name": "Wool Sweater", "description": "Warm wool sweater for winter", "price": 59.99, "category": categories["Clothing"]},
]

# Insert products into the database
for product_data in products:
    user_instance = users.get(product_data["user"])  # Fetch User instance
    if user_instance:  # Ensure user exists
        Product.objects.create(
            user=user_instance,
            name=product_data["name"],
            description=product_data["description"],
            price=product_data["price"],
            category=product_data["category"]
        )

print("✅ Products successfully seeded!")




# Sample data
sample_users = [{
        "username": "john_doe",
        "first_name": "John",
        "last_name": "Doe",
        "email": "john@example.com",
        "phone": "+2348001111111",
        "address": "123 Main St",
        "city": "Lagos",
        "state": "Lagos",
        "zipcode": "100001",
        "country": "Nigeria",
        "profile_bio": "Passionate software developer",
        "homepage_link": "https://johndoe.com",
        "facebook_link": "https://facebook.com/johndoe",
        "instagram_link": "https://instagram.com/johndoe",
        "linkedin_link": "https://linkedin.com/in/johndoe",
        "x_link": "https://x.com/johndoe"
    },
    {
        "username": "jane_smith",
        "first_name": "Jane",
        "last_name": "Smith",
        "email": "jane@example.com",
        "phone": "+2348002222222",
        "address": "456 Side St",
        "city": "Abuja",
        "state": "FCT",
        "zipcode": "900001",
        "country": "Nigeria",
        "profile_bio": "Tech enthusiast and entrepreneur",
        "homepage_link": "https://janesmith.com",
        "facebook_link": "https://facebook.com/janesmith",
        "instagram_link": "https://instagram.com/janesmith",
        "linkedin_link": "https://linkedin.com/in/janesmith",
        "x_link": "https://x.com/janesmith"
    },
    {
        "username": "mike_tech",
        "first_name": "Mike",
        "last_name": "Tech",
        "email": "mike@example.com",
        "phone": "+2348003333333",
        "address": "789 Tech Ave",
        "city": "Ibadan",
        "state": "Oyo",
        "zipcode": "200001",
        "country": "Nigeria",
        "profile_bio": "Cybersecurity expert and blogger",
        "homepage_link": "https://miketech.com",
        "facebook_link": "https://facebook.com/miketech",
        "instagram_link": "https://instagram.com/miketech",
        "linkedin_link": "https://linkedin.com/in/miketech",
        "x_link": "https://x.com/miketech"
    },
    {
        "username": "linda_dsn",
        "first_name": "Linda",
        "last_name": "Dsn",
        "email": "linda@example.com",
        "phone": "+2348004444444",
        "address": "101 Data Science St",
        "city": "Enugu",
        "state": "Enugu",
        "zipcode": "400001",
        "country": "Nigeria",
        "profile_bio": "Data scientist working with AI models",
        "homepage_link": "https://lindadsn.com",
        "facebook_link": "https://facebook.com/lindadsn",
        "instagram_link": "https://instagram.com/lindadsn",
        "linkedin_link": "https://linkedin.com/in/lindadsn",
        "x_link": "https://x.com/lindadsn"
    },
    {
        "username": "david_ai",
        "first_name": "David",
        "last_name": "Ai",
        "email": "david@example.com",
        "phone": "+2348005555555",
        "address": "203 ML Lane",
        "city": "Port Harcourt",
        "state": "Rivers",
        "zipcode": "500001",
        "country": "Nigeria",
        "profile_bio": "AI researcher and machine learning engineer",
        "homepage_link": "https://davidai.com",
        "facebook_link": "https://facebook.com/davidai",
        "instagram_link": "https://instagram.com/davidai",
        "linkedin_link": "https://linkedin.com/in/davidai",
        "x_link": "https://x.com/davidai"
    },
    {
        "username": "nora_cloud",
        "first_name": "Nora",
        "last_name": "Cloud",
        "email": "nora@example.com",
        "phone": "+2348006666666",
        "address": "305 Cloud Computing St",
        "city": "Benin City",
        "state": "Edo",
        "zipcode": "300001",
        "country": "Nigeria",
        "profile_bio": "Cloud architect specializing in AWS and Azure",
        "homepage_link": "https://noracloud.com",
        "facebook_link": "https://facebook.com/noracloud",
        "instagram_link": "https://instagram.com/noracloud",
        "linkedin_link": "https://linkedin.com/in/noracloud",
        "x_link": "https://x.com/noracloud"
    },
    {
        "username": "samuel_dev",
        "first_name": "Samuel",
        "last_name": "Dev",
        "email": "samuel@example.com",
        "phone": "+2348007777777",
        "address": "408 Backend Rd",
        "city": "Abeokuta",
        "state": "Ogun",
        "zipcode": "110001",
        "country": "Nigeria",
        "profile_bio": "Backend developer with Django expertise",
        "homepage_link": "https://samueldev.com",
        "facebook_link": "https://facebook.com/samueldev",
        "instagram_link": "https://instagram.com/samueldev",
        "linkedin_link": "https://linkedin.com/in/samueldev",
        "x_link": "https://x.com/samueldev"
    },
    {
        "username": "flora_uiux",
        "first_name": "Flora",
        "last_name": "Uiux",
        "email": "flora@example.com",
        "phone": "+2348008888888",
        "address": "509 UX Street",
        "city": "Calabar",
        "state": "Cross River",
        "zipcode": "540001",
        "country": "Nigeria",
        "profile_bio": "UX/UI designer passionate about accessibility",
        "homepage_link": "https://florauiux.com",
        "facebook_link": "https://facebook.com/florauiux",
        "instagram_link": "https://instagram.com/florauiux",
        "linkedin_link": "https://linkedin.com/in/florauiux",
        "x_link": "https://x.com/florauiux"
    },
    {
        "username": "tobi_crypto",
        "first_name": "Tobi",
        "last_name": "Crypto",
        "email": "tobi@example.com",
        "phone": "+2348009999999",
        "address": "601 Blockchain Ave",
        "city": "Ilorin",
        "state": "Kwara",
        "zipcode": "240001",
        "country": "Nigeria",
        "profile_bio": "Blockchain and crypto trader",
        "homepage_link": "https://tobicrypto.com",
        "facebook_link": "https://facebook.com/tobicrypto",
        "instagram_link": "https://instagram.com/tobicrypto",
        "linkedin_link": "https://linkedin.com/in/tobicrypto",
        "x_link": "https://x.com/tobicrypto"
    },
    {
        "username": "grace_robot",
        "first_name": "Grace",
        "last_name": "Robot",
        "email": "grace@example.com",
        "phone": "+2348010000000",
        "address": "702 Robotics Way",
        "city": "Uyo",
        "state": "Akwa Ibom",
        "zipcode": "520001",
        "country": "Nigeria",
        "profile_bio": "Robotics engineer building autonomous systems",
        "homepage_link": "https://gracerobot.com",
        "facebook_link": "https://facebook.com/gracerobot",
        "instagram_link": "https://instagram.com/gracerobot",
        "linkedin_link": "https://linkedin.com/in/gracerobot",
        "x_link": "https://x.com/gracerobot"
    }
    # Add 8 more users with different data
]

# Creating users and profiles
# Creating users and profiles
for data in sample_users:
    user, created = User.objects.get_or_create(username=data["username"], email=data["email"])
    if created:
        user.set_password("password123")  # Default password
        user.first_name = data["first_name"]
        user.last_name = data["last_name"]
        user.save()

    profile, created = Profile.objects.get_or_create(
        user=user,
        phone=data["phone"],
        address=data["address"],
        city=data["city"],
        state=data["state"],
        zipcode=data["zipcode"],
        country=data["country"],
        profile_bio=data["profile_bio"],
        homepage_link=data.get("homepage_link", ""),
        facebook_link=data.get("facebook_link", ""),
        instagram_link=data.get("instagram_link", ""),
        linkedin_link=data.get("linkedin_link", ""),
        x_link=data.get("x_link", ""),
    )

print("✅ User profiles seeded successfully!")

