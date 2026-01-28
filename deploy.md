# 🚀 Deployment Guide

This guide explains how to deploy the **Flask Backend** to Vercel and the **React Native Frontend** (as a web app) to Netlify or Vercel.

---

## 🏗 1. Backend Deployment (Vercel)

We will deploy the Flask API to VercelServerless Functions using the `vercel.json` configuration we created.

### Prerequisites
*   [Vercel CLI](https://vercel.com/docs/cli) installed (`npm i -g vercel`)
*   Vercel account

### Steps
1.  **Navigate to Backend:**
    ```bash
    cd backend
    ```

2.  **Deploy:**
    Run the following command:
    ```bash
    npx vercel
    ```
    **Follow the interactive prompts:**
    *   **Set up and deploy?** `yes`
    *   **Scope:** Select your account.
    *   **Link to existing project?** `no`
    *   **Project Name:** `internshala-backend` (MUST be lowercase!)
    *   **Directory:** `./` (Press Enter)

3.  **Environment Variables:**
    On your Vercel Project Dashboard > Settings > Environment Variables, add:
    *   `MONGO_URI`: Your MongoDB Atlas Connection String
    *   `JWT_SECRET_KEY`: A strong random string
    *   `PLAYBACK_TOKEN_SECRET`: Another strong random string

4.  **Get URL:**
    Vercel will give you a production URL (e.g., `https://your-project.vercel.app`).
    **Copy this URL.** You will need it for the frontend.

---

## 📱 2. Frontend Deployment (Web)

Since this is a React Native (Expo) app, we can export it as a static website and host it on Netlify or Vercel.

### Prerequisites
*   Install Web dependencies:
    ```bash
    cd frontend
    npx expo install react-dom react-native-web @expo/metro-runtime
    ```

*   Update `src/config/api.js`:
    Change `BASE_URL` to your **new Backend Vercel URL**.
    ```javascript
    // src/config/api.js
    const BASE_URL = 'https://your-backend-project.vercel.app'; 
    ```

### Option A: Deploy to Netlify (Recommended)
1.  **Build Website:**
    ```bash
    npx expo export --platform web
    ```
    This creates a `dist` folder.

2.  **Deploy:**
    *   **Drag & Drop:** Go to [Netlify Drop](https://app.netlify.com/drop) and drag the `dist` folder.
    *   **CLI:**
        ```bash
        npm install -g netlify-cli
        netlify deploy --prod --dir=dist
        ```

### Option B: Deploy to Vercel
1.  **Build:**
    ```bash
    npx expo export --platform web
    ```
2.  **Deploy:**
    ```bash
    vercel deploy dist
    ```

---

## 🧪 Verification
1.  Open your frontend URL.
2.  Sign up a new user.
3.  Ensure videos load (Dashboard) and play (Streaming).
