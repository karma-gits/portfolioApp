import pickle
import streamlit as st
import requests

def tableau():
    # display table of tableau projects
    with st.container(border=True):
        with st.container(border=True):
            st.markdown("""
                        <h3> FHV NYC 2023 🚕 | 🖥️ <a href="https://public.tableau.com/app/profile/karma.tabs/viz/FHV-NYC2023/FHV-NYC-Dashboard"> Tableau</span></a> | 
								<a href="https://github.com/karma-gits/vin_decoder" class="icon brands fa-github" style="font-size:24px"><span class="label">Github</span></a>
								</h3>                        
                        """, unsafe_allow_html=True)
            st.image("images/fulls/01.jpg", caption="FHV NYC 2023",use_column_width=True)
            st.info("- I used Python to scrape large amounts of data, which took 18 hours to complete. \n- The data from FHV was then analyzed and cleaned using SQL and Excel. \n- The ultimate goal was to visualize the insights gained from the data using Tableau, allowing for a deeper understanding and presentation of the findings.")
        
        st.write('___')   
        with st.container(border=True):
            st.markdown("""
                        <h3> AirBnB NYC 2022 🏠  |  🖥️ <a href="https://public.tableau.com/app/profile/karma.tabs/viz/Airbnb_Dashboard_16733188991360/Dashboard1">Tableau</span></a>
								</h3>                        
                        """, unsafe_allow_html=True)
            st.image("images/fulls/02.jpg", caption="AirBnB NYC 2022",use_column_width=True)
            st.info("-  utilized SQL to extract and query the Airbnb data, and then worked with Excel to analyze and clean the datasets. \n- The ultimate goal was to leverage Tableau to create informative and interactive visualizations, providing insights into Airbnb trends and patterns")
        
        st.write('___')
        with st.container(border=True):
            st.markdown("""                        
                        <h3> Every New EV Models - 2023 🔋  |  🖥️ <a href="https://public.tableau.com/views/NewElectricVehicleModelinU_S_for2023/Dashboard">Tableau</span></a> | 
								<a href="https://github.com/karma-gits" class="icon brands fa-github" style="font-size:24px"><span class="label">Github</span></a>
								</h3>                        
                        """, unsafe_allow_html=True)
            st.image("images/fulls/03.jpg", caption="Every New EV Models - 2023",use_column_width=True)
            st.info("- I scraped data from the website using Python. \n- The scraped data was then used to create interactive and informative visualizations with Tableau. \n- The goal was to gain insights and understand trends and patterns from the scraped data.  ")