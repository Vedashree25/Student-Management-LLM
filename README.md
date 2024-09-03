<<<<<<< HEAD
# Student-Management-LLM
The primary goal of this project is to create a Student Management System that is connected with a Large Language Model (LLM) agent to address questions from students and book-related queries. The frontend of the system is either constructed with FastAPI or Streamlit, while the backend is an LLM agent.

## Features

- An agent that follows instructions to answer queries about books or related topics.
- Based on the student's inquiry, or recommends books, papers, and articles.
- Responds to enquiries to encourage further communication.

## Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/Vedashree25/Student-Management-LLM.git
   cd Student-Management-LLM
=======
# Student Management using LLM

## Overview

The item being developed is a student management system that uses an LLM (large language model) to recommend books and respond to enquiries from students. It can be deployed on Firebase and has a frontend built with Streamlit.

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

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Streamlit](https://streamlit.io/)
- [Transformers by Hugging Face](https://huggingface.co/transformers/)
- [Firebase](https://firebase.google.com/)
>>>>>>> origin/main
