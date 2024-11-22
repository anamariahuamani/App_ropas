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
        rx.image(src="https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.pinimg.com%2F236x%2F17%2Fcf%2F0e%2F17cf0e89a0f159e0844b8706a42690b8.jpg&tbnid=MyWUEcFMCxlsYM&vet=10CAgQxiAoC2oXChMIgLCTpqnwiQMVAAAAAB0AAAAAEAc..i&imgrefurl=https%3A%2F%2Fin.pinterest.com%2Fpatriciabaldiviezos%2Flooks-invierno%2F&docid=JE0CHKIcH36aMM&w=235&h=320&itg=1&q=elegante%20sport%20ropas%20moda%20con%20peque%C3%B1as%20enlaces&ved=0CAgQxiAoC2oXChMIgLCTpqnwiQMVAAAAAB0AAAAAEAc",width="400px"),
      ),
      rx.link(
          rx.button(rx.icon(tag="airplay"),"Registrate",),
          href="",
          is_external=False,
      ),
      align="center",
      text_align="center",
      height="676px",
      background="#efdbea",
      
    )