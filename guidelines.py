import openai

# obtain your api key
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()
    

# read and set the api key
openai.api_key = open_file('openaiapikey.txt')


def get_completion(prompt, model = "gpt-3.5-turbo"):
    messages = [{ "role": "user", "content": prompt }]
    response = openai.ChatCompletion.create(
        model = model,
        messages = messages,
        temperature = 0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]


########### Principle 1 - Write clear and specific instructions 

# write clear and specific instructions 
'''
Tactic 1: Use delimiters 
Triple quotes: """,
Triple backticks: ```,
Triple dashes: ---,
Angle brackets: <>,
XML tags: <tag> </tag>
'''

text1 = f"""
You should express what you want a model to do by \
providing instructions that are as clear and \
specific as you can possibly make them. \
This will guide the model towards the desired output, \
and reduce the chances of receiving irrelevant \
or incorrect responses. Don't confuse writing a \
clear prompt with writing a short prompt. \
In many cases, longer prompts provide more clarity \
and context for the model, which can lead to \
more detailed and relevant outputs. 
"""

prompt1 = f"""
Summarize the text delimited by triple backticks \
into a single sentence.
```{text1}```
"""

response1 = get_completion(prompt=prompt1)
print(response1)

# Tactic 2: Ask for strcutured output HTML/JSON

prompt2 = f"""
Generate a list of three made-up book titles along \
with their authors and genres.
Provide them in JSON format with the following keys:
book_id, title, author, genre.
"""

response2 = get_completion(prompt=prompt2)
print(response2)


# Tactic 3: Check whether conditions are satisfied 
# Check assumptions required to do the task


text_1 = f"""
Making a cup of tea is easy! First, you need to get some \
water boiling. While that's happening, \
grab a cup and put a tea bag in it. Once the water is \
hot enough, just pour it over the tea bag. \
Let it sit for a bit so the tea can steep. After a \
few minutes, take out the tea bag. If you \
like, you can add some sugar or milk to taste. \
And that's it! You've got yourself a delicious \
cup of tea to enjoy. 
"""

prompt3 = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - ...
...
Step N - ...

If the text does not contain a sequence of instructions, \
then simply write \ "No steps provided.\ "

\ " \ " \ " {text_1} \ " \ " \ "
"""

response3 = get_completion(prompt=prompt3)
print("Completion for Text 1:")
print(response3)


text_2 = f"""
The sun is shining brightly today, and the birds are \
singing. It's a beautiful day to go for a \
walk in the part. The flowers are blooming, and the \
trees are swaying gently in the breeze. People \
are out and about, enjoying the lovely weather. \
Some are having picnics, while others are playing \
games or simply relaxing on the grass. It's a \
perfect day to spend time outdoors and appreciate the \
beauty of nature. 
"""

prompt31 = f"""
You will be provided with text delimited by triple quotes. 
If it contains a sequence of instructions, \
re-write those instructions in the following format:

Step 1 - ...
Step 2 - ...
...
Step N - ...

If the text does not contain a sequence of instructions, \
then simply write \ "No steps provided.\ "

\ " \ " \ " {text_2} \ " \ " \ "
"""

response31 = get_completion(prompt=prompt31)
print("Completion for Text 2:")
print(response31)


# Tactic 4: Few-shot prompting 
# Give successful examples of completing tasks 
# Then ask model to perform the task 

prompt4 = f"""
Your task is to answer in a consistent style.

<child>: Teach me about patience. 

<grandparent>: The river that carves the deepest \
valley flows from a modest spring; the \
grandest symphony originates from a single note; \
the most intricate tapestry begins with a solitary thread. 

<child> : Teach me about resilience. 
"""

response4 = get_completion(prompt=prompt4)
print(response4)

'''
Resilience is like a tree that bends with the wind but never breaks. 
It is the ability to bounce back from adversity and keep moving forward, 
even when things get tough. Just like a tree that grows stronger with each storm it weathers, 
resilience is a quality that can be developed and strengthened over time. 
'''

########### Principle 2 - Give the model time to think 


'''
# Tactic 1: Specify the steps to complete a task 
Step 1: ...
Step 2: ...
...
Step N: ...

'''

text5 = f"""
In a charming village, siblings Jack and Jill set out on \
a quest to fetch water from a hilltop \
well. As they climbed, singing joyfully, misfortune \
struck-Jack tripped on a stone and tumbled \
down the hill, with Jill following suit. \
Though slightly battered, the pair returned home to \
comforting embraces. Despite the mishap, \
their adventourous spirits remained undimmed, and they \
continued exploring with delight. 
"""

# exmaple 1
prompt_1 = f"""
Perform the following actions:
1 - Summarize the following text delimited by triple \
backticks with 1 sentence. 
2 - Translate the summary into French. 
3 - List each name in the French summary. 
4 - Output a json object that contains the following \
keys: french_summary, num_names. 

Separate your answer with line brakes. 

Text:
```{text5}```
"""

response5 = get_completion(prompt=prompt_1)
print("Completion for prompt 1: ")
print(response5)


# example 2, asking for output in a specified format

prompt_2 = f"""
Your task is to perform the following actions: 
1 - Summarize the following text delimited by
triple quotes with 1 sentence. 
2 - Translate that summary into French. 
3 - List each name in the French summmary. 
4 - Output a json object that contains the 
following keys: french_summary, num_names. 

Use the following format:
Text: <text to summarize>
Summary: <summary>
Translation: <summary translation>
Names: <list of names in Italian summary>
Output JSON: <json with summart and num_names>

Text to summarize: <{text5}>
"""

response6 = get_completion(prompt=prompt_2)
print("\nCompletion for prompt 2:")
print(response6)


'''
# Tactic 2: Instruct the model to work out its
own solution before rushing to a conclusion 

'''

prompt_3 = f"""
Determine if the student's solution is correct or not. 

Question:
I'm bulding a solar power installation and I need \
help working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot 
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations
as a function of the number of square feet. 

Student's Solution:
Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
"""

response7 = get_completion(prompt=prompt_3)
print(response7)

prompt_4 = f"""
Your task is to determine if the student' solution \
is correct or not. 
To solve the problem do the following:
- First, work out your own solution to the problem.
- Then compare your solution to the student's solution \
and evaluate if the student's solution is correct or not. 
Don't decide if the student's solution is correct until 
you have done the problem yourself. 

Use the following format:
Question:
```

question here
```

Student's solution:
```

student's solution here
```

Actual solution:
```

steps to work out the solution and your solution here
```

Is the student's solution the same as actual solution \
just calculated:
```

yes or no
```

Student grade:
```

correct or incorrect
```

Question:
```
I'm bulding a solar power installation and I need \
help working out the financials. 
- Land costs $100 / square foot
- I can buy solar panels for $250 / square foot 
- I negotiated a contract for maintenance that will cost \
me a flat $100k per year, and an additional $10 / square \
foot
What is the total cost for the first year of operations
as a function of the number of square feet. 
``` 

Student's Solution:
```

Let x be the size of the installation in square feet.
Costs:
1. Land cost: 100x
2. Solar panel cost: 250x
3. Maintenance cost: 100,000 + 100x
Total cost: 100x + 250x + 100,000 + 100x = 450x + 100,000
```

Actual solution:
"""

response8 = get_completion(prompt=prompt_4)
print(response8)


'''
Model Limitations

Hallucination
Makes statements that sound plausible but are not true 
'''

prompt_limitation = f"""
Tell me about AeroGlide UltraSlim Smart Toothbrush by Boie
"""
response_limitation = get_completion(prompt=prompt_limitation)
print(response_limitation)

'''
Reducing hallucinations:
First find relevant information,
then answer the question
based on the relevant information. 
'''

