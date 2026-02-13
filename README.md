# Fit Friend: AI-Powered Wellness Dashboard

## Overview
Fit Friend is a dual-mode AI consultant designed to simplify healthy living. It leverages Large Language Models (LLMs) to provide instant, personalized nutrition advice and workout programming. 

Unlike basic chatbots, Fit Friend uses **Session State Segregation** to maintain independent conversation histories for nutrition and fitness, ensuring a clean and focused user experience.

## Technical Power-Ups
This project highlights advanced AI application development skills:
* **Stateful Memory Management:** Implemented custom dictionary-based session states in Streamlit to keep "Recipe" and "Workout" contexts separate.
* **Inference Speed:** Powered by **Groq** using the **Llama 3.3 70B** model, achieving sub-second response times.
* **Prompt Engineering:** Developed domain-specific system prompts for "Expert Chef" and "Weight Training Specialist" personas.
* **Modular OOP:** Built with a clean Class-based structure in Python for high maintainability.

## Project Architecture
```text
fit-friend/
├── app.py              # Advanced Streamlit UI (Sidebar, Chat Buffers)
├── fit_friend.py    # WellnessBot Logic & Groq Integration
├── .env                # API Credentials (Protected)
└── requirements.txt    # Dependency Manifest
```

## To get and run the project
### Clone & Install:

Bash

```pip install -r requirements.txt```

Set API Key: Add your GROQ_API_KEY to the .env file.

### Launch:

Bash

```streamlit run app.py```
