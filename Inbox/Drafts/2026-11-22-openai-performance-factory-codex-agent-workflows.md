=== DRY RUN (no API call) ===

Retrieved 8 chunks for topic: 'OpenAI Performance Factory: how Codex-powered agent workflows find and fix performance issues to keep ChatGPT fast'
  [0.863] How OpenAI’s Performance Factory keeps ChatGPT fast (web: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
  [0.750] How OpenAI’s Performance Factory keeps ChatGPT fast (web: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
  [0.725] How OpenAI’s Performance Factory keeps ChatGPT fast (web: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
  [0.695] How OpenAI’s Performance Factory keeps ChatGPT fast (web: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
  [0.625] How OpenAI’s Performance Factory keeps ChatGPT fast (web: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
  [0.589] How OpenAI’s Performance Factory keeps ChatGPT fast (web: https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
  [0.579] Set up a context engineering flow in VS Code (doc: context-engineering-workflow.md)
  [0.578] Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps | Microsoft Foundry Blog (brief: attachment)

Would call model: claude-sonnet-5

--- assembled content object (user message) ---
INPUT OBJECT START:

Content Topic
OpenAI Performance Factory: how Codex-powered agent workflows find and fix performance issues to keep ChatGPT fast

Hook/Introduction
(none - craft one from the topic and key insights)

Key Insights
- How OpenAI’s Performance Factory keeps ChatGPT fast: # How OpenAI’s Performance Factory keeps ChatGPT fast > Learn how OpenAI built the Performance Factory, a system of Codex-powered workflows that finds and fixes performance issues to help keep ChatGPT fast.
- Set up a context engineering flow in VS Code: ompounding errors and maintains working code. **Separate concerns**: Use different agents for different activities (planning versus implementation versus review) to maintain focused, relevant context.
- Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps | Microsoft Foundry Blog: ards. • For AutoGen users: • AutoGen pioneered many orchestration patterns (GroupChat, GraphFlow, event- driven runtimes), which are now unified in Agent Framework under the Workflow abstraction.

SEO Keywords
openai, performance, factory, codex-powered, agent, workflows, find, issues, keep, chatgpt, fast, keeps

Source Video
(none found in the index)

Content Type
Blog Post

Summary Transcript
[web] How OpenAI’s Performance Factory keeps ChatGPT fast (https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
# How OpenAI’s Performance Factory keeps ChatGPT fast > Learn how OpenAI built the Performance Factory, a system of Codex-powered workflows that finds and fixes performance issues to help keep ChatGPT fast. November 19, 2026 [Engineering](/news/engineering/) # How OpenAI’s Performance Factory keeps ChatGPT fast Our Codex-powered system automates finding and fixing performance issues.

[web] How OpenAI’s Performance Factory keeps ChatGPT fast (https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
in a rapidly changing environment. With the Performance Factory, what an engineer learns from one slowdown can shape how we investigate and fix the next one, even months later in a different service. Next time you’re using ChatGPT and notice a slowdown, there’s a good chance the Performance Factory is already figuring out why.

[web] How OpenAI’s Performance Factory keeps ChatGPT fast (https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
ll share how our use of Codex evolved into what’s now the Performance Factory, walk through our first running workflow, and share early lessons from building and running agent workflows in production. ## The path from manual investigations to automated workflows As we used Codex for more of our performance work, we noticed a progression in how our team worked.

[web] How OpenAI’s Performance Factory keeps ChatGPT fast (https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
Gregg, Pieter Hooimeijer, Nick Cooper, and Louis Brandy.

[web] How OpenAI’s Performance Factory keeps ChatGPT fast (https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
ns at an unprecedented speed. The Performance Factory, which runs in the cloud and automates investigating and resolving performance problems, enables us to keep pace with the ambition of our roadmap. In the Performance Factory, our engineers define workflows for recurring jobs and write instructions for the Codex agents that carry them out.

[web] How OpenAI’s Performance Factory keeps ChatGPT fast (https://openai.com/index/how-openai-performance-factory-keeps-chatgpt-fast)
regressions in ChatGPT’s first token latency—we built advanced tools, like CPU and allocation profilers, to make those investigations easier. Over time, we accumulated more than 30 performance tools. **2. Codex as a partner** . Once we had **** Codex as a partner, engineers could ask, “Why did this get slower?” and work with Codex to investigate, even in an unfamiliar system.

[doc] Set up a context engineering flow in VS Code (context-engineering-workflow.md)
ompounding errors and maintains working code. **Separate concerns**: Use different agents for different activities (planning versus implementation versus review) to maintain focused, relevant context. **Version your context**: Use git to track changes to your context engineering setup, allowing you to revert problematic changes and understand what works best.

[brief] Introducing Microsoft Agent Framework: The Open-Source Engine for Agentic AI Apps | Microsoft Foundry Blog (attachment)
ards. • For AutoGen users: • AutoGen pioneered many orchestration patterns (GroupChat, GraphFlow, event- driven runtimes), which are now unified in Agent Framework under the Workflow abstraction. • The AssistantAgent maps directly to the new ChatAgent, which is multi-turn by default and continues tool invocation until a result is ready.

Status
Draft
INPUT OBJECT FINISH.

WRITTEN BLOG START:

