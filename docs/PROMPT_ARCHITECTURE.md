# 6-Component AI Agent Prompt Architecture

To ensure deterministic and high-quality outputs from LLMs in our automation pipelines, all system prompts MUST adhere to this framework:

1. **Role**: Define the exact persona and expertise level.
2. **Task**: State the specific, singular objective.
3. **Input**: Describe the exact format of the incoming data context.
4. **Output**: Define the strict formatting requirements (e.g., JSON schema, Markdown).
5. **Constraints**: List absolute rules (e.g., "Do not include conversational filler").
6. **Capabilities**: Outline what the agent assumes it can do or tools it represents.
