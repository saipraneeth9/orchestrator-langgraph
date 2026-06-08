from langgraph.graph import (
    StateGraph,
    START,
    END,
)

from orchestrator.source_trust import source_trust_node
from orchestrator.state import (
    OrchestratorState,
)

from orchestrator.intent_classifier import (
    intent_classifier_node,
)

from orchestrator.retrieval_strategy import (
    retrieval_strategy_node,
)

from orchestrator.source_selector import (
    source_selector_node,
)

from orchestrator.retrieval_router import (
    retrieval_router,
)

from orchestrator.response_normalizer import (
    response_normalizer_node,
)

from orchestrator.answer_classifier import (
    answer_classifier_node,
)

from orchestrator.answer_aggregator import (
    answer_aggregator_node,
)

from orchestrator.answer_synthesizer import (
    answer_synthesizer_node,
)

from agents.sharepoint_agent import (
    sharepoint_agent,
)

from agents.servicenow_agent import (
    servicenow_agent,
)

from agents.confluence_agent import (
    confluence_agent,
)

from agents.barnum_agent import (
    barnum_agent,
)

from orchestrator.answer_validator import (

    answer_validator_node,

)

from orchestrator.conflict_resolution import (
    conflict_resolution_node,
)

from orchestrator.low_confidence import (
    low_confidence_node,
)

from orchestrator.response_strategy import (
    response_strategy_node,
)

from orchestrator.strategy_router import (
    strategy_router,
)

from orchestrator.direct_response import (
    direct_response_node,
)

from orchestrator.answer_topology import (
    answer_topology_node,
)

# --------------------------------------------------
# Graph Builder
# --------------------------------------------------

builder = StateGraph(
    OrchestratorState
)

# --------------------------------------------------
# Core Orchestration Nodes
# --------------------------------------------------

builder.add_node(
    "intent_classifier",
    intent_classifier_node,
)

builder.add_node(
    "retrieval_strategy",
    retrieval_strategy_node,
)

builder.add_node(
    "source_selector",
    source_selector_node,
)

# --------------------------------------------------
# Agent Nodes
# --------------------------------------------------

builder.add_node(
    "sharepoint_agent",
    sharepoint_agent,
)

builder.add_node(
    "servicenow_agent",
    servicenow_agent,
)

builder.add_node(
    "confluence_agent",
    confluence_agent,
)

builder.add_node(
    "barnum_agent",
    barnum_agent,
)


# --------------------------------------------------
# Answer Pipeline Nodes
# --------------------------------------------------

builder.add_node(
    "response_normalizer",
    response_normalizer_node,
)

builder.add_node(
    "answer_classifier",
    answer_classifier_node,
)

builder.add_node(
    "answer_aggregator",
    answer_aggregator_node,
)

builder.add_node(
    "answer_synthesizer",
    answer_synthesizer_node,
)

builder.add_node(
    "answer_validator",
    answer_validator_node,
)

builder.add_node(
    "conflict_resolution",
    conflict_resolution_node,
)

builder.add_node(
    "low_confidence",
    low_confidence_node,
)

builder.add_node(
    "response_strategy",
    response_strategy_node,
)

builder.add_node(
    "direct_response",
    direct_response_node,
)

builder.add_node(
    "answer_topology",
    answer_topology_node,
)

builder.add_node(
    "source_trust",
    source_trust_node,
)
# --------------------------------------------------
# Main Flow
# --------------------------------------------------

builder.add_edge(
    START,
    "intent_classifier",
)

builder.add_edge(
    "intent_classifier",
    "retrieval_strategy",
)

builder.add_edge(
    "retrieval_strategy",
    "source_selector",
)

# --------------------------------------------------
# Dynamic Parallel Fan-Out
# --------------------------------------------------

builder.add_conditional_edges(
    "source_selector",
    retrieval_router,
)

# --------------------------------------------------
# Parallel Agent Fan-In
# --------------------------------------------------

builder.add_edge(
    "sharepoint_agent",
    "response_normalizer",
)

builder.add_edge(
    "servicenow_agent",
    "response_normalizer",
)

builder.add_edge(
    "confluence_agent",
    "response_normalizer",
)

builder.add_edge(
    "barnum_agent",
    "response_normalizer",
)

# --------------------------------------------------
# Answer Processing Pipeline
# --------------------------------------------------

builder.add_edge(
    "response_normalizer",
    "answer_classifier",
)

builder.add_edge(
    "answer_classifier",
    "source_trust",
)

builder.add_edge(
    "source_trust",
    "answer_aggregator",
)

builder.add_edge(
    "answer_aggregator",
    "answer_topology",
)

builder.add_edge(
    "answer_topology",
    "answer_validator",
)

builder.add_edge(
    "answer_validator",
    "response_strategy",
)

builder.add_conditional_edges(
    "response_strategy",
    strategy_router,
)



# --------------------------------------------------
# Finish
# --------------------------------------------------

builder.add_edge(
    "direct_response",
    END,
)

builder.add_edge(
    "answer_synthesizer",
    END,
)

builder.add_edge(
    "conflict_resolution",
    END,
)

builder.add_edge(
    "low_confidence",
    END,
)

# --------------------------------------------------
# Compile Graph
# --------------------------------------------------

graph = builder.compile()