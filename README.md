
# Simple Password Generator

This is a modern and interactive password generator built with Streamlit. It allows users to create secure passwords with various customization options.

## Features
- Set password length (6–50 characters).
- Include uppercase letters, numbers, and special characters.
- Easy-to-use interface.
- One-click copy functionality.

## How to Run Locally
1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/password-generator.git
   cd password-generator
   ```
2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
3. Run the app:
   ```bash
   streamlit run app.py
   ```

## Deployment on Streamlit Community Cloud

Ensure the following files are in the repository for smooth deployment:
1. **`requirements.txt`**: Specifies Python dependencies.
2. **`packages.txt`**: Includes system-level dependencies.

Streamlit Community Cloud will automatically detect and install these dependencies during deployment.

To deploy:
1. Push your repository to GitHub.
2. Link the repository to Streamlit Community Cloud.
3. The app should run without issues.

## License
This project is licensed under the MIT License.
