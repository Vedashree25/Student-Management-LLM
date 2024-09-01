<<<<<<< HEAD
# Student-Management-LLM
This project is focused on developing a Student Management System integrated with a Large Language Model (LLM) agent to handle book-related inquiries and student questions. The system is built with a backend LLM agent and a frontend using either Streamlit or FastAPI.

## Features

- Instruction-based agent for responding to book or topic-related questions.
- Suggests or recommends books, papers, and articles based on the student's query.
- Follows up on questions for continued interaction.
- Proper code structure with separation across supervisor, adapter, and LLM layers.
- Logs user interactions for history tracking.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vedashree25/Student-Management-LLM.git
   cd Student-Management-LLM
=======
# Student Management System with LLM

## Project Overview

This project is a student management system that leverages a Large Language Model (LLM) to provide book recommendations and answer student queries. It uses Streamlit for the frontend and is deployable on Firebase.

## Features

- Instruction-based agent for book and student-related queries.
- Suggests answers and recommends books, papers, and articles based on queries.
- Logging of user interactions.

## Prerequisites

- Python 3.8+
- Node.js (for Firebase CLI)
- Firebase CLI
- Git

## Installation

1. **Clone the Repository**

    ```bash
    git clone https://github.com/Vedashree25/Student-Management-LLM.git
    cd Student-Management-LLM
    ```

2. **Set Up a Virtual Environment**

    ```bash
    python -m venv venv
    ```

3. **Activate the Virtual Environment**

      ```bash
      venv\Scripts\activate
      ```

4. **Install Dependencies**

    ```bash
    pip install -r requirements.txt
    ```

## Usage

1. **Run the Backend**

    ```bash
    python src/main.py
    ```

2. **Run the Frontend**

    ```bash
    streamlit run app.py
    ```

## Deployment to Firebase

1. **Install Firebase CLI**

    ```bash
    npm install -g firebase-tools
    ```

2. **Login to Firebase**

    ```bash
    firebase login
    ```

3. **Initialize Firebase in the Project**

    ```bash
    firebase init
    ```

    - Select Firebase Hosting and set up your public directory (e.g., `public`).
    - Choose "No" for configuring as a single-page app if it's not applicable.
    - Configure GitHub Action for deployment if you want.

4. **Deploy to Firebase**

    ```bash
    firebase deploy
    ```

## Logs

- Logs of user interactions are stored in `logs/user_interactions.log`.

## Contributing

If you'd like to contribute to this project, please follow these steps:

1. Fork the repository.
2. Create a feature branch (`git checkout -b feature/YourFeature`).
3. Commit your changes (`git commit -am 'Add new feature'`).
4. Push to the branch (`git push origin feature/YourFeature`).
5. Create a new Pull Request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Transformers by Hugging Face](https://huggingface.co/transformers/)
- [Firebase](https://firebase.google.com/)
>>>>>>> origin/main
