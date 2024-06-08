# Simple Clock Web Application

```markdown

This is a Simple Clock web application built with web2py, providing both digital and analog clock displays with dynamic background changes based on the time of day. Users can select their preferred time zone from a list of options.

![Simple Clock Demo](demo.gif)

## Features

- **Dual Clock Display**: Digital and analog clock formats for convenience.
- **Time Zone Selection**: Users can choose their preferred time zone from a list of options.
- **Dynamic Backgrounds**: The background changes based on the time of day, providing a visually appealing experience.

## Tech Stack

- **Backend**: Python
  - **Framework**: web2py
- **Frontend**: HTML, CSS, JavaScript

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/yourusername/simple-clock-web2py.git
   ```

2. Change directory to the project folder:

   ```bash
   cd simple-clock-web2py
   ```

3. Install web2py:

   ```bash
   pip install web2py
   ```

4. Run the web2py server:

   ```bash
   python web2py.py -a 'your_admin_password' -p 8000
   ```

5. Open your web browser and go to `http://127.0.0.1:8000/simple-clock-web2py`.

## Code Overview

The project structure is organized as follows:

- `applications/`: Contains the web2py application.
- `applications/simple-clock-web2py/`: Main application directory.
  - `controllers/`: Contains the Python controllers for routing and handling requests.
  - `models/`: Contains the Python models defining the data structure.
  - `views/`: Contains the HTML views for rendering the user interface.
  - `static/`: Contains static files such as CSS, JavaScript, and images.
- `web2py.py`: Main script to run the web2py server.

## Usage

- Select your preferred time zone from the dropdown list.
- Enjoy the dual clock display and watch as the background changes dynamically based on the time of day.

## Contributing

Contributions are welcome! Please feel free to submit a pull request or open an issue if you have any suggestions, bug reports, or feature requests.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
```

This README.md file provides users with more detailed information about the code structure, frameworks used, and how to install and use the Simple Clock Web Application project.
