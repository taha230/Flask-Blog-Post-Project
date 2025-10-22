# Flask Blog Application

A comprehensive blog application built with Flask that provides user management, post creation, commenting, and interaction features.

This project is based on the original code from <a href=alihamidzadeh/Web-Application-with-Flask>
 and has been modified to fix bugs and improve functionality.


<div align="center" style="margin-bottom:30px;">
 <img width="1340" height="839" alt="Screenshot from 2025-10-22 14-06-18" src="https://github.com/user-attachments/assets/fea20e25-df5c-4ea9-bb1f-0b89db3fc163" />
</div>
<br><br> <!-- add more <br> if you need more space -->


## 📝 Features

### User Management
- **User Registration & Authentication**: Secure user registration and login system
- **Role-Based Access Control**: Three user roles - Admin, Author, and Regular User
- **Password Security**: MD5 hashing with salt for enhanced password security
- **Change Password**: Users can update their passwords securely
- **Admin User Management**: Admins can view and manage all users

### Post Management
- **Create Posts**: Authors and admins can create new blog posts
- **Edit Posts**: Users can edit their own posts (admins can edit any post)
- **Delete Posts**: Users can delete their own posts (admins can delete any post)
- **Post Display**: Clean, responsive post display with author information

### Interaction Features
- **Like/Dislike System**: Users can like or dislike posts
- **Comments**: Users can comment on posts
- **Comment Management**: Users can view and interact with comments

### Security Features
- **CSRF Protection**: Built-in CSRF protection using Flask-WTF
- **Session Management**: Secure session handling
- **Role-Based Permissions**: Different access levels for different user types
- **Password Hashing**: Secure password storage with salt

## 🛠️ Technology Stack

- **Backend**: Flask 2.3.2
- **Database**: SQLite with SQLAlchemy ORM
- **Forms**: Flask-WTF for form handling and validation
- **Templates**: Jinja2 templating engine
- **Security**: CSRF protection, password hashing

## 📁 Project Structure

```
Flask_Blog_Application/
├── app/
│   ├── __init__.py          # Flask app initialization
│   ├── models.py            # Database models (User, Post, Comment, PostLike)
│   ├── routes.py            # Application routes and views
│   ├── forms.py             # WTForms for form handling
│   ├── auth.py              # Authentication utilities
│   └── templates/           # HTML templates
│       ├── base.html        # Base template
│       ├── index.html       # Home page
│       ├── login.html       # Login page
│       ├── create_post.html # Create post form
│       ├── edit_post.html   # Edit post form
│       ├── change_password.html # Change password form
│       └── admin_users.html # Admin user management
├── config.py                # Configuration settings
├── createUser.py           # User creation utility
├── run.py                  # Application entry point
├── requirements.txt        # Python dependencies
└── instance/
    └── blog.db            # SQLite database
```

## 🚀 Installation & Setup

### Prerequisites
- Python 3.7+
- pip (Python package installer)

### Installation Steps

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd Flask_Blog_Application
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python run.py
   ```

5. **Access the application**
   Open your browser and navigate to `http://localhost:5000`

## 🧪 User Roles

| Role    | Permissions |
|---------|-------------|
| `admin` | Manage users, posts, and can access security-sensitive features |
| `author` | Create and edit their own posts |
| `normal` | Can read, comment, like/dislike posts |


## 🔧 Configuration

The application uses `config.py` for configuration settings:

```python
class Config:
    SECRET_KEY = 'dev'  # Use a stronger key in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SALT_STRING = 'TAHAHAMEDANI'  # Salt for password hashing
```

## 🛡 Password Hashing Logic

```python
hashlib.md5((raw_password + f"{user.id}Ferdowsi").encode()).hexdigest()
```

- Uses MD5 + static salt pattern SALT_STRING
- Based on `user.id`, making hashes unique per user

## 📊 Database Models

### User Model
- `id`: Primary key
- `username`: Unique username
- `password`: Hashed password with salt
- `role`: User role (admin, author, user)

### Post Model
- `id`: Primary key
- `title`: Post title
- `content`: Post content
- `author_id`: Foreign key to User

### Comment Model
- `id`: Primary key
- `content`: Comment text
- `post_id`: Foreign key to Post
- `user_id`: Foreign key to User

### PostLike Model
- `id`: Primary key
- `post_id`: Foreign key to Post
- `user_id`: Foreign key to User
- `value`: Like/dislike value

## 🔐 Security Features

- **Password Hashing**: MD5 with salt for secure password storage
- **CSRF Protection**: Flask-WTF provides CSRF tokens for all forms
- **Session Management**: Secure session handling
- **Role-Based Access**: Different permissions for different user types

## 🌐 URLs

| Route | Purpose |
|-------|---------|
| `/` | Homepage with posts |
| `/login` | Login page |
| `/logout` | Logout |
| `/create` | New post (author/admin) |
| `/admin/users` | Manage users (admin only) |
| `/instance` | Intentionally exposed directory |

---

## 🚀 Getting Started

1. **Create your first user** using the `createUser.py` script:
   ```bash
   python createUser.py
   ```

2. **Login** with your credentials

3. **Start creating posts** and interacting with the blog!

## 📝 Usage Examples

### Creating a Post
1. Login as an author or admin
2. Navigate to `/create`
3. Fill in the title and content
4. Submit the form

### Adding Comments
1. View any post on the home page
2. Scroll to the comments section
3. Add your comment and submit

### Liking Posts
1. Click the like/dislike buttons on any post
2. Your interaction will be recorded

## 🔧 Development

### Adding New Features
1. Update models in `app/models.py`
2. Add routes in `app/routes.py`
3. Create templates in `app/templates/`
4. Update forms in `app/forms.py` if needed

### Database Migrations
The application uses SQLAlchemy for database management. Database changes require updating the models and recreating the database.

## 📄 License

This project is open source and available under the MIT License.

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## 📞 Contact

**Taha Hamedani**  
Email: taha.hamedani8@gmail.com

For questions, suggestions, or collaboration opportunities, please don't hesitate to reach out!
