document.addEventListener("DOMContentLoaded", () => {
    const uploadForm = document.getElementById("uploadForm");
    const upperGrid = document.getElementById("upperGrid");
    const lowerGrid = document.getElementById("lowerGrid");
    const chatMessages = document.getElementById("chatMessages");
    const userInput = document.getElementById("userInput");
    const sendMessage = document.getElementById("sendMessage");

    /**
     * Append a message to the chatbot conversation window.
     */
    const appendMessage = (message, sender) => {
        const messageDiv = document.createElement("div");
        messageDiv.textContent = `${sender}: ${message}`;
        chatMessages.appendChild(messageDiv);
        chatMessages.scrollTop = chatMessages.scrollHeight; // Auto-scroll to the latest message
    };

    /**
     * Handle image upload and display processed results.
     */
    uploadForm.addEventListener("submit", async (event) => {
        event.preventDefault();

        const formData = new FormData(uploadForm);

        try {
            const response = await fetch("/upload", {
                method: "POST",
                body: formData,
            });

            if (response.ok) {
                const data = await response.json();

                // Display upper region
                upperGrid.innerHTML = "";
                const upperImg = document.createElement("img");
                upperImg.src = data.upper.image;
                upperImg.alt = data.upper.label;
                upperGrid.appendChild(upperImg);
                const upperLabel = document.createElement("p");
                upperLabel.textContent = data.upper.label;
                upperGrid.appendChild(upperLabel);

                // Display lower region
                lowerGrid.innerHTML = "";
                const lowerImg = document.createElement("img");
                lowerImg.src = data.lower.image;
                lowerImg.alt = data.lower.label;
                lowerGrid.appendChild(lowerImg);
                const lowerLabel = document.createElement("p");
                lowerLabel.textContent = data.lower.label;
                lowerGrid.appendChild(lowerLabel);

                // Notify the user
                appendMessage(
                    "Image processed successfully! You can now ask the AI Stylist about your outfit.",
                    "System"
                );
            } else {
                appendMessage("Error processing the image.", "System");
            }
        } catch (error) {
            console.error("Error during image upload:", error);
            appendMessage("An error occurred during image upload.", "System");
        }
    });

    /**
     * Handle chatbot interactions and send image labels for comments.
     */
    sendMessage.addEventListener("click", async () => {
        const message = userInput.value.trim();
        if (!message) return;

        // Append user's message to the chat
        appendMessage(message, "You");

        // Extract the labels for the upper and lower regions
        const upperLabel =
            document.querySelector("#upperGrid p")?.textContent || "Unknown";
        const lowerLabel =
            document.querySelector("#lowerGrid p")?.textContent || "Unknown";

        try {
            const response = await fetch("/chat", {
                method: "POST",
                headers: { "Content-Type": "application/json" },
                body: JSON.stringify({ upper_label: upperLabel, lower_label: lowerLabel }),
            });

            if (response.ok) {
                const data = await response.json();
                appendMessage(data.response, "AI Stylist");
            } else {
                appendMessage("Sorry, something went wrong.", "AI Stylist");
            }
        } catch (error) {
            console.error("Error during chatbot interaction:", error);
            appendMessage("An error occurred during chatbot interaction.", "System");
        }

        // Clear the user input field
        userInput.value = "";
    });
});
