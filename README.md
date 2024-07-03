Get out of that hole chatbot.


Full disclosure. I plagarized a good chunk of this code from a tutorial, but it's been heavily modified to serve my purpose.
The original author is [pixiegami](https://github.com/pixegami)


The main changes I intend to make are:
# - to utilize Groq instead of Ollama for the inference; I'm looking to use mixtral 7x22b.
- I want this to run in a container.
- I want this to have a simple gui it starts up.
- I eventually want this to serve as a "front end" to the "get out of that hole" repo, it would ideally utilize those documents for RAG, which then anyone can question.
- I want better logging.
- I want a graphql connector to connect the docker to another container that's going to serve a frontend.
# - I need to replace the embeddings function with something other than ollama.