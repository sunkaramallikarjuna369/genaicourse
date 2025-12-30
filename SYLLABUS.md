# GenAI 75-Day Course - Complete Detailed Syllabus

## Course Overview

This is the **detailed 75-day course** (1 hour per day) designed for BTech freshers with no prior knowledge. This version provides more in-depth explanations, additional exercises, and extended practice compared to the 50-day fast-track version.

**Key Differences from 50-Day Version:**
- More time for each concept
- Multiple exercises per topic
- Review and practice days
- Extended project work
- Comprehensive interview preparation

---

## Module 0: Setup & Python Essentials (Days 1-5)

### Day 1: Welcome & Course Introduction
**What you'll learn:** Understanding the course and your GenAI journey

**Topics:**
- What is this course about?
- What will you be able to do after 75 days?
- How to get the most out of this course
- Setting expectations and goals
- Overview of the GenAI industry

**Detailed Explanation:**

Generative AI (GenAI) is a type of artificial intelligence that can CREATE new content. Unlike traditional AI that only analyzes or classifies data, GenAI can generate text (like ChatGPT writing essays, emails, code), images (like DALL-E or Midjourney creating pictures), audio (like AI generating music or voice), and video (like AI creating short clips).

The GenAI market is growing rapidly. Companies need developers who can build applications using LLM APIs, create chatbots and virtual assistants, implement RAG systems for enterprise data, and deploy and maintain AI applications.

**Simple Exercise 1:**
Write down your answers to these questions:
1. What do you want to build with GenAI?
2. What type of job do you want after this course?
3. How many hours per week can you dedicate to practice?

**Simple Exercise 2:**
Try these AI tools (free versions):
- ChatGPT: https://chat.openai.com
- Google Gemini: https://gemini.google.com
- Claude: https://claude.ai

Ask each one: "Explain what you are in 3 simple sentences"

---

### Day 2: Environment Setup - Part 1
**What you'll learn:** Installing Python on your computer

**Topics:**
- What is Python and why use it for AI?
- Downloading Python
- Installing Python step-by-step
- Verifying installation

**Detailed Explanation:**

Python is the most popular programming language for AI because it is easy to learn with simple syntax that reads like English, has a huge ecosystem with thousands of AI libraries available, is the industry standard used by all major AI companies, and has a great community making it easy to find help and tutorials.

**Step-by-Step Installation (Windows):**
1. Open your browser and go to: https://www.python.org/downloads/
2. Click the big yellow button "Download Python 3.12.x"
3. Open the downloaded file
4. VERY IMPORTANT: Check the box that says "Add Python to PATH"
5. Click "Install Now"
6. Wait for installation to complete
7. Click "Close"

**Simple Exercise 1:**
Verify Python is installed correctly:
```bash
python --version
```
You should see: Python 3.12.x

**Simple Exercise 2:**
Try Python in interactive mode:
```python
>>> print("Hello!")
>>> 2 + 2
>>> exit()
```

---

### Day 3: Environment Setup - Part 2
**What you'll learn:** Installing VS Code and setting it up for Python

**Topics:**
- What is VS Code?
- Installing VS Code
- Installing Python extension
- Creating your first Python file

**Detailed Explanation:**

VS Code (Visual Studio Code) is a free code editor made by Microsoft. It's the most popular editor for Python development because it is free and open source, lightweight but powerful, has great Python support, has a built-in terminal, and has extensions for everything.

**Step-by-Step Installation:**
1. Go to: https://code.visualstudio.com/
2. Click "Download for Windows/Mac"
3. Run the installer
4. Accept the license agreement
5. Keep default options, click Next
6. Click Install
7. Launch VS Code

**Simple Exercise 1:**
Create your first Python file:
```python
# This is my first Python program!
print("Hello, World!")
print("I am learning GenAI!")
print("This is exciting!")
```

**Simple Exercise 2:**
Experiment with print:
```python
print("My name is [Your Name]")
print("I am a BTech student")
print("I want to become a GenAI developer")
print("=" * 30)
```

---

### Day 4: Python Basics - Variables and Data Types
**What you'll learn:** Storing and using information in Python

**Topics:**
- What are variables?
- Different types of data
- Naming rules for variables
- Basic operations

**Detailed Explanation:**

A variable is like a labeled box where you store information. You give it a name, and Python remembers what's inside.

```python
name = "Rahul"      # This stores the text "Rahul"
age = 20            # This stores the number 20
height = 5.8        # This stores a decimal number
is_student = True   # This stores True or False
```

**Data Types in Python:**
- str (string): Text like "Hello", 'World'
- int (integer): Whole numbers like 10, -5, 0
- float: Decimal numbers like 3.14, -2.5
- bool (boolean): True or False

**Simple Exercise 1:**
Create variables for yourself:
```python
my_name = "Your Name"
my_age = 20
my_college = "Your College Name"
my_branch = "Computer Science"
my_cgpa = 8.5

print("Name:", my_name)
print("Age:", my_age)
print("College:", my_college)
print("Branch:", my_branch)
print("CGPA:", my_cgpa)
```

**Simple Exercise 2:**
Practice math operations:
```python
a = 10
b = 3

print("Addition:", a + b)
print("Subtraction:", a - b)
print("Multiplication:", a * b)
print("Division:", a / b)
print("Integer Division:", a // b)
print("Remainder:", a % b)
print("Power:", a ** b)
```

**Simple Exercise 3:**
String operations:
```python
first_name = "Rahul"
last_name = "Kumar"

full_name = first_name + " " + last_name
print("Full name:", full_name)
print("Name length:", len(full_name))
print("Uppercase:", full_name.upper())
print("Lowercase:", full_name.lower())
```

---

### Day 5: Python Basics - Input, Lists, and Loops
**What you'll learn:** Getting user input, storing multiple items, and repeating actions

**Topics:**
- Taking input from users
- Lists (storing multiple items)
- For loops (repeating actions)
- If-else (making decisions)
- Functions (reusable code)

**Detailed Explanation:**

Getting User Input:
```python
name = input("What is your name? ")
print("Hello,", name)

age = int(input("What is your age? "))
print("Next year you will be", age + 1)
```

Lists - Storing Multiple Items:
```python
fruits = ["apple", "banana", "mango"]
print(fruits[0])  # apple
print(fruits[-1]) # mango
fruits.append("orange")
print(len(fruits))  # 4
```

For Loops:
```python
for fruit in fruits:
    print("I like", fruit)

for i in range(5):
    print("Number:", i)
```

If-Else:
```python
age = 18
if age >= 18:
    print("You are an adult")
else:
    print("You are a minor")
```

**Simple Exercise 1:**
Create a simple calculator:
```python
print("=== Simple Calculator ===")
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /): ")

if operation == "+":
    result = num1 + num2
elif operation == "-":
    result = num1 - num2
elif operation == "*":
    result = num1 * num2
elif operation == "/":
    result = num1 / num2
else:
    result = "Invalid operation"

print("Result:", result)
```

**Simple Exercise 2:**
Work with lists:
```python
movies = []
movies.append(input("Enter movie 1: "))
movies.append(input("Enter movie 2: "))
movies.append(input("Enter movie 3: "))

print("\nYour favorite movies:")
for i, movie in enumerate(movies, 1):
    print(f"{i}. {movie}")
```

**Simple Exercise 3:**
Create functions:
```python
def greet(name):
    return f"Hello, {name}! Welcome to GenAI course!"

def add_numbers(a, b):
    return a + b

def is_even(number):
    return number % 2 == 0

print(greet("Rahul"))
print(add_numbers(5, 3))
print(is_even(10))
```

---

## Module 1: Web & Data Fundamentals (Days 6-12)

### Day 6: Working with Files - Reading
**What you'll learn:** How to read data from files

**Topics:**
- Why work with files?
- Opening files in Python
- Reading entire file
- Reading line by line

**Detailed Explanation:**

Files are how we store data permanently. When you close your program, variables disappear, but files stay on your computer.

```python
# Read entire file
with open("myfile.txt", "r") as file:
    content = file.read()
    print(content)

# Read line by line
with open("myfile.txt", "r") as file:
    for line in file:
        print(line.strip())
```

**Simple Exercise 1:**
Read and print a file:
```python
with open("sample.txt", "r") as file:
    content = file.read()
    print("File contents:")
    print(content)
    print(f"\nTotal characters: {len(content)}")
```

**Simple Exercise 2:**
Count lines and words:
```python
with open("sample.txt", "r") as file:
    lines = file.readlines()
    total_lines = len(lines)
    total_words = sum(len(line.split()) for line in lines)
    
    print(f"Total lines: {total_lines}")
    print(f"Total words: {total_words}")
```

---

### Day 7: Working with Files - Writing
**What you'll learn:** How to save data to files

**Topics:**
- Creating new files
- Writing text to files
- Appending to existing files

**Simple Exercise 1:**
Create a diary program:
```python
from datetime import datetime

def add_diary_entry():
    now = datetime.now()
    date_str = now.strftime("%Y-%m-%d %H:%M")
    
    print("Write your diary entry:")
    entry = input()
    
    with open("diary.txt", "a") as file:
        file.write(f"\n--- {date_str} ---\n")
        file.write(entry + "\n")
    
    print("Entry saved!")

def read_diary():
    try:
        with open("diary.txt", "r") as file:
            print(file.read())
    except FileNotFoundError:
        print("No diary entries yet!")

choice = input("1. Add entry  2. Read diary: ")
if choice == "1":
    add_diary_entry()
else:
    read_diary()
```

---

### Day 8: JSON - Understanding the Format
**What you'll learn:** What JSON is and why it's important

**Topics:**
- What is JSON?
- JSON syntax rules
- JSON vs Python dictionaries

**Detailed Explanation:**

JSON (JavaScript Object Notation) is a way to store and exchange data. It's used everywhere - APIs send data in JSON, configuration files use JSON, databases store JSON, and AI models return JSON.

```json
{
    "name": "Rahul",
    "age": 20,
    "is_student": true,
    "subjects": ["Math", "Physics", "AI"]
}
```

**Simple Exercise 1:**
Understand JSON structure:
```python
student = {
    "name": "Rahul Kumar",
    "age": 20,
    "college": "IIT Delhi",
    "is_active": True,
    "courses": ["AI", "ML", "Python"],
    "grades": {"AI": 95, "ML": 88, "Python": 92}
}

print("Name:", student["name"])
print("First course:", student["courses"][0])
print("AI grade:", student["grades"]["AI"])
```

---

### Day 9: JSON - Reading and Writing
**What you'll learn:** Working with JSON files in Python

**Topics:**
- The json module
- Reading JSON files
- Writing JSON files

**Simple Exercise 1:**
Create and save student data:
```python
import json

students = [
    {"name": "Rahul", "age": 20, "marks": 85},
    {"name": "Priya", "age": 21, "marks": 92},
    {"name": "Amit", "age": 20, "marks": 78}
]

with open("students.json", "w") as file:
    json.dump(students, file, indent=4)
    print("Data saved to students.json")

with open("students.json", "r") as file:
    loaded_students = json.load(file)
    
print("\nLoaded students:")
for student in loaded_students:
    print(f"  {student['name']}: {student['marks']} marks")
```

**Simple Exercise 2:**
Build a contact book:
```python
import json

def load_contacts():
    try:
        with open("contacts.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_contacts(contacts):
    with open("contacts.json", "w") as file:
        json.dump(contacts, file, indent=4)

def add_contact(name, phone, email):
    contacts = load_contacts()
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print(f"Added {name}")

def show_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts yet!")
        return
    
    print("\n=== Contacts ===")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']}")

add_contact("Rahul", "9876543210", "rahul@email.com")
show_contacts()
```

---

### Day 10: Making API Calls - Introduction
**What you'll learn:** What APIs are and how they work

**Topics:**
- What is an API?
- HTTP methods (GET, POST)
- Understanding API responses

**Detailed Explanation:**

API = Application Programming Interface. Think of an API like a waiter in a restaurant - you (the customer) want food, the kitchen (the server) makes food, and the waiter (the API) takes your order and brings your food.

**Simple Exercise 1:**
Make your first API call:
```python
import requests

response = requests.get("https://official-joke-api.appspot.com/random_joke")
print("Status code:", response.status_code)

joke = response.json()
print("\nSetup:", joke["setup"])
print("Punchline:", joke["punchline"])
```

**Simple Exercise 2:**
Get multiple jokes:
```python
import requests

response = requests.get("https://official-joke-api.appspot.com/random_ten")
jokes = response.json()

print("=== 5 Random Jokes ===\n")
for i, joke in enumerate(jokes[:5], 1):
    print(f"Joke {i}:")
    print(f"  {joke['setup']}")
    print(f"  {joke['punchline']}\n")
```

---

### Day 11: Making API Calls - Practice
**What you'll learn:** Working with different APIs

**Topics:**
- Finding free APIs
- Error handling
- Processing API data

**Simple Exercise 1:**
Get random user data:
```python
import requests

def get_random_user():
    response = requests.get("https://randomuser.me/api/")
    data = response.json()
    user = data["results"][0]
    
    return {
        "name": f"{user['name']['first']} {user['name']['last']}",
        "email": user["email"],
        "country": user["location"]["country"]
    }

print("=== Random Users ===\n")
for i in range(3):
    user = get_random_user()
    print(f"Name: {user['name']}")
    print(f"Email: {user['email']}")
    print(f"Country: {user['country']}\n")
```

---

### Day 12: Introduction to FastAPI
**What you'll learn:** Creating your own API

**Topics:**
- What is FastAPI?
- Creating endpoints
- Running your server

**Simple Exercise 1:**
Create a basic API:
```python
from fastapi import FastAPI

app = FastAPI(title="My First API")

@app.get("/")
def home():
    return {"message": "Welcome to my API!"}

@app.get("/hello/{name}")
def hello(name: str):
    return {"message": f"Hello, {name}!"}

@app.get("/add/{a}/{b}")
def add(a: int, b: int):
    return {"result": a + b}

# Run with: uvicorn filename:app --reload
```

**Simple Exercise 2:**
Create a student API:
```python
from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class Student(BaseModel):
    name: str
    age: int
    grade: str

students = []

@app.get("/students")
def get_students():
    return {"students": students}

@app.post("/students")
def add_student(student: Student):
    students.append(student.dict())
    return {"message": "Student added", "student": student}
```

---

## Module 2: LLM Fundamentals & Prompt Engineering (Days 13-24)

### Day 13: Understanding Large Language Models
**What you'll learn:** How AI chatbots actually work

**Topics:**
- What is a Large Language Model?
- How LLMs are trained
- Tokens and tokenization
- Context windows explained

**Detailed Explanation:**

A Large Language Model (LLM) is an AI that has learned patterns from billions of text documents. It can understand questions, generate human-like text, translate languages, write code, and summarize documents.

Tokens are how LLMs read text. A token is roughly 1 token ≈ 4 characters or 0.75 words. The context window is the AI's "memory" - how much text it can consider at once. GPT-3.5 has about 4,000 tokens, GPT-4 has 8,000 to 128,000 tokens.

**Simple Exercise 1:**
Estimate tokens:
```python
def estimate_tokens(text):
    return len(text) // 4

text = "Artificial Intelligence is transforming the world."
print(f"Text: '{text}'")
print(f"Estimated tokens: {estimate_tokens(text)}")
```

---

### Day 14: Getting API Access
**What you'll learn:** Setting up accounts and API keys

**Topics:**
- Creating OpenAI account
- Getting API keys
- Keeping keys secure

**Simple Exercise 1:**
Set up environment variables:
```python
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if api_key:
    print("API key loaded successfully!")
    print(f"Key starts with: {api_key[:10]}...")
else:
    print("No API key found. Check your .env file.")
```

---

### Day 15: Your First LLM API Call
**What you'll learn:** Making AI respond through your code

**Topics:**
- Installing OpenAI library
- Making API calls
- Understanding responses

**Simple Exercise 1:**
Make your first API call:
```python
from openai import OpenAI

client = OpenAI()

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "user", "content": "Say hello in 5 different languages"}
    ]
)

print(response.choices[0].message.content)
```

**Simple Exercise 2:**
Create a question-answer program:
```python
from openai import OpenAI

client = OpenAI()

def ask_ai(question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": question}]
    )
    return response.choices[0].message.content

print("AI:", ask_ai("What is Python?"))
print("\nAI:", ask_ai("Give me 3 tips for learning programming"))
```

---

### Day 16: Understanding Messages and Roles
**What you'll learn:** How to structure conversations with AI

**Topics:**
- System messages
- User messages
- Assistant messages
- Multi-turn conversations

**Simple Exercise 1:**
Create different AI personalities:
```python
from openai import OpenAI

client = OpenAI()

def chat_with_personality(personality, question):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": personality},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

question = "Explain what a variable is in programming"

print("=== Friendly Teacher ===")
print(chat_with_personality(
    "You are a friendly teacher who explains things simply to beginners.",
    question
))

print("\n=== Technical Expert ===")
print(chat_with_personality(
    "You are a technical expert who gives precise, detailed explanations.",
    question
))
```

**Simple Exercise 2:**
Build a conversation with memory:
```python
from openai import OpenAI

client = OpenAI()

messages = [
    {"role": "system", "content": "You are a helpful assistant. Remember what the user tells you."}
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

print("User: My name is Rahul")
print("AI:", chat("My name is Rahul"))

print("\nUser: What is my name?")
print("AI:", chat("What is my name?"))
```

---

### Day 17: Prompt Engineering Fundamentals
**What you'll learn:** How to write effective prompts

**Topics:**
- What is prompt engineering?
- Clear instructions
- Providing context
- Specifying format

**Detailed Explanation:**

Prompt Engineering is the skill of writing instructions that get the best results from AI.

Key Principles:
1. Be Specific - "Write 3 paragraphs about golden retrievers" instead of "Write about dogs"
2. Provide Context - "I am a beginner programmer. Explain what a function is using simple words"
3. Specify Format - "List 5 fruits in a numbered list with their colors"
4. Give Examples - Show the AI what you want

**Simple Exercise 1:**
Compare bad vs good prompts:
```python
from openai import OpenAI

client = OpenAI()

def ask(prompt):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    return response.choices[0].message.content

print("=== Bad Prompt ===")
print(ask("Write about AI"))

print("\n=== Good Prompt ===")
print(ask("""
Write a brief explanation of Artificial Intelligence for a 10-year-old student.

Requirements:
- Use simple words
- Include 2 real-life examples
- Keep it under 100 words
- End with an encouraging message
"""))
```

---

### Day 18: Advanced Prompt Techniques
**What you'll learn:** More powerful prompting methods

**Topics:**
- Few-shot prompting
- Chain of thought
- Role-playing prompts

**Simple Exercise 1:**
Practice few-shot prompting:
```python
from openai import OpenAI

client = OpenAI()

prompt = """
Classify the sentiment of movie reviews as Positive, Negative, or Neutral.

Examples:
Review: "This movie was absolutely amazing! Best film I've seen all year."
Sentiment: Positive

Review: "Terrible waste of time. The plot made no sense."
Sentiment: Negative

Review: "It was okay. Nothing special but not bad either."
Sentiment: Neutral

Now classify:
Review: "I loved every minute of it! The acting was superb."
Sentiment:
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
```

**Simple Exercise 2:**
Use chain of thought:
```python
from openai import OpenAI

client = OpenAI()

prompt = """
Solve this problem step by step:

A train travels at 60 km/h for 2 hours, then at 80 km/h for 1.5 hours.
What is the total distance traveled?

Please:
1. Identify what we know
2. Write the formula needed
3. Calculate step by step
4. Give the final answer with units
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": prompt}]
)

print(response.choices[0].message.content)
```

---

### Day 19: Getting Structured Output (JSON)
**What you'll learn:** Making AI respond in specific formats

**Topics:**
- Why structured output matters
- Requesting JSON responses
- Parsing AI responses

**Simple Exercise 1:**
Get structured data:
```python
from openai import OpenAI
import json

client = OpenAI()

prompt = """
Create information about a fictional person and return ONLY valid JSON.

The JSON should have:
{
    "name": "full name",
    "age": number,
    "occupation": "job title",
    "hobbies": ["hobby1", "hobby2", "hobby3"]
}

Return only the JSON, no other text.
"""

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You only respond with valid JSON."},
        {"role": "user", "content": prompt}
    ]
)

result = response.choices[0].message.content
data = json.loads(result)
print(f"Name: {data['name']}")
print(f"Age: {data['age']}")
print(f"Hobbies: {', '.join(data['hobbies'])}")
```

---

### Day 20: Building Prompt Templates
**What you'll learn:** Creating reusable prompts

**Topics:**
- Why use templates?
- Creating flexible prompts
- Template libraries

**Simple Exercise 1:**
Create a template library:
```python
from openai import OpenAI

client = OpenAI()

TEMPLATES = {
    "explain": """
    Explain {topic} to a {audience}.
    Use simple language and include {num_examples} examples.
    Keep it under {max_words} words.
    """,
    
    "summarize": """
    Summarize the following text in {num_sentences} sentences.
    
    Text: {text}
    """,
    
    "translate": """
    Translate the following text to {language}.
    
    Text: {text}
    """
}

def use_template(template_name, **kwargs):
    template = TEMPLATES.get(template_name)
    prompt = template.format(**kwargs)
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )
    
    return response.choices[0].message.content

print(use_template("explain",
    topic="recursion",
    audience="10-year-old",
    num_examples=2,
    max_words=150
))
```

---

### Day 21-24: Review and Practice Days

**Day 21:** Review LLM basics - tokens, context, messages
**Day 22:** Practice prompt engineering techniques
**Day 23:** Build a multi-purpose AI assistant
**Day 24:** Create a prompt library for common tasks

---

## Module 3: LLM Application Development (Days 25-34)

### Day 25: Building Chat Applications
**What you'll learn:** Creating interactive chat experiences

**Simple Exercise:**
```python
from openai import OpenAI

client = OpenAI()

class ChatApp:
    def __init__(self):
        self.messages = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    
    def chat(self, user_input):
        self.messages.append({"role": "user", "content": user_input})
        
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=self.messages
        )
        
        reply = response.choices[0].message.content
        self.messages.append({"role": "assistant", "content": reply})
        
        return reply
    
    def run(self):
        print("Chat started! Type 'quit' to exit.\n")
        
        while True:
            user_input = input("You: ").strip()
            
            if user_input.lower() == 'quit':
                print("Goodbye!")
                break
            
            response = self.chat(user_input)
            print(f"AI: {response}\n")

app = ChatApp()
app.run()
```

---

### Day 26: Streaming Responses
**What you'll learn:** Getting AI responses word by word

**Simple Exercise:**
```python
from openai import OpenAI

client = OpenAI()

stream = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Tell me a short story about a robot"}],
    stream=True
)

print("Story: ", end="")
for chunk in stream:
    if chunk.choices[0].delta.content:
        print(chunk.choices[0].delta.content, end="")
print()
```

---

### Day 27: Error Handling & Retries
**What you'll learn:** Making your app reliable

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
                time.sleep(2)
    return "Sorry, something went wrong."

print(safe_api_call("Say hello"))
```

---

### Day 28: Function Calling / Tools
**What you'll learn:** Making AI use tools

**Simple Exercise:**
```python
from openai import OpenAI
import json

client = OpenAI()

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

def get_weather(city):
    return f"The weather in {city} is sunny, 25°C"

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "What's the weather in Mumbai?"}],
    tools=tools
)

if response.choices[0].message.tool_calls:
    tool_call = response.choices[0].message.tool_calls[0]
    args = json.loads(tool_call.function.arguments)
    result = get_weather(args["city"])
    print(result)
```

---

### Day 29-30: Building APIs with LLMs

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
            {"role": "system", "content": "Summarize in 2 sentences."},
            {"role": "user", "content": question.text}
        ]
    )
    return {"summary": response.choices[0].message.content}
```

---

### Day 31-34: Mini Projects

**Day 31:** CLI AI Assistant
**Day 32:** Text Analyzer Tool
**Day 33:** Code Explainer
**Day 34:** Review and Integration

---

## Module 4: RAG - Retrieval-Augmented Generation (Days 35-48)

### Day 35: What is RAG?
**What you'll learn:** Understanding RAG and why it's important

**Detailed Explanation:**

RAG (Retrieval-Augmented Generation) solves a key problem: AI doesn't know YOUR data. ChatGPT knows general information but not your company documents, college handbook, or product manual.

RAG works by:
1. Storing your documents in a searchable format
2. When a question comes, finding relevant documents
3. Giving those documents to the AI along with the question
4. AI answers based on YOUR data

---

### Day 36: Text Embeddings
**What you'll learn:** Converting text to numbers AI understands

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

text1 = "I love eating pizza"
text2 = "Pizza is my favorite food"
text3 = "The weather is nice today"

emb1 = get_embedding(text1)
print(f"Embedding length: {len(emb1)}")
print("Text 1 and 2 are about the same topic (pizza)")
print("Text 3 is about something different (weather)")
```

---

### Day 37-38: Vector Databases

**Simple Exercise:**
```python
import chromadb

client = chromadb.Client()
collection = client.create_collection("my_documents")

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

results = collection.query(
    query_texts=["Tell me about coding"],
    n_results=2
)

print("Most relevant documents:")
for doc in results['documents'][0]:
    print(f"- {doc}")
```

---

### Day 39-40: Document Loading and Chunking

**Simple Exercise:**
```python
def simple_chunk(text, chunk_size=500, overlap=50):
    chunks = []
    start = 0
    
    while start < len(text):
        end = start + chunk_size
        chunk = text[start:end]
        chunks.append(chunk)
        start = end - overlap
    
    return chunks

long_text = "This is a very long document. " * 100
chunks = simple_chunk(long_text, chunk_size=200, overlap=20)

print(f"Total chunks: {len(chunks)}")
print(f"First chunk: {chunks[0][:50]}...")
```

---

### Day 41-43: Building RAG Systems

**Simple Exercise:**
```python
import chromadb
from openai import OpenAI

client = OpenAI()
chroma = chromadb.Client()
collection = chroma.create_collection("knowledge_base")

knowledge = [
    "Our company was founded in 2020 in Bangalore.",
    "We have 500 employees across India.",
    "Our main product is an AI-powered chatbot.",
    "Office hours are 9 AM to 6 PM, Monday to Friday.",
    "Contact HR at hr@company.com for queries."
]

collection.add(documents=knowledge, ids=[f"doc{i}" for i in range(len(knowledge))])

def ask_with_rag(question):
    results = collection.query(query_texts=[question], n_results=2)
    context = "\n".join(results['documents'][0])
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Answer based on this information:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

print(ask_with_rag("When was the company founded?"))
print(ask_with_rag("How can I contact HR?"))
```

---

### Day 44-46: RAG with Citations and Evaluation

**Simple Exercise:**
```python
def ask_with_citations(question):
    results = collection.query(query_texts=[question], n_results=2)
    context = "\n".join(results['documents'][0])
    sources = results['ids'][0]
    
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": f"Answer based on:\n{context}"},
            {"role": "user", "content": question}
        ]
    )
    
    return {
        "answer": response.choices[0].message.content,
        "sources": sources
    }

result = ask_with_citations("What are the office hours?")
print(f"Answer: {result['answer']}")
print(f"Sources: {result['sources']}")
```

---

### Day 47-48: RAG Project - Document Q&A Bot

**Simple Exercise:**
```python
import chromadb
from openai import OpenAI

class DocumentQABot:
    def __init__(self):
        self.client = OpenAI()
        self.chroma = chromadb.Client()
        self.collection = self.chroma.create_collection("docs")
    
    def add_documents(self, documents):
        self.collection.add(
            documents=documents,
            ids=[f"doc_{i}" for i in range(len(documents))]
        )
        print(f"Added {len(documents)} documents")
    
    def ask(self, question):
        results = self.collection.query(query_texts=[question], n_results=3)
        context = "\n".join(results['documents'][0])
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": f"Answer based only on:\n{context}\n\nIf not in context, say 'I don't know.'"},
                {"role": "user", "content": question}
            ]
        )
        
        return {
            "answer": response.choices[0].message.content,
            "sources": results['documents'][0]
        }

bot = DocumentQABot()
bot.add_documents([
    "Python was created by Guido van Rossum in 1991.",
    "Python is known for its simple and readable syntax.",
    "Popular Python frameworks include Django and Flask."
])

result = bot.ask("Who created Python?")
print(f"Answer: {result['answer']}")
```

---

## Module 5: AI Agents & Workflows (Days 49-58)

### Day 49-50: Understanding AI Agents

An AI agent is an AI that can take actions, not just answer questions. It can use tools, make decisions, and complete multi-step tasks.

---

### Day 51-53: Building Agents

**Simple Exercise:**
```python
from openai import OpenAI
import json

client = OpenAI()

tools = [
    {
        "type": "function",
        "function": {
            "name": "calculator",
            "description": "Perform math calculations",
            "parameters": {
                "type": "object",
                "properties": {
                    "expression": {"type": "string"}
                },
                "required": ["expression"]
            }
        }
    }
]

def calculator(expression):
    try:
        return str(eval(expression))
    except:
        return "Error"

def agent(user_message):
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}],
        tools=tools
    )
    
    message = response.choices[0].message
    
    if message.tool_calls:
        tool_call = message.tool_calls[0]
        args = json.loads(tool_call.function.arguments)
        result = calculator(args["expression"])
        return f"Calculated: {result}"
    
    return message.content

print(agent("What is 25 * 4?"))
```

---

### Day 54-56: Agent Memory and Workflows

**Simple Exercise:**
```python
class AgentWithMemory:
    def __init__(self):
        self.client = OpenAI()
        self.conversation = []
        self.facts = []
    
    def remember_fact(self, fact):
        self.facts.append(fact)
        print(f"Remembered: {fact}")
    
    def chat(self, message):
        system_message = "You are a helpful assistant."
        if self.facts:
            system_message += f"\n\nRemember:\n" + "\n".join(self.facts)
        
        self.conversation.append({"role": "user", "content": message})
        
        response = self.client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[{"role": "system", "content": system_message}] + self.conversation
        )
        
        reply = response.choices[0].message.content
        self.conversation.append({"role": "assistant", "content": reply})
        
        return reply

agent = AgentWithMemory()
agent.remember_fact("User's name is Priya")
print(agent.chat("What do you know about me?"))
```

---

### Day 57-58: Agent Projects

Build a Research Assistant that can search, summarize, and generate reports.

---

## Module 6: Fine-tuning & Model Adaptation (Days 59-65)

### Day 59-60: Understanding Fine-tuning

Fine-tuning is training an existing model on your specific data to customize its behavior.

When to use what:
- Prompt Engineering: Quick, free, good for most cases
- RAG: When you need custom knowledge
- Fine-tuning: When you need custom behavior/style

---

### Day 61-62: Preparing Training Data

**Simple Exercise:**
```python
import json

training_data = [
    {
        "messages": [
            {"role": "system", "content": "You are a customer support agent."},
            {"role": "user", "content": "How do I return a product?"},
            {"role": "assistant", "content": "To return: 1) Log in, 2) Go to Orders, 3) Click Return."}
        ]
    }
]

with open("training_data.jsonl", "w") as f:
    for item in training_data:
        f.write(json.dumps(item) + "\n")

print("Training data saved!")
```

---

### Day 63-65: Fine-tuning Process and LoRA

Learn about the fine-tuning process and efficient methods like LoRA.

---

## Module 7: Deployment & Production (Days 66-70)

### Day 66-67: Docker Basics

**Dockerfile:**
```dockerfile
FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt
COPY . .
EXPOSE 8000
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

### Day 68: Environment Variables & Secrets

```python
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("Please set OPENAI_API_KEY")
```

---

### Day 69-70: Cloud Deployment and Security

Deploy to Render, Railway, or Fly.io. Learn about rate limiting, input validation, and logging.

---

## Module 8: Capstone Project & Interview Prep (Days 71-75)

### Day 71-72: Capstone Project

Choose and build one of:
1. Study Buddy Bot - RAG chatbot for textbooks
2. Customer Support Agent - Multi-tool assistant
3. Content Creator - Blog/social media generator
4. Code Helper - Programming assistant

---

### Day 73: Portfolio & Resume

Create a GitHub portfolio with good READMEs for all your projects.

---

### Day 74-75: Interview Preparation

**Technical Questions to Practice:**

1. What is the difference between RAG and fine-tuning?
2. Explain how embeddings work in simple terms.
3. What is prompt injection and how do you prevent it?
4. How would you reduce hallucinations in an LLM application?
5. Explain tokens and context window.
6. What is temperature in LLM APIs?
7. How do AI agents differ from chatbots?
8. What are the key components of a RAG system?
9. How would you evaluate a RAG system?
10. What security considerations are important for GenAI apps?

---

## Congratulations!

You have completed the 75-Day Detailed GenAI Course!

### What You've Achieved:
- Strong Python foundation for AI
- Deep understanding of LLMs
- Advanced prompt engineering skills
- Production-ready RAG applications
- AI agent development
- Deployment and security knowledge
- Interview readiness

### Your Portfolio Should Include:
1. Python fundamentals project
2. API integration project
3. Prompt engineering library
4. LLM-powered API service
5. RAG chatbot with evaluation
6. AI agent suite
7. Capstone project

### Next Steps:
1. Keep building and experimenting
2. Contribute to open-source AI projects
3. Stay updated with AI news
4. Apply for GenAI developer positions
5. Join AI communities

---

**Best of luck with your GenAI career!**
