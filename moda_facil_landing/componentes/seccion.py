import reflex as rx
def seccion()->rx.Component:
    return rx.vstack(
        rx.container(
            rx.hstack(
                rx.heading(
                    rx.text.strong(
                        "",
                        color=("gray",10),
                        font_size="1.5em",
                        text_align="center",
                        margin_bottom="1em"
                    ),
                    rx.hstack(
                    rx.text.span(
                        "tenemos los mejores prendas de moda y de mejor calidad y alos mejores precios y te todas las tallas para niños  y jovenes",
                        color=("black",10),
                        font_size="1.2em",
                        align="left",
                        widht="60%",
                        margin_right="2em")),
                    ),
           
            rx.image(src="https://promova.com/content/large_ropa_de_mujer_53c6ef780d.png",
                     widht=200,
                     height=200,
                     align="center"),
            ),
            
            
            rx.vstack(
                rx.link(
                rx.button(rx.icon(tag="pen"),"Regístrate",),
                href="https://forms.gle/EW5kp8VP7Uma89fDA",
                is_external=False,
                margin_top="5em",
                padding="5em",
                justify="center",
                position="absolute",
                top="50%",
                left="40%"
            ),
            align_items="center"            ),

       ),
        
            padding_top="5em",
            align="center",
            text_align="start",
            height="750px",
            background="#FF87A5"
    )