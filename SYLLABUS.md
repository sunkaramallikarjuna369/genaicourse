# GenAI 50-Day Course - Complete Syllabus

## Course Overview

This is a fast-track 50-day course (1 hour per day) designed for BTech freshers with no prior knowledge. By the end, you will be ready for GenAI developer job interviews.

---

## Module 0: Setup & Python Essentials (Days 1-3)

### Day 1: Welcome & Environment Setup
**What you'll learn:** How to set up your computer for AI development

**Topics:**
- What is Generative AI? (Simple explanation with examples)
- Why learn GenAI? (Job opportunities)
- Installing Python on your computer
- Installing VS Code (code editor)
- Creating your first Python file

**Simple Exercise:**
- Install Python and VS Code
- Create a file called `hello.py`
- Write: `print("Hello, I am learning GenAI!")`
- Run it and see the output

---

### Day 2: Python Basics - Part 1
**What you'll learn:** Basic Python programming

**Topics:**
- Variables (storing information)
- Data types (numbers, text, true/false)
- Print statements (showing output)
- Taking input from user
- Simple math operations

**Simple Exercise:**
```python
# Create a program that asks for your name and age
name = input("What is your name? ")
age = input("What is your age? ")
print("Hello " + name + "! You are " + age + " years old.")
```

---

### Day 3: Python Basics - Part 2
**What you'll learn:** Lists, loops, and functions

**Topics:**
- Lists (storing multiple items)
- For loops (repeating actions)
- If-else (making decisions)
- Functions (reusable code blocks)

**Simple Exercise:**
```python
# Create a list of your favorite foods and print each one
foods = ["pizza", "biryani", "dosa"]
for food in foods:
    print("I like " + food)

# Create a simple function
def greet(name):
    return "Hello, " + name + "!"

print(greet("Student"))
```

---

## Module 1: Web & Data Fundamentals (Days 4-7)

### Day 4: Working with Files
**What you'll learn:** Reading and writing files in Python

**Topics:**
- Opening files
- Reading file content
- Writing to files
- Working with text files

**Simple Exercise:**
```python
# Write to a file
with open("my_notes.txt", "w") as file:
    file.write("Today I learned about files in Python!")

# Read from a file
with open("my_notes.txt", "r") as file:
    content = file.read()
    print(content)
```

---

### Day 5: JSON - The Language of APIs
**What you'll learn:** Working with JSON data

**Topics:**
- What is JSON? (Data format used everywhere)
- Reading JSON files
- Creating JSON data
- Converting between Python and JSON

**Simple Exercise:**
```python
import json

# Create a dictionary (like JSON)
student = {
    "name": "Rahul",
    "age": 20,
    "subjects": ["Math", "Physics", "AI"]
}

# Convert to JSON string
json_string = json.dumps(student)
print(json_string)

# Convert back to Python
data = json.loads(json_string)
print(data["name"])
```

---

### Day 6: Making API Calls
**What you'll learn:** How to talk to web services

**Topics:**
- What is an API? (Simple explanation)
- Installing the `requests` library
- Making GET requests
- Understanding responses

**Simple Exercise:**
```python
import requests

# Get a random joke from the internet
response = requests.get("https://official-joke-api.appspot.com/random_joke")
joke = response.json()

print("Setup:", joke["setup"])
print("Punchline:", joke["punchline"])
```

---

### Day 7: Introduction to FastAPI
**What you'll learn:** Creating your own API

**Topics:**
- What is FastAPI?
- Creating a simple server
- Making endpoints
- Testing your API

**Simple Exercise:**
```python
# Install: pip install fastapi uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Welcome to my first API!"}

@app.get("/greet/{name}")
def greet(name: str):
    return {"message": f"Hello, {name}!"}

# Run with: uvicorn filename:app --reload
```

---

## Module 2: LLM Fundamentals & Prompt Engineering (Days 8-14)

### Day 8: What are Large Language Models?
**What you'll learn:** Understanding how AI chatbots work

**Topics:**
- What is an LLM? (Simple explanation)
- How do ChatGPT, Gemini work?
- Tokens (how AI reads text)
- Context window (AI's memory limit)

**Simple Exercise:**
- Go to ChatGPT or Gemini
- Ask: "Explain what you are in simple words"
- Ask: "Count the words in this sentence: I love learning AI"
- Notice how it understands and responds

---

### Day 9: Getting API Access
**What you'll learn:** Setting up API keys to use AI in your code

**Topics:**
- Creating accounts (OpenAI, Google AI, Groq)
- Getting API keys
- Keeping keys safe (environment variables)
- Free tier limits

**Simple Exercise:**
```python
# Create a .env file with your API key
# OPENAI_API_KEY=your-key-here

import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
print("API key loaded!" if api_key else "No API key found")
```

---

### Day 10: Your First LLM API Call
**What you'll learn:** Making AI respond through code

**Topics:**
- Installing OpenAI library
- Making a simple API call
- Understanding the response
- Handling errors

**Simple Exercise:**
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Say hello in 3 different languages"}
    ]
)

print(response.choices[0].message.content)
```

---

### Day 11: Prompt Engineering Basics
**What you'll learn:** How to write better prompts

**Topics:**
- What is prompt engineering?
- Clear instructions
- Giving examples (few-shot)
- Setting the context

**Simple Exercise:**
```python
# Bad prompt
bad_prompt = "Write about dogs"

# Good prompt
good_prompt = """
You are a friendly teacher explaining to a 10-year-old.
Topic: Dogs
Include: 3 interesting facts
Length: 5 sentences
"""

# Try both and compare the results!
```

---

### Day 12: System Messages & Roles
**What you'll learn:** Controlling AI behavior

**Topics:**
- System message (AI's personality)
- User message (your question)
- Assistant message (AI's response)
- Creating different AI personalities

**Simple Exercise:**
```python
from openai import OpenAI
client = OpenAI()

# Create a helpful teacher
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a friendly teacher who explains things simply. Use examples from daily life."},
        {"role": "user", "content": "What is machine learning?"}
    ]
)

print(response.choices[0].message.content)
```

---

### Day 13: Structured Output (JSON)
**What you'll learn:** Getting AI to respond in a specific format

**Topics:**
- Why structured output matters
- Asking for JSON responses
- Parsing AI responses
- Handling format errors

**Simple Exercise:**
```python
from openai import OpenAI
import json

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "Always respond in JSON format only."},
        {"role": "user", "content": """
        Give me information about India in this exact JSON format:
        {
            "country": "name",
            "capital": "city name",
            "population": "number",
            "languages": ["list", "of", "languages"]
        }
        """}
    ]
)

# Parse the JSON response
data = json.loads(response.choices[0].message.content)
print("Capital:", data["capital"])
```

---

### Day 14: Prompt Patterns & Templates
**What you'll learn:** Reusable prompt techniques

**Topics:**
- Common prompt patterns
- Creating prompt templates
- Chain of thought prompting
- Building a prompt library

**Simple Exercise:**
```python
# Create reusable prompt templates

def summarize_prompt(text, length="short"):
    return f"""
    Summarize the following text in a {length} paragraph.
    
    Text: {text}
    
    Summary:
    """

def translate_prompt(text, language):
    return f"""
    Translate the following text to {language}.
    Keep the meaning exactly the same.
    
    Text: {text}
    
    Translation:
    """

# Use the templates
text = "Artificial Intelligence is changing the world."
print(summarize_prompt(text))
print(translate_prompt(text, "Hindi"))
```

---

## Module 3: LLM Application Development (Days 15-20)

### Day 15: Building a Chat Application
**What you'll learn:** Creating a conversation with AI

**Topics:**
- Maintaining conversation history
- Multi-turn conversations
- Memory in chatbots

**Simple Exercise:**
```python
from openai import OpenAI
client = OpenAI()

# Store conversation history
messages = [
    {"role": "system", "content": "You are a helpful assistant."}
]

def chat(user_message):
    messages.append({"role": "user", "content": user_message})
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=messages
    )
    
    assistant_message = response.choices[0].message.content
    messages.append({"role": "assistant", "content": assistant_message})
    
    return assistant_message

# Have a conversation
print(chat("My name is Rahul"))
print(chat("What is my name?"))  # It remembers!
```

---

### Day 16: Streaming Responses
**What you'll learn:** Getting AI responses word by word

**Topics:**
- What is streaming?
- Why use streaming? (Better user experience)
- Implementing streaming
- Handling stream chunks

**Simple Exercise:**
```python
from openai import OpenAI
client = OpenAI()

# Stream the response
stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Tell me a short story about a robot"}],
    stream=True
)

# Print each word as it comes
print("Story: ", end="")
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
print()  # New line at end
```

---

### Day 17: Error Handling & Retries
**What you'll learn:** Making your app reliable

**Topics:**
- Common API errors
- Try-except blocks
- Automatic retries
- Rate limiting

**Simple Exercise:**
```python
from openai import OpenAI
import time

client = OpenAI()

def safe_api_call(prompt, max_retries=3):
    for attempt in range(max_retries):
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}]
            )
            return response.choices[0].message.content
        except Exception as e:
            print(f"Attempt {attempt + 1} failed: {e}")
            if attempt < max_retries - 1:
                time.sleep(2)  # Wait before retry
    return "Sorry, something went wrong."

# Test it
result = safe_api_call("Say hello")
print(result)
```

---

### Day 18: Function Calling / Tools
**What you'll learn:** Making AI use tools

**Topics:**
- What is function calling?
- Defining functions for AI
- AI deciding which function to use
- Executing functions

**Simple Exercise:**
```python
from openai import OpenAI
import json

client = OpenAI()

# Define a simple tool
tools = [
    {
        "type": "function",
        "function": {
            "name": "get_weather",
            "description": "Get the weather for a city",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {"type": "string", "description": "City name"}
                },
                "required": ["city"]
            }
        }
    }
]

# Our fake weather function
def get_weather(city):
    return f"The weather in {city} is sunny, 25°C"

# Ask AI about weather
response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What's the weather in Mumbai?"}],
    tools=tools
)

# Check if AI wants to use a tool
if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = get_weather(args["city"])
    print(result)
```

---

### Day 19: Building an API with LLM
**What you'll learn:** Creating a web API powered by AI

**Topics:**
- Combining FastAPI with LLM
- Creating AI endpoints
- Handling requests
- Returning responses

**Simple Exercise:**
```python
from fastapi import FastAPI
from openai import OpenAI
from pydantic import BaseModel

app = FastAPI()
client = OpenAI()

class Question(BaseModel):
    text: str

@app.post("/ask")
def ask_ai(question: Question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question.text}]
    )
    return {"answer": response.choices[0].message.content}

@app.post("/summarize")
def summarize(question: Question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "Summarize the text in 2 sentences."},
            {"role": "user", "content": question.text}
        ]
    )
    return {"summary": response.choices[0].message.content}

# Run: uvicorn filename:app --reload
```

---

### Day 20: Mini Project - CLI Assistant
**What you'll learn:** Building a complete command-line AI assistant

**Topics:**
- Putting everything together
- User-friendly interface
- Multiple features
- Project structure

**Simple Exercise:**
```python
from openai import OpenAI

client = OpenAI()

def assistant():
    print("=" * 50)
    print("Welcome to AI Assistant!")
    print("Commands: 'quit' to exit, 'clear' to reset")
    print("=" * 50)
    
    messages = [
        {"role": "system", "content": "You are a helpful, friendly assistant. Keep responses brief."}
    ]
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        elif user_input.lower() == 'clear':
            messages = [messages[0]]  # Keep system message
            print("Conversation cleared!")
            continue
        elif not user_input:
            continue
        
        messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=messages
        )
        
        reply = response.choices[0].message.content
        messages.append({"role": "assistant", "content": reply})
        
        print(f"\nAssistant: {reply}")

if __name__ == "__main__":
    assistant()
```

---

## Module 4: RAG - Retrieval-Augmented Generation (Days 21-29)

### Day 21: What is RAG?
**What you'll learn:** Understanding RAG and why it's important

**Topics:**
- Problem: AI doesn't know your data
- Solution: RAG (give AI your documents)
- How RAG works (simple explanation)
- Real-world examples

**Simple Exercise:**
- Think of 3 situations where you'd want AI to answer from YOUR documents
- Examples: Company FAQ, College handbook, Product manual
- Write down why normal ChatGPT can't help in these cases

---

### Day 22: Text Embeddings
**What you'll learn:** Converting text to numbers AI understands

**Topics:**
- What are embeddings? (Text as numbers)
- Why embeddings matter
- Creating embeddings
- Comparing text similarity

**Simple Exercise:**
```python
from openai import OpenAI

client = OpenAI()

def get_embedding(text):
    response = client.embeddings.create(
        model="text-embedding-3-small",
        input=text
    )
    return response.data[0].embedding

# Get embeddings for similar sentences
text1 = "I love eating pizza"
text2 = "Pizza is my favorite food"
text3 = "The weather is nice today"

emb1 = get_embedding(text1)
emb2 = get_embedding(text2)
emb3 = get_embedding(text3)

print(f"Embedding length: {len(emb1)}")
print("Text 1 and 2 are about the same topic (pizza)")
print("Text 3 is about something different (weather)")
```

---

### Day 23: Vector Databases
**What you'll learn:** Storing and searching embeddings

**Topics:**
- What is a vector database?
- Why we need it for RAG
- Introduction to ChromaDB
- Storing and retrieving vectors

**Simple Exercise:**
```python
# Install: pip install chromadb
import chromadb

# Create a database
client = chromadb.Client()
collection = client.create_collection("my_documents")

# Add some documents
documents = [
    "Python is a programming language",
    "Machine learning is a type of AI",
    "Pizza is a popular Italian food",
    "India is a country in Asia"
]

collection.add(
    documents=documents,
    ids=["doc1", "doc2", "doc3", "doc4"]
)

# Search for similar documents
results = collection.query(
    query_texts=["Tell me about coding"],
    n_results=2
)

print("Most relevant documents:")
for doc in results['documents'][0]:
    print(f"- {doc}")
```

---

### Day 24: Document Loading
**What you'll learn:** Reading different file types

**Topics:**
- Loading text files
- Loading PDF files
- Loading web pages
- Handling different formats

**Simple Exercise:**
```python
# Install: pip install pypdf

# Load a text file
def load_text_file(filepath):
    with open(filepath, 'r') as f:
        return f.read()

# Load a PDF file
from pypdf import PdfReader

def load_pdf(filepath):
    reader = PdfReader(filepath)
    text = ""
    for page in reader.pages:
        text += page.extract_text()
    return text

# Example usage
# text_content = load_text_file("notes.txt")
# pdf_content = load_pdf("document.pdf")
```

---

### Day 25: Text Chunking
**What you'll learn:** Breaking documents into smaller pieces

**Topics:**
- Why chunking matters
- Different chunking strategies
- Chunk size and overlap
- Best practices

**Simple Exercise:**
```python
def simple_chunk(text, chunk_size=500, overlap=50):
    """Split text into overlapping chunks"""
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap  # Overlap with previous chunk
    
    return chunks

# Example
long_text = "This is a very long document. " * 100
chunks = simple_chunk(long_text, chunk_size=200, overlap=20)

print(f"Total chunks: {len(chunks)}")
print(f"First chunk: {chunks[0][:50]}...")
```

---

### Day 26: Building a Simple RAG System
**What you'll learn:** Putting RAG components together

**Topics:**
- Complete RAG pipeline
- Loading → Chunking → Embedding → Storing
- Retrieving relevant chunks
- Generating answers

**Simple Exercise:**
```python
import chromadb
from openai import OpenAI

client = OpenAI()
chroma = chromadb.Client()
collection = chroma.create_collection("knowledge_base")

# Step 1: Add your knowledge
knowledge = [
    "Our company was founded in 2020 in Bangalore.",
    "We have 500 employees across India.",
    "Our main product is an AI-powered chatbot.",
    "Office hours are 9 AM to 6 PM, Monday to Friday.",
    "Contact HR at hr@company.com for queries."
]

collection.add(documents=knowledge, ids=[f"doc{i}" for i in range(len(knowledge))])

# Step 2: RAG function
def ask_with_rag(question):
    # Find relevant documents
    results = collection.query(query_texts=[question], n_results=2)
    context = "\n".join(results['documents'][0])
    
    # Ask AI with context
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Answer based on this information:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

# Test it
print(ask_with_rag("When was the company founded?"))
print(ask_with_rag("How can I contact HR?"))
```

---

### Day 27: Adding Citations
**What you'll learn:** Showing sources for AI answers

**Topics:**
- Why citations matter
- Tracking source documents
- Displaying references
- Building trust with users

**Simple Exercise:**
```python
def ask_with_citations(question):
    # Find relevant documents with metadata
    results = collection.query(
        query_texts=[question], 
        n_results=2,
        include=["documents", "metadatas"]
    )
    
    context = "\n".join(results['documents'][0])
    sources = results['ids'][0]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Answer based on this information:\n{context}\n\nBe specific and accurate."},
            {"role": "user", "content": question}
        ]
    )
    
    answer = response.choices[0].message.content
    
    return {
        "answer": answer,
        "sources": sources,
        "context_used": results['documents'][0]
    }

# Test
result = ask_with_citations("What are the office hours?")
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
```

---

### Day 28: RAG Evaluation
**What you'll learn:** Testing if your RAG system works well

**Topics:**
- What makes a good RAG system?
- Testing retrieval quality
- Testing answer quality
- Simple evaluation metrics

**Simple Exercise:**
```python
# Create test questions with expected answers
test_cases = [
    {
        "question": "When was the company founded?",
        "expected_keywords": ["2020", "Bangalore"]
    },
    {
        "question": "How many employees?",
        "expected_keywords": ["500"]
    }
]

def evaluate_rag(test_cases):
    results = []
    for test in test_cases:
        answer = ask_with_rag(test["question"])
        
        # Check if expected keywords are in answer
        found = [kw for kw in test["expected_keywords"] if kw.lower() in answer.lower()]
        score = len(found) / len(test["expected_keywords"])
        
        results.append({
            "question": test["question"],
            "answer": answer,
            "score": score
        })
        print(f"Q: {test['question']}")
        print(f"A: {answer}")
        print(f"Score: {score * 100}%\n")
    
    return results

evaluate_rag(test_cases)
```

---

### Day 29: RAG Project - Document Q&A Bot
**What you'll learn:** Building a complete RAG application

**Topics:**
- End-to-end RAG project
- User-friendly interface
- Error handling
- Project organization

**Simple Exercise:**
```python
# Complete RAG Chatbot Project
import chromadb
from openai import OpenAI

class DocumentQABot:
    def __init__(self):
        self.client = OpenAI()
        self.chroma = chromadb.Client()
        self.collection = self.chroma.create_collection("docs")
    
    def add_documents(self, documents):
        """Add documents to knowledge base"""
        self.collection.add(
            documents=documents,
            ids=[f"doc_{i}" for i in range(len(documents))]
        )
        print(f"Added {len(documents)} documents")
    
    def ask(self, question):
        """Ask a question and get answer with sources"""
        # Retrieve
        results = self.collection.query(query_texts=[question], n_results=3)
        context = "\n".join(results['documents'][0])
        
        # Generate
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Answer based only on this context:\n{context}\n\nIf the answer is not in the context, say 'I don't have information about that.'"},
                {"role": "user", "content": question}
            ]
        )
        
        return {
            "answer": response.choices[0].message.content,
            "sources": results['documents'][0]
        }

# Usage
bot = DocumentQABot()
bot.add_documents([
    "Python was created by Guido van Rossum in 1991.",
    "Python is known for its simple and readable syntax.",
    "Popular Python frameworks include Django and Flask.",
    "Python is widely used in AI and machine learning."
])

result = bot.ask("Who created Python?")
print(f"Answer: {result['answer']}")
```

---

## Module 5: AI Agents & Workflows (Days 30-35)

### Day 30: What are AI Agents?
**What you'll learn:** Understanding AI agents

**Topics:**
- What is an AI agent?
- Agents vs simple chatbots
- Tools and actions
- Real-world agent examples

**Simple Exercise:**
- Think about a personal assistant
- List 5 tasks it should be able to do
- For each task, what "tools" would it need?
- Example: "Check weather" needs a weather API tool

---

### Day 31: Building a Simple Agent
**What you'll learn:** Creating your first AI agent

**Topics:**
- Agent architecture
- Tool definition
- Decision making
- Executing actions

**Simple Exercise:**
```python
from openai import OpenAI
import json

client = OpenAI()

# Define tools the agent can use
tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform math calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string", "description": "Math expression like '2 + 2'"}
                },
                "required": ["expression"]
            }
        }
    },
    {
        "type": "function",
        "function": {
            "name": "get_time",
            "description": "Get current time",
            "parameters": {"type": "object", "properties": {}}
        }
    }
]

# Tool implementations
def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Error in calculation"

def get_time():
    from datetime import datetime
    return datetime.now().strftime("%H:%M:%S")

# Simple agent
def agent(user_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
        tools=tools
    )
    
    message = response.choices[0].message
    
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        tool_name = tool_call.function.name
        args = json.loads(tool_call.function.arguments)
        
        if tool_name == "calculator":
            result = calculator(args["expression"])
        elif tool_name == "get_time":
            result = get_time()
        
        return f"Used {tool_name}: {result}"
    
    return message.content

print(agent("What is 25 * 4?"))
print(agent("What time is it?"))
```

---

### Day 32: Multi-Tool Agents
**What you'll learn:** Agents with multiple capabilities

**Topics:**
- Adding more tools
- Tool selection logic
- Chaining tool calls
- Handling complex requests

**Simple Exercise:**
```python
# Agent with multiple tools
import requests

def search_wikipedia(query):
    """Search Wikipedia for information"""
    url = f"https://en.wikipedia.org/api/rest_v1/page/summary/{query}"
    response = requests.get(url)
    if response.status_code == 200:
        return response.json().get("extract", "No information found")[:500]
    return "Could not find information"

def translate_text(text, target_language):
    """Translate text (simplified - uses AI)"""
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Translate to {target_language}. Only output the translation."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

# Test the tools
print(search_wikipedia("Python_programming"))
print(translate_text("Hello, how are you?", "Hindi"))
```

---

### Day 33: Agent Memory
**What you'll learn:** Giving agents memory

**Topics:**
- Short-term memory (conversation)
- Long-term memory (stored facts)
- Memory management
- When to remember/forget

**Simple Exercise:**
```python
class AgentWithMemory:
    def __init__(self):
        self.client = OpenAI()
        self.conversation = []
        self.facts = []  # Long-term memory
    
    def remember_fact(self, fact):
        """Store important information"""
        self.facts.append(fact)
        print(f"Remembered: {fact}")
    
    def chat(self, message):
        # Include facts in context
        system_message = "You are a helpful assistant."
        if self.facts:
            system_message += f"\n\nRemember these facts:\n" + "\n".join(self.facts)
        
        self.conversation.append({"role": "user", "content": message})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_message}] + self.conversation
        )
        
        reply = response.choices[0].message.content
        self.conversation.append({"role": "assistant", "content": reply})
        
        return reply

# Usage
agent = AgentWithMemory()
agent.remember_fact("User's name is Priya")
agent.remember_fact("User is studying Computer Science")

print(agent.chat("Hello!"))
print(agent.chat("What do you know about me?"))
```

---

### Day 34: Workflow Automation
**What you'll learn:** Creating multi-step workflows

**Topics:**
- What are workflows?
- Sequential steps
- Conditional logic
- Error handling in workflows

**Simple Exercise:**
```python
class SimpleWorkflow:
    def __init__(self):
        self.client = OpenAI()
    
    def research_and_summarize(self, topic):
        """Workflow: Research a topic and create a summary"""
        print(f"Step 1: Researching {topic}...")
        
        # Step 1: Generate research points
        research = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"List 5 key points about {topic}"}]
        ).choices[0].message.content
        
        print("Step 2: Creating summary...")
        
        # Step 2: Summarize the research
        summary = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Create a brief, easy-to-understand summary."},
                {"role": "user", "content": f"Summarize this:\n{research}"}
            ]
        ).choices[0].message.content
        
        print("Step 3: Translating to Hindi...")
        
        # Step 3: Translate
        hindi = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Translate to Hindi:\n{summary}"}]
        ).choices[0].message.content
        
        return {
            "research": research,
            "summary": summary,
            "hindi_summary": hindi
        }

# Run workflow
workflow = SimpleWorkflow()
result = workflow.research_and_summarize("Artificial Intelligence")
print("\n=== Final Summary ===")
print(result["summary"])
```

---

### Day 35: Agent Project - Research Assistant
**What you'll learn:** Building a complete agent application

**Topics:**
- Complete agent project
- Multiple tools integration
- User interaction
- Practical use case

**Simple Exercise:**
```python
class ResearchAssistant:
    def __init__(self):
        self.client = OpenAI()
        self.research_notes = []
    
    def search(self, query):
        """Search for information"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": f"Provide factual information about: {query}"}]
        )
        info = response.choices[0].message.content
        self.research_notes.append({"query": query, "info": info})
        return info
    
    def summarize_research(self):
        """Summarize all research"""
        if not self.research_notes:
            return "No research notes yet."
        
        all_notes = "\n\n".join([f"Topic: {n['query']}\n{n['info']}" for n in self.research_notes])
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Create a comprehensive summary of all research."},
                {"role": "user", "content": all_notes}
            ]
        )
        return response.choices[0].message.content
    
    def generate_report(self, title):
        """Generate a formatted report"""
        summary = self.summarize_research()
        
        report = f"""
# Research Report: {title}

## Summary
{summary}

## Sources Researched
"""
        for note in self.research_notes:
            report += f"- {note['query']}\n"
        
        return report

# Usage
assistant = ResearchAssistant()
assistant.search("Benefits of renewable energy")
assistant.search("Solar power technology")
assistant.search("Wind energy advantages")

report = assistant.generate_report("Renewable Energy Overview")
print(report)
```

---

## Module 6: Fine-tuning & Model Adaptation (Days 36-40)

### Day 36: Understanding Fine-tuning
**What you'll learn:** What fine-tuning is and when to use it

**Topics:**
- What is fine-tuning?
- Fine-tuning vs Prompt Engineering vs RAG
- When to fine-tune
- Costs and considerations

**Simple Exercise:**
- Create a comparison table:
  | Method | When to Use | Pros | Cons |
  |--------|-------------|------|------|
  | Prompt Engineering | | | |
  | RAG | | | |
  | Fine-tuning | | | |

---

### Day 37: Preparing Training Data
**What you'll learn:** Creating datasets for fine-tuning

**Topics:**
- Data format requirements
- Creating training examples
- Data quality importance
- JSONL format

**Simple Exercise:**
```python
import json

# Create training data for a customer support bot
training_data = [
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for TechStore."},
            {"role": "user", "content": "How do I return a product?"},
            {"role": "assistant", "content": "To return a product at TechStore: 1) Log into your account, 2) Go to 'My Orders', 3) Click 'Return' next to the item, 4) Print the return label, 5) Ship within 7 days. Refund processes in 3-5 business days."}
        ]
    },
    {
        "messages": [
            {"role": "system", "content": "You are a helpful customer support agent for TechStore."},
            {"role": "user", "content": "What's your refund policy?"},
            {"role": "assistant", "content": "TechStore offers a 30-day refund policy for all products. Items must be unused and in original packaging. Electronics have a 15-day return window. Refunds are processed to the original payment method within 3-5 business days."}
        ]
    }
]

# Save as JSONL file
with open("training_data.jsonl", "w") as f:
    for item in training_data:
        f.write(json.dumps(item) + "\n")

print("Training data saved!")
print(f"Total examples: {len(training_data)}")
```

---

### Day 38: Fine-tuning Process
**What you'll learn:** How to fine-tune a model

**Topics:**
- Uploading training data
- Starting fine-tuning job
- Monitoring progress
- Using fine-tuned model

**Simple Exercise:**
```python
from openai import OpenAI

client = OpenAI()

# Step 1: Upload training file
# file = client.files.create(
#     file=open("training_data.jsonl", "rb"),
#     purpose="fine-tune"
# )
# print(f"File ID: {file.id}")

# Step 2: Create fine-tuning job
# job = client.fine_tuning.jobs.create(
#     training_file=file.id,
#     model="gpt-3.5-turbo"
# )
# print(f"Job ID: {job.id}")

# Step 3: Check job status
# status = client.fine_tuning.jobs.retrieve(job.id)
# print(f"Status: {status.status}")

# Step 4: Use fine-tuned model (after completion)
# response = client.chat.completions.create(
#     model="ft:gpt-3.5-turbo:your-org::your-model-id",
#     messages=[{"role": "user", "content": "How do I return a product?"}]
# )

print("Fine-tuning steps demonstrated!")
print("Note: Actual fine-tuning requires API credits")
```

---

### Day 39: LoRA and Efficient Fine-tuning
**What you'll learn:** Modern fine-tuning techniques

**Topics:**
- What is LoRA?
- Why LoRA is efficient
- Open-source fine-tuning
- Hugging Face basics

**Simple Exercise:**
```python
# Conceptual understanding of LoRA
# (Actual implementation requires GPU)

"""
LoRA (Low-Rank Adaptation) Explained Simply:

Instead of changing ALL the model's parameters (billions!),
LoRA only changes a SMALL part (millions).

Think of it like this:
- Full fine-tuning = Rebuilding the entire house
- LoRA = Just redecorating one room

Benefits:
1. Much faster training
2. Uses less memory
3. Smaller file sizes
4. Can switch between different "styles" easily

Example use cases:
- Train a model to write like Shakespeare
- Train a model for medical terminology
- Train a model for your company's style
"""

# Pseudo-code for LoRA fine-tuning
"""
from peft import LoraConfig, get_peft_model
from transformers import AutoModelForCausalLM

# Load base model
model = AutoModelForCausalLM.from_pretrained("meta-llama/Llama-2-7b")

# Configure LoRA
lora_config = LoraConfig(
    r=16,  # Rank (smaller = more efficient)
    lora_alpha=32,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.05
)

# Apply LoRA
model = get_peft_model(model, lora_config)

# Now train with your data!
"""

print("LoRA concept explained!")
```

---

### Day 40: Choosing the Right Approach
**What you'll learn:** Decision framework for model customization

**Topics:**
- Decision flowchart
- Cost-benefit analysis
- Hybrid approaches
- Best practices

**Simple Exercise:**
```python
def recommend_approach(requirements):
    """
    Help decide: Prompt Engineering vs RAG vs Fine-tuning
    """
    
    questions = {
        "need_custom_knowledge": "Do you need the AI to know specific information (like your company docs)?",
        "need_custom_style": "Do you need the AI to respond in a specific style/format?",
        "have_training_data": "Do you have 100+ examples of ideal responses?",
        "have_budget": "Do you have budget for fine-tuning ($50+)?",
        "need_real_time_updates": "Does your information change frequently?"
    }
    
    # Decision logic
    if requirements.get("need_custom_knowledge") and requirements.get("need_real_time_updates"):
        return "RAG - Best for dynamic knowledge that changes"
    
    if requirements.get("need_custom_style") and requirements.get("have_training_data") and requirements.get("have_budget"):
        return "Fine-tuning - Best for consistent custom behavior"
    
    if requirements.get("need_custom_knowledge") and not requirements.get("need_real_time_updates"):
        return "RAG or Fine-tuning - Depends on data size"
    
    return "Prompt Engineering - Start here, it's free and fast!"

# Example
my_requirements = {
    "need_custom_knowledge": True,
    "need_custom_style": False,
    "have_training_data": False,
    "have_budget": False,
    "need_real_time_updates": True
}

print(recommend_approach(my_requirements))
```

---

## Module 7: Deployment & Production (Days 41-45)

### Day 41: Introduction to Deployment
**What you'll learn:** Taking your app from laptop to internet

**Topics:**
- What is deployment?
- Development vs Production
- Deployment options
- Basic requirements

**Simple Exercise:**
- List 3 apps you use daily (WhatsApp, YouTube, etc.)
- Think: Where do they run? (Not on your phone!)
- Understand: Your AI app needs a "home" on the internet too

---

### Day 42: Docker Basics
**What you'll learn:** Packaging your app

**Topics:**
- What is Docker?
- Why use containers?
- Creating a Dockerfile
- Building and running containers

**Simple Exercise:**
```dockerfile
# Dockerfile for our AI app
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements first (for caching)
COPY requirements.txt .
RUN pip install -r requirements.txt

# Copy application code
COPY . .

# Expose port
EXPOSE 8000

# Run the app
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

```python
# requirements.txt
fastapi
uvicorn
openai
python-dotenv
```

```bash
# Commands to run
# docker build -t my-ai-app .
# docker run -p 8000:8000 my-ai-app
```

---

### Day 43: Environment Variables & Secrets
**What you'll learn:** Keeping API keys safe

**Topics:**
- Why hide secrets?
- Environment variables
- .env files
- Secret management

**Simple Exercise:**
```python
# NEVER do this:
# api_key = "sk-abc123..."  # BAD! Anyone can see this

# DO this instead:
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Please set OPENAI_API_KEY environment variable")

# Create a .env file (add to .gitignore!)
# .env contents:
# OPENAI_API_KEY=your-key-here

# .gitignore contents:
# .env
# *.pyc
# __pycache__/
```

---

### Day 44: Deploying to Cloud
**What you'll learn:** Putting your app online

**Topics:**
- Cloud platforms (Render, Railway, Fly.io)
- Deployment steps
- Domain names
- Monitoring basics

**Simple Exercise:**
```python
# Complete deployable FastAPI app
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from openai import OpenAI
import os

app = FastAPI(title="My AI API")
client = OpenAI()

class Question(BaseModel):
    text: str

@app.get("/")
def home():
    return {"status": "running", "message": "AI API is live!"}

@app.get("/health")
def health():
    return {"status": "healthy"}

@app.post("/ask")
def ask(question: Question):
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "user", "content": question.text}],
            max_tokens=500
        )
        return {"answer": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Deploy to Render:
# 1. Push code to GitHub
# 2. Connect GitHub to Render
# 3. Set environment variables
# 4. Deploy!
```

---

### Day 45: Security & Best Practices
**What you'll learn:** Making your app safe

**Topics:**
- Prompt injection attacks
- Rate limiting
- Input validation
- Logging and monitoring

**Simple Exercise:**
```python
from fastapi import FastAPI, HTTPException, Request
from slowapi import Limiter
from slowapi.util import get_remote_address
import re

app = FastAPI()
limiter = Limiter(key_func=get_remote_address)

# Security: Input validation
def validate_input(text: str) -> str:
    # Remove potential injection attempts
    dangerous_patterns = [
        r"ignore previous instructions",
        r"forget everything",
        r"you are now",
    ]
    
    for pattern in dangerous_patterns:
        if re.search(pattern, text.lower()):
            raise HTTPException(status_code=400, detail="Invalid input detected")
    
    # Limit length
    if len(text) > 1000:
        raise HTTPException(status_code=400, detail="Input too long")
    
    return text

# Rate limiting: Max 10 requests per minute
@app.post("/ask")
@limiter.limit("10/minute")
def ask(request: Request, question: Question):
    clean_text = validate_input(question.text)
    # ... rest of the code
    
# Logging
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.post("/ask")
def ask(question: Question):
    logger.info(f"Received question: {question.text[:50]}...")
    # ... process
    logger.info("Response sent successfully")
```

---

## Module 8: Capstone Project & Interview Prep (Days 46-50)

### Day 46: Capstone Project Planning
**What you'll learn:** Planning your final project

**Topics:**
- Choosing a project idea
- Project requirements
- Architecture design
- Timeline planning

**Simple Exercise:**
Choose ONE project idea:

1. **Study Buddy Bot** - RAG chatbot for a textbook/course
2. **Customer Support Agent** - Multi-tool support assistant
3. **Content Creator** - Blog/social media content generator
4. **Code Helper** - Programming assistant with examples
5. **Personal Finance Advisor** - Budget and savings assistant

Plan your project:
- What problem does it solve?
- What features will it have?
- What tools/APIs will you use?
- How will users interact with it?

---

### Day 47: Capstone - Building Core Features
**What you'll learn:** Implementing main functionality

**Topics:**
- Setting up project structure
- Implementing core logic
- Testing features
- Iterating on feedback

**Simple Exercise:**
```python
# Example: Study Buddy Bot - Core Structure
import chromadb
from openai import OpenAI
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Study Buddy")
client = OpenAI()
chroma = chromadb.Client()
collection = chroma.create_collection("study_materials")

class StudyRequest(BaseModel):
    question: str
    subject: str = "general"

class StudyBuddy:
    def __init__(self):
        self.client = OpenAI()
    
    def add_study_material(self, content: str, subject: str):
        """Add notes/textbook content"""
        collection.add(
            documents=[content],
            metadatas=[{"subject": subject}],
            ids=[f"doc_{collection.count()}"]
        )
    
    def ask_question(self, question: str, subject: str = None):
        """Ask a question about study materials"""
        # Retrieve relevant content
        where_filter = {"subject": subject} if subject else None
        results = collection.query(
            query_texts=[question],
            n_results=3,
            where=where_filter
        )
        
        context = "\n".join(results['documents'][0]) if results['documents'][0] else ""
        
        # Generate answer
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"You are a helpful study assistant. Use this context to answer:\n{context}\n\nIf the answer isn't in the context, provide general knowledge but mention it."},
                {"role": "user", "content": question}
            ]
        )
        
        return {
            "answer": response.choices[0].message.content,
            "sources_used": len(results['documents'][0])
        }
    
    def generate_quiz(self, topic: str, num_questions: int = 5):
        """Generate practice questions"""
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Create simple multiple choice questions for students."},
                {"role": "user", "content": f"Create {num_questions} quiz questions about {topic}. Format: Question, 4 options (A-D), Correct answer."}
            ]
        )
        return response.choices[0].message.content

buddy = StudyBuddy()

@app.post("/add-material")
def add_material(content: str, subject: str):
    buddy.add_study_material(content, subject)
    return {"status": "Material added"}

@app.post("/ask")
def ask(request: StudyRequest):
    return buddy.ask_question(request.question, request.subject)

@app.get("/quiz/{topic}")
def quiz(topic: str, count: int = 5):
    return {"quiz": buddy.generate_quiz(topic, count)}
```

---

### Day 48: Capstone - UI and Polish
**What you'll learn:** Making your project user-friendly

**Topics:**
- Adding a simple UI (Streamlit)
- Error handling
- User experience improvements
- Documentation

**Simple Exercise:**
```python
# Streamlit UI for Study Buddy
# Install: pip install streamlit

import streamlit as st
from study_buddy import StudyBuddy

st.title("Study Buddy - Your AI Learning Assistant")

# Initialize
if 'buddy' not in st.session_state:
    st.session_state.buddy = StudyBuddy()

# Sidebar for adding materials
with st.sidebar:
    st.header("Add Study Material")
    subject = st.text_input("Subject")
    content = st.text_area("Paste your notes here")
    if st.button("Add Material"):
        if content and subject:
            st.session_state.buddy.add_study_material(content, subject)
            st.success("Material added!")

# Main area
tab1, tab2 = st.tabs(["Ask Questions", "Take Quiz"])

with tab1:
    st.header("Ask a Question")
    question = st.text_input("What would you like to know?")
    if st.button("Ask"):
        if question:
            with st.spinner("Thinking..."):
                result = st.session_state.buddy.ask_question(question)
                st.write(result["answer"])
                st.caption(f"Used {result['sources_used']} sources")

with tab2:
    st.header("Practice Quiz")
    topic = st.text_input("Quiz topic")
    if st.button("Generate Quiz"):
        if topic:
            with st.spinner("Creating quiz..."):
                quiz = st.session_state.buddy.generate_quiz(topic)
                st.write(quiz)

# Run: streamlit run app.py
```

---

### Day 49: Portfolio & Resume
**What you'll learn:** Showcasing your work

**Topics:**
- Creating a GitHub portfolio
- Writing good READMEs
- Resume tips for GenAI roles
- LinkedIn optimization

**Simple Exercise:**
```markdown
# Project README Template

## Project Name
One line description of what it does.

## Demo
[Link to live demo or video]

## Features
- Feature 1
- Feature 2
- Feature 3

## Tech Stack
- Python 3.10
- FastAPI
- OpenAI API
- ChromaDB
- Streamlit

## Installation
```bash
git clone https://github.com/yourusername/project
cd project
pip install -r requirements.txt
```

## Usage
```bash
# Set your API key
export OPENAI_API_KEY=your-key

# Run the app
streamlit run app.py
```

## Architecture
[Simple diagram or explanation]

## What I Learned
- How to build RAG applications
- Prompt engineering techniques
- Deploying AI applications

## Future Improvements
- Add feature X
- Improve Y
- Optimize Z

## Contact
Your Name - your.email@example.com
```

---

### Day 50: Interview Preparation & Course Completion
**What you'll learn:** Preparing for GenAI job interviews

**Topics:**
- Common interview questions
- Technical concepts review
- Behavioral questions
- Mock interview practice

**Simple Exercise:**

**Technical Questions to Practice:**

1. What is the difference between RAG and fine-tuning?
2. Explain how embeddings work in simple terms.
3. What is prompt injection and how do you prevent it?
4. How would you reduce hallucinations in an LLM application?
5. Explain the concept of tokens and context window.
6. What is temperature in LLM APIs?
7. How do AI agents differ from simple chatbots?
8. What are the key components of a RAG system?
9. How would you evaluate a RAG system's performance?
10. What security considerations are important for GenAI apps?

**Coding Challenge Practice:**
```python
# Challenge: Build a simple sentiment analyzer
def analyze_sentiment(text):
    """
    Use an LLM to analyze sentiment.
    Return: positive, negative, or neutral
    """
    # Your code here
    pass

# Challenge: Create a text summarizer with length control
def summarize(text, max_words=50):
    """
    Summarize text within word limit.
    """
    # Your code here
    pass

# Challenge: Build a simple Q&A system
def answer_from_context(context, question):
    """
    Answer question based only on given context.
    If answer not in context, say "I don't know"
    """
    # Your code here
    pass
```

---

## Congratulations!

You have completed the 50-Day GenAI Course!

### What You've Learned:
- Python programming for AI
- LLM fundamentals and APIs
- Prompt engineering
- Building RAG applications
- Creating AI agents
- Fine-tuning concepts
- Deploying AI applications
- Security best practices

### Your Portfolio Should Include:
1. CLI AI Assistant
2. RAG Document Q&A Bot
3. Research Assistant Agent
4. Capstone Project

### Next Steps:
1. Keep building projects
2. Contribute to open-source
3. Stay updated with AI news
4. Apply for GenAI roles
5. Join AI communities

### Resources for Continued Learning:
- OpenAI Documentation
- LangChain Documentation
- Hugging Face Courses
- AI Twitter/X community
- YouTube tutorials

---

**Good luck with your GenAI career!**
