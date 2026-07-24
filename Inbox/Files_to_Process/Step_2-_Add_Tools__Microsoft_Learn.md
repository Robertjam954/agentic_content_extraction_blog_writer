---
source_file: "Step_2-_Add_Tools__Microsoft_Learn.pdf"
title: "Step 2- Add Tools | Microsoft Learn"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: 8e06144ab39ada29e0ba41b1dbcf426755c89cb2623da1cd41cf373dbf81f73a
has_content: true
---

# Step 2- Add Tools | Microsoft Learn
Step 2: Add Tools
Tools let your agent call custom functions — like
fetching weather data, querying a database, or
calling an API.
Define a tool with the @tool decorator:
Python
Create an agent with the tool:
Python
# NOTE: approval_mode="never_require" is
for sample brevity.
# Use "always_require" in production for
user confirmation before tool execution.
@tool(approval_mode="never_require")
def get_weather(
    location: Annotated[str, Field(de‐
scription="The location to get the
weather for.")],
) -> str:
    """Get the weather for a given loca‐
tion."""
    conditions = ["sunny", "cloudy",
"rainy", "stormy"]
    return f"The weather in {location}
is {conditions[randint(0, 3)]} with a
high of {randint(10, 30)}°C."
agent = Agent(
    client=client,
    name="WeatherAgent",
https://learn.microsoft.com/en-us/agent-framework/get-started/add-tools?pivots=programming-language-python 7/16/26, 4:32 PM
Page 1 of 2

Go deeper:
Tools overview — learn about all available tool
types
Function tools — advanced function tool
patterns
Tool approval — human-in-the-loop for tool
calls
Last updated on 07/10/2026
    instructions="You are a helpful
weather agent. Use the get_weather tool
to answer questions.",
    tools=[get_weather],
)
 Tip
See the full sample for the complete
runnable file.
Next steps
Step 3: Multi-Turn Conversations
https://learn.microsoft.com/en-us/agent-framework/get-started/add-tools?pivots=programming-language-python 7/16/26, 4:32 PM
Page 2 of 2

---
Source file: Step_2-_Add_Tools__Microsoft_Learn.pdf
