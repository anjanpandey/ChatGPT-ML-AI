import openai

'''

import openai
import os

from dotenv import load_dotenv, find_dotenv
_ = load_dotenv(find_dotenv()) # read local .env file

openai.api_key  = os.getenv('OPENAI_API_KEY')

'''

# obtain your api key
def open_file(filepath):
    with open(filepath, 'r', encoding='utf-8') as infile:
        return infile.read()


# read and set the api key
openai.api_key = open_file('openaiapikey.txt')


def get_completion(prompt, model="gpt-3.5-turbo"): # Andrew mentioned that the prompt/ completion paradigm is preferable for this class
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]



prod_review = """
Got this panda plush toy for my daughter's birthday, \
who loves it and takes it everywhere. It's soft and \ 
super cute, and its face has a friendly look. It's \ 
a bit small for what I paid though. I think there \ 
might be other options that are bigger for the \ 
same price. It arrived a day earlier than expected, \ 
so I got to play with it myself before I gave it \ 
to her.
"""

prompt_summarize = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words. 

Review: ```{prod_review}```
"""

response_summarize = get_completion(prompt_summarize)
print(response_summarize)



prompt_shipping_focuse = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
Shipping deparmtment. 

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that mention shipping and delivery of the product. 

Review: ```{prod_review}```
"""

response_shipping_focuse = get_completion(prompt_shipping_focuse)
print(response_shipping_focuse)


prompt_price_and_value = f"""
Your task is to generate a short summary of a product \
review from an ecommerce site to give feedback to the \
pricing deparmtment, responsible for determining the \
price of the product.  

Summarize the review below, delimited by triple 
backticks, in at most 30 words, and focusing on any aspects \
that are relevant to the price and perceived value. 

Review: ```{prod_review}```
"""

response_price_and_value = get_completion(prompt_price_and_value)
print(response_price_and_value)



prompt_extract = f"""
Your task is to extract relevant information from \ 
a product review from an ecommerce site to give \
feedback to the Shipping department. 

From the review below, delimited by triple quotes \
extract the information relevant to shipping and \ 
delivery. Limit to 30 words. 

Review: ```{prod_review}```
"""

response_extract = get_completion(prompt_extract)
print(response_extract)


# Summarize multiple product reviews


review_1 = prod_review 

# review for a standing lamp
review_2 = """
Needed a nice lamp for my bedroom, and this one \
had additional storage and not too high of a price \
point. Got it fast - arrived in 2 days. The string \
to the lamp broke during the transit and the company \
happily sent over a new one. Came within a few days \
as well. It was easy to put together. Then I had a \
missing part, so I contacted their support and they \
very quickly got me the missing piece! Seems to me \
to be a great company that cares about their customers \
and products. 
"""

# review for an electric toothbrush
review_3 = """
My dental hygienist recommended an electric toothbrush, \
which is why I got this. The battery life seems to be \
pretty impressive so far. After initial charging and \
leaving the charger plugged in for the first week to \
condition the battery, I've unplugged the charger and \
been using it for twice daily brushing for the last \
3 weeks all on the same charge. But the toothbrush head \
is too small. I’ve seen baby toothbrushes bigger than \
this one. I wish the head was bigger with different \
length bristles to get between teeth better because \
this one doesn’t.  Overall if you can get this one \
around the $50 mark, it's a good deal. The manufactuer's \
replacements heads are pretty expensive, but you can \
get generic ones that're more reasonably priced. This \
toothbrush makes me feel like I've been to the dentist \
every day. My teeth feel sparkly clean! 
"""

# review for a blender
review_4 = """
So, they still had the 17 piece system on seasonal \
sale for around $49 in the month of November, about \
half off, but for some reason (call it price gouging) \
around the second week of December the prices all went \
up to about anywhere from between $70-$89 for the same \
system. And the 11 piece system went up around $10 or \
so in price also from the earlier sale price of $29. \
So it looks okay, but if you look at the base, the part \
where the blade locks into place doesn’t look as good \
as in previous editions from a few years ago, but I \
plan to be very gentle with it (example, I crush \
very hard items like beans, ice, rice, etc. in the \ 
blender first then pulverize them in the serving size \
I want in the blender then switch to the whipping \
blade for a finer flour, and use the cross cutting blade \
first when making smoothies, then use the flat blade \
if I need them finer/less pulpy). Special tip when making \
smoothies, finely cut and freeze the fruits and \
vegetables (if using spinach-lightly stew soften the \ 
spinach then freeze until ready for use-and if making \
sorbet, use a small to medium sized food processor) \ 
that you plan to use that way you can avoid adding so \
much ice if at all-when making your smoothie. \
After about a year, the motor was making a funny noise. \
I called customer service but the warranty expired \
already, so I had to buy another one. FYI: The overall \
quality has gone done in these types of products, so \
they are kind of counting on brand recognition and \
consumer loyalty to maintain sales. Got it in about \
two days.
"""

# create an array of all reviews
reviews = [review_1, review_2, review_3, review_4]


for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 

    Summarize the review below, delimited by triple \
    backticks in at most 20 words. 

    Review: ```{reviews[i]}```
    """

    response = get_completion(prompt)
    print(i+1, response, "\n")



result = ""

for i in range(len(reviews)):
    prompt = f"""
    Your task is to generate a short summary of a product \ 
    review from an ecommerce site. 

    Summarize the review below, delimited by triple \
    backticks in at most 20 words. 

    Review: ```{reviews[i]}```
    """

    result += get_completion(prompt)
    

new_prompt = f"""
Your taks is to generate a poem of a product \
review from an eccommerce site. 


Review: ```{result}```
"""

response = get_completion(new_prompt)
    
print(response)


'''
Soft and cute, my daughter's delight,
This panda plush toy, a joy in sight.
But for the price, a bit too small,
Still, it arrived early, no delay at all.

An affordable lamp, with storage to spare,
Fast shipping, and customer service that cares.
Easy to assemble, missing parts replaced,
This purchase left me feeling quite amazed.

A toothbrush with a small head, but effective clean,
Good battery life, a deal if bought for a price serene.
But beware, the cost can fluctuate,
From $49 to $70-$89, a change in rate.

The base of the blender, not as good as before,
But with gentle use, it'll last for more.
A tip for smoothies, freeze the fruits and veggies,
A year later, the motor made a funny noise, oh so edgy.

The warranty had expired, a disappointment to see,
Overall quality has gone down, not as good as it used to be.
But still, these products have their charm,
And with a little care, they'll do no harm.
'''


prompt_translate = f"""
Translate the response in espaniol

Response: ```{response}```
"""

new_response = get_completion(prompt_translate)
print(new_response)

"""
Respuesta: Suave y lindo, la delicia de mi hija,
Este peluche de panda, una alegría a la vista.
Pero por el precio, un poco pequeño,
Aún así, llegó temprano, sin retrasos en absoluto.

Una lámpara asequible, con espacio de almacenamiento de sobra,
Envío rápido y servicio al cliente que se preocupa.
Fácil de montar, piezas faltantes reemplazadas,
Esta compra me dejó bastante sorprendido.

Un cepillo de dientes con una cabeza pequeña, pero una limpieza efectiva,
Buena duración de la batería, una oferta si se compra a un precio sereno.
Pero cuidado, el costo puede fluctuar,
De $49 a $70-$89, un cambio en la tasa.

La base de la licuadora, no tan buena como antes,
Pero con un uso suave, durará más.
Un consejo para los batidos, congelar las frutas y verduras,
Un año después, el motor hizo un ruido divertido, oh tan atrevido.

La garantía había expirado, una decepción ver,
En general, la calidad ha disminuido, no es tan buena como solía ser.
Pero aún así, estos productos tienen su encanto,
Y con un poco de cuidado, no causarán daño.

"""


