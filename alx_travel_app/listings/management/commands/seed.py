from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from listings.models import Listing, Booking, Review
from datetime import date, timedelta
from decimal import Decimal
import random

class Command(BaseCommand):
    help = 'Seeds the database with sample data for listings, bookings, and reviews'

    def handle(self, *args, **kwargs):
        self.stdout.write(self.style.SUCCESS('Starting database seeding...'))

        # Create users
        users = []
        for i in range(5):
            username = f'user{i+1}'
            if not User.objects.filter(username=username).exists():
                user = User.objects.create_user(
                    username=username,
                    email=f'user{i+1}@example.com',
                    password='password123'
                )
                users.append(user)
            else:
                users.append(User.objects.get(username=username))

        # Create listings
        listings = []
        sample_listings = [
            {
                'title': 'Cozy Beachfront Cottage',
                'description': 'A charming cottage by the sea.',
                'location': 'Malibu, CA',
                'price_per_night': Decimal('150.00'),
                'max_guests': 4
            },
            {
                'title': 'Urban Loft Downtown',
                'description': 'Modern loft in the heart of the city.',
                'location': 'New York, NY',
                'price_per_night': Decimal('200.00'),
                'max_guests': 2
            },
            {
                'title': 'Mountain Retreat',
                'description': 'Secluded cabin with stunning views.',
                'location': 'Aspen, CO',
                'price_per_night': Decimal('250.00'),
                'max_guests': 6
            }
        ]

        for data in sample_listings:
            listing = Listing.objects.create(
                title=data['title'],
                description=data['description'],
                location=data['location'],
                price_per_night=data['price_per_night'],
                max_guests=data['max_guests'],
                owner=random.choice(users)
            )
            listings.append(listing)

        # Create bookings
        for listing in listings:
            for _ in range(random.randint(1, 3)):
                start_date = date.today() + timedelta(days=random.randint(1, 30))
                end_date = start_date + timedelta(days=random.randint(1, 7))
                days = (end_date - start_date).days
                total_price = listing.price_per_night * days
                Booking.objects.create(
                    listing=listing,
                    user=random.choice(users),
                    start_date=start_date,
                    end_date=end_date,
                    total_price=total_price,
                    status=random.choice(['pending', 'confirmed', 'cancelled'])
                )

        # Create reviews
        for listing in listings:
            for _ in range(random.randint(1, 2)):
                Review.objects.create(
                    listing=listing,
                    user=random.choice(users),
                    rating=random.randint(1, 5),
                    comment=f"This was a {random.choice(['great', 'wonderful', 'decent'])} stay!"
                )

        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))
