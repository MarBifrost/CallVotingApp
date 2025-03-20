# Call Voting App

## Description

Call Voting App is a Django-based application that retrieves call data from a MySQL database and presents statistics about calls. It features a custom authentication system with restricted access based on IP filtering and user authentication. Only registered users can log in and access the main statistics page.

## Features

User Authentication: Custom login view with authentication validation.

IP-Based Authentication: Only specified IPs can authenticate.

Call Data Statistics: View the total number of calls for today and filter call statistics by number and date range.

MySQL Database: The application retrieves data from a MySQL database.

SQLite for User Authentication: Predefined users are stored in an SQLite database for login validation.

Security Measures: Only registered users can log in (redirect_authenticated_user = True), and unauthorized users receive a 404 error.

## Requirements

Install the required dependencies using:

requirements.txt includes:
  Django==5.1.5
  dnspython==2.7.0
  idna==3.10
  lightpick==0.0.1b0
  mysql-connector-python==9.2.0
  mysqlclient==2.2.7
  pycodestyle==2.12.1
  pymongo==4.11.1
  sniffio==1.3.1
  sqlparse==0.5.3
  typing_extensions==4.12.2
  tzdata==2025.1
  whitenoise==6.8.2


## Installation and Setup

    1. Clone the Repository

    2. Set Up Virtual Environment (Optional but Recommended)

    3. Install Dependencies

    4. Configure Database

    Ensure you have a MySQL database set up and update your settings.py accordingly:

    Run migrations:

    5. Create Superuser (For Admin Access)

    6. Run the Development Server

### Usage

#### Login Page

The app features a Custom Login View, where only registered users can log in.

Login credentials are validated using SQLite.

Users attempting to access the main page without authentication will receive a 404 error.

Only users from specific IP addresses are allowed to authenticate.

#### Main Page (Statistics)

Once logged in, users can access the statistics page to:

- View total call count for today.

- Filter calls by a specific number.

- Filter calls by date range.


Handles authentication and displays call statistics.

#### Access Control:

Users must be logged in.

Unauthorized users receive a 404 error.

#### Statistics Display:

Total number of calls for today.

Filter by called_number.

Filter by start_date and end_date.

#### Error Handling:

Users receive an error message if invalid input is provided.

#### Security Features

Login Required: Enforced using login_required.

IP-Based Authentication: Users can only log in from specified IPs.

Redirect Authenticated Users: Prevents already logged-in users from accessing the login page again.

### Future Improvements

Implement role-based access control (RBAC).

Add user activity logs.

Enhance UI/UX with a modern frontend framework.



## License

This project is licensed under the MIT License.

#### Contact

For questions or suggestions, contact the project maintainer at margaprindashvili@gmail.com.
