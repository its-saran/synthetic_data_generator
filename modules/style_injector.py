
class Styles:
    @staticmethod
    def inject(st):
        css = f"""
            <style>
            
            div[data-testid="stSidebarHeader"] {{
                padding-bottom: 0px;
            }}

            #stDecoration {{
                visibility: hidden;
            }}

            .block-container.st-emotion-cache-1jicfl2.ea3mdgi5 {{
                padding-bottom: 0px;
                padding-top: 30px;
                padding-right: 25px;
                padding-left: 30px;
            }}

            header {{
                visibility: hidden
            }}

            div[height="550"] {{
                background-color: black;
                padding: 0;
                border: 0;
                border-radius: 0;
            }}

            div[data-testid="stSidebarUserContent"] .stTextInput label, button[kind="secondary"] svg, div[data-testid="stSidebarCollapseButton"] {{
                display: none;
            }}
            


            #app div .container-xxl {{
                padding: 0px !important;
            }}

            div[data-testid="stSidebarContent"]{{
                background-color: black;
            }}

            section[data-testid="stSidebar"] {{
                width: 320px !important; # Set the width to your desired value
            }}

            div[data-testid="stSidebarContent"] .stExpander details {{
                background-color: #0e1117;
            }}

            div[data-testid="stSidebarContent"] .stExpander details input {{
                background-color: black;
            }}

            div[data-testid="stSidebarContent"] .stExpander details button {{
                background-color: #ff4b4b;
            }}

            div[data-testid="stSidebarUserContent"] {{
                padding-bottom:0px;
            }}

            </style>
        """

        st.markdown(css, unsafe_allow_html=True)
