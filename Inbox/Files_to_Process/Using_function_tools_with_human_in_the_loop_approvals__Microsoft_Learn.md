---
source_file: "Using_function_tools_with_human_in_the_loop_approvals__Microsoft_Learn.pdf"
title: "Using function tools with human in the loop approvals | Microsoft Learn"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: e81d84bffe7abaa449b6c88e599f4c773d3a0f1fa51f832ed2f5ef330641ea53
has_content: true
---

# Using function tools with human in the loop approvals | Microsoft Learn
Using function tools with
human in the
loop approvals
This tutorial step shows you how to use function
tools that require human approval with an agent.
When agents require any user input, for example to
approve a function call, this is referred to as a
human-in-the-loop pattern. An agent run that
requires user input, will complete with a response
that indicates what input is required from the user,
instead of completing with a final answer. The caller
of the agent is then responsible for getting the
required input from the user, and passing it back to
the agent as part of a new agent run.
For prerequisites and installing Python packages,
see the Create and run a simple agent step in this
tutorial.
When using functions, it's possible to indicate for
each function, whether it requires human approval
Prerequisites
Create the agent with function
tools requiring approval
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 1 of 13

before being executed. This is done by setting the
approval_mode parameter to "always_require"
when using the @tool decorator.
Here is an example of a simple function tool that
fakes getting the weather for a given location.
Python
To create a function that requires approval, you can
use the approval_mode parameter:
Python
When creating the agent, you can now provide the
from typing import Annotated
from agent_framework import tool
@tool
def get_weather(location: Annotated[str,
"The city and state, e.g. San Francisco,
CA"]) -> str:
    """Get the current weather for a
given location."""
    return f"The weather in {location}
is cloudy with a high of 15°C."
@tool(approval_mode="always_require")
def get_weather_detail(location: Anno‐
tated[str, "The city and state, e.g. San
Francisco, CA"]) -> str:
    """Get detailed weather information
for a given location."""
    return f"The weather in {location}
is cloudy with a high of 15°C, humidity
88%."
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 2 of 13

approval requiring function tool to the agent, by
passing a list of tools to the Agent constructor.
Python
Since you now have a function that requires
approval, the agent might respond with a request
for approval instead of executing the function
directly and returning the result. You can check the
response for any user input requests, which
indicates that the agent requires user approval for a
function.
Python
from agent_framework import Agent
from agent_framework.openai import Open‐
AIChatClient
async with Agent(
    client=OpenAIChatClient(),
    name="WeatherAgent",
    instructions="You are a helpful
weather assistant.",
    tools=[get_weather, get_weather_de‐
tail],
) as agent:
    # Agent is ready to use
    pass
result = await agent.run("What is the
detailed weather like in Amsterdam?")
if result.user_input_requests:
    for user_input_needed in re‐
sult.user_input_requests:
        if user_input_needed.function_‐
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 3 of 13

If there are any function approval requests, the
detail of the function call including name and
arguments can be found in the function_call
property on the user input request. This can be
shown to the user, so that they can decide whether
to approve or reject the function call.
Once the user has provided their input, you can
create a response using the
to_function_approval_response method on the
user input request. Pass True to approve the
function call, or False to reject it.
The response can then be passed to the agent in a
new Message, to get the result back from the agent.
Python
call is None:
            continue
        print(f"Function: {user_in‐
put_needed.function_call.name}")
        print(f"Arguments: {user_in‐
put_needed.function_call.arguments}")
from agent_framework import Message
# Get user approval (in a real applica‐
tion, this would be interactive)
user_approval = True  # or False to re‐
ject
# Create the approval response
approval_message = Message(
    role="user",
    contents=[user_input_needed.to_func‐
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 4 of 13

When working with multiple function calls that
require approval, you may need to handle approvals
in a loop until all functions are approved or rejected:
Python
tion_approval_response(user_approval)]
)
# Continue the conversation with the ap‐
proval
final_result = await agent.run([
    "What is the detailed weather like
in Amsterdam?",
    Message(role="assistant", contents=
[user_input_needed]),
    approval_message
])
print(final_result.text)
Handling approvals in a loop
async def handle_approvals(query: str,
agent) -> str:
    """Handle function call approvals in
a loop."""
    current_input = query
    while True:
        result = await agent.run(curren‐
t_input)
        if not result.user_input_re‐
quests:
            # No more approvals needed,
return the final result
            return result.text
        # Build new input with all con‐
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 5 of 13

Whenever you are using function tools with human
text
        new_inputs = [query]
        for user_input_needed in re‐
sult.user_input_requests:
            if user_input_needed.func‐
tion_call is None:
                continue
            print(f"Approval needed for:
{user_input_needed.function_call.name}")
            print(f"Arguments: {user_in‐
put_needed.function_call.arguments}")
            # Add the assistant message
with the approval request
            new_inputs.append(Mes‐
sage(role="assistant", contents=
[user_input_needed]))
            # Get user approval (in
practice, this would be interactive)
            user_approval = True  # Re‐
place with actual user input
            # Add the user's approval
response
            new_inputs.append(
                Message(role="user",
contents=[user_input_needed.to_func‐
tion_approval_response(user_approval)])
            )
        # Continue with all the context
        current_input = new_inputs
# Usage
result_text = await handle_ap‐
provals("Get detailed weather for Seat‐
tle and Portland", agent)
print(result_text)
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 6 of 13

in the loop approvals, remember to check for user
input requests in the response, after each agent run,
until all function calls have been approved or
rejected.
Python
Complete example
# Copyright (c) Microsoft. All rights
reserved.
import asyncio
from random import randrange
from typing import TYPE_CHECKING, Anno‐
tated, Any
from agent_framework import Agent, Agen‐
tResponse, Message, tool
from agent_framework.openai import Open‐
AIChatClient
if TYPE_CHECKING:
    from agent_framework import Support‐
sAgentRun
"""
Demonstration of a tool with approvals.
This sample demonstrates using AI func‐
tions with user approval workflows.
It shows how to handle function call ap‐
provals without using threads.
"""
conditions = ["sunny", "cloudy", "rain‐
ing", "snowing", "clear"]
# NOTE: approval_mode="never_require" is
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 7 of 13

for sample brevity. Use "always_require"
in production; see samples/02-
agents/tools/function_tool_with_ap‐
proval.py and samples/02-
agents/tools/function_tool_with_ap‐
proval_and_sessions.py.
@tool(approval_mode="never_require")
def get_weather(location: Annotated[str,
"The city and state, e.g. San Francisco,
CA"]) -> str:
    """Get the current weather for a
given location."""
    # Simulate weather data
    return f"The weather in {location}
is {conditions[randrange(0, len(condi‐
tions))]} and {randrange(-10, 30)}°C."
# Define a simple weather tool that re‐
quires approval
@tool(approval_mode="always_require")
def get_weather_detail(location: Anno‐
tated[str, "The city and state, e.g. San
Francisco, CA"]) -> str:
    """Get the current weather for a
given location."""
    # Simulate weather data
    return (
        f"The weather in {location} is
{conditions[randrange(0, len(condi‐
tions))]} and {randrange(-10, 30)}°C, "
        "with a humidity of 88%. "
        f"Tomorrow will be {condi‐
tions[randrange(0, len(conditions))]}
with a high of {randrange(-10, 30)}°C."
    )
async def handle_approvals(query: str,
agent: "SupportsAgentRun") -> AgentRe‐
sponse:
    """Handle function call approvals.
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 8 of 13

When we don't have a thread, we need
to ensure we include the original query,
    the approval request, and the ap‐
proval response in each iteration.
    """
    result = await agent.run(query)
    while len(result.user_input_re‐
quests) > 0:
        # Start with the original query
        new_inputs: list[Any] = [query]
        for user_input_needed in re‐
sult.user_input_requests:
            print(
                f"\nUser Input Request
for function from {agent.name}:"
                f"\n  Function:
{user_input_needed.function_call.name}"
                f"\n  Arguments:
{user_input_needed.function_call.argu‐
ments}"
            )
            # Add the assistant message
with the approval request
            new_inputs.append(Mes‐
sage("assistant", [user_input_needed]))
            # Get user approval
            user_approval = await asyn‐
cio.to_thread(input, "\nApprove function
call? (y/n): ")
            # Add the user's approval
response
            new_inputs.append(
                Message("user",
[user_input_needed.to_function_ap‐
proval_response(user_approval.lower() ==
"y")])
            )
        # Run again with all the context
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 9 of 13

result = await agent.run(new_in‐
puts)
    return result
async def handle_approvals_stream‐
ing(query: str, agent: "SupportsAgent‐
Run") -> None:
    """Handle function call approvals
with streaming responses.
    When we don't have a thread, we need
to ensure we include the original query,
    the approval request, and the ap‐
proval response in each iteration.
    """
    current_input: str | list[Any] =
query
    has_user_input_requests = True
    while has_user_input_requests:
        has_user_input_requests = False
        user_input_requests: list[Any] =
[]
        # Stream the response
        async for chunk in agen‐
t.run(current_input, stream=True):
            if chunk.text:
                print(chunk.text,
end="", flush=True)
            # Collect user input re‐
quests from the stream
            if chunk.user_input_re‐
quests:
                user_input_requests.ex‐
tend(chunk.user_input_requests)
        if user_input_requests:
            has_user_input_requests =
True
            # Start with the original
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 10 of 13

query
            new_inputs: list[Any] =
[query]
            for user_input_needed in
user_input_requests:
                print(
                    f"\n\nUser Input Re‐
quest for function from {agent.name}:"
                    f"\n  Function:
{user_input_needed.function_call.name}"
                    f"\n  Arguments:
{user_input_needed.function_call.argu‐
ments}"
                )
                # Add the assistant mes‐
sage with the approval request
                new_inputs.append(Mes‐
sage("assistant", [user_input_needed]))
                # Get user approval
                user_approval = await
asyncio.to_thread(input, "\nApprove
function call? (y/n): ")
                # Add the user's ap‐
proval response
                new_inputs.append(
                    Message("user",
[user_input_needed.to_function_ap‐
proval_response(user_approval.lower() ==
"y")])
                )
            # Update input with all the
context for next iteration
            current_input = new_inputs
async def run_weather_agent_with_ap‐
proval(stream: bool) -> None:
    """Example showing AI function with
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 11 of 13

approval requirement."""
    print(f"\n=== Weather Agent with Ap‐
proval Required ({'Streaming' if stream
else 'Non-Streaming'}) ===\n")
    async with Agent(
        client=OpenAIChatClient(),
        name="WeatherAgent",
        instructions=("You are a helpful
weather assistant. Use the get_weather
tool to provide weather information."),
        tools=[get_weather, get_weath‐
er_detail],
    ) as agent:
        query = "Can you give me an up‐
date of the weather in LA and Portland
and detailed weather for Seattle?"
        print(f"User: {query}")
        if stream:
            print(f"\n{agent.name}: ",
end="", flush=True)
            await handle_approval‐
s_streaming(query, agent)
            print()
        else:
            result = await handle_ap‐
provals(query, agent)
            print(f"\n{agent.name}: {re‐
sult}\n")
async def main() -> None:
    print("=== Demonstration of a tool
with approvals ===\n")
    await run_weather_agent_with_ap‐
proval(stream=False)
    await run_weather_agent_with_ap‐
proval(stream=True)
if __name__ == "__main__":
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 12 of 13

Last updated on 07/10/2026
    asyncio.run(main())
Next steps
Code Interpreter
https://learn.microsoft.com/en-us/agent-framework/agents/tools/tool-approval?pivots=programming-language-python 7/16/26, 4:34 PM
Page 13 of 13

---
Source file: Using_function_tools_with_human_in_the_loop_approvals__Microsoft_Learn.pdf
