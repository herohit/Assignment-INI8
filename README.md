# Project Setup Guide

This README file provides instructions on how to set up and run the project locally on your machine. Please follow the steps below carefully.

## SQL Configuration
1. Install MySQL: Install MySQL from the community page.
2. Configure Database: Configure your local MySQL database with the following credentials:
```bash
        User: 'root'
        Password: 'qwerty@123'
        Host: 'localhost'
        Port: '3306'
```
3. Run SQL Script: After successfully installing and configuring MySQL, execute the SQL script named that is present in the git repository.
 ```bash 
sql_script_assignment.sql
 ```

## Files Configuration
1. Install Virtual Environment

```python
pip install virtualenv

```
2. Create Virtual Environment: Create a virtual environment using the following command:

```python
python -m venv env
```

3.Activate Virtual Environment: Navigate to the directory where the env folder is present and activate the virtual environment using the following command:

```python
.\env\Scripts\activate
```

4. Install Required Packages: Install the necessary packages from the requirements.txt file using the command:
```python
pip install -r requirements.txt
```

5.Download and Extract Repository: Download the git repository and extract it into the directory where the env folder is present.

6.Run Django Server: Navigate to the project_registration folder and run the following command in the terminal:
```python
python manage.py runserver
```

7.Access the Application: Once the server is running, open your web browser and go to the following address: http://127.0.0.1:8000/

Congratulations! You have successfully set up and launched the project locally on your machine. If you encounter any issues during the setup process, feel free to reach out for assistance.
