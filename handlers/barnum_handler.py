class BarnumHandler:

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
                        "Community users reported intermittent approval delays.",
                },
            ]
        }