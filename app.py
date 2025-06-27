from flask import Flask, request, render_template, session, redirect, url_for, send_from_directory
from langchain_core.messages import HumanMessage
from main import react_graph
import os

app = Flask(__name__)
app.secret_key = 'supersecretkey'  # Needed for session
SCREENSHOT_DIR = os.path.abspath(".")

@app.route("/", methods=["GET", "POST"])
def index():
    if "chat_history" not in session:
        session["chat_history"] = []

    screenshot_file = None

    if request.method == "POST":
        command = request.form["command"]
        session["chat_history"].append({"role": "user", "text": command})

        response = react_graph.invoke({"messages": [HumanMessage(content=command)]})
        assistant_msg = ""

        for msg in response["messages"]:
            if isinstance(msg.content, str):
                if msg.content.lower().startswith("screenshot_") and msg.content.endswith(".png"):
                    screenshot_file = msg.content
                    assistant_msg = "screenshot saved"
                else:
                    assistant_msg = msg.content

        session["chat_history"].append({"role": "assistant", "text": assistant_msg})

        # Store the filename for the screenshot separately
        session["screenshot_file"] = screenshot_file

        return redirect(url_for("index"))

    return render_template(
        "index.html",
        chat_history=session["chat_history"],
        screenshot_file=session.get("screenshot_file")
    )


@app.route("/download/<filename>")
def download(filename):
    return send_from_directory(SCREENSHOT_DIR, filename, as_attachment=True)


@app.route("/clear")
def clear():
    session.clear()
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
