from langchain_core.prompts import ChatPromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser

from dotenv import load_dotenv

load_dotenv()  # Remember to use .env in production

llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash-lite", temperature=0)
prompt = ChatPromptTemplate.from_template(
    """
    Please analyze the following HTML table and convert its information into a single, well-written, narrative paragraph.
    The paragraph should fluently summarize the key data and relationships presented in the table.
    Do not start with phrases like "This table shows..." or "The paragraph describes...".
    Directly present the information as a descriptive summary.

    **HTML Table:**
    ```html
    {table_html}
    ```
    """
)
output_parser = StrOutputParser()
chain = prompt | llm | output_parser