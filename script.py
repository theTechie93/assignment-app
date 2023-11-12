import os
import sys

from langchain.chains import ConversationalRetrievalChain
from langchain.chat_models import ChatOpenAI
from langchain.document_loaders import TextLoader
from langchain.indexes import VectorstoreIndexCreator


import constants

# Set a openai key to access the openai apis
os.environ["OPENAI_API_KEY"] = constants.API_KEY

# Set initial user query to none
query = None


if len(sys.argv) > 1:
    # Get the asked query from the terminal arguments
    query = sys.argv[1]

# load the data to train the AI model
loader = TextLoader("data/data.json")
index = VectorstoreIndexCreator().from_loaders([loader])

# Get the Conversational Change for asked query
chain = ConversationalRetrievalChain.from_llm(
    llm=ChatOpenAI(model="gpt-3.5-turbo"),
    retriever=index.vectorstore.as_retriever(search_kwargs={"k": 1}),
)

# Initial Script which will run when app starts
chat_history = []
while True:
    # As user a query
    if not query:
        query = input("Ask me a trip suggestions: ")
    if query in ['quit', 'q', 'exit']:
        sys.exit()

    # Get response from the model for designed data
    result = chain({"question": query, "chat_history": chat_history})
    print(result['answer'])

    # Update chat history, which can be used to retrieve response for repeated questions
    chat_history.append((query, result['answer']))
    query = None
