# Personal Portfolio Backend

This repository contains the backend code for my personal portfolio website. It's built using Django and Django Rest Framework.

## Setup

To set up the project locally, follow these steps:

1. Clone the repository: `git clone https://github.com/your-username/personal-portfolio-backend.git`
2. Navigate to the project directory: `cd personal-portfolio-backend`
3. Create a new virtual environment: `python3 -m venv env`
4. Activate the virtual environment: `source env/bin/activate` (for Linux/macOS) or `env\Scripts\activate` (for Windows)
5. Install the required dependencies: `pip install -r requirements.txt`
6. Make a serverless Database using Neon DB https://neon.tech/docs/guides/django
7. Run the database migrations: `python manage.py migrate`
8. Load the initial data: `python manage.py loaddata projects.json`
9. Start the development server: `python manage.py runserver`

The API will be available at `http://localhost:8000/api/`.

## Endpoints

The following endpoints are available:

- `/api/projects/`: Returns a list of all projects.

## Running the Django Application with Docker

To run the Django application using Docker, follow these steps:

## Running the Django Application with Docker

To run the Django application using Docker, follow these steps:

1. Build the Docker image:

```
    sudo docker build -t django-app .
```

2. Run the Docker container:

```
    sudo docker run -p 8000:8000 django-app
```

This command will start the Docker container and map port 8000 from the container to port 8000 on your host machine.

3. Access the Django application:
Once the Docker container is running, you can access the Django application by opening your web browser and navigating to `http://localhost:8000`.

Note: If you are using Docker on a remote server, replace `localhost` with the IP address or hostname of the server.

4. To stop the Docker container, use the following command:
```
    sudo docker stop <container_id>
```


Replace `<container_id>` with the ID or name of the running container. You can find the container ID by running `sudo docker ps` command.

That's it! You now have the Django application running inside a Docker container.



## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
