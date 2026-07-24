---
source_file: "Step_3-_Multi-Turn_Conversations__Microsoft_Learn.pdf"
title: "Step 3- Multi-Turn Conversations | Microsoft Learn"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: a18b9c6274d686a6b326468c88b7d0ee039eed7a230132314cd2ed975b66f041
has_content: true
---

# Step 3- Multi-Turn Conversations | Microsoft Learn
Step 3: Multi-Turn
Conversations
Use a session to maintain conversation context so
the agent remembers what was said earlier.
Use AgentSession to maintain context across
multiple calls:
Python
Python
client = FoundryChatClient(
    project_endpoint="https://your-pro‐
ject.services.ai.azure.com",
    model="gpt-4o",
    credential=AzureCliCredential(),
)
agent = Agent(
    client=client,
    name="ConversationAgent",
    instructions="You are a friendly as‐
sistant. Keep your answers brief.",
)
# Create a session to maintain conversa‐
tion history
session = agent.create_session()
# First turn
result = await agent.run("My name is Al‐
ice and I love hiking.", session=ses‐
sion)
https://learn.microsoft.com/en-us/agent-framework/get-started/multi-turn?pivots=programming-language-python 7/16/26, 4:34 PM
Page 1 of 2

Go deeper:
Multi-turn conversations — advanced
conversation patterns
Middleware — intercept and modify agent
interactions
Last updated on 07/10/2026
print(f"Agent: {result}\n")
# Second turn — the agent should remem‐
ber the user's name and hobby
result = await agent.run("What do you
remember about me?", session=session)
print(f"Agent: {result}")
 Tip
See the full sample for the complete
runnable file.
Next steps
Step 4: Memory & Persistence
https://learn.microsoft.com/en-us/agent-framework/get-started/multi-turn?pivots=programming-language-python 7/16/26, 4:34 PM
Page 2 of 2

---
Source file: Step_3-_Multi-Turn_Conversations__Microsoft_Learn.pdf
