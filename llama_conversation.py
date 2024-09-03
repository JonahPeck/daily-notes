import click
import os
import replicate
from chat_session import ChatSession

class LlamaChatSession(ChatSession):
    def __init__(self, username):
        super().__init__(username)
        self.client = replicate.Client(api_token=os.getenv("REPLICATE_API_KEY"))
        self.model_version = "meta/meta-llama-3-70b-instruct"
        self.conversation_history = []

    def chat(self)
        while True:
            question = click.prompt("LLaMa - Ask anything you'd like: (type 'exit' to quit)")

            if question.lower() in ["exit"]:
                click.echo("Thanks for chatting!")
                break

            self.conversation_history.append({"role": "user", "content": question})

            input_data = {
                "top_p": 0.9,
                "prompt": self._create_prompt(question),
                "min_tokens": 0,
                "temperature": 0.6,
                "presence_penalty": 1.15
            }

            try:
                # Stream the response from the model
                streamed_response = ""
                for event in replicate.stream(self.model_version, input=input_data):
                    streamed_response += str(event)
                    click.echo(str(event), nl=False)  # Print the event in real-time

                # Process the complete response
                answer = streamed_response.strip()
                self.conversation_history.append({"role": "assistant", "content": answer})

                # Save the interaction in the database
                self.save_interaction(question, answer)

                click.echo(f"LLaMa says: {answer}")

            except Exception as e:
                click.echo(f"An error occurred: {e}")

    def _create_prompt(self, user_input):
        return f"<|begin_of_text|><|start_header_id|>system<|end_header_id|>\n\nYou are a helpful assistant<|eot_id|><|start_header_id|>user<|end_header_id|>\n\n{user_input}<|eot_id|><|start_header_id|>assistant<|end_header_id|>\n\n"
