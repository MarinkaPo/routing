
def change_text_input_under_condition(attribute, condition_level):

    if attribute <= condition_level:

        css_style = """
        <style>
        .stTextInput [data-baseweb=base-input] {
                                                background-color: rgb(250,199,202);
                                                -webkit-text-fill-color: black;
                                                border: 2px solid red;
                                                border-radius: 0px; 
                                            }
        </style>
        """

    else:

        css_style = """
        <style>
        .stTextInput > [data-baseweb=input] {
                                            background-color: rgb(240, 242, 246);
                                            -webkit-text-fill-color: black;
                                        }        
        </style>
        """

    return css_style