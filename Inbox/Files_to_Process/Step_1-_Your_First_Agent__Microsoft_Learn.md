---
source_file: "Step_1-_Your_First_Agent__Microsoft_Learn.pdf"
title: "Step 1- Your First Agent | Microsoft Learn"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: 42b1878c52cf918c5a81c7cd4e04d5c6dd80a612f4e64cf3013b5f26c601a81a
has_content: true
---

# Step 1- Your First Agent | Microsoft Learn
Step 1: Your First Agent
Create an agent and get a response — in just a few
lines of code.
Bash
Create and run an agent:
Python
Python
pip install agent-framework azure-iden‐
tity
client = FoundryChatClient(
    project_endpoint="https://your-pro‐
ject.services.ai.azure.com",
    model="gpt-4o",
    credential=AzureCliCredential(),
)
agent = Agent(
    client=client,
    name="HelloAgent",
    instructions="You are a friendly as‐
sistant. Keep your answers brief.",
)
# Non-streaming: get the complete re‐
sponse at once
result = await agent.run("What is the
capital of France?")
print(f"Agent: {result}")
https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent?pivots=programming-language-python 7/16/26, 4:32 PM
Page 1 of 3

Or stream the response:
Python
# Streaming: receive tokens as they are
generated
print("Agent (streaming): ", end="",
flush=True)
async for chunk in agent.run("Tell me a
one-sentence fun fact.", stream=True):
    if chunk.text:
        print(chunk.text, end="",
flush=True)
print()
７ Note
Agent Framework does not automatically load
.env files. To use a .env file for configuration,
call load_dotenv() at the start of your script:
Python
Alternatively, set environment variables directly
in your shell or IDE. See the settings migration
note for details.
from dotenv import load_dotenv
load_dotenv()
 Tip
See the full sample for the complete
https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent?pivots=programming-language-python 7/16/26, 4:32 PM
Page 2 of 3

Go deeper:
Agents overview — understand agent
architecture
Providers — see all supported providers
Last updated on 07/10/2026
runnable file.
Next steps
Step 2: Add Tools
https://learn.microsoft.com/en-us/agent-framework/get-started/your-first-agent?pivots=programming-language-python 7/16/26, 4:32 PM
Page 3 of 3

---
Source file: Step_1-_Your_First_Agent__Microsoft_Learn.pdf
