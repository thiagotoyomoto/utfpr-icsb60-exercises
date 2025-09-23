from pymongo import MongoClient
from documents.restaurant import Restaurant
from documents.address import Address
from documents.grade import Grade
from pprint import pprint

def main():
    client = MongoClient("mongodb://mongo:mongo@localhost:27017/")
    db = client["example"]
    collection = db["restaurants"]

    # Create fake address data
    fake_address = Address.of(
        building="456",
        coord=[-73.985130, 40.758896],
        street="Broadway",
        zipcode="10036"
    )

    # Create fake grade data
    fake_grades = [
        Grade.of(
            date="2024-01-15T00:00:00.000+00:00",
            grade="A",
            score=92.5
        ),
        Grade.of(
            date="2023-08-20T00:00:00.000+00:00", 
            grade="B",
            score=85.0
        ),
        Grade.of(
            date="2023-03-10T00:00:00.000+00:00",
            grade="A",
            score=88.7
        )
    ]

    new_restaurant = Restaurant.of(
        name="Tony's Authentic Italian Bistro",
        cuisine="Italian",
        borough="Manhattan",
        address=fake_address,
        grades=fake_grades,
        restaurant_id="123456"
    )

    collection.insert_one(new_restaurant.to_dict())

    fetched_document = collection.find_one({
        'restaurant_id': '123456'
    })

    if fetched_document:
        restaurant = Restaurant(fetched_document)
        pprint(restaurant.to_dict())
    else:
        print("No restaurant found.")

if __name__ == "__main__":
    main()
