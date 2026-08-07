# AI Chatbot Project Blueprint

> **Tech Stack:** LangGraph • Streamlit • Hugging Face • SQLite/PostgreSQL • SQLAlchemy • LangGraph Checkpoints • Persistent Memory

---

# Project Structure

```text
AI_CHATBOT/
│
├── 📄 app.py                         # Main Streamlit application entry point
│
├── 📂 config/
│   └── config.py                     # Environment variables & application settings
│
├── 📂 graph/
│   ├── state.py                      # LangGraph State definition
│   ├── graph_builder.py              # Builds and compiles the LangGraph workflow
│   ├── nodes.py                      # All graph nodes (LLM, tools, router, etc.)
│   └── edges.py                      # Graph edges & conditional routing logic
│
├── 📂 memory/
│   ├── checkpoint.py                 # LangGraph checkpoint configuration
│   ├── thread_manager.py             # Conversation Thread IDs
│   └── persistence.py                # Persistent memory management
│
├── 📂 llm/
│   └── huggingface.py                # Hugging Face model loading
│
├── 📂 database/
│   ├── database.py                   # SQLAlchemy connection
│   ├── models.py                     # Database models
│   └── crud.py                       # Database CRUD operations
│
├── 📂 services/
│   ├── chat_service.py               # Main chatbot business logic
│   └── history_service.py            # Chat history operations
│
├── 📂 utils/
│   ├── logger.py                     # Logging configuration
│   └── helper.py                     # Utility functions
│
├── 📂 frontend/
│   ├── sidebar.py                    # Sidebar components
│   ├── chat_ui.py                    # Chat interface
│   └── styles.py                     # Custom CSS
│
├── 📂 static/                        # Static assets
│
├── 📂 prompts/
│   └── system_prompt.py              # System prompts
│
├── 📄 requirements.txt               # Python dependencies
│
└── 📄 .env                           # Environment variables
```

---

# 🏗️ Layer Architecture

```text
                ┌────────────────────────┐
                │     Streamlit UI       │
                └────────────┬───────────┘
                             │
                     Chat Service Layer
                             │
                ┌────────────▼───────────┐
                │     LangGraph Flow     │
                └────────────┬───────────┘
                             │
      ┌──────────────────────┼──────────────────────┐
      │                      │                      │
      ▼                      ▼                      ▼
  HuggingFace LLM      Memory System          Database
      │                      │                      │
      └──────────────────────┴──────────────────────┘
                             │
                       Response to UI
```

---

#  Module Responsibilities

| Folder | Responsibility |
|---------|---------------|
| **config** | Application configuration |
| **graph** | Complete LangGraph workflow |
| **memory** | Checkpoints, Threads & Persistence |
| **llm** | Hugging Face model loading |
| **database** | SQL connection and storage |
| **services** | Business logic |
| **frontend** | Streamlit UI |
| **utils** | Helper functions & logging |
| **prompts** | Prompt engineering |

---

#  Future Expansion

- ✅ Authentication
- ✅ Multi-user Support
- ✅ RAG Integration
- ✅ Tool Calling
- ✅ Vector Database
- ✅ File Upload
- ✅ Image Input
- ✅ Voice Chat
- ✅ SQL Agent
- ✅ PDF Chat
- ✅ Web Search
- ✅ Memory Summarization
- ✅ Conversation Analytics
- ✅ Agentic Workflows
- ✅ Human-in-the-loop
- ✅ Multi-Agent System

---

#  Current Goal

Build a production-ready chatbot using:

- LangGraph
- Streamlit
- Hugging Face LLM
- SQL Database
- Persistent Memory
- Checkpoints
- Threads
- Streaming Responses
- Modular Architecture