class SharePointHandler:

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
                        "Employees receive 20 PTO days annually according to policy.",
                },
            ]
        }