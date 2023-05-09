# Personal Portfolio Backend

This repository contains the backend code for my personal portfolio website. It's built using Django and Django Rest Framework.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/personal-portfolio-backend.git`
2. Navigate to the project directory: `cd personal-portfolio-backend`
3. Create a new virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (for Linux/macOS) or `env\Scripts\activate` (for Windows)
5. Install the required dependencies: `pip install -r requirements.txt`
6. Create a new PostgreSQL database and update the database credentials in `personal_portfolio/settings.py`
7. Run the database migrations: `python manage.py migrate`
8. Load the initial data: `python manage.py loaddata projects.json`
9. Start the development server: `python manage.py runserver`

The API will be available at `http://localhost:8000/api/`.

## Endpoints

The following endpoints are available:

- `/api/projects/`: Returns a list of all projects.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
