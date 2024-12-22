welcome_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Welcome to Q&A</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            background-color: #f0f4f8;
            margin: 0;
        }
        .container {
            text-align: center;
            background-color: #ffffff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 4px 10px rgba(0, 0, 0, 0.1);
        }
        input {
            padding: 10px;
            margin: 10px 0;
            width: 80%;
            border: 1px solid #ccc;
            border-radius: 4px;
        }
        button {
            padding: 10px 20px;
            background-color: #007BFF;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background-color: #0056b3;
        }
        .answer {
            margin-top: 20px;
            padding: 10px;
            background-color: #e9f7fe;
            border: 1px solid #bce0fd;
            border-radius: 4px;
            max-width: 80%;
            margin-left: auto;
            margin-right: auto;
        }
    </style>
</head>
<body>

    <div class="container">
        <h1>Welcome to Q&A</h1>
        <input type="text" id="user-question" placeholder="Ask a question..." />
        <button onclick="askQuestion()">Ask</button>
        <div class="answer" id="answer"></div>
    </div>

    <script>
        async function askQuestion() {
            const question = document.getElementById("user-question").value;
            if (!question) {
                alert("Please enter a question.");
                return;
            }

            const responseDiv = document.getElementById("answer");
            responseDiv.textContent = "Loading...";

            try {
                const response = await fetch("http://127.0.0.1:5001/ask", {
                    method: "POST",
                    headers: {
                        "Content-Type": "application/json",
                    },
                    body: JSON.stringify({ question })
                });

                const data = await response.json();
                responseDiv.textContent = data.answer || "Sorry, I couldn't find an answer.";
            } catch (error) {
                responseDiv.textContent = "Error: " + error.message;
            }
        }
    </script>

</body>
</html>

"""
