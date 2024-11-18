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
        rx.image(src="https://encrypted-tbn0.gstatic.com/images?q=tbn:AN…gjvQ5qRDhSN1PNE5lNHmMaIkCJCsbx069bh9xKP4&usqp=CAU",width="400px"),
      ),
      rx.link(
          rx.button(rx.icon(tag="airplay"),"Registrate",),
          href="https://forms.gle/PvYHtu3D2NfWUq3f6",
          is_external=False,
      ),
      align="center",
      text_align="center",
      height="676px",
      background="#efdbea",
      
    )