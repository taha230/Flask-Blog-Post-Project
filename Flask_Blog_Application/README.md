# Flask Blog Application

A comprehensive blog application built with Flask that provides user management, post creation, commenting, and interaction features.

## 🚀 Features

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

## 👥 User Roles

### Admin
- Full access to all features
- Can create, edit, and delete any post
- Can manage users
- Can view admin panel

### Author
- Can create, edit, and delete their own posts
- Can comment and like posts
- Can change their password

### Regular User
- Can comment and like posts
- Can change their password
- Cannot create or edit posts

## 🔧 Configuration

The application uses `config.py` for configuration settings:

```python
class Config:
    SECRET_KEY = 'dev'  # Use a stronger key in production
    SQLALCHEMY_DATABASE_URI = 'sqlite:///blog.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SALT_STRING = 'TAHAHAMEDANI'  # Salt for password hashing
```

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

## 🎯 API Endpoints

- `GET /` - Home page with all posts
- `GET/POST /login` - User login
- `GET /logout` - User logout
- `GET/POST /create` - Create new post
- `GET/POST /edit/<post_id>` - Edit existing post
- `POST /delete/<post_id>` - Delete post
- `GET/POST /admin/users` - Admin user management
- `GET/POST /change-password` - Change user password
- `GET /like/<post_id>/<action>` - Like/dislike post
- `POST /comment/<post_id>` - Add comment to post

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
