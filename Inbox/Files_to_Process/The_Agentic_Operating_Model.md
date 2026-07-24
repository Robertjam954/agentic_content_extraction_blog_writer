---
source_file: "The_Agentic_Operating_Model.pdf"
title: "The Agentic Operating Model"
ingested: 2026-07-24
type: pdf
source: attachment
sha256: f47dbe2d72a775f60b5c16355c96d599ab2bc6ae8d11f3ab2e70ca3d2596bda4
has_content: true
---

# The Agentic Operating Model
The Agentic
Operating Model
Aligning People, Process, and
Technology for Production AI at Scale
THE AGENTIC OPERATING MODEL
People · Process · Technology
PEOPLE
Platform Engineers
Agent Engineers
Non-Technical Builders
PROCESS
Build
Test
Deploy
Monitor
Iterate + Govern (continuous)
TECHNOLOGY
Agent Frameworks
Observability
Runtime
Platform
No-Code
Agents for Agents
GOVERNANCE  SECURITY FINOPS COMPLIANCE INTEROP
EBOOK • 01

THE AGENTIC OPERATING MODEL • TOC
T able of Contents
0.0
1.0
Foreword

Part I · People
The Three Rings: Who Builds, Who Adopts1.
The Three Disciplines: Hire and Reskill2.
3
5
5
8
2.0 Part II · Process
The Agent Development Lifecycle3.
Test in Depth4.
Deploy, Monitor, and Govern5.
10
10
12
14
3.0 Part III · Technology
The LangChain Stack Supports Every Phase6.
15
15
4.0 Part IV · Cross-cutting Concerns
The Agentic Risk T axonomy7 .
FinOps for Agentic Workloads8.
Standards Alignment9.
Independence Across People, Process, and Technology10.
19
20
21
22
22
5.0 Part V · J ourney
The Maturity J ourney11.
In Practice12.
Critical Success Factors  13.
Conclusion
23
2 3
2 6
2 7
2 8
02

THE AGENTIC OPERATING MODEL • 03
Foreword
Agents are moving from prototypes to production today. They handle customer interactions, automate workflows,
and drive measurable business outcomes.

But the teams building the best agents are not following the traditional software development lifecycle. Unlike
traditional software, agents are non-deterministic, stateful, and dependent on models, prompts, and tools that change
without warning. The engineering playbooks enterprises have relied on to build and operate software for decades do
not translate.

The pace of change in AI also requires a different approach and mindset across the organization, both bottom-up
and top-down.
The traditional development playbook does not fit
A well-staffed team with no agent improvement process ships agents that break silently. A rigorous process with
inadequate tooling creates manual overhead that stops scaling. Powerful technology in poorly structured teams
produces fragmented, ungoverned systems.

Traditional software is deterministic. Unit tests validate logic, CI/CD enforces gates, monitoring alerts on exceptions
that should not happen. Agents break every one of these assumptions:
Dimension
Behavior
Testing
Debugging
Versioning
Monitoring
Iteration
Failure mode
Builder
population
Traditional Software
Deterministic, code-driven
Unit tests validate logic
Stack traces find the root cause
Code commits
Exceptions, error rates
Specs to code changes
Crash, exception, wrong output
Software engineers
Agentic Systems
Probabilistic, prompt-driven
Evaluation suites measure quality
Trace analysis inspects the reasoning
Prompts, models, data, tools, and code
Accuracy, hallucination rates, confidence drift,
cost per interaction
Failure clusters to prompt, model, or tool
refinement
Plausible-but-wrong output, goal drift, tool
misuse, cost overrun
Engineers and non-engineers ( S M Es, ops,
marketing, support, finance, HR)
The last row in the table above is the one most enterprises underweight. ML  used to be the province of a narrow elite
of ML  engineers and data labelers. Agents have widened the aperture: anyone who can write a prompt, define an
evaluation, or wire a tool can meaningfully shape an agent.   AI fluency, not engineering headcount, is the new
bottleneck.
03

THE AGENTIC OPERATING MODEL • 04
The Agentic Operating Model
We recently introduced the  Agent Development Lifecycle (ADLC) , a continual product development process for building
reliable agents. This whitepaper introduces The Agentic Operating Model (AOM): a single operating model that
aligns People, Process, and Technology so an enterprise can build, test, deploy, monitor, govern, and continuously improve
agent systems at scale.

The Agentic Operating Model is the scaffolding that lets the LangSmith-enabled ADLC run reliably inside an enterprise.
Because the models, tools, and frameworks beneath every agent change constantly, neutrality and vendor
independence are a design requirement rather than an afterthought.

And most importantly, agents produce vast amounts of behavioral data, with the improvement opportunities buried inside
that data. Manually reviewing agent behavior is not feasible, so accelerating agent delivery is itself contingent on using
agents.

Three principles shape the AOM:
Principle What it means
Agent engineering is a new Agent behavior is not captured in code; it lives in the traces of its
discipline execution. Prompt engineering, evaluation, and observability are engineering
priorities from day one. Treating them as polish that comes after the agent
ships is the most expensive mistake enterprises make.
Allow teams to work fast without breaking things. This starts with
establishing enterprise consistency for agent infrastructure. Speed and
domain relevance need decentralized teams, and increasingly, decentralized
non-engineer builders. Y ou need all three.
The organizations that compound advantage in A I  are the ones that close the
loop fastest, from a production failure to a measurable quality improvement.
Establish enabling constraints
Improvement must be continuous
Three vertical pillars (People, Process, Technology) intersect with the cross-cutting concerns
( G overnance, Security,  F inOps, Compliance,  I nteroperability). E ach pillar is necessary; the model works only when
all are aligned.
W hat thi s  doc um ent co v er s
Part
I ·  P eople
II ·  P rocess
III ·  T echnolog y
I V  ·  C ross - cutting
concerns
V  ·  J ourne y
What it c ov ers
The three rings of builders and the skills each ring brings
The ADLC, and how each skill maps to each phase
The agent engineering stack that supports the process, end to end
H ow the technology enforces what the people and process commit to across G overnance,
Security, F inOps, Compliance, and I nteroperability
H ow an organization matures through these pillars, and how LangChain accelerates
each transition
04

THE AGENTIC OPERATING MODEL • 05
Part I · People
1. The Three Rings: Who Builds, Who Adopts
The most common organizational failure in enterprise AI
programs is going to an extreme.
Too centralized: one team builds all agents and
delivery becomes a bottleneck.
Too decentralized: every team picks their own stack,
and the result is sprawl, duplicated infrastructure,
and ungoverned risk.
Too engineer-only: the people closest to the work
(operators, analysts, SMEs) never participate in
agent creation, and the organization’s
institutionalknowledge stays trapped outside the
loop.
RING 3  ·  NON - TECHNICAL BU ILDER S
SMEs, ops, marketing, support
I mpro v e q ua l it y  or b ui ld  no -c o d e
RING 2  ·  AGENT ENGINEER S
D omain agent teams
B ui ld  on t h e p l at f orm
RING 1  ·  PLAT F ORM ENGINEER S
Ena bl ing team
Ow ns in f ra, go v ernan c e,
primiti v es, patterns
The Agentic Operating Model resolves all three by
organizing builders into three concentric rings, with
governance distributed across them rather than
parked in a separate review board.
Ring
Ring 1 · Platform
Engineers
Ring 2  · A gent
Engineers
Ring 3  · N on - T e ch ni c al
Bu il d ers
Who
Horizontal platform /
applied-AI / platform-
governance
D omain engineering
teams (product, ops,
customer, fi nance,
etc.)
SMEs, operators,
analysts, support,
marketing, sales,
fi nance, HR. Anyone
who works with the
domain knowledge an
agent needs.
What they own
Model gateway, tool gateway,
evaluation infrastructure,
observability backplane, audit
logging, policy engine,
reference patterns
D omain-speci fi c agents, risk
classi fi cation at design time,
evaluation thresholds for their
domain, compliance ownership
for the agents they ship
P rompts, skills, evaluation
criteria, ground truth,
feedback on production
behavior, and increasingly,
their own agents
How they participate
They build the substrate,
operate the eval fl ywheel
for the portfolio, set the
governance bar, curate the
data, and run evaluations
that govern q uality.
Self-serve the platform to
build and ship domain
agents within paved-path
patterns and governance
bar. C o-building with the
P latform team is an
optional accelerator for
fi rst use cases, not a
prere q uisite.
U se agents in their daily
work. Build agents in no-
code surfaces.
05

THE AGENTIC OPERATING MODEL • 06
Governance, security and compliance are a set of responsibilities baked into all three rings, with shared infrastructure
provided by Ring 1 and shared accountability owned by Rings 2 and 3.
Start small and scale
Not all organizations and teams require clear distinctions between platform and agent engineering teams at the
beginning of their agent engineering journey. In this world, it helps to collapse Rings 1 and 2 into a single ring,
while Ring 3 remains distinct.

As agent adoption increases across teams, an organic distinction between Rings 1 and 2 will emerge to maintain
agility and scale.

For the remainder of this document, merge Rings 1 and 2 if you are early in your agent journey.
RING 3 · NON-
TECHNICAL BUILDERS
SMEs, ops, marketing, support
Improve quality or build no-code
RINGS 1+2 ·
(COMBINED)
Platform +
Agent Engineers
B uild t h e infra,
patterns, and t h e
domain agents
Improve quality or build no-code
SMEs, ops, marketing, support
RING 3 · NON-
TECHNICAL BUILDERS
RING 2 ·
AGENT ENGINEERS
D omain agent teams
B uild on t h e platform
RING 1 · PLAT F ORM
ENGINEERS
Enabling team
Ow ns infra,
governance,
primitives, patterns
EARL Y  —  R ings  1 &  2 as  one AS Y OU SCALE —  1 and  2 split  out
Why Ring 3 is the underweighted lever
Most enterprise AI strategies have a serious Ring 1 plan and a workable Ring 2 plan. Ring 3 is where they fall short,
and it is also where the largest fraction of the workforce sits.

In classical ML, the answer to "who builds the model?" was a small team of specialists. With agents, the answer
changes. The people who know what good looks like in the domain are no longer separate from the people who can
shape the agent. A claims adjuster who has handled a thousand claims can write the prompt that handles the next
thousand better than a prompt engineer who has handled none. A support lead who has triaged ten thousand tickets
can define the eval that matters more accurately than a data scientist who is two steps removed.
06

THE AGENTIC OPERATING MODEL • 07
No-code surfaces like  LangSmith Fleet  (LangChain's natural-language agent builder, covered in Part III) make it easy to
create prototypes and internal agents, often for productivity and collaboration. A non-engineer describes the agent's
behavior in natural language, and the system produces a working agent that runs on the same runtime, observability, and
governance backbone as a code-built one.

This changes what an enterprise must invest in:
Investment WHY it matters
Universal AI fluency Every employee should be able to use agents in their daily work. The base rate
of “AI-aware work” determines how fast the organization compounds. Change
management and demystifying AI agents need to be a conscious and coordinated
effort.
A growing share of agents should be built by the SMEs who own the domain. Train
them on prompt design, evaluation thinking, and where the governance guardrails
are.
If the only way to build is to write P ython, R ing 3  is e x cluded by
construction. N o-code tooling, with shared governance underneath, are the entry
p o in t.
Many enterprises still treat “building software” as someone else ’ s j ob. L eaders
have to make it e x plicit that agent building is part of every role ’ s surface
area, the same way spreadsheet building once was.
AI literacy for builders in
Ring 3
Tooling that meets builders
where they are
Role modeling and cultural
p ermission
AI fluency is the new spreadsheet. Treating it as a specialist skill is the most predictable way to be
overtaken by an organization that treats it as a baseline.
The Agent Engineering Hub, not a gatekeeping committee
The three-ring pattern operates as an   Agent Engineering H ub. W hen present, R ing 1  produces patterns, primitives, and
reference implementations, then spreads them outward through R ings 2  and 3 . It should not be a review board that
approves or denies use cases. G atekeeping is top-down and slow, while a hub is collaborative and multiplies enablement.
Think of it as a train-the-trainer pattern adapted for agent engineering, e x tended one ring further to include the people
who do the work the agents are automating.
Governance, security and compliance
Three functions share governance accountability. They are usually not three separate teams. Who  typically  owns  it
Function
D ay - to - day o p eration
O versight and audit
M andate and p olicy
Who typically owns it
P latform team (R ing 1)
Security /  InfoSec
Compliance
E x isting security and compliance functions do not need to be replaced. They need AI-speci fi c awareness around new threat
vectors : prompt in j ection, token leakage through chat surfaces, conte x t-window data e x fi ltration. P art I V  returns to how
governance is enforced through the technology pillar.
07

THE AGENTIC OPERATING MODEL • 08
2. The Three Disciplines: Hire and Reskill
Building an agent-capable organization does not require replacing existing talent. It requires hiring a small number of
specialists to anchor new capabilities, and systematically reskilling high-performing employees in adjacent disciplines.

Agent engineering is not one new role. It is three existing disciplines, each expanded. This framing, drawn from  LangChain's
overview of agent engineering as a new discipline , clarifies who you actually hire, who you reskill, and how those people fit
into the ADLC in Part II.
Discipline 1 · Product Thinking
Defining what the agent should do, writing the prompts that drive its behavior (often thousands of lines), and writing the
evaluations that say whether it is actually working. Think of this as product management with a wider surface area, where
behavior is specified in the artifact that drives the behavior rather than in a separate spec document.
Where it lives Reskill from New skills to learn
Rings 1, 2, and 3 (Ring 3 Product managers, business analysts, Prompt design, eval criteria definition,
most underrated) SMEs, ops leads, content/comms failure - cluster analysis, iteration loops
specialists over specs
Discipline 2  · E ngineering
B uilding the tools the agent calls, the runtime that e x ecutes it durably, the human - in - the - loop pauses that keep it safe, and
the platform primitives the rest of the organi z ation builds on. Think of this as software engineering with a wider surface area,
covering state, memory, tool orchestration, non - deterministic debugging, and sandbo x ing. Responsibility for implementing
agents ’  performance improvements is owned primarily by engineers.
Where it lives
Rings 1 and 2
Reskill from
B ackend / full - stack engineers,
Dev O ps / infra engineers, M L
engineers
New skills to learn
Tool calling patterns, state and memory,
durable e x ecution, model serving, sandbo x
isolation, prompt - as - artifact discipline
Discipline 3  · D a t a  S cience
B uilding the systems that measure agent performance: evaluation harnesses, A / B  testing, monitoring, and error analysis on
production traces. Think of this as data science applied to reliability metrics for unpredictable systems, not standard
statistical analysis on tidy datasets. This skillset is often in high demand, and in a world of agents that emit millions of traces
it re q uires dedicated focus. C ontinuous - improvement agents that q uantify and iterate on other agents ’  performance are a
key force - multiplier for these teams.
Where it lives
Rings 1 and 2
Reskill from
Data scientists, QA  engineers, M L
engineers
New skills to learn
LL M - as -j udge design, golden / synthetic /
adversarial dataset construction,
regression suites, online vs o ff line
eval, cost-per-correct-answer thinking
08

THE AGENTIC OPERATING MODEL • 09
What to hire vs reskill, by discipline
Discipline Hire to anchor (typical 1–3 FTE)
Product Thinking One senior Agent PM with eval and prompt
fluency
One agent platform engineer, one applied-AI
engineer
One evaluation engineer with red-team
experience
AI security engineer, conversational/trust
designer (often one of each at the org level)
Engineering
Data Science
Adjacent specialists
Reskill to scale
Existing PMs, BAs, and SMEs in every
BU
Existing backend, DevOps, and ML
engineers
Existing data scientists and QA
engineers
Pull from security and U X
A doption is the mu ltiplier
The three disciplines describe who builds, while   adoption fluency tells you whether the rest of the org gets value from
what gets built .  An enterprise that hires brilliant agent engineers and never trains the rest of the workforce has built a
F ormula 1  car and forgotten to teach anyone to drive .  Programs that work tend to share a few features :
Mandatory AI literacy training for every employee, with role-speci fi c tracks .
Internal communities of practice where R ing 3  builders share working agents
and ask R ing 2  teams for help .
R ecognition and incentives that reward agent building, not just agent
consumption .
A no-code- fi rst policy for new automations under a de fi ned risk threshold,
with a paved path to upgrade into R ing 2  if the agent grows .
The three disciplines from this section now map directly onto the   Agent Development Lifecycle   in Part II .  Each phase of
the ADL C  has a primary discipline and a primary ring .  The Agentic Operating Model only works when the right
combination shows up at the right phase .
09

THE AGENTIC OPERATING MODEL • 10
Part II · Process
3. The Agent Development Lifecycle
Traditional software follows a predictable arc: define requirements, build, test, ship. The Agent Development
Lifecycle (ADLC) is different. The cycle is shorter, continuous, and driven by evaluation rather than specs.
The lifecycle is four phases plus two continuous practices. The phases are sequenced for any single agent
release. The continuous practices run across all phases all the time.
Skills × phases: who shows up where
Every phase requires a primary discipline (Section 2) and a primary ring (Section 1). The Agentic Operating
Model fails when a phase runs without one of these.
10

THE AGENTIC OPERATING MODEL • 11
Phase
Build
Test
Deploy
M o n ito r
I te ra te
(c o n ti n uous )
G o v e rn
(c o n ti n uous )
Primary discipline
Product Thinking +
Engineering
Data Science + Product
Thinking
Engineering
Data Science + Engineering
All three disciplines
All three disciplines
Primary ring
Ring 2 builds; Ring 1 provides
patterns; Ring 3 builds in
Fleet
Ring 2 owns; Ring 1 provides
infra; Ring 3 contributes
ground truth
Ring 1 provides the runtime;
Ring 2 operates the rollout
Ring 1 provides observability;
Ring 2 watches; Ring 3 reports
issues
All three rings
All three rings ,  plus Security
and C ompliance
What good looks like
Working agent with
externalized prompts and
typed tool schemas
Pass/fail signal against
quality thresholds before
promotion
Agent live with version
control ,  HI T L,  and rollback
V isibility into actual
behavior and where it fails
Failure →  root cause →  fi x →
re - evaluate ,  in days not
quarters
C ost ,  access ,  discoverability
under control as the portfolio
scales
I teration and governance often constitute more than 80%  of agent funding ,  so a conscious and deliberate approach to
automation is non - negotiable .
Build: choosing the right abstraction
The B uild phase opens with a choice of abstraction level .  G et this wrong and the agent is harder to maintain than it should
be .  G et it right and the team moves at a pace that matches the cadence the rest of the framework demands .
Ab straction
F ra m e w o r k s  ( e .g.,
LangChain )
R u n ti m es  ( e .g.,
LangGraph )
H arn esses  ( e .g.,
Deep Agents )
N o - c ode  ( e .g.,
Lang Sm ith Fl eet )
B est f or
C omposing model calls ,  tools ,
prompts ,  retrieval ,  structured
outputs
Stateful ,  multi - step agents with
control fl ow ,  durability ,  human
intervention ,  branching ,  looping ,
pausing ,  resuming
L ong - horizon autonomous workloads
with skills ,  M C P integrations ,
hooks ,  middleware ,  fi lesystem
support
N on - engineer participation .  S M Es
and operators building their own
agents
Primary ring
Ring 2
Ring 2
Ring 1 or
advanced Ring 2
Ring 3
What it pro v ides
The building blocks .  V endor -
neutral integrations across
the ecosystem
The execution substrate .
G raph - based state management
with checkpointing
The opinionated sca ff olding .
H igher - level patterns for
autonomous agents
The natural - language entry
point .  Same runtime and
governance as code - built
agents
11

THE AGENTIC OPERATING MODEL • 12
4. Test in Depth
The Test phase is the engine of agent improvement. Evaluation is the most universally weak area in enterprise AI
programs, and treating it as a continuous practice rather than a deployment checkpoint is the single biggest
differentiator between organizations that compound on AI investment and those that stall.
Dataset construction (Data Science + Ring 3 SMEs)
Datasets are the ground truth for agent quality. Ring 3 SMEs are usually the most valuable contributors, while
the Data Science discipline owns the framework.
Dataset Type
Golden / Curated
Synthetic
Trajectory
Regression
A d v ersarial
Purpose
Validate against real-world ground truth
Comprehensive edge-case coverage
Verify execution paths through the graph
P revent quality degradation
Test in j ection and j ailbreak resistance
How to build
SME curation plus production trace
selection
LLM-generated test cases with SME review
Capture expected tool sequences and node
traversal
Curate from previously resolved failures
Red-team contributions, public threat
datasets
E v a l uator se l ection
Evaluators score agent runs against the datasets.
Ev aluator type B est f or
Ground - truth correctness T asks with a knowable right answer
Tradeo ff
Low
Criteria -b ased (LLM- as - judge ) G rounding, policy adherence, efficiency, helpfulness H igh, use selectively
Deter m inistic / heuristic Schema, format, exact match Low, use for all veri fi able assertions
H u m an annotation q ueues N uanced quality j udgment, dataset curation H igh, but generates ground truth
P air w ise co m parison Ranking prompt variants, A /B  decisions Medium
A lign e v als Aligning LLM-as- j udge evaluators with human
j udgment ;  reducing scorer drift
Medium upfront ( needs human-labeled
examples ) , low ongoing
12

THE AGENTIC OPERATING MODEL • 13
Experiments, simulations, and the iteration cycle
B eyond static datasets, the Test phase includes   experiments  ( prompt variants, models, retrieval strategies, tool schemas
compared side by side )  and   simulations  ( multi-turn evals for conversational, voice, and support agents ).
Root cause
Prompt not following instructions
Model capability limitation
Fix strategy
Add examples, clarify constraints, few-shot demonstrations
Upgrade model for that specific node only
Routing or classification error Enhance supervisor prompt with routing rules and examples
Knowledge gap Expand knowledge base, refine retrieval strategy
Tool misuse Tighten tool schemas, improve tool descriptions, add guardrails
This cycle is what  LangSmith Engine  (Section 6) automates. Engine detects recurring failures in traces, diagnoses the root
cause, proposes a fix, and deploys an evaluator to catch regressions, closing the loop the Data Science discipline runs by
hand at lower maturity stages.
Closing the Loop: From Observation to Action
O bservability alone does not improve agents .  The value of traces, evals, and dashboards is only reali z ed when teams can
move q uickly from signal to diagnosis to fix, and do so repeatedly, at the pace production demands .  I n practice, this loop
breaks down not because teams lack data, but because the work of interpreting that data is slow, manual, and competes
with the work of building .

The teams shipping the best agents have found ways to make this iteration cycle a first-class discipline, not an
afterthought triggered by customer complaints .  They treat production failures as structured inputs to a continuous
improvement process :  clustering them by pattern, tracing them to root cause, proposing a targeted fix, and verifying the
fix holds before it reaches users again .  The faster and more reliably a team can run this loop, the better their agents
become .

As agent complexity and trace volume grow, running this loop by hand becomes the bottleneck .  The natural next step is to
ask :  what parts of this cycle can be systemati z ed, accelerated, or automated entirely, and what would that unlock for the
teams responsible for agent q uality ?
13

THE AGENTIC OPERATING MODEL • 14
5. Deploy, Monitor, and Govern
Deploy (Engineering · Ring 1 + Ring 2)
The Deploy phase is about reliable execution environments, not just shipping code.
Durable runtime with checkpointed state. Long-running agents survive infrastructure failures and resume
from the last checkpoint.
Human-in-the-loop checkpoints for sensitive operations. The agent pauses, a human reviews and approves, the
agent continues.
Sandboxes  for code writing and filesystem access. Isolated execution that cannot escape its boundary.
Context Hub  for the behavior files that shape an agent (prompts, skills, policies, examples). Versioned,
environment-tagged, managed independently from agent code.
Gradual rollout with canary at 5–10%, then 25%, 50%, 75%, then full, each stage monitored before advancing.
M oni t or (D ata  Sc ien c e + Engineering · Ring 1 + Ring 2 + Ring 3  f ee dback )
W hen a traditional application fails, you read a stack trace. W hen an agent fails, you need the reasoning chain. That
re q uires four kinds of production visibility :
Pillar
T ra c e s
S i g nal s
What it captures
F ull trajectory of an agent run :  inputs, model calls, tool invocations, outputs, final response
A utomated q uality scoring :  LL M -as-judge, regex patterns, policy compliance
F eed b a ck E xplicit (ratings, corrections) and implicit (escalation, abandonment) attached back to the run.
R ing 3  is usually the largest source.
Da shb oard s A ggregate views of usage, latency, cost, tool calls, evaluator scores, and failure patterns
S tandard application metrics (latency, uptime, error rate) miss the agent-specific failures :  the agent calling the wrong tool,
relying on the wrong context, skipping a re q uired approval step, or producing an answer that sounds plausible but is wrong.
These failures are invisible without agent-specific traces and signals.
14

THE AGENTIC OPERATING MODEL • 15
Govern (Continuous · all rings)
Governance is a continuous practice that operates across Build, Test, Deploy, and Monitor at the
same time. Three concerns matter most as the agent portfolio scales. Each maps to a specific
technology enforcement point in Part III.
Govern concern
Cost
Too l  access
What good looks like
Token budgets per agent, per tenant, per time window.
Spend alerts. Cost attribution per agent, per node, per
feature.
Every tool call passes through a policy engine. Scoped
tokens, audit trails, H ITL for sensitive operations.
Enforcement point
LangSmith LLM Gateway  (Section 6)
Tool Gateway +  LangGraph
interrupts
D iscovera b i l ity Prompts, skills, tools, and agents are reusable across
teams. A new team starting on a new agent should not
be rebuilding what already e x ists.
SmithDB  + LangSmith prompt/skill
registry
This is where the People → Process story hands off cleanly to Technology: every governance concern named here is
enforced by a specific component of the LangChain stack in Part III.
Part III · Technology
6. The LangChain Stack Supports Every Phase
The Agentic Operating Model is
enabled by an integrated stack
covering every phase of the
ADLC and every governance
concern from Part II.

Unlike point solutions that solve
one problem in isolation, the
components are designed so
each strengthens the others.
15

THE AGENTIC OPERATING MODEL • 16
The mapping from process to stack is direct:
ADLC phase Primary stack components
Build Deep Agents, LangChain, LangGraph (code) · Fleet (no-code)
Test Datasets, Evals, Annotation Queues, Simulations
Deploy Runtime, Agent Server, Sandboxes, Context Hub
Monitor Tracing, Dashboards, Online Evals, User Feedback
Iterate LangSmith Engine (auto loop), Chat (assisted), Insights
Traces, SmithDBSmithDB (data layer)
Govern (continuous) LangSmith LLM Gateway, Tool Gateway, Policy engine, SmithDB audit
Build: framework, runtime, harness, no-code
The four abstractions introduced in Section 3 are concrete products in the stack:

Deep Agents (harness) adds structured planning, persistent memory, MCP integration, hooks, and middleware. Use it for
long-horizon autonomous workloads.

LangChain (framework) composes model calls, tools, prompts, retrieval, and structured outputs. 600+ integrations across
providers, vector stores, and tools. Use it for RAG pipelines, integration glue, and as the composition layer inside more
complex agents.

LangGraph (runtime) provides state, control flow, durability, human intervention, branching, looping, pausing, resuming. Use
it when the agent needs more than a linear chain.

LangSmith Fleet (no-code) is the Ring 3 entry point. Non-engineers describe the agent's behavior in natural language and
the system produces a working agent. It runs on the same runtime, observability, governance, and trace history as code-
built agents, so a Fleet agent can be picked up and extended in LangGraph without losing context.
16

THE AGENTIC OPERATING MODEL • 17
Test: evaluation and datasets
LangSmith  is where the inner loop of the ADLC lives. For the Test phase it provides Evaluation (offline + online, LLM-as-
judge, deterministic validators, human annotation queues), Prompt Management (versioned artifacts with audit trail and
rollback), and Datasets (manual curation, production sampling, synthetic generation). Test is covered in depth in Section
4; here it is the evaluation substrate the rest of the stack builds on.
D e p loy: L an gSm it h  D e p loy m ent and S andbo x es
La ng Sm ith  Deployme nt  i s  the produc ti o n ru ntime for  s tate ful  agent s:  dur a bl e e x e cu ti o n ,  c he ckpo inte d  s tate ,  h or i zo nta l
sc a l ing ,  th r ea d  management ,  v e rs i o ne d  d e ploy ment s,  a u t o mati c  rollb a ck.  Obs e rv a b i l it y,  e v a lu ati o n ,  an d  d e ploy ment
u ni fi e d  in a s ing l e pl at for m .

LangSmith Sandboxes  prov i d e i sol ate d  e x e cu ti o n en v i ro nment s  for  the r i sk ie r  p a r t s  of  agent work:  cod e gene r ati o n an d
e x e cu ti o n ,  fil e sys tem a cc e ss,  u nt rus te d  t ool  c a lls.  A  s an dbox  c ann o t e sc a p e it s  bou n d a ry,  w hi c h i s  w hat ma k e s  T ie r  2  an d
T ie r  3  agent s  ( the r i sk  tie rs  d e fi ne d  in Se c ti o n 7)  d e ploy a bl e at a ll  w ith ou t ta k ing o n u n bou n d e d  bl a s t r a d i us.
Monitor: observability
Once an agent is live, LangSmith Observability traces every run automatically with full state and cost. Observability alone
is not enough. Most enterprises arrive at LangSmith for observability, but observability is just the start of agent
improvement. The harder problem appears once traces are flowing: trace volume compounds, and each trace is
heterogeneous and deeply nested. Left alone, that volume and complexity compounds into a source of paralysis rather
than analysis.
Iterate: actionable observability
The iteration layer is how LangChain delivers actionable observability, actively converting traces into signal rather than
noise. Three components do that work on top of the LangSmith substrate:

Chat:  an interactive AI copilot for trace analysis and debugging, used by the Data Science and Engineering
disciplines during failure investigation, serving as both a peer and an aid.

Insights : automated pattern discovery that clusters agent behavior, surfaces where the agent performs well versus
poorly, and most importantly, shows behavioral drift over time. It is instrumental in uncovering emerging user behavior
or the impact of changing compliance controls. Agent teams can compress the analysis phase and directly leverage
these insights into their sprint planning rituals.

LangSmith Engine : is the agent that runs the iteration cycle on your behalf. Where a human spends hours sifting
through traces to find failures, Engine automatically clusters production issues by severity and root cause, surfacing
50 or more actionable issues per month within hours of them occurring, not after a customer complaint.

Once issues are identified, Engine doesn't stop at diagnosis. It proposes targeted fixes (a prompt edit, a Context Hub
update, or a code PR), each grounded directly in the traces that revealed the problem. It simultaneously generates the
evaluators and dataset examples needed to prevent that class of failure from returning, turning every production
incident into a permanent improvement to your eval suite. Engine is what lets the Data Science discipline scale beyond
what a human team can review by hand. It is the Agentic Operating Model's "Stage 4 / Scaling" capability turned into a
product.
17

THE AGENTIC OPERATING MODEL • 18
The compounding effect is significant. Teams operating Engine ship agent improvements weekly rather than monthly,
catch regressions before they reach users, and redirect engineering time from reactive debugging toward building new
capabilities. At scale, Engine replaces what would otherwise require 2–3 dedicated engineers working full-time, at
roughly one-tenth the cost.
Together they show up throughout your journey.

Solving the cold start: Insights gives a team its first plain-English read on how an agent is actually being used, and Engine
provides the practical substrate to start running the ADLC in earnest.

Sustaining and scaling: strategic use of Insights reports keeps Rings 2 and especially 3 engaged with production reality,
while Engine stretches the limited capacity of Ring 1 and Ring 2 much further.

All of this continual learning requires complex operations over traces at scale, which is why SmithDB sits underneath it. It is
LangChain's bet that long-term continual learning, agents improving agents, demands purpose-built infrastructure, so
these tools stay durable as the trace corpus grows.
SmithDB: the data layer
SmithDB is the purpose-built distributed database that powers LangSmith's observability, and serves both human and
agent consumers. Engineered in Rust on Apache DataFusion and Vortex, it is designed for the shape of agent telemetry
that general-purpose databases handle slowly and expensively: deeply nested traces with hundreds of spans, multi-
modal payloads, and long-open spans that arrive in pieces over hours.

The practical effect: slow observability is itself a bottleneck in the agent development loop. SmithDB makes the queries
that loop depends on fast enough to use continuously, instead of as after-the-fact reviews.
Capability
Trace-tree loading (P50 ~92ms)
Fu ll-te x t searc h  across
p a y loads (P50 ~ 4 00ms)
Why it matters in the ADLC
Add examples, clarify constraints, few-shot demonstrations
Upgrade model for that specific node only
M etadata and f eed b ac k  fi ltering Enhance supervisor prompt with routing rules and examples
JSON  qu eries on str u ct u red o u t pu ts Expand knowledge base, refine retrieval strategy
T h read reconstr u ction
C ost ,  latenc y,  and to k en aggregations
Tighten tool schemas, improve tool descriptions, add guardrails
The data behind the FinOps attribution tables in Section 8
SmithDB powers high-volume organizations like Clay, Vanta, Unify, and Cogent Security.

Beyond the speed, SmithDB is where the artifacts of the Agentic Operating Model accumulate over time: every trace,
evaluation, annotation, and dataset. By collecting, evaluating, and annotating traces today, an enterprise is curating the
data that will shape future agents. Explicit examples of what "good" and "bad" look like will always matter in AI and ML
system design.
18

THE AGENTIC OPERATING MODEL • 19
Govern: LangSmith LLM Gateway
The LangSmith LLM Gateway is the centralized enforcement point for everything that crosses an LLM boundary. Rather
than distributing API keys, spend rules, and PII controls across every agent and every team, the Gateway concentrates
them at the model boundary.
Gateway capability
Credential management
Spend limits
What it enforces
API keys stored once in LangSmith; agents authenticate with LangSmith credentials, not provider
keys
Hard limits at organization, workspace, API key, or user level; 402 hard-block on overrun
PII detection and redaction Names, places, nationality, religion, political affiliation, ages, all redacted before leaving the
gateway
Secrets redaction Phone numbers, SSNs, API keys, tokens across ma j or platforms
Au dit logging
R eal - time cost v isi b ilit y
T race u ni fi cation
Administrative changes and every invocation logged
B y workspace, user, and API key
E very Gateway re q uest appears as a trace in LangSmith, so observability does not fragment
across systems
E ngine integration Policy violations surface as issues in LangSmith E ngine, with click-
through to the originating trace
Mu lti - pro v ider Anthropic, OpenAI, Google Gemini today, with model-neutral
architecture
The Gateway is where the governance commitments from Sections 1–5 become enforced in practice. Sections 7 and 8
return to it as the anchor for both governance and FinOps.
P art IV  ·  C ro ss-cu tting C on c ern s
Governance, security, FinOps, compliance, and interoperability are not a separate workstream. They are how the People
commitments ( who owns what )  and the Process commitments ( what gets checked when )  become enforceable through
the Technology stack .

This part covers them through four lenses :  a risk ta x onomy that scales controls to each agent ' s blast radius ( Section 7 ) ,
FinOps for token-based, multi-model workloads ( Section 8 ) , standards alignment for the regulations you must already
answer to ( Section 9) , and vendor independence that keeps interoperability open across all three pillars ( Section 10 ).

Security and compliance do not get standalone sections because they run through all four, enforced at the LLM
Gateway, the risk tiers, and the audit trail rather than bolted on separately.
19

THE AGENTIC OPERATING MODEL • 20
7 . The Agentic Risk T axonomy
As agents move from read-only retrieval to taking actions, governance becomes as critical as agent logic. The Agentic
Operating Model classifies every agent into one of three tiers, with controls scaled to the tier. Classification is a Product
Thinking + Engineering activity that happens at design time during Build, and is re-evaluated whenever tool or model
authorization changes. Each tier inherits the controls of the one below it.
Tier
1: Bounded (read-only,
informational)
Examples
Retrieval, summarization, classification,
knowledge-base Q&A, content generation for
human review
Required controls (additive)
Input/output filtering (LLM Gateway), audit logging
(LLM Gateway + SmithDB), evaluation gates at
deploy (LangSmith)
2: Actuating (consequential
actions)
Sending communications, writing to systems of
record, multi-step workflows, modifying customer-
facing data
All Tier 01 , plus H ITL approval (LangGraph
interrupts), scoped tool tokens (Tool Gateway), rate
limits, real-time policy enforcement (LLM Gateway)
All Tier 02 , plus pre-deployment red-team simulation,
dedicated runtime guardrails, behavioral anomaly
monitoring (Insights Agent), named accountable
owner, regulatory mapping, sandbo x ed code
e x ecution
3 : Autonomous /  H igh-stakes (long-
hori z on, regulated, fi nancial)
Long-horizon autonomous workflows ;  financial,
legal, or medical actions ;  agent-to-agent
coordination
Risk categories: software vs. agents
Ris k  cate g or y Traditional S o f t w are Ag entic AI
I n p ut mani p ulation SQL in j ection, X SS Prompt in j ection, j ailbreaking
Wh ere en f orcement lives
LLM Gateway input
filtering
D ata ex p osure Direct DB access Conte x t window leakage,
retrieval over-permissioning
LLM Gateway PII /
secrets redaction
Authori z ation API auth
checks
Tool access control, model
allowlisting
Tool Gateway, LLM Gateway
model allowlists
Audita b ility Transaction logs F ull agent decision trace with
reasoning
LangSmith + SmithDB
C ost control Infrastructure spend Token budgets, model routing, per-
agent F inOps
LLM Gateway
G oal alignment
C om p ounding errors
N /A
Bounded by retry logic
Goal misspecification, reward hacking,
scope creep
Evaluation + H ITL (LangGraph
interrupts)
Errors compound across
reasoning chains
Insights Agent + Engine
20

THE AGENTIC OPERATING MODEL • 21
Every risk category has a named enforcement point in the stack. Governance commitments without enforcement points
become principle without practice.
8. F in Op s  f o r A gentic  W o rkl oads
F in O ps for agents is the most universally absent capability in enterprise A I  programs. Agent systems consume tokens
continuously, call multiple models per interaction, and run in long-lived background processes.   Without an e x plicit
operating model for cost, agentic workloads silently destroy unit economics .

F in O ps in the Agentic O perating Model is anchored in the   Lang S mith LLM Gateway   ( S ection 6 ). Every cost lever and every
attribution dimension is enforced there.
The three cost levers
Lever What it controls
Routing Which model handles which node
Caching
Budgets
Whether repeated work re-runs
What spend is allowed at all
Specific controls (enforcement point)
Auto-route to cheaper models when quality permits; reserve
frontier models for high-stakes nodes (LLM Gateway routing
policy)
Eliminate redundant model calls (platform caching layer)
Hard limits per org/workspace/key/user and token budgets
per agent/tenant/window; spend alerts on deviation;
concurrency caps (runtime quota); token and wall-clock
caps on long-running autonomous agents (Deep Agents),
all enforced at the LLM Gateway
Cost attribution as the foundation
Attribution Dimension Why it matters
P er-agent Lets product teams own their unit economics
Where the d ata comes from
Lang S mith trace metadata +  Gateway
P er-tenant R equired for chargeback in multi-tenant deployments Gateway workspace dimension
P er-feature I denti fi es which user-facing capabilities pay back Trace metadata
P er-node S urfaces which steps in the graph drive cost LangGraph trace
P er-interaction Links cost to business outcome (revenue, de fl ection, NPS ) Lang S mith +  business event j oin
The right model is the cheapest model that meets the quality bar, not the most capable one available. Cost-per-
correct-answer should be tracked alongside accuracy.
21

THE AGENTIC OPERATING MODEL • 22
9. Standards Alignment
The Agentic Operating Model is designed to b e compati b le with the ma j or external guidelines and regulations an enterprise
must already answer to. The Risk T axonomy (Section 7) maps to the risk classification each re q uires ;  the LLM Gateway,
SmithD B , and audit logging produce the evidence.
Standard
NIST AI RMF + 600-1
EU AI Act
ISO/IEC 42001
AI TRiSM (Gartner)
What it requires
GOVERN / MAP / MEASURE / MANAGE across the
lifecycle, plus 12 GenAI risk categories
Risk classification, transparency, human
oversight for high-risk systems
AI management system: policy, planning,
operation, evaluation, improvement
Governance, runtime inspection, information
governance, infrastructure security
How the AOM satisfies it
The ADLC phases, the risk taxonomy
(Sec 7), and Gateway audit logging
Risk tiers (Sec 7), HITL interrupts,
full trace audit
The operating model itself, plus the
continuous ADLC
LLM Gateway, o b serva b ility, SmithD B
10. Independence Across People,
Process, and Technology
Single-vendor agent platforms look fast on day one and expensive on day 3 6 5 . Agents that run on proprietary runtimes, store
prompts in proprietary registries, and emit traces in proprietary formats are agents you cannot move.   The Agentic Operating
Model treats vendor independence as a design re q uirement across all three pillars.
Three risks of single-vendor lock-in
PillarR is k W hat keeps it independentWhat it m eans
PeopleLock-in
cost
Open, transfera b le skills (prompt design, evaluation, agent engineering), not vendorW hen pricing changes or a vendor deprecates a feature, you are stuck. Migration cost
grows with every prompt, eval, and trace stored in a proprietary system.certifications.
Capa b ility ceilingProcess The ADLC is a pattern, not a product. B uild →  Test →  Deploy →  Monitor →  Iterate →  Govern runs onY our agents can do only what your single vendor supports. B est-in-class models, tools, and orchestration
patterns from elsewhere stay out of reach.any capa b le stack.
Technology
Compliance
fragility
Open, inspecta b le harnesses (MIT -licensed LangChain, LangGraph, Deep Agents), open trace formats
(OpenTelemetry), open protocols (MCP , A2A, ACP), and a multi-provider gateway you can re-routeRegulatory rules change. A vendor that misses a regional deadline takes your compliance posture down with
them, and your agents go dark with it.
22

THE AGENTIC OPERATING MODEL • 23
Wh at k ee ps  ea ch  pill ar p orta bl e
PillarPillar What keeps it independentWhat keeps it independent
PeoplePeople Open, transferable skills (prompt design, evaluation, agent engineering), not vendorOpen, transferable skills (prompt design, evaluation, agent engineering), not vendor
certifications.certifications.
ProcessProcess The ADLC is a pattern, not a product. Build → Test → Deploy → Monitor → Iterate → Govern runs onThe ADLC is a pattern, not a product. Build → Test → Deploy → Monitor → Iterate → Govern runs on
any capable stack.any capable stack.
TechnologyTechnology Open, inspectable harnesses (MIT -licensed LangChain, LangGraph, Deep Agents), open trace formatsOpen, inspectable harnesses (MIT -licensed LangChain, LangGraph, Deep Agents), open trace formats
(OpenTelemetry), open protocols (MCP , A2A, ACP), and a multi-provider gateway you can re-route(OpenTelemetry), open protocols (MCP , A2A, ACP), and a multi-provider gateway you can re-route
N eutra li ty is  o ff en s e ,  not j u s t d e f en s e
The best model shifts fast: one 2 0%  better on your workload can land with weeks of notice. N eutrality lets you switch to it
immediately, run a cheap model for routing and a frontier model for the high-stakes node, and use cross-provider ensembles
and j udges. It captures upside from a rapidly improving market, not j ust insurance against lock-in. LangChain ' s stack is
designed to coexist with whichever model providers, cloud agent platforms, and orchestration ecosystems the enterprise
already uses.  Y ou should never have to pick one.
Part V · Journey
11. The Maturity Journey
Agent engineering maturity has four stages: Exploring → Building → Operating → Scaling. Most enterprises entering agent
development today look like Stage 1 (Exploring): one team prototyping with LLMs, inconsistent tracing, manual testing. The
path to Stage 4 (Scaling), where agent engineering is an organizational capability, is structured. It does not happen by accident,
and it does not happen as a pure technology upgrade. Every stage transition is a People + Process + Technology move
together.

Organizations are usually uneven across dimensions: strong observability with weak evals, or strong evals with little human
alignment. The gap between dimensions is the opportunity. Process
S ta g e 1  · Expl or i n g:  Ag ent s  a s  e xp er im ent s
D i m ensi o n What it l oo ks like
Summa ry One team prototyping with LLMs. Tracing is new or inconsistent.
People A handful of curious engineers. N o defined disciplines ;  R ing 3  not yet involved.
Process Ad-hoc pilots. Manual testing. N o shared lifecycle.
Technology Whatever each team picked. Probably notebooks.
Si gn atu re  s i gn a ls < 1 0K  monthly traces ;  1 – 2 active pro j ects ;  <5%  engineering adoption ;  no o ff line eval runs
23

THE AGENTIC OPERATING MODEL • 24
Stage 2 · Building: Agents with measurable quality
Dimension What it looks like
Summary A team has shipped to production. Basic tracing and offline evals in place for 1–2 apps.
People A nascent Ring 1 platform team forms; first Ring 2 BU teams co-build with it. First SME (Ring
3) reviewers.
Process Shared ADLC. Offline evals against first datasets. Developers check traces when something
breaks.
Technology Shared platform :  LangChain +  Lang G raph +  LangSmith tracing in production. First Fleet
pilots in Ring 3.
Signature signals 1 0K – 500K  monthl y  traces; 3– 5  active pro jects; 5 –2 0%  engineering adoption; 1–1 0  offline eval
runs / month
Stage 3 · Operating: Agents with closed-loop learning
Dimension What it looks like
Summary Multiple apps in production with s y stematic observabilit y,  online evals ,  human review ,  and
production intelligence. Q ualit y  is activel y  managed.
People All three disciplines hired and reskilled to scale; Ring 3 builders active across multiple BUs;
annotation q ueues run regularl y .
Process Online evals (LLM-as- judge on sampled prod traces) plus offline eval suites that gate deplo y s.
FinOps treated alongside latenc y  and accurac y  as a core q ualit y  dimension. Failure-to-fi x  c y cle
time tracked.
Technology
Signature signals
LLM G atewa y  enforcing budgets and polic y . SmithDB powering fast trace search and FinOps
attribution. Sandbo x es for actuating tiers.
500K –1 0 M monthl y  traces; 6 –1 5  active pro jects; 2 0 – 50%  engineering adoption; 11–1 00
offline eval runs / month; online eval rules running on prod
Stage 4 · Scaling: Agents as an organizational capability
Dimension What it looks like
Summary Agent engineering is an organi z ational capabilit y . Multiple teams ,  automated improvement loops ,
cost governance ,  proactive insights.
People Universal A I  fl uenc y . P latform team serves the org; non-engineers ( P Ms ,  SMEs) also on the
platform. Agent building is a normal job activit y,  not a specialist function.
Process
Technology
I mprovement loop runs continuousl y . G overnance is proactive ,  not reactive. Online eval results
auto-feed offline datasets. Annotation focused on novel /  edge cases.
I nsights Agent generating clusters from production traces (production intelligence at scale).
LangSmith Engine running the auto-loop end to end (detect →  diagnose →  fi x  →  eval). SmithDB
making the trace corpus fast enough to close the loop in seconds.
Signature signals 1 0 M +  monthl y  traces; 1 5+  active pro jects; 50%+  engineering adoption; 1 00+  offline eval runs /
month; continuous online eval as the primar y  q ualit y  signal
24

THE AGENTIC OPERATING MODEL • 25
What each transition requires
Transition
Exploring →
Building
Key unlock
A hanGet traces
flowing from
production and run
your first evalsdful of
curious
People move
Form Ring 1; identify
Ring 2 first-wave
teams; first Ring 3
pilots
Process move
Adopt a shared ADLC;
create the first dataset; run
the first offline experiment
Technology move
Enable LangSmith
tracing in prod;
LangChain/
LangGraph as the
default build layer
Building →
Operating
Move from offline-
only to online evals;
close the loop
between prod data
and development
Hire to anchor each
discipline; reskill
broadly; expand Ring
3 enablement
LLM-as-judge rules on prod
traces; annotation queues;
calibrate evaluators against
human labels; treat FinOps as a
quality dimension
LLM Gateway ,
SmithDB ,
Sandboxes; Fleet at
scale; quality
dashboards
Operating →
Scaling
Stop drowning in traces;
let the platform surface
what matters
U niversal A I  fluency
across the workforce;
agent building is a normal
job activity
I mprovement loop runs
continuously; governance
is proactive; online eval
results auto-populate
offline datasets
I nsights for clustering
and trend analysis;
LangSmith Engine
running the auto-loop;
cost attribution and
automated
remediation
How LangChain supports each transition
Moving through these stages is rarely a pure technology problem .  LangChain provides support against all three pillars .
F unction W hat it covers M ost relevant stage
Deployed Engineering Embedded engineering advisory for high-priority initiatives .
Architectural guidance and best-practice transfer .
Exploring → Building ,  and Building →
Operating
Enablement &  Education Every stage; heaviest Building →
Operating → Scaling
P rofessional Services
Structured curriculum for upskilling existing engineers into
agent engineers ,  platform engineers ,  and evaluation engineers .
W orkshops ,  certifications ,  reference implementations .  I ncludes
the A I  literacy tracks that scale Ring 3 adoption .
Engagement-based delivery focused on agent engineering .
Co-builds production agents with the customer ' s team ,
instilling eval-driven iteration cycles ,  prompt versioning
discipline ,  and trace-based debugging as habits that outlast
the engagement .
Building → Operating ,  and
Operating → Scaling
P roduction-grade support for LangSmith ,  the LLM Gateway ,
and the deployment runtime .  I ncident response ,
troubleshooting ,  escalation paths .
Every stage; criticality grows with
maturity
Strategic relationship management across the customer ' s
agent portfolio .  Roadmap alignment ,  contract evolution ,
adoption tracking .
Every stage
T he maturity journey is one organi z ation ' s responsibility to walk .   LangChain ' s role is to make sure that journey is faster ,  less
risky ,  and less lonely .
Support
Account Management
25

THE AGENTIC OPERATING MODEL • 26
12. In Practice
Below, we describe two organizations operating at very different scales, each illustrating what happens when People,
Process, and Technology line up around the same goals. The first prioritized velocity without giving up centralization; the
second prioritized governance across a heavily regulated footprint. Both grew into platforms that scale without fragmenting.
A global automotive manufacturer
This organization's Enterprise AI team started with a clear mandate and a hard constraint: get AI into production across
supply chain, manufacturing, R&D, and customer-facing properties, without creating a centralized bottleneck that slowed
every business unit down.

Working with LangChain, they built a central platform on LangGraph and LangSmith that functions as the foundation every
agent team builds on. The results reflect what happens when the platform and org structure are set up correctly. Agent
deployment time dropped from three months to one week. One use case that previously took six months to reach production
shipped in four days. A single engineer can now spin up a new production agent end-to-end.

The platform now runs approximately 50 agents in production across the organization, with 300,000 traces per week flowing
through LangSmith. The team issued an enterprise-wide mandate: every production AI application, regardless of framework,
pushes telemetry to LangSmith, driving a single observability standard across LangGraph, CrewAI, LlamaIndex, OpenAI
Agent Builder, and AgentCore. It replaced fragmented monitoring with a consistent signal the central team can act on.

The business impact is concrete. A manufacturing agent saves millions of dollars by rapidly diagnosing line stoppages. An AI
intake bot replaced a sixty-to-seventy question manual process previously managed by an external firm. Their internal multi-
agent platform serves 20,000 daily active users, with an agent builder tool targeting rollout to 56,000 employees.

What made this work wasn't any single tool. It was the combination of a governed platform, a central team that operated as a
hub rather than a bottleneck, and a reskilling model that turned high-performing engineers into agent builders without
replacing them.
A global telecommunications provider
This organization's challenge was different. Operating across dozens of countries and business entities, their priority wasn't
velocity. It was governance at scale. Different regulatory environments, strict data isolation requirements between entities,
and thousands of employees who needed to access AI capabilities without creating uncontrolled sprawl.

Working with LangChain, they built a production platform for enterprise AI on LangChain, LangGraph, and LangSmith, now
serving over 100 enterprise customers. Internally, they are rolling out self-hosted LangSmith instances across multiple entities,
with governance, PII filtering, and access isolation built into the foundation rather than retrofitted later.
26

THE AGENTIC OPERATING MODEL • 27
The architectural decisions they made early are e x actly the ones that will let them scale to thousands of employees without
rebuilding the governance layer when requirements change :  open harnesses, self-hosted observability, A B A C  controls
defined at the platform level from the start.
13. Critical Success Factors
Factor
Build evaluation infrastructure
FactorCentralize platform, decentralize
delivery, distribute fluency
early
Treat prompts as production
M onitor everyt h in g  from day one
artifactsE mbed security and compliance in t h e
Treat Fin O ps as a q uality dimension
Gateway
D e fi ne o w ners h ip per a g ent
I nvest in R in g  3 fluency
P lan for iteration, not perfection
Pillar
Process + Tech
People
Process + Tech
Tech
Tech (+ People +
Process)
Process + Tech
People
People
Process
Why it matters
Without it, you have no feedback loop. Golden
datasets before first deployment.
All three failure modes (centralized bottleneck,
decentralized sprawl, engineer-only) are equally
common.
Version-control every prompt. Measure the impact of
every change.
O bservability added retroactively is orders of
magnitude harder.
L ate reviews create bottlenecks and miss
architectural risks. The LL M Gateway makes
enforcement automatic.
Agentic costs scale super-linearly. Token budgets
and per-agent attribution from day one.
Without it, quality degrades with no accountable
party. E very agent has a named owner across all
three rings.
The largest fraction of the workforce sits here.
Treating A I  fl uency as a specialist skill is the
most predictable way to be overtaken.
The first version of any agent will be wrong. B udget
cycles. Measure improvement. 17/17
27

THE AGENTIC OPERATING MODEL • 28
Conclusion
The shift to agents is an organizational transformation, rather than a technology upgrade.

The technology is here today. LangChain, LangGraph, and Deep Agents provide the OSS build layer at every
abstraction level. LangSmith, together with Engine, Chat, and Insights, provides observability, evaluation, and the
closed-loop improvement engine. LangSmith Deployment and Sandboxes provide the runtime and isolation.
SmithDB makes the trace and evaluation corpus fast enough to query continuously. The LangSmith LLM Gateway
anchors governance, security, and FinOps in a single enforcement point.

What remains is the organizational will to adopt a new way of building software, where:
Evaluation precedes deployment,
Traces precede debugging,
Production data precedes the next iteration, and
Every employee, not only engineers, participates in agent creation and improvement.

The Agentic Operating Model is how an enterprise puts that into practice across People, Process, and
Technology, together.

Speak with the LangChain team  to learn more about accelerating your agent development initiatives.
Factor Pillar Why it matters
28

---
Source file: The_Agentic_Operating_Model.pdf
