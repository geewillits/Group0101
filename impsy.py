#defeating the impostor syndrome
print('Imposter syndrome is loosely defined as doubting your abilities and feeling like a fraud.\nAmong other feelings such us:\n')

def print_feeling():
    print("1. Inability to assess competence and skills")
    print("2. Berating your performance")
    print("3. Fear that you won't live up to expectations")
    print("4. Overachieving")
    print("5. Sabotaging your own success")
    print("6. Disappointed when you fall short")
    print("Write exit to leave\n")


advices = ["If you have long-held beliefs about your incompetence in social and performance situations,\n make a realistic assessment of your abilities. Write down your accomplishments and what you are good at,\nand compare that with your self-assessment.\n", 
"Question your thoughts. As you start to assess your abilities and take baby steps,\nquestion whether your thoughts are rational.\nDoes it make sense that you are a fraud, given everything that you know?\n",
"Use social media moderately. The overuse of social media may be related to feelings of inferiority.\nIf you try to portray an image on social media that doesn't match who you really are or that is impossible to achieve,\nit will only make your feelings of being a fraud worse.\n",
"Focus on others. While this might feel counterintuitive, try to help others in the same situation as you.\nIf you see someone who seems awkward or alone, ask that person a question to bring them into the group.\nAs you practice your skills, you will build confidence in your own abilities.\n",
"Stop fighting your feelings. Don't fight the feelings of not belonging.\nInstead, try to lean into them and accept them. It's only when you acknowledge them\nthat you can start to unravel those core beliefs that are holding you back.\n",
"Take baby steps. Don't focus on doing things perfectly, but rather,\ndo things reasonably well and reward yourself for taking action.\nFor example, in a group conversation, offer an opinion or share a story about yourself.\n"
]

print_feeling()
while True:
    choice = input('Write the number associated to your feeling to receive an advice: ')
    if choice.lower() == "exit":
        break
    try:
        choiceint = int(choice)
    except:
        print("Please enter a number between 1-6 or exit")
        continue
    if choiceint >= 1 and choiceint <= 6 :
        print(advices[choiceint-1])
    else:
        print("Please enter a number between 1-6 or exit")
