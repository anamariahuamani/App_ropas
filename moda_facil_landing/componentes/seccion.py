import reflex as rx
def seccion()->rx.Component:
  return rx.vstack(
      rx.hstack(
        rx.vstack(
          rx.text("¿Te gustan mis prendas?",
          rx.text("¿te gustarian probarte con las prendas a"),
          rx.text("son los mejores prendas y"),
          rx.text("generar ingresos por tus creaciones?"),
),  
        ),
        rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQVbd505RwV50rfn2p5vZ-0hHGdbeMf1a49rQ&s",width="400px"),
      ),
      rx.link(https://forms.gle/PZiZiAevu7GrFB628
          rx.button(rx.icon(tag="airplay"),"Registrate",),
          href="",
          is_external=False,
      ),
      align="center",
      text_align="center",
      height="676px",
      background="#efdbea",
      
    )