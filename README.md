Weather Forecast App
This is a web application that allows users to get astronomical weather forecasts for a specific city by providing the city name and their email address. The application utilizes Django, Celery, Redis, and RabbitMQ to deliver accurate and timely astronomical weather data to users' emails.

How to Use
Clone the repository to your local machine.
Install the required dependencies by running pip install -r requirements.txt.
Make sure you have Redis and RabbitMQ installed and running on your machine.
Set up your email configuration in the Django settings to enable email sending.
Run the Django development server using python manage.py runserver.
Access the application in your web browser at http://localhost:8000.
Enter the desired city name and your email address in the provided input fields.
Click the "Get Weather Forecast" button to request the astronomical weather data.
The Celery task will be triggered to fetch the data from the Weather API in the background.
You will receive the astronomical weather forecast in your email shortly after the task completes.
Technologies Used
Django: The web framework used to build the application.
Celery: Used for asynchronous task processing to fetch weather data in the background.
Redis: Acts as the result backend for Celery, storing task results.
RabbitMQ: The message broker for communication between the Django application and Celery worker.
RapidAPI (weatherapi-com.p.rapidapi.com): The API used to fetch astronomical weather data.
Project Structure
The main components of the project are organized as follows:


Contributing
If you find any issues or have suggestions for improvement, please feel free to open an issue or submit a pull request. Your contributions are welcome and appreciated.

License
This project is licensed under the MIT License - see the LICENSE file for details.
