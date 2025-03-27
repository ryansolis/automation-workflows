# Automation Directory

## Project Overview
Automation Directory is a project showcasing automation workflows for different platforms. It consists of two main components:

- **Backend**: Built with FastAPI (Python) to handle API requests and data processing.
- **Frontend**: Built with React (TypeScript) for the user interface.

---

## 📌 Prerequisites
Ensure you have the following installed before proceeding:

- **Git** - [Download](https://git-scm.com/downloads)
- **Python (3.9+)** - [Download](https://www.python.org/downloads/)
- **Node.js (18+)** - [Download](https://nodejs.org/)
- **pip** (comes with Python)
- **Virtual Environment (venv)**
- **FastAPI & Dependencies**
- **React & Dependencies**

---

## 🚀 Setup Instructions

### 1️⃣ Clone the Repository
```sh
git clone https://github.com/ryansolis/automation-workflows.git
cd automation-workflows
```

### 2️⃣ Backend Setup (FastAPI)
```sh
cd backend
python -m venv venv  # Create virtual environment
source venv/bin/activate  # Activate venv (Mac/Linux)
venv\Scripts\activate  # Activate venv (Windows)

pip install -r requirements.txt  # Install dependencies
uvicorn main:app --reload  # Start FastAPI server
```
Backend will run at: `http://127.0.0.1:8000`

### 3️⃣ Frontend Setup (React + TypeScript)
```sh
cd ../frontend
npm install  # Install dependencies
npm run dev  # Start frontend
```
Frontend will be available at: `http://localhost:5173`

---

## 🛠️ Running the Project
1. Start the **backend** first:
   ```sh
   cd backend
   source venv/bin/activate  # or venv\Scripts\activate for Windows
   uvicorn main:app --reload
   ```
2. Then, start the **frontend**:
   ```sh
   cd frontend
   npm run dev
   ```

---


## 🤝 Contributing
1. Fork the repo
2. Create a new branch (`git checkout -b feature-branch`)
3. Commit your changes (`git commit -m "Added new feature"`)
4. Push to GitHub (`git push origin feature-branch`)
5. Open a Pull Request

---

## 📄 License
This project is licensed under the MIT License.

---

### 🔗 Links
- [Backend Docs](http://127.0.0.1:8000/docs) (Swagger UI)
- [Live Frontend](#) (If deployed)


