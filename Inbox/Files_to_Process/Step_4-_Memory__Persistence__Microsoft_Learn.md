---
source_file: "Step_4-_Memory__Persistence__Microsoft_Learn.pdf"
title: "Step 4- Memory & Persistence | Microsoft Learn"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: b836222c22144a491efc8e848c2aa981d06c1fe09d125bb51faff504090dfe1d
has_content: true
---

# Step 4- Memory & Persistence | Microsoft Learn
Step 4: Memory
& Persistence
Add context to your agent so it can remember user
preferences, past interactions, or external
knowledge.
Define a context provider that stores user info in
session state and injects personalization
instructions:
Python
class UserMemoryProvider(Context‐
Provider):
    """A context provider that remembers
user info in session state."""
    DEFAULT_SOURCE_ID = "user_memory"
    def __init__(self):
        super().__init__(self.DEFAULT_‐
SOURCE_ID)
    async def before_run(
        self,
        *,
        agent: Any,
        session: AgentSession | None,
        context: SessionContext,
https://learn.microsoft.com/en-us/agent-framework/get-started/memory?pivots=programming-language-python 7/16/26, 4:36 PM
Page 1 of 6

Create an agent with the context provider:
        state: dict[str, Any],
    ) -> None:
        """Inject personalization in‐
structions based on stored user info."""
        user_name = state.get("user_‐
name")
        if user_name:
            context.extend_instructions(
                self.source_id,
                f"The user's name is
{user_name}. Always address them by
name.",
            )
        else:
            context.extend_instructions(
                self.source_id,
                "You don't know the
user's name yet. Ask for it politely.",
            )
    async def after_run(
        self,
        *,
        agent: Any,
        session: AgentSession | None,
        context: SessionContext,
        state: dict[str, Any],
    ) -> None:
        """Extract and store user info
in session state after each call."""
        for msg in context.input_mes‐
sages:
            text = msg.text if hasat‐
tr(msg, "text") else ""
            if isinstance(text, str) and
"my name is" in text.lower():
                state["user_name"] =
text.lower().split("my name is")
[-1].strip().split()[0].capitalize()
https://learn.microsoft.com/en-us/agent-framework/get-started/memory?pivots=programming-language-python 7/16/26, 4:36 PM
Page 2 of 6

Python
Run it — the agent now has access to the context:
Python
client = FoundryChatClient(
    project_endpoint="https://your-pro‐
ject.services.ai.azure.com",
    model="gpt-4o",
    credential=AzureCliCredential(),
)
agent = Agent(
    client=client,
    name="MemoryAgent",
    instructions="You are a friendly as‐
sistant.",
    context_providers=[UserMemory‐
Provider()],
)
session = agent.create_session()
# The provider doesn't know the user yet
— it will ask for a name
result = await agent.run("Hello! What's
the square root of 9?", session=session)
print(f"Agent: {result}\n")
# Now provide the name — the provider
stores it in session state
result = await agent.run("My name is Al‐
ice", session=session)
print(f"Agent: {result}\n")
# Subsequent calls are personalized —
name persists via session state
result = await agent.run("What is 2 +
2?", session=session)
print(f"Agent: {result}\n")
https://learn.microsoft.com/en-us/agent-framework/get-started/memory?pivots=programming-language-python 7/16/26, 4:36 PM
Page 3 of 6

# Inspect session state to see what the
provider stored
provider_state = session.s‐
tate.get("user_memory", {})
print(f"[Session State] Stored user
name: {provider_state.get('user_‐
name')}")
 Tip
See the full sample for the complete
runnable file.
７ Note
In Python, persistence/memory is handled by
ContextProvider and HistoryProvider
implementations. InMemoryHistoryProvider is
the built-in local, in-memory history provider.
RawAgent may auto-add
InMemoryHistoryProvider() in specific cases
(for example, when using a session with no
configured context providers and no service-
side storage indicators), but this is not
guaranteed in all scenarios. If you always want
local persistence, add an
InMemoryHistoryProvider explicitly. Also
make sure only one history provider has
load_messages=True, so you don't replay
multiple stores into the same invocation.
https://learn.microsoft.com/en-us/agent-framework/get-started/memory?pivots=programming-language-python 7/16/26, 4:36 PM
Page 4 of 6

You can also add an audit store by appending
another history provider at the end of the list of
context_providers with
store_context_messages=True:
Python
from agent_framework import InMemo‐
ryHistoryProvider
from agent_framework.mem0 import
Mem0ContextProvider
memory_store = InMemoryHistory‐
Provider(load_messages=True) # add
local history for a reused or seri‐
alized session
agent_memory = Mem0Context‐
Provider("user-memory", api_key=...,
agent_id="my-agent")  # add Mem0
provider for agent memory
audit_store = InMemoryHistory‐
Provider(
    "audit",
    load_messages=False,
    store_context_messages=True,  #
include context added by other
providers
)
agent = client.as_agent(
    name="MemoryAgent",
    instructions="You are a friendly
assistant.",
    context_providers=[memory_store,
agent_memory, audit_store],  # audit
store last
)
https://learn.microsoft.com/en-us/agent-framework/get-started/memory?pivots=programming-language-python 7/16/26, 4:36 PM
Page 5 of 6

Go deeper:
Persistent storage — store conversations in
databases
Chat history — manage chat history and
memory
Last updated on 07/10/2026
Next steps
Step 5: Workflows
https://learn.microsoft.com/en-us/agent-framework/get-started/memory?pivots=programming-language-python 7/16/26, 4:36 PM
Page 6 of 6

---
Source file: Step_4-_Memory__Persistence__Microsoft_Learn.pdf
