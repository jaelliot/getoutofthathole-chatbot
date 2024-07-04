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
- Replace the pdf functionality with markdown. That way the file can retain formatting, but be much smaller.
- I need to optimize the chunk size and overlapping. The size is currently at 800 for chunk size, and 80 for the overlap.
- Look into a lightweight vector index for efficient searching and retrieval.
- enable conditional database loading; that way I can save resources avoiding redundant operations.
- Implement lazy loading to free up resources at startup.
- implement result caching to store results.
- refactor to utilize OOP principles; break the files down into smaller modules which follow OOP principles. 
- I need to make various bits asynchronous to avoid locking up the app.
- I need to figure out how to make an efficient data structure.
- I need to implement lazy loading for the UI Components.
- I need to implement lru-caching and st.cache_data (follow best practices for caching; utilize cache invalidation, cache size, TTL)
- Give the caching functions their own files.
- integrate robust error handling into the code; for example include permissions checks for anything which interacts with the databases.
