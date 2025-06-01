# ALX Travel App (0x00)

A Django-based travel application with REST API, Swagger documentation, and database seeding.

## Setup Instructions

1. **Clone the Repository**:
   ```bash
   git clone https://github.com/your-username/alx_travel_app_0x00.git
   cd alx_travel_app_0x00
   ```

2. **Set Up Virtual Environment**:
   ```bash
   python3.12 -m venv venv
   source venv/bin/activate
   ```

3. **Install Dependencies**:
   Install MySQL dependencies:
   ```bash
   sudo apt-get update
   sudo apt-get install python3-dev default-libmysqlclient-dev build-essential pkg-config
   ```
   Install Python dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment**:
   Create a `.env` file in the project root with:
   ```
   SECRET_KEY=your-secret-key-here
   DEBUG=True
   DB_NAME=alx_travel_db
   DB_USER=your-mysql-user
   DB_PASSWORD=your-mysql-password
   DB_HOST=localhost
   DB_PORT=3306
   ```

5. **Set Up MySQL Database**:
   ```bash
   mysql -u root -p -e "CREATE DATABASE alx_travel_db;"
   ```

6. **Run Migrations**:
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

7. **Seed the Database**:
   ```bash
   python manage.py seed
   ```

8. **Run the Server**:
   ```bash
   python manage.py runserver
   ```
   Access the API documentation at `http://localhost:8000/swagger/`.

## Project Structure
- `listings/models.py`: Defines `Listing`, `Booking`, and `Review` models.
- `listings/serializers.py`: Serializers for `Listing` and `Booking` models.
- `listings/management/commands/seed.py`: Management command to seed the database.

## Database Seeding
Run `python manage.py seed` to populate the database with sample users, listings, bookings, and reviews.
