Get out of that hole chatbot.


Full disclosure. This code was heavily modified from [pixiegami](https://github.com/pixegami)s tutorial.

The sources I used for this code are the groq documentation, pixiegami's rag tutorial, cohere's embeddings tutorial and documentation.


The main changes I intend to make are:

- ~~to utilize Groq instead of Ollama for the inference; I'm looking to use mixtral 7x22b.~~
- ~~I want this to run in a container.~~
- ~~I want this to have a simple gui it starts up.~~
- ~~I eventually want this to serve as a "front end" to the "get out of that hole" repo, it would ideally utilize those documents for RAG, which then anyone can question.~~
- I want better logging.
- ~~I need to replace the embeddings function with something other than ollama.~~
- I need to fix the various bugs.