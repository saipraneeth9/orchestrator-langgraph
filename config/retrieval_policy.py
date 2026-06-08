RETRIEVAL_POLICY = {

    "policy_lookup": {

        "search_incidents": False,

        "search_documentation": True,

        "search_community": False,

        "max_sources": 3,
    },

    "incident_lookup": {

        "search_incidents": True,

        "search_documentation": False,

        "search_community": False,

        "max_sources": 5,
    },

    "troubleshooting": {

        "search_incidents": True,

        "search_documentation": True,

        "search_community": True,

        "max_sources": 10,
    },

    "how_to": {

        "search_incidents": False,

        "search_documentation": True,

        "search_community": False,

        "max_sources": 5,
    },

    "root_cause_analysis": {

        "search_incidents": True,

        "search_documentation": True,

        "search_community": False,

        "max_sources": 10,
    },

    "general_knowledge": {

        "search_incidents": False,

        "search_documentation": True,

        "search_community": False,

        "max_sources": 5,
    },
}