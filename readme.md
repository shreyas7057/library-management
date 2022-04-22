# Library Management System Project

<!-- Technologies Used -->
Backend: Python(Django)
Frontend: HTML5, CSS3, Bootstrap
Database: MySQL

The project was to perform operations like CRUD. User will signup or login as admin who can add books, view all books, update books and delete books.

As we needed to signup using email so we create custom user model. As Django comes with default authentication system which as default login field as username. But we changed it to email address. 

Then we created 2 tables in books app. One table was Author and another was Book. The relation between Book table and Author table was Many Books and One Author. So we used author as foreign key in book table.


For Book and Author we created functions for CRUD operations. 

To store data we used MySQL as database. MySQL is Relational Database so it stored all data in row and column format. 

Also, Django comes with sqlite3 as default database but we changed it to MySQL. We used mysqlclient library to connect MySQL to Django. 


Urls:
    path('admin/', admin.site.urls),
    
    # urls for frontend used in HTML and CSS
    path('accounts/',include('accounts.urls')),
    path('',include('books.urls')),

    # default api ui provided by DRF
    path('api/',include('books.api.urls')),

    # API with swagger library
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
