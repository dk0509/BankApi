# 🏦 Bank Branch API Server – Methodology

This project implements a RESTful API server using **Django** to provide data about Indian banks and their branches. Below is the method and thought process followed in solving the assignment:

---

## ✅ Problem Breakdown

The assignment required:
- Creating an API server in Python.
- Using given CSV/SQL files as data source.
- Either implementing GraphQL or REST endpoints.
- Serving bank and branch data via API.

---

## 🧩 Chosen Approach

### 1. **Framework Chosen**
- Selected **Django** since I have basic knowledge of it.

### 2. **Database Setup**
- Used the provided repository.
- Created two models: `Bank` and `Branch`.
- Bank and Branch are related via a ForeignKey.
- Data was imported into SQLite using a Django custom management command.

### 3. **CSV Import Logic**
- Wrote a command: `python manage.py load_data`
- Parsed each CSV row and used `bulk_create` to efficiently store data.
- Used `get_or_create()` during earlier iterations, then optimized with `bulk_create`.

### 4. **API Design**
Implemented two REST endpoints:

#### a. **GET /banks/**
Returns a list of all banks.

#### b. **GET /branches/<ifsc_code>/**
Returns branch and bank details for the given IFSC code.

Used `select_related()` to optimize DB joins for foreign key lookups. 

---

## 🧪 Testing
- Used Postman and browser to test endpoints.
- Verified multiple IFSC queries to ensure correctness.

---

## 📌 Summary
- Cleanly structured Django app.
- CSV file loaded into SQLite.
- Optimized data import and query performance.
- RESTful endpoints without using Django REST Framework.
- Followed all project instructions.

---

## ⏱ Time Taken
Total estimated time spent: **4 hours**  

---

## 🚀 How to Use

### 1. **Clone the Repository**
```bash
git clone https://github.com/dk0509/BankApi
cd BankApi
```

### 2. **Install Django** (if not already installed)
```bash
pip install django
```

### 3. **Apply Migrations**
```bash
python manage.py migrate
```

### 4. **Load the Data**
```bash
python manage.py load_data
```

### 5. **Start the Server**
```bash
python manage.py runserver
```

### 6. **API Endpoints**

#### 🔹 List of Banks
- URL: `http://127.0.0.1:8000/banks/`

#### 🔹 Branch Details by IFSC
- URL: `http://127.0.0.1:8000/branches/<ifsc_code>/`

Example:  
```http
http://127.0.0.1:8000/branches/ABHY0065001/
```

---
