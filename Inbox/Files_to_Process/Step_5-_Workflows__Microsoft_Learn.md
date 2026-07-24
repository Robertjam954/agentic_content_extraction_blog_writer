---
source_file: "Step_5-_Workflows__Microsoft_Learn.pdf"
title: "Step 5- Workflows | Microsoft Learn"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: 4260002579fc5238b0517471643b37e609148957cbc19d19c4fefb04d4fb2158
has_content: true
---

# Step 5- Workflows | Microsoft Learn
Step 5: Workflows
Workflows let you chain multiple steps together —
each step processes data and passes it to the next.
Define workflow steps (executors) and connect them
with edges:
Python
# Step 1: A class-based executor that
converts text to uppercase
class UpperCase(Executor):
    def __init__(self, id: str):
        super().__init__(id=id)
    @handler
    async def to_upper_case(self, text:
str, ctx: WorkflowContext[str]) -> None:
        """Convert input to uppercase
and forward to the next node."""
        await ctx.send_message(text.up‐
per())
# Step 2: A function-based executor that
reverses the string and yields output
@executor(id="reverse_text")
async def reverse_text(text: str, ctx:
WorkflowContext[Never, str]) -> None:
    """Reverse the string and yield the
final workflow output."""
    await ctx.yield_output(text[::-1])
def create_workflow():
    """Build the workflow: UpperCase →
https://learn.microsoft.com/en-us/agent-framework/get-started/workflows?pivots=programming-language-python 7/16/26, 4:36 PM
Page 1 of 3

Build and run the workflow:
Python
Go deeper:
Workflows overview — understand workflow
architecture
Sequential workflows — linear step-by-step
patterns
reverse_text."""
    upper = UpperCase(id="upper_case")
    return WorkflowBuilder(start_execu‐
tor=upper).add_edge(upper, reverse_‐
text).build()
workflow = create_workflow()
events = await workflow.run("hello
world")
print(f"Output: {events.get_outputs()}")
print(f"Final state: {events.get_fi‐
nal_state()}")
 Tip
See the full sample for the complete
runnable file.
Next steps
Step 6: Agent Harness
https://learn.microsoft.com/en-us/agent-framework/get-started/workflows?pivots=programming-language-python 7/16/26, 4:36 PM
Page 2 of 3

Agents in workflows — using agents as
workflow steps
Last updated on 07/10/2026
https://learn.microsoft.com/en-us/agent-framework/get-started/workflows?pivots=programming-language-python 7/16/26, 4:36 PM
Page 3 of 3

---
Source file: Step_5-_Workflows__Microsoft_Learn.pdf
