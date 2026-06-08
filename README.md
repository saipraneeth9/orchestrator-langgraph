# Orchestrator LangGraph

A sophisticated multi-agent orchestration system built with LangGraph that coordinates multiple data source agents (SharePoint, ServiceNow, Confluence, Barnum) to retrieve, process, and synthesize answers to complex queries.

## Overview

Orchestrator LangGraph is an enterprise-grade answer generation system that:

- **Orchestrates Multiple Agents**: Manages SharePoint, ServiceNow, Confluence, and Barnum agents to query diverse data sources
- **Intent Classification**: Understands user intent to route queries to appropriate sources
- **Intelligent Retrieval**: Employs dynamic retrieval strategies based on query characteristics
- **Answer Aggregation**: Combines responses from multiple sources with conflict detection and resolution
- **Quality Validation**: Validates answers based on confidence scores, consistency checks, and topology analysis
- **Response Strategy Selection**: Chooses optimal response strategy (direct, consolidate, resolve conflict, low confidence handling)
- **End-to-End Tracing**: Provides detailed execution traces for debugging and auditing

## Architecture

### Core Components

#### Orchestrator Pipeline
- **Intent Classifier** (`intent_classifier.py`): Determines query intent and source relevance
- **Retrieval Strategy** (`retrieval_strategy.py`): Selects retrieval approach based on query type
- **Source Selector** (`source_selector.py`): Identifies which agents should handle the query
- **Retrieval Router** (`retrieval_router.py`): Routes queries to selected agents
- **Response Normalizer** (`response_normalizer.py`): Standardizes agent responses to common format
- **Answer Classifier** (`answer_classifier.py`): Classifies answers by type and confidence
- **Answer Aggregator** (`answer_aggregator.py`): Combines multiple answers and detects conflicts
- **Answer Synthesizer** (`answer_synthesizer.py`): Synthesizes final answer from aggregated results
- **Answer Validator** (`answer_validator.py`): Validates answer quality and confidence

#### Response Management
- **Response Strategy** (`response_strategy.py`): Determines how to present the answer based on validation results
- **Conflict Resolver** (`conflict_resolver.py`): Resolves conflicting answers from multiple sources
- **Direct Response** (`direct_response.py`): Handles straightforward answer delivery

#### Agents
- **SharePoint Agent** (`agents/sharepoint_agent.py`): Queries SharePoint documents and sites
- **ServiceNow Agent** (`agents/servicenow_agent.py`): Retrieves incidents and knowledge articles
- **Confluence Agent** (`agents/confluence_agent.py`): Searches Confluence documentation
- **Barnum Agent** (`agents/barnum_agent.py`): Interfaces with Barnum data source

### Data Models (schemas/)
- `agent_output.py`: Raw output from agents
- `agent_response.py`: Processed agent responses
- `aggregated_answers.py`: Combined answers with topology info
- `answer_classification.py`: Classification results for answers
- `answer_topology.py`: Analysis of answer relationships (conflicting, redundant, complementary)
- `answer_type.py`: Categorization of answer types
- `conflict_analysis.py`: Details of detected conflicts
- `evidence_package.py`: Supporting evidence for answers
- `final_answer.py`: Final answer delivered to user
- `intent_result.py`: Intent classification results
- `validation_result.py`: Quality and confidence validation results
- `response_strategy.py`: Selected strategy for response delivery
- `trace_event.py`: Execution trace events for auditing

### Configuration
- **Settings** (`config/settings.py`): Global configuration parameters
- **Ranking Policy** (`config/ranking_policy.py`): Rules for ranking multiple answers
- **Retrieval Policy** (`config/retrieval_policy.py`): Policies governing retrieval behavior
- **Source Registry** (`config/source_registry.py`): Registration of available sources

### Utilities
- **Similarity Helper** (`helpers/similarity_helper.py`): Similarity matching algorithms
- **Search Helper** (`helpers/search_helper.py`): Search optimization utilities
- **Tracing** (`utils/tracing.py`): Performance tracing and timing utilities
- **Conflict Detector** (`utils/conflict_detector.py`): Detects conflicting answers
- **Response Extractor** (`utils/response_extractor.py`): Extracts structured responses

## Key Features

### Answer Conflict Resolution
The system detects when multiple sources provide conflicting answers and resolves them using:
1. **Trust-based Resolution**: Prioritizes answers from higher-trust sources
2. **Confidence Gap Analysis**: Considers confidence scores when sources disagree
3. **LLM Resolution**: Uses an LLM to synthesize conflicting information when gaps are small

### Quality Validation
- Confidence score evaluation
- Source trustworthiness assessment
- Answer consistency checking
- Topology analysis for answer relationships

### Response Strategy Selection
Based on validation results, the system chooses:
- **DIRECT_RESPONSE**: Single confident answer
- **RESOLVE_CONFLICT**: Handle conflicting answers
- **CONSOLIDATE**: Combine complementary answers
- **LOW_CONFIDENCE**: Acknowledge uncertainty with alternatives

### Execution Tracing
Every operation is traced with:
- Node name and status
- Execution duration
- Metadata about decisions made
- Error information when applicable

## Installation

### Prerequisites
- Python 3.10+
- LangGraph
- LangChain
- Ollama (for LLM operations)

### Setup

1. Clone the repository:
```bash
git clone <repository-url>
cd orchestrator-langgraph
```

2. Create a virtual environment:
```bash
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Configure environment variables (if needed):
```bash
cp .env.example .env
# Edit .env with your configuration
```

## Usage

### Basic Query Processing

```python
from orchestrator.graph import build_orchestrator_graph

# Build the orchestration graph
graph = build_orchestrator_graph()

# Execute a query
result = graph.invoke({
    "query": "What is the process for submitting a leave request?"
})

# Access the final answer
print(result["final_answer"].answer)
print(f"Confidence: {result['final_answer'].confidence}")
```

### With Execution Trace

```python
# Get detailed execution trace
trace_events = result.get("execution_trace", [])
for event in trace_events:
    print(f"{event.node}: {event.status} ({event.duration_ms}ms)")
    print(f"  Metadata: {event.metadata}")
```

## Project Structure

```
orchestrator-langgraph/
├── agents/                 # Multi-source agents
│   ├── sharepoint_agent.py
│   ├── servicenow_agent.py
│   ├── confluence_agent.py
│   └── barnum_agent.py
├── clients/               # External service clients
│   ├── embedding_client.py
│   └── ollama_client.py
├── config/                # Configuration modules
│   ├── settings.py
│   ├── ranking_policy.py
│   └── retrieval_policy.py
├── handlers/              # Agent response handlers
│   ├── sharepoint_handler.py
│   ├── servicenow_handler.py
│   ├── confluence_handler.py
│   └── barnum_handler.py
├── helpers/               # Utility helpers
│   ├── search_helper.py
│   └── similarity_helper.py
├── orchestrator/          # Core orchestration pipeline
│   ├── graph.py          # Main orchestration graph
│   ├── state.py          # Graph state definition
│   ├── intent_classifier.py
│   ├── retrieval_strategy.py
│   ├── source_selector.py
│   ├── retrieval_router.py
│   ├── response_normalizer.py
│   ├── answer_classifier.py
│   ├── answer_aggregator.py
│   ├── answer_synthesizer.py
│   ├── answer_validator.py
│   ├── answer_topology.py
│   ├── response_strategy.py
│   ├── conflict_resolver.py
│   └── direct_response.py
├── prompts/               # LLM prompt templates
│   ├── intent_classifier_prompt.py
│   ├── retrieval_strategy_prompt.py
│   ├── answer_classifier_prompt.py
│   └── synthesizer_prompt.py
├── schemas/               # Data model definitions
│   ├── agent_output.py
│   ├── aggregated_answers.py
│   ├── answer_topology.py
│   ├── conflict_analysis.py
│   ├── final_answer.py
│   └── ... (other schemas)
├── tests/                 # Test suite
│   ├── test_agents.py
│   ├── test_orchestrator.py
│   ├── test_answer_aggregator.py
│   └── ... (other tests)
├── utils/                 # Utility modules
│   ├── tracing.py
│   ├── conflict_detector.py
│   └── response_extractor.py
└── README.md
```

## Configuration

### Environment Variables

Key environment variables for configuration:
- `OLLAMA_API_URL`: URL to Ollama service (default: http://localhost:11434)
- `LLM_MODEL`: LLM model to use (e.g., llama2, mistral)
- `EMBEDDING_MODEL`: Embedding model for similarity searches
- `SOURCE_TRUST_WEIGHTS`: JSON configuration for source trustworthiness

### Confidence Thresholds

Configure in `orchestrator/response_strategy.py`:
- `LOW_CONFIDENCE_THRESHOLD`: Minimum confidence for direct response (default: 0.50)
- `HIGH_CONFIDENCE_GAP`: Threshold for trust-based conflict resolution (default: 0.10)
- `LOW_CONFIDENCE_GAP`: Threshold for LLM-based resolution (default: 0.03)

## Testing

Run the test suite:

```bash
pytest tests/ -v
```

Run specific test:

```bash
pytest tests/test_answer_aggregator.py -v
```

With coverage:

```bash
pytest tests/ --cov=orchestrator --cov-report=html
```

## Performance and Monitoring

### Execution Tracing

All operations are timed and traced:
```python
# Access timing information
trace_events = result.get("execution_trace", [])
total_duration = sum(e.duration_ms for e in trace_events)
print(f"Total execution time: {total_duration}ms")
```

### Debug Mode

Enable detailed logging:
```python
import logging
logging.basicConfig(level=logging.DEBUG)
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/improvement`)
3. Make your changes and add tests
4. Ensure tests pass and code is formatted
5. Commit your changes (`git commit -am 'Add feature'`)
6. Push to the branch (`git push origin feature/improvement`)
7. Create a Pull Request

## Troubleshooting

### Common Issues

**LLM Connection Issues**
- Ensure Ollama is running: `ollama serve`
- Check API URL in configuration
- Verify model is available: `ollama list`

**Agent Failures**
- Check source credentials in configuration
- Review agent handler logs
- Verify network connectivity to source systems

**Low Confidence Answers**
- Check retrieval strategy selection
- Review answer topology analysis
- Consider enabling LLM synthesis

## Roadmap

- [ ] Multi-turn conversation support
- [ ] User feedback loop for answer quality improvement
- [ ] Caching layer for frequent queries
- [ ] Performance optimization for parallel agent calls
- [ ] Advanced conflict resolution strategies
- [ ] Integration with additional data sources
- [ ] Web UI for query submission and result visualization

## License

[Specify License Here]

## Contact

For questions or support, please contact: [Contact Information]

## Acknowledgments

Built with:
- [LangGraph](https://github.com/langchain-ai/langgraph) - Graph-based orchestration
- [LangChain](https://github.com/langchain-ai/langchain) - LLM framework
- [Ollama](https://ollama.ai/) - Local LLM inference
