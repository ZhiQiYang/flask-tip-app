import sys
import os
from flask import Flask, request, render_template_string

# 加入使用者安裝的模組路徑（這段根據你環境調整）
sys.path.append(os.path.expanduser("~/Library/Mobile Documents/com~apple~CloudDocs/Documents/lib/python3.10/site-packages"))

app = Flask(__name__)

# HTML 模板字串
html_form = """
<!DOCTYPE html>
<html>
<head>
    <title>Tip Calculator</title>
</head>
<body>
    <h2>Tip Calculator</h2>
    <form method="get">
        <label>Bill Amount: <input type="number" name="bill" step="0.01" required></label><br><br>
        <label>Tip %: <input type="number" name="tip" step="0.1" required></label><br><br>
        <label>People: <input type="number" name="people" required></label><br><br>
        <button type="submit">Calculate</button>
    </form>
    {% if result %}
    <h3>Result:</h3>
    <p>Total: ${{ total }}</p>
    <p>Each person pays: ${{ share }}</p>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET"])
def home():
    bill = request.args.get("bill")
    tip = request.args.get("tip")
    people = request.args.get("people")

    if bill and tip and people:
        try:
            bill = float(bill)
            tip = float(tip)
            people = int(people)
            total = bill + (bill * tip / 100)
            share = round(total / people, 2)
            return render_template_string(html_form, result=True, total=round(total, 2), share=share)
        except:
            return "Invalid input!"
    return render_template_string(html_form, result=False)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)