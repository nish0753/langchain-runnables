from langchain_groq import ChatGroq
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableSequence

load_dotenv()
model = ChatGroq(model="llama-3.3-70b-versatile")
parser = StrOutputParser()

prompt1 = PromptTemplate(
    template = 'Write a joke about {topic}',
    input_variables = ['topic']
)

prompt2 = PromptTemplate(
    template = 'Explain the following joke: {joke}',
    input_variables = ['joke']
)

chain = RunnableSequence(prompt1,model,parser,prompt2,model,parser)
print(chain.invoke({'topic':'AI'}))
chain.get_graph().print_ascii()
