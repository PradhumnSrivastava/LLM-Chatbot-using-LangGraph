# LLM-Chatbot-using-LangGraph

Building a production-ready LLM Chatbot from scratch using **LangGraph**, **Hugging Face**, and **Streamlit**. The project follows a step-by-step development approach, where every feature is implemented incrementally to understand the complete architecture of a modern AI chatbot.

## Roadmap

### Phase 1: Project Foundation

* [x] Initialize Git repository
* [x] Create project folder structure
* [x] Create `requirements.txt`
* [x] Design chatbot state (`State`)
* [x] Create Hugging Face LLM wrapper
* [x] Implement first LangGraph node (`generate_response`)
* [x] Build and compile the initial LangGraph workflow

### Phase 2: Basic Chatbot

* [ ] Create application entry point (`app.py`)
* [ ] Invoke LangGraph workflow
* [ ] Build a basic Streamlit chatbot interface
* [ ] Connect user input with the workflow

### Phase 3: Conversation Management

* [ ] Support multiple chat sessions
* [ ] Create new chat functionality
* [ ] Store conversation history
* [ ] Manage conversation threads

### Phase 4: Persistence

* [ ] Integrate SQLite
* [ ] Persist chat history
* [ ] Restore previous conversations
* [ ] Implement LangGraph checkpoints

### Phase 5: Advanced LangGraph Features

* [ ] Conditional edges
* [ ] Multiple nodes
* [ ] Prompt Builder node
* [ ] History Loader node
* [ ] History Saver node
* [ ] Streaming responses
* [ ] Error handling

### Phase 6: Production Features

* [ ] PostgreSQL integration
* [ ] Configuration management
* [ ] Logging
* [ ] Exception handling
* [ ] Environment management

### Phase 7: Future Enhancements

* [ ] RAG integration
* [ ] Tool calling
* [ ] Web search
* [ ] Memory
* [ ] Authentication
* [ ] Docker
* [ ] Deployment
