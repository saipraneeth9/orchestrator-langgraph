class ConfluenceHandler:

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
                        "PTO approvals are processed through Workday.",
                },
            ]
        }