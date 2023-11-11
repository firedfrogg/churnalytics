import streamlit as st
from streamlit_option_menu import option_menu

import predict_churn, home

st.set_page_config(
    page_title="Customer's Prediction App"
)


class Multiapp:

    def __init__(self):
        self.apps = []

    def add_app(self, title, function):
        self.apps.append({
            "title": title,
            "function": function
        })

    def run(self):
        with st.sidebar:
            app = option_menu(
                menu_title='Navigate',
                options=['Home', 'Predict'],
                menu_icon='chat-text-fill',
                icons=['person-circle', 'info-circle-fill'],
                default_index=0,
                styles={
                    "container": {"padding": "5!important", "background-color": 'black'},
                    "icon": {"color": "white", "font-size": "12px"},
                    "nav-link": {"color": "white", "font-size": "12px", "text-align": "left", "margin": "0px",
                                 "--hover-color": "blue"},
                    "nav-link-selected": {"background-color": "#02ab21"},
                }
            )

        if app == 'Home':
            home.app()

        if app == "Predict":
            predict_churn.main()


if __name__ == '__main__':
    multiapp = Multiapp()
    multiapp.add_app("Home", home.app)
    multiapp.add_app("Predict", predict_churn.main)
    multiapp.run()
