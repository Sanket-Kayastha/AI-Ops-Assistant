Setup Instructions:

Clone the given repository --> Create and activate virtual environment(if required) --> Install dependencies(pip install -r requirements.txt) -->
create (.env) file In this file provide two api keys (GROQ_API_KEY=your_groq_api_key_here and WEATHER_API_KEY=your_openweather_api_key_here)-->
open app.py file and in the terminal type(flask run) know app is Running on (http://127.0.0.1:5000) local host.

Environment Variables:

GROQ_API_KEY=your_groq_api_key_here
WEATHER_API_KEY=your_openweather_api_key_here

Architecture explanation:

Agents:

PlannerAgent --> It convert the user task into strict json formate, Its plan or decide which tool need to use either WeatherTool or QuotesTool or both required.
User task and required tool pass to groq llm .

ExecutorAgent --> It execute the tools. It fetch the tools and task required then match the coorect tool and provide task so that tools requests the task through 
their api url and return a precise output. Here, no llm call.

VerifierAgent --> It verifies the output. It Cleans, validates, and formats tool output. Ensure that the output is in valid json formate only.

Tools:

In this project i used two tools called quotes_tool and weather_tool.

quotes_tool --> Fetch random quotes. we provide a public API endpoint It returns a random quote.

weather_tool --> Fetch real time city weather.

List of Integrated API:

1. Groq LLM API
2. OpenWeather API
3. Quotes API

Prompts Example to test the system:

1.What is the weather of delhi
2.Give a inspirational quote
3.provide weather of mumbai and a emotional quote

Limitations/Tradeoff

1. Planner dependency: Planner relies on LLM to select correct tool.
2. If user not provide clear prompt then it may result to incorrect tool selections.
3. There is a need of json framework so that output must be precise in valid json formate.
4. No Persistent Memory there is no long term storage. Each request is stateless.



