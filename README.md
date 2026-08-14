# LLM-Chatbot-using-LangGraph

Building a production-ready LLM Chatbot from scratch using **LangGraph**, **Hugging Face**, and **Streamlit**. The project follows a step-by-step development approach, where every feature is implemented incrementally to understand the complete architecture of a modern AI chatbot.

## Roadmap

### Phase 1: Project Foundation

- [x] Initialize Git repository
- [x] Create project folder structure
- [x] Create `requirements.txt`
- [x] Design chatbot state (`State`)
- [x] Create Hugging Face LLM wrapper
- [x] Implement first LangGraph node (`generate_response`)
- [x] Build and compile the initial LangGraph workflow
- [x] Implement conversation history
- [x] Add `HumanMessage` and `AIMessage` to conversation history
- [x] Create `update_history` node
- [x] Add state reducer using `Annotated` and `operator.add`
- [x] Integrate LangGraph checkpointer
- [x] Implement thread-based conversation state using `thread_id`
- [x] Test multi-turn conversation memory

### Phase 2: Basic Chatbot

- [x] Create application entry point (`app.py`)
- [x] Invoke LangGraph workflow
- [ ] Build a basic Streamlit chatbot interface
- [ ] Connect user input with the workflow

### Phase 3: Conversation Management

- [ ] Support multiple chat sessions
- [ ] Create new chat functionality
- [x] Store conversation history
- [x] Manage conversation threads using `thread_id`
- [ ] Display previous conversations
- [ ] Switch between chat sessions

### Phase 4: Persistence

- [ ] Integrate SQLite checkpointer
- [ ] Persist chat history across application restarts
- [ ] Restore previous conversations
- [ ] Implement persistent LangGraph checkpoints
- [ ] Test checkpoint recovery

### Phase 5: Advanced LangGraph Features

- [ ] Conditional edges
- [ ] Multiple nodes
- [ ] Prompt Builder node
- [ ] History Loader node
- [ ] History Saver node
- [ ] Streaming responses
- [ ] Error handling
- [ ] State reducers
- [ ] Command-based routing
- [ ] Parallel execution

### Phase 6: Production Features

- [ ] PostgreSQL integration
- [ ] Configuration management
- [ ] Logging
- [ ] Exception handling
- [ ] Environment management
- [ ] Structured project configuration
- [ ] Testing with `pytest`

### Phase 7: AI Features

- [ ] RAG integration
- [ ] Tool calling
- [ ] Web search
- [ ] Long-term memory
- [ ] Conversation summarization
- [ ] Context management
- [ ] Agentic workflows

### Phase 8: Deployment & DevOps

- [ ] Docker
- [ ] Docker Compose
- [ ] CI/CD
- [ ] GitHub Actions
- [ ] PostgreSQL deployment
- [ ] Application deployment
- [ ] Monitoring
- [ ] Production logging

### Phase 9: Security & Authentication

- [ ] User authentication
- [ ] Session management
- [ ] API security
- [ ] Environment variable management
- [ ] Secrets management
- [ ] Rate limiting

### Phase 10: Future Enhancements

- [ ] Multimodal input
- [ ] Voice input
- [ ] File upload
- [ ] Document processing
- [ ] Multiple LLM providers
- [ ] Model selection
- [ ] Advanced memory architecture
- [ ] Human-in-the-loop