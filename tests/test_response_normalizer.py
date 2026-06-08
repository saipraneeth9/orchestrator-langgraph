from pprint import pprint

from utils.response_extractor import (
    extract_answer,
)


payloads = [

    {
        "source": "agent_1",
        "answer": "Answer format",
    },

    {
        "source": "agent_2",
        "response": {
            "text": "Response text format",
        },
    },

    {
        "source": "agent_3",
        "messages": [
            {
                "role": "user",
                "content": "Question",
            },
            {
                "role": "assistant",
                "content": "Assistant answer",
            },
        ],
    },

    {
        "source": "agent_4",
        "result": {
            "summary": "Summary answer",
        },
    },
]

for payload in payloads:

    print("\n")
    print("=" * 80)

    pprint(payload)

    print(
        "\nExtracted:"
    )

    print(
        extract_answer(
            payload
        )
    )