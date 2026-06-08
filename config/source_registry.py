SOURCE_REGISTRY = {

    "sharepoint": {

        "capabilities": [
            "documentation",
            "policies",
            "procedures",
        ],

        "authority": 0.90,

        "evidence_type": "policy",
    },

    "servicenow": {

        "capabilities": [
            "incidents",
            "tickets",
            "outages",
        ],

        "authority": 1.00,

        "evidence_type": "incident",
    },

    "barnum": {

        "capabilities": [
            "community",
            "troubleshooting",
            "workarounds",
        ],

        "authority": 0.70,

        "evidence_type": "community_knowledge",
    },

    "confluence": {

        "capabilities": [
            "documentation",
            "knowledge",
            "guides",
        ],

        "authority": 0.95,

        "evidence_type": "knowledge_article",
    },
}