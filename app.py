import streamlit as st
import json
from modules import Table, Styles
from streamlit_option_menu import option_menu
import datetime
from streamlit_extras.row import row


def load_config(path):
    with open(path, 'r') as file:
        return json.load(file)


class App:
    def __init__(self, config):
        self.config = config
        self.selected_table = ''

        st.set_page_config(
            layout=self.config['app']['page']['layout'],
            page_title=self.config['app']['page']['title'],
            page_icon=self.config['app']['page']['icon'],
            initial_sidebar_state=self.config['app']['page']['sidebar'],
        )

        if 'tables' not in st.session_state:
            st.session_state['tables'] = {}
        if 'expander_open' not in st.session_state:
            st.session_state['expander_open'] = True  # Start with expander open

    def show(self):
        with st.sidebar:
            # Control expander state
            with st.expander("Create Table", expanded=st.session_state['expander_open']):
                col1, col2 = st.columns([8, 2])

                with col1:
                    table_name = st.text_input(label="Enter table name", placeholder="Enter table name",
                                               label_visibility='hidden')
                with col2:
                    if st.button("", icon=":material/add:"):
                        if table_name and table_name not in st.session_state['tables']:
                            table = Table()
                            table.create(table_name)

                            st.session_state['tables'][table_name] = table
                            st.session_state['expander_open'] = False

                            st.rerun()

            # Container for displaying created tables
            with st.container(height=550):
                if st.session_state['tables']:
                    table_keys = list(st.session_state['tables'].keys())
                    default_index = len(table_keys) - 1  # Default to the last created table
                    selected_table = option_menu(
                        None,
                        table_keys,
                        default_index=default_index,
                        styles=self.config['app']['options-menu']
                    )
                else:
                    selected_table = None

        if selected_table:
            s_table = st.session_state['tables'][selected_table]
            st.write(s_table.table)

            col1, col2, col3 = st.columns([1, 1, 1])

            column_name = col1.text_input('Column Name')
            col_type = col3.selectbox("Column type", options=['Number', 'Text', 'Date'])
            nrows = col2.number_input("Number of rows", value=100, min_value=1, step=1, format="%d")

            expander = st.expander("Column Options")
            sec1, sec2, sec3 = expander.columns([1, 1, 1])
            col_props = {}
            if col_type == 'Number':
                col_props['start'] = sec1.number_input("Start", value=1, min_value=1, step=1, format="%d")
                col_props['end'] = sec2.number_input("End", value=1000, min_value=1, step=1, format="%d")
                col_props['step'] = sec3.number_input("Step", value=1, min_value=1, step=1, format="%d")
            elif col_type == 'Date':
                col_props['start'] = sec1.date_input("Start Date", datetime.date(2024, 10, 1))
                col_props['end'] = sec2.date_input("End date", datetime.date(2024, 10, 31))
                col_props['freq'] = sec3.selectbox("Frequency", ('D', 'W', 'MS', 'ME'))
            elif col_type == 'Text':
                col_props['text'] = sec1.text_input("Text")
                col_props['type'] = sec2.selectbox("Type", ('Repeat'))

                expander1 = st.expander("Conditions")

                cont1, cont2 = expander1.columns([1, 1])
                cont1.selectbox("Select Country", ["Germany", "Italy", "Japan", "USA"])
                cont2.text_input("Your name")

            if st.button("Generate Column"):
                s_table.generate_column(column_name, nrows, col_type, col_props)
                st.session_state['tables'][selected_table] = s_table
                st.rerun()


if __name__ == '__main__':
    config = load_config("config/config.json")
    web_app = App(config)
    web_app.show()
    Styles.inject(st)


