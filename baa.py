import random

sheep_faces = [
    r"""
     (\(\ 
     (-.-) 
    o_(")(")
    """,
    r"""
      |\__/|
     (='.'=)
     (")_(")
    """,
    r"""
     ,__, 
    (o.o) 
    <( )>
    """,
    r"""
       ,__,  
      (o.o)  
      (> <)  
    """,
]

compliments = [
    "You're a cybersecurity genius!",
    "Even the NSA couldn't crack your vault!",
    "Sheep approves of your password strength! 🐑",
    "Hackers cry when they see your encryption!",
]

criticisms = [
    "I've seen stronger passwords in my wool collection.",
    "A hacker could guess that in seconds!",
    "Baaaad password. Try again! 🐑",
    "I hope that's not your banking password... 😬",
]

def baa_react(password_strength):
    face = random.choice(sheep_faces)
    if password_strength > 8:
        message = random.choice(compliments)
    else:
        message = random.choice(criticisms)
    
    return f"{face}\n\n{message}"

if __name__ == "__main__":
    print(baa_react(random.randint(1, 10)))
