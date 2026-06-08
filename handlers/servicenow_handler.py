class ServiceNowHandler:

    def search(
        self,
        query: str,
    ):

        return {

            "messages": [

                {
                    "role": "user",
                    "content": query,
                },

                {
                    "role": "assistant",
                    "content":
                        "PTO approvals are failing due to integration latency.",
                },
            ]
        }