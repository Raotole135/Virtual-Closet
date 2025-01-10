**AI Virtual Closet and Stylist Chatbot**

Project Overview

This project is a web-based application that combines AI-powered image processing and a chatbot to create a Virtual Closet and an AI Stylist. Users can upload images of outfits, classify clothing items (e.g., shirts, pants, dresses), and receive tailored styling recommendations through a conversational chatbot.

Key Features

Virtual Closet:

Extracts and separates upper and lower clothing items from uploaded images.

Classifies clothing items using a pre-trained Vision Transformer (ViT) model.

Displays processed images with dynamic labels for each clothing item.

AI Stylist Chatbot:

Provides detailed feedback on the uploaded outfit.

Suggests improvements, complementary accessories, and styling tips.

Uses pre-trained GPT-based models for generating natural language responses.

Web Interface:

User-friendly design with sections for image upload, processed results, and chatbot interactions.

Responsive layout for better usability.

Technologies Used

Backend

Flask: Web framework for backend functionality.

Rembg: Background removal for clothing images.

Transformers: Hugging Face library for Vision Transformer and GPT models.

Waitress/Gunicorn: Production WSGI servers.

Frontend

HTML, CSS, JavaScript: For a clean and interactive user interface.

Deployment

Render: For hosting the web application.

Challenges and Decisions

1. Image Processing:

Tried: Vision Transformer for image classification.

Challenges:

Pre-trained models required additional fine-tuning for specific clothing categories.

High computational costs for real-time image classification on large datasets.

Solution: Used a lightweight pre-trained Vision Transformer model from Hugging Face for acceptable performance.

2. AI Chatbot:

Tried:

OpenAI's gpt-4 and gpt-3.5-turbo.

Alternatives like Cohere and AI21 Labs.

Challenges:

OpenAI's models incurred high costs for frequent API usage.

Alternative APIs (Cohere/AI21) had latency issues and limited free usage quotas.

Solution: Used Hugging Face's GPT-2 model for generating stylist recommendations locally.

3. Deployment:

Tried:

Gunicorn: Incompatible with Windows during local development due to fcntl dependency.

AWS EC2: Time-consuming setup with limited scalability for quick iterations.

Solution: Deployed on Render, leveraging its free tier and simple GitHub integration.

Setup Instructions

1. Clone the Repository

git clone https://github.com/<your-username>/AI_Virtual_Closet.git
cd AI_Virtual_Closet

2. Install Dependencies

pip install -r requirements.txt

3. Run the Application Locally

On Windows:

waitress-serve --port=5000 application:app

On Linux/Mac:

gunicorn -w 4 -b 0.0.0.0:5000 application:app

4. Visit the App

Open your browser and navigate to:

http://127.0.0.1:5000

Future Improvements

Enhanced Classification:

Fine-tune Vision Transformer with a custom dataset for improved clothing detection accuracy.

Advanced Chatbot:

Integrate gpt-4 or similar advanced models if budget and resources allow.

Mobile Compatibility:

Develop a mobile app with the same functionality for a broader audience.

Shopping Integration:

Search for similar clothing items online and provide shopping links.

Credits

Pre-trained Models: Hugging Face Transformers.

Deployment: Render.com. (Due to costing and free tier plan the model is not up i tried it on render but due to unavailability of ports its not able to deploy)

Background Removal: Rembg library.

Contact

For queries or suggestions, please contact:

Name: Omkar Raotole

Email: omkarraotole135@gmail.com


