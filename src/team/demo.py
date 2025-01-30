"""
Module that contains methods of each workshop participant for their generated HTML code segment
"""

# pylint: disable=C0116


def generate_angelina():
    return """
        <div class="profile" style="background-color: hotpink;">
          <h2>Angelina</h2>
          <img src="https://prod.liveshare.vsengsaas.visualstudio.com/join?F363688CC9A37F12C88B9FA691A41A5597A9" alt="Alice's picture">
          <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/2BpTWuuL2IBm3al6xVpBuC?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
"""


def generate_student():
    return """
        <div class="profile" style="background-color: lightblue;">
          <h2>The Optimal Graduate Student</h2>
          <img src="https://i.pinimg.com/564x/49/36/01/4936013e5fc4e1a82ba4ce079e5a4cae.jpg" alt="Alice's picture">
          <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/60nZcImufyMA1MKQY3dcCH?utm_source=generator&theme=0" width="100%" height="352" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
"""


def generate_rabab():
    return """
        <div class="profile" style="background-color: green;">
          <h2 style="font: italic small-caps bold 16px/2 cursive;">Yer a witch, Rabab</h2>
          <img src="https://upload.wikimedia.org/wikipedia/commons/3/34/Slytherin.png" alt="Rabab's picture">
          <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/67Pk171oVMmMdSxQxATLXW?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
"""


def generate_Nilesh():  # pylint: disable=C0103
    return """
        <div class="profile" style="background-color: blue;">
          <h2>Nilesh</h2>
          <img src="https://upload.wikimedia.org/wikipedia/commons/9/97/DNA_Double_Helix.png" alt="Alice's picture">
          <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/2BpTWuuL2IBm3al6xVpBuC?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
"""


def generate_sam():
    return """
        <div class="profile" style="background-color: hotpink;">
          <h2>Sam</h2>
          <img src="https://randomuser.me/api/?gender=male" alt="random picture">
          <iframe style="border-radius:12px" src="https://open.spotify.com/embed/track/2BpTWuuL2IBm3al6xVpBuC?utm_source=generator" width="100%" height="152" frameBorder="0" allowfullscreen="" allow="autoplay; clipboard-write; encrypted-media; fullscreen; picture-in-picture" loading="lazy"></iframe>
        </div>
"""


def generate_James():  # pylint: disable=C0103
    i = 0

    while True:
        print("Nice presentation Ange!!")
        i = i + 1

        if i == 1000:
            break

    return ""
