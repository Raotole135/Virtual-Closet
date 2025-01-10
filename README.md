**AI Virtual Closet and Stylist Chatbot**

Project Overview

This project is a web-based application that combines AI-powered image processing and a chatbot to create a Virtual Closet and an AI Stylist. Users can upload images of outfits, classify clothing items (e.g., shirts, pants, dresses), and receive tailored styling recommendations through a conversational chatbot. The goal is to simplify personal wardrobe management and provide expert-like fashion advice using artificial intelligence.

Key Deliverables

A working prototype of the AI Virtual Closet and Stylist Chatbot, demonstrating end-to-end functionality.

This README file, which includes:

The problem solved by the project.

The tools, frameworks, and algorithms used.

Instructions to run the solution.

Optional: A brief (1-2 minute) video demo to showcase the functionality and user interaction.

Problem Solved

The project addresses two main challenges in personal fashion management:

Clothing Classification: Automating the process of identifying and categorizing clothing items from user-uploaded images.

Traditional methods require manual sorting and tagging, which is time-consuming.

Styling Recommendations: Offering personalized fashion advice for outfits, including tips for improvement and accessory suggestions.

Conventional methods rely on human expertise, which is not always accessible or cost-effective.

This solution bridges the gap between manual wardrobe management and AI-driven styling, making fashion advice and digital closet organization accessible to all users.

Tools, Frameworks, and Algorithms Used

Backend

Flask: Lightweight and efficient web framework for backend development.

Rembg: Python library for background removal from images, allowing precise clothing extraction.

Transformers: Hugging Face library used for implementing Vision Transformer (ViT) and GPT models.

Waitress/Gunicorn: Production-grade WSGI servers for serving the application.

Frontend

HTML, CSS, JavaScript: For designing a responsive and user-friendly interface.

Deployment

Render: A modern cloud platform chosen for its free tier, ease of integration, and scalability.

Algorithms

Vision Transformer (ViT): Utilized for image classification to identify upper and lower clothing items dynamically.

GPT-2: Fine-tuned for generating natural and engaging styling recommendations based on classified clothing items.

Setup Instructions

1. Clone the Repository

git clone https://github.com/<your-username>/AI_Virtual_Closet.git
cd AI_Virtual_Closet

2. Install Dependencies

Install all necessary Python libraries using:

pip install -r requirements.txt

3. Run the Application Locally

On Windows:

Run the application using waitress, which is compatible with Windows:

waitress-serve --port=5000 application:app

On Linux/Mac:

Run the application using gunicorn:

gunicorn -w 4 -b 0.0.0.0:5000 application:app

(Due to free tier plan the ports are limited and hence model can't be deployed for long time. It does work but due to limited resource not deployed on render)
![image](https://github.com/user-attachments/assets/bd57e984-0dae-4ffa-8c2d-c071c2bce1ff)

4. Visit the App

Access the application in your web browser at:

http://127.0.0.1:5000

Evaluation Criteria

1. Technical Feasibility

The solution effectively processes uploaded images to extract clothing items and provides styling advice dynamically.

2. Creativity

Combines cutting-edge AI technologies like Vision Transformer and GPT for seamless integration of image processing and conversational recommendations.

3. Scalability

Designed to handle multiple users and can be extended to integrate with e-commerce platforms or mobile applications for broader usability.

4. User Experience

The application provides a visually appealing and intuitive interface, ensuring a smooth user experience with interactive features.

Future Improvements

Enhanced Classification:

Fine-tune the Vision Transformer model with a custom dataset for better accuracy in identifying specific clothing types (e.g., formal vs. casual).

Advanced Chatbot:

Replace GPT-2 with a more advanced model like GPT-4 for richer and more context-aware recommendations.

Mobile Compatibility:

Develop a mobile application to enhance accessibility and user convenience.

Shopping Integration:

Include features to search for similar clothing items online and provide direct shopping links to users.

Outfit Suggestions:

Enable the chatbot to suggest complete outfits based on the user's existing virtual closet.


Credits

Pre-trained Models: Hugging Face Transformers.

Deployment: Render.com for hosting and serving the application.

Background Removal: Rembg library for seamless clothing extraction.

Contact

For queries or suggestions, please contact:

Name: Omkar Raotole

Email: omkarraotole135@gmail.com


