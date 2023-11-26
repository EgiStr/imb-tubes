# Path: TUBES/IMB/app.py

# import library that will be used in this app
import streamlit as st
from streamlit_option_menu import option_menu

from model import load_data, CrudDateset
from controllers import ListDataController,Auth
# start the app
def main():
    # set logo of the app in the browser tab
    st.set_page_config(
        page_title="IMB",
        page_icon="./logo.jpg",
        layout="centered",
        initial_sidebar_state="expanded",
    )
    # create title
    auth = Auth()

    

    # get session state
    if "index" not in st.session_state:  # check if index is not in session state
        st.session_state["index"] = 0  # set index to 0
    if "page" not in st.session_state:  # check if page is not in session state
        st.session_state["page"] = 0
    if "route" not in st.session_state:  # check if route is not in session state
        st.session_state["route"] = "Home"
    if "authentication_status" not in st.session_state :
        st.session_state["authentication_status"] = None
    if "name" not in st.session_state :
        st.session_state["name"] = None


    # create sidebar navigation with option menu
    def on_change_nav(key):
        st.session_state["route"] = st.session_state[key]

    # create sidebar navigation with option menu
    # check if user is authenticated or not
    if st.session_state["authentication_status"]:
        option_menu(
            menu_title=None,
            options=["Home", "Form Pengaduan", "Statistic Data", "About","dahsboard","Logout"],

            orientation="horizontal",
            key="nav-1",
            menu_icon=None,
            styles={
                "btn_class": "primary",
                "dropdown_class": "primary",
                "btn_width": "150px",
                "font_family": "Arial",
                "font_size": "17px",
                "padding": "0px",
                "margin": "0px",
                "background_color": "#ffffff",
                "hover_color": "#fafafa",
                "border_radius": "0px",
                "active_color": "#ffffff",
                # navbar full screen
                "navbar": "fixed",
                "width": "100hv",
                "z_index": "999",

            },
            on_change=on_change_nav,
            default_index=0,

        )
    else:
        option_menu(
            menu_title=None,
            orientation="horizontal",
            options=["Home", "Form Pengaduan", "Statistic Data", "About","Login"],

            key="nav-1",
            menu_icon=None,
            styles={
                "btn_class": "primary",
                "dropdown_class": "primary",
                "btn_width": "150px",
                "font_family": "Arial",
                "font_size": "17px",
                "padding": "0px",
                "margin": "0px",
                "background_color": "#ffffff",
                "hover_color": "#fafafa",
                "border_radius": "0px",
                "active_color": "#ffffff",
                # navbar full screen
                "navbar": "fixed",
                "width": "100hv",
                "z_index": "999",

            },
            on_change=on_change_nav,
            default_index=0,

        )
    # untuk manage data
    crud = CrudDateset(load_data())
    # untuk manage routing
    controller = ListDataController(crud,auth)
    


    # create if condition to show the selected option menu
    if st.session_state["route"] == "Detail Laporan":
        controller.detail_data()
    elif st.session_state["route"] == "Home":
        controller.list_data()
    elif st.session_state["route"] == "Form Pengaduan":
        controller.add_data()
    elif st.session_state["route"] == "Statistic Data":
        controller.statistic_data()
    elif st.session_state["route"] == "About":
        controller.about()
    elif st.session_state["route"] == "Login":
        controller.login()
    elif st.session_state["route"] == "Logout":
        controller.logout()
    elif st.session_state["route"] == "dashboard":
        controller.dashboard()
        
    



if __name__ == "__main__":
    main()
