# Password Manager

| Build Status | License | Python Version |
|--------------|---------|----------------|
| ![Build Status](https://img.shields.io/badge/build-passing-brightgreen) | ![License](https://img.shields.io/badge/license-MIT-blue) | ![Python Version](https://img.shields.io/badge/python-3.x-blue) |

This is a simple password manager application built using Python and Tkinter. It allows users to generate strong passwords, save them securely, and search for saved passwords.

## Features

- **Password Generation**: Generates strong, random passwords with letters, numbers, and symbols.
- **Password Storage**: Saves passwords to a local JSON file.
- **Password Retrieval**: Searches for and retrieves passwords for specified websites.

## Requirements

- Python 3.x
- Tkinter (usually included with Python)
- JSON (Python standard library)

## Installation

1. **Clone the repository:**

   ```sh
   git clone https://github.com/yourusername/password-manager.git
   cd password-manager
   ```

2. **Install dependencies:**

   No additional dependencies are required apart from the standard Python library.

3. **Run the application:**

   ```sh
   python main.py
   ```

## Usage

1. **Generate a Password:**

   - Click on the "Generate" button to create a new random password.
   - The generated password will be displayed in the password field.

2. **Save a Password:**

   - Enter the website, email/username, and password in the respective fields.
   - Click the "Add" button to save the password.
   - If the fields are empty, a warning will be displayed.
   - Confirmation will be asked before saving the password.
   - The password will be saved to a file named `password.json`.

3. **Search for a Password:**

   - Enter the website name in the website field.
   - Click on the "Search" button.
   - If the website is found in the `password.json` file, the corresponding email and password will be displayed in a message box.
   - If the website is not found, a message box will notify that no data is stored for the website.

## File Structure

- `main.py`: The main script containing the application code.
- `password.json`: The JSON file where passwords are stored.
- `logo.png`: The logo image displayed in the application.

## Tag Details

| Tag  | Name       | Trigger Results                                      |
|------|------------|------------------------------------------------------|
| 1.0  | Initial Release | Basic functionality: generate, save, and search passwords |

## Screenshots
https://github.com/Girma35/Password-Manager/assets/143084812/7169d3fa-9d95-4231-bb79-07d1058896ba

## Contributing

If you have any suggestions or find any bugs, please feel free to create an issue or submit a pull request.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
