def extract_answer(payload):

    if not payload:
        return ""

    if isinstance(
        payload,
        str,
    ):
        return payload

    # Pattern 1
    if "answer" in payload:

        return payload["answer"]

    # Pattern 2
    if "response" in payload:

        response = payload["response"]

        if isinstance(
            response,
            dict,
        ):

            if "text" in response:

                return response["text"]

    # Pattern 3
    if "messages" in payload:

        messages = payload["messages"]

        for message in reversed(messages):

            role = message.get(
                "role"
            )

            if role in (
                "assistant",
                "agent",
            ):

                return (

                    message.get(
                        "content"
                    )

                    or

                    message.get(
                        "message"
                    )

                    or

                    ""
                )

    # Pattern 4
    if "result" in payload:

        result = payload["result"]

        if isinstance(
            result,
            dict,
        ):

            if "summary" in result:

                return result["summary"]

    return str(payload)