-- ============================================
-- 1. Insert Subjects
-- ============================================
INSERT INTO courses_subject (title, slug) VALUES
('Python Programming', 'python-programming'),
('Web Development', 'web-development'),
('Data Science', 'data-science'),
('Database Design', 'database-design'),
('Machine Learning', 'machine-learning'),
('Mobile Development', 'mobile-development'),
('DevOps & Cloud', 'devops-cloud'),
('Cybersecurity', 'cybersecurity'),
('UI/UX Design', 'ui-ux-design'),
('Software Engineering', 'software-engineering');

-- ============================================
-- 2. Insert Courses (owner_id = 1)
-- ============================================
INSERT INTO courses_course (title, slug, overview, created_at, owner_id, subject_id) VALUES
('Python Fundamentals', 'python-fundamentals',
 'Learn the basics of Python programming, including syntax, data types, control flow, functions, and object-oriented programming. Perfect for beginners who want to start their coding journey.',
 '2024-01-15 10:00:00', 1, 1),

('Advanced Python Techniques', 'advanced-python-techniques',
 'Take your Python skills to the next level with decorators, generators, context managers, metaclasses, and asynchronous programming patterns.',
 '2024-01-20 11:30:00', 1, 1),

('Django Web Development', 'django-web-development',
 'Build robust, scalable web applications with Django. Covers models, views, templates, forms, authentication, and deployment best practices.',
 '2024-02-01 09:15:00', 1, 2),

('Modern JavaScript & React', 'modern-javascript-react',
 'Master modern JavaScript (ES6+) and build interactive user interfaces with React. Includes hooks, state management, and component architecture.',
 '2024-02-10 14:00:00', 1, 2),

('Data Analysis with Pandas', 'data-analysis-pandas',
 'Learn to manipulate, analyze, and visualize data using the Pandas library. Covers DataFrames, Series, merging, grouping, and time series analysis.',
 '2024-02-18 08:45:00', 1, 3),

('Introduction to Machine Learning', 'introduction-machine-learning',
 'Understand the core concepts of machine learning, including supervised and unsupervised learning, model evaluation, and popular algorithms.',
 '2024-03-01 12:00:00', 1, 5),

('SQL & Relational Databases', 'sql-relational-databases',
 'Master SQL from basic queries to advanced joins, subqueries, indexing, and database normalization. Includes MySQL and PostgreSQL examples.',
 '2024-03-08 10:30:00', 1, 4),

('Flutter Mobile App Development', 'flutter-mobile-app-development',
 'Build cross-platform mobile applications with Flutter and Dart. Covers widgets, state management, navigation, and API integration.',
 '2024-03-15 16:20:00', 1, 6),

('Docker & Kubernetes Essentials', 'docker-kubernetes-essentials',
 'Learn containerization with Docker and orchestration with Kubernetes. Covers images, containers, pods, services, and CI/CD pipelines.',
 '2024-03-22 13:10:00', 1, 7),

('Ethical Hacking & Penetration Testing', 'ethical-hacking-penetration-testing',
 'Explore cybersecurity fundamentals, vulnerability assessment, and ethical hacking techniques used to secure modern systems.',
 '2024-04-01 09:00:00', 1, 8);

-- ============================================
-- 3. Insert Modules
-- ============================================

-- Course 1: Python Fundamentals (course_id = 1)
INSERT INTO courses_module (title, description, course_id) VALUES
('Getting Started with Python', 'Install Python, set up your IDE, and write your first program.', 1),
('Variables and Data Types', 'Understand integers, floats, strings, booleans, and type conversion.', 1),
('Control Flow', 'Learn if/else statements, loops, and logical operators.', 1),
('Functions and Modules', 'Define functions, use parameters, and organize code into modules.', 1),
('Object-Oriented Programming', 'Classes, objects, inheritance, and encapsulation in Python.', 1);

-- Course 2: Advanced Python Techniques (course_id = 2)
INSERT INTO courses_module (title, description, course_id) VALUES
('Decorators and Closures', 'Write reusable code with decorators and understand closures.', 2),
('Generators and Iterators', 'Master lazy evaluation with generators and custom iterators.', 2),
('Context Managers', 'Use the with statement and build your own context managers.', 2),
('Metaclasses and Descriptors', 'Dive deep into Python internals and advanced class customization.', 2),
('Async Programming', 'Learn asyncio, coroutines, and concurrent programming patterns.', 2);

-- Course 3: Django Web Development (course_id = 3)
INSERT INTO courses_module (title, description, course_id) VALUES
('Django Setup and Project Structure', 'Install Django, create a project, and understand the MVT architecture.', 3),
('Models and Databases', 'Define models, run migrations, and interact with the ORM.', 3),
('Views and URLs', 'Create function-based and class-based views with URL routing.', 3),
('Templates and Static Files', 'Build dynamic HTML pages with Django templates.', 3),
('Authentication and Authorization', 'Implement user login, registration, and permissions.', 3);

-- Course 4: Modern JavaScript & React (course_id = 4)
INSERT INTO courses_module (title, description, course_id) VALUES
('ES6+ Features', 'Arrow functions, destructuring, spread operators, and template literals.', 4),
('React Fundamentals', 'Components, props, state, and JSX syntax.', 4),
('React Hooks', 'useState, useEffect, useContext, and custom hooks.', 4),
('State Management', 'Context API, Redux, and Zustand for managing application state.', 4),
('Routing and API Integration', 'React Router and fetching data from REST APIs.', 4);

-- Course 5: Data Analysis with Pandas (course_id = 5)
INSERT INTO courses_module (title, description, course_id) VALUES
('Introduction to Pandas', 'Series, DataFrames, and basic operations.', 5),
('Data Cleaning', 'Handle missing values, duplicates, and data type conversions.', 5),
('Data Transformation', 'Merging, joining, grouping, and pivoting data.', 5),
('Time Series Analysis', 'Work with datetime indexes, resampling, and rolling windows.', 5),
('Data Visualization', 'Create charts with Matplotlib and Seaborn from Pandas data.', 5);

-- Course 6: Introduction to Machine Learning (course_id = 6)
INSERT INTO courses_module (title, description, course_id) VALUES
('ML Fundamentals', 'Types of learning, datasets, and the ML workflow.', 6),
('Supervised Learning', 'Linear regression, logistic regression, and decision trees.', 6),
('Unsupervised Learning', 'Clustering with K-means and dimensionality reduction with PCA.', 6),
('Model Evaluation', 'Cross-validation, confusion matrices, and performance metrics.', 6),
('Introduction to Neural Networks', 'Perceptrons, activation functions, and a simple neural network.', 6);

-- Course 7: SQL & Relational Databases (course_id = 7)
INSERT INTO courses_module (title, description, course_id) VALUES
('SQL Basics', 'SELECT, WHERE, ORDER BY, and LIMIT clauses.', 7),
('Joins and Relationships', 'INNER, LEFT, RIGHT, and FULL OUTER joins.', 7),
('Subqueries and CTEs', 'Write nested queries and common table expressions.', 7),
('Indexing and Performance', 'Understand indexes and query optimization.', 7),
('Database Design', 'Normalization, ER diagrams, and schema design principles.', 7);

-- Course 8: Flutter Mobile App Development (course_id = 8)
INSERT INTO courses_module (title, description, course_id) VALUES
('Dart Programming Basics', 'Variables, functions, and object-oriented Dart.', 8),
('Flutter Widgets', 'Stateless and stateful widgets, layout, and styling.', 8),
('Navigation and Routing', 'Navigate between screens and pass data.', 8),
('State Management', 'Provider, Riverpod, and BLoC patterns.', 8),
('API Integration', 'Fetch and display data from REST APIs.', 8);

-- Course 9: Docker & Kubernetes Essentials (course_id = 9)
INSERT INTO courses_module (title, description, course_id) VALUES
('Docker Fundamentals', 'Images, containers, volumes, and Dockerfiles.', 9),
('Docker Compose', 'Multi-container applications with docker-compose.', 9),
('Kubernetes Basics', 'Pods, deployments, services, and kubectl.', 9),
('Scaling and Networking', 'ReplicaSets, ingress, and service discovery.', 9),
('CI/CD Pipelines', 'Automate builds and deployments with GitHub Actions.', 9);

-- Course 10: Ethical Hacking & Penetration Testing (course_id = 10)
INSERT INTO courses_module (title, description, course_id) VALUES
('Cybersecurity Fundamentals', 'CIA triad, threat models, and security principles.', 10),
('Reconnaissance and Scanning', 'Information gathering with Nmap and OSINT tools.', 10),
('Vulnerability Assessment', 'Identify and analyze security weaknesses.', 10),
('Exploitation Techniques', 'Common attack vectors and exploitation frameworks.', 10),
('Reporting and Remediation', 'Document findings and recommend fixes.', 10);
