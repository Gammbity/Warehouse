# Warehouse Management System

A Python-based Warehouse Management System (WMS) featuring a Command Line Interface (CLI) for managing products, warehouses, and users. The system supports two distinct roles: **Superuser** and **Admin**.

## Features

### Superuser
- **Manage Admins**: Create, view, update, and delete admin accounts.
- **Manage Warehouses**: Create, view, and delete warehouses.
- **Reports**: View system reports.

### Admin
- **Product Management**: Add, update, and delete products.
- **Inventory Monitoring**: View all products with automatic warnings for low stock (less than 5 items).
- **Search**: Search for products by name.
- **Transfers**: Transfer products between warehouses.
- **History**: View a history of actions performed in the system.

## Getting Started

### Prerequisites
- Python 3.x

### Running the Application
To start the application, run the `menu.py` file:

```bash
python menu.py
```

## Usage

Upon running the application, you will be presented with the main menu where you can choose to access the **Admin Panel** or **SuperUser Panel**.

### Default Credentials

**Superuser:**
- **Username:** `root`
- **Password:** `123`

**Admin:**
- **Username:** `yevgenevic`
- **Password:** `1`

## Project Structure

- `menu.py`: Main entry point of the application.
- `dastur_kodlari/`: Source code directory.
  - `alisher/`: Contains Superuser logic.
  - `shahzoda/`: Contains Admin logic.
- `dastur_kodlari/*/data/`: JSON files used for data storage (admins, warehouses, products, history).
