# ITlan - Trainee & Course Management

![image](https://github.com/user-attachments/assets/3a40c413-d02e-43c1-a80d-78a54ef3e891)



## 📌 Project Overview
This project is part of the **ITlan** system and consists of two Django applications:
- **Trainee Management (`trainee_app`)**: Handles trainee information, including adding, updating, and deleting records.
- **Course Management (`course_app`)**: Manages courses, including their details and assignments.

Both apps are integrated with Django's authentication system and use Bootstrap for a modern UI. The project follows best practices in Django development, including the use of **class-based views**, **Django forms**, and **template inheritance**.

---

## 🏗️ Project Structure
```
ITlan/
│── ITlan/               # Main Django project
│   │── settings.py      # Project settings
│   │── urls.py          # Root URL configuration
│   │── wsgi.py          # WSGI entry point
│   │── asgi.py          # ASGI entry point
│
│── trainee_app/         # Trainee management app
│   │── models.py        # Trainee database models
│   │── views.py         # Trainee-related view functions
│   │── urls.py          # URL routing for trainees
│   │── forms.py         # Django forms for trainee input
│   │── templates/
│   │   ├── trainee_list.html      # Displays all trainees
│   │   ├── add_trainee.html       # Form to add a trainee
│   │   ├── update_trainee.html    # Form to update a trainee
│
│── course_app/          # Course management app
│   │── models.py        # Course database models
│   │── views.py         # Course-related view functions
│   │── urls.py          # URL routing for courses
│   │── forms.py         # Django forms for course input
│   │── templates/
│   │   ├── course_list.html       # Displays all courses
│   │   ├── add_course.html        # Form to add a course
│   │   ├── update_course.html     # Form to update a course
│
│── templates/           # Shared templates
│   │── base.html        # Base template with navbar and footer
│   │── home.html        # Welcome page
│
│── static/              # Static assets (CSS, JS, images)
│── manage.py            # Django management script
│── README.md            # Project documentation
```

---

## 🔥 Features
### 🧑‍🎓 Trainee Management (`trainee_app`)
- ✅ **View Trainees**: Displays a table of trainees with details.
- ✅ **Add Trainee**: Form to add a new trainee.
- ✅ **Update Trainee**: Modify trainee details using Django forms.
- ✅ **Delete Trainee**: Remove a trainee from the system.

### 📚 Course Management (`course_app`)
- ✅ **View Courses**: Displays a table of courses with descriptions.
- ✅ **Add Course**: Form to add a new course.
- ✅ **Update Course**: Modify course details.
- ✅ **Delete Course**: Remove a course from the system.

### 🔐 Authentication
- 🔹 **User Login**: Secure login system.
- 🔹 **User Logout**: Ends user sessions securely.
- 🔹 **User Registration**: Allows new users to sign up.

### 🌐 Navigation
- 🏫 **Trainee List**
- ➕ **Add Trainee**
- 📚 **Course List**
- ➕ **Add Course**
- 🔐 **Login/Logout**

---

## 🛠️ Setup Instructions
### **1️⃣ Clone the Repository**
```sh
git clone https://github.com/raghad-rgb/django-lab1.git
cd ITlan
```

### **2️⃣ Create a Virtual Environment**
```sh
python -m venv env
source env/bin/activate  # On Windows use `env\Scripts\activate`
```

### **3️⃣ Install Dependencies**
```sh
pip install -r requirements.txt
```

### **4️⃣ Apply Migrations**
```sh
python manage.py migrate
```

### **5️⃣ Create a Superuser**
```sh
python manage.py createsuperuser
```

### **6️⃣ Run the Development Server**
```sh
python manage.py runserver
```

### **7️⃣ Open the Browser and Visit**
```sh
http://127.0.0.1:8000/
```

---

## 📄 API Endpoints & URLs
| Route                         | Description              | HTTP Method |
|--------------------------------|--------------------------|------------|
| `/trainee/`                    | Trainee List            | `GET`      |
| `/trainee/add/`                | Add Trainee Form        | `GET, POST`|
| `/trainee/update/<id>/`        | Update Trainee          | `GET, POST`|
| `/trainee/delete/<id>/`        | Delete Trainee          | `POST`     |
| `/course/`                     | Course List             | `GET`      |
| `/course/add/`                 | Add Course Form         | `GET, POST`|
| `/course/update/<id>/`         | Update Course          | `GET, POST`|
| `/course/delete/<id>/`         | Delete Course          | `POST`     |

---

## 🏆 Credits
Developed by **Raghad Gamal** ❤️ Using **Django & Bootstrap** for a modern experience.

---

## 📝 License
This project is **open-source** and available under the **MIT License**.

---
### 🎉 **Happy Coding! 🚀**


