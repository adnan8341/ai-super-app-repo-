# OmniAI - Universal Multi-Model Mobile App

OmniAI is a production-ready mobile application built with **Flutter** and **FastAPI**. It features a smart AI router that automatically switches between OpenAI, Google Gemini, DeepSeek, and Grok (xAI) based on the user's task.

## 🚀 Key Features
- **Multi-Model Routing:** Automatic model selection for Coding, Research, or Logic.
- **Cross-Platform:** Single codebase for Android & iOS using Flutter.
- **Cloud-Synced:** Firebase/Supabase integration for chat history and profiles.
- **Security First:** API keys are never exposed; all processing happens via the FastAPI proxy.

## 🛠 Tech Stack
- **Frontend:** Flutter (Riverpod for state management)
- **Backend:** FastAPI (Python 3.10+)
- **Database:** Firebase Firestore / Supabase
- **Auth:** Firebase Auth (Email & Google)
- **AI APIs:** GPT-4, Gemini Pro, DeepSeek-V3, Grok-1

## 📦 Installation & Setup

### Backend
1. `cd backend`
2. `python -m venv venv`
3. `source venv/bin/activate` (or `venv\Scripts\activate` on Windows)
4. `pip install -r requirements.txt`
5. Create a `.env` file based on `.env.example`.
6. `uvicorn app.main:app --reload`

### Frontend
1. `cd frontend`
2. `flutter pub get`
3. Update `api_service.dart` with your local or hosted backend URL.
4. `flutter run`

## ⚖️ License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
