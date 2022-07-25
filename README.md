An app template for large Flask applications with Flask-SQLAlchemy integration. The application has the following structure:

```
.
├── app
│   ├── extensions.py
│   ├── __init__.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models
│   │   ├── post.py
│   │   └── question.py
│   ├── posts
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── questions
│   │   ├── __init__.py
│   │   └── routes.py
│   └── templates
│       ├── base.html
│       ├── index.html
│       ├── posts
│       │   ├── categories.html
│       │   └── index.html
│       └── questions
│           └── index.html
├── config.py
```
