from flask import Flask, render_template, request
from dotenv import load_dotenv

from agents.planner import PlannerAgent
from agents.executor import ExecutorAgent
from agents.verifier import VerifierAgent

load_dotenv()

app = Flask(__name__)

planner = PlannerAgent()
executor = ExecutorAgent()
verifier = VerifierAgent()

@app.route("/", methods=["GET", "POST"])
def index():
    plan = result = final_output = None

    if request.method == "POST":
        task = request.form["task"]

        plan = planner.plan(task)
        result = executor.execute(plan)
        final_output = verifier.verify(result)

    return render_template(
        "index.html",
        plan=plan,
        result=result,
        final_output=final_output
    )

if __name__ == "__main__":
    app.run(debug=True)
