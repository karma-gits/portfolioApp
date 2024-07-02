import pickle
import streamlit as st
import pandas as pd


# Stock Price Prediction
def stockPrice():
    #st.header(":green[:chart_with_upwards_trend: Stock Prediction :chart_with_upwards_trend:]",divider="green")
    
    # load the model
    modelOpenPush = pickle.load(open('Stocks\modelOpenPush.pkl','rb'))
    modelHodDrop = pickle.load(open('Stocks\modelHodDrop.pkl','rb'))
    modelEodVolume = pickle.load(open('Stocks\modelEodVolume.pkl','rb'))
    modelClosedRed = pickle.load(open('Stocks\modelClosedRed.pkl','rb'))
    
  
    # Create a dropdown menu to select the stock
    allColumns = ['open', 'gap', 'hod', 'low', 'close', 'eodVolume', 'pmVolume', 'floatShares', 'marketCap', 'openPush', 'hodToClose', 'closedRed']
    X = ['open', 'gap', 'pmVolume', 'floatShares', 'marketCap']
    
    def user_options():
        col1, col2 = st.columns([1,1])
        with col1:
            marketCap = st.number_input("Enter Market Cap in Millions", 0.00, 10000.00, 35.00)
            floatShares = st.number_input("Enter Float Shares in Millions", 0.00, 1000.0, 10.0)
        with col2:
            openPrice = st.number_input("Enter Open Price", 1.0, 25.00, 3.50)
            gap = st.number_input("Enter Gap", 15.00, 100.00, 42.28)
            volume = st.number_input("Enter Volume", 200000, 10000000, 2154000)
        
            
        user_data = {
            'open' : openPrice,
            'gap': gap,
            'pmVolume': volume,
            'floatShares': floatShares*1000000,
            'marketCap': marketCap*1000000
        }
        return pd.DataFrame(user_data, index=[0])
    finaldf = user_options()
    
    ## Prediction
    
    predicted_openpush = modelOpenPush.predict(finaldf)
    predicted_hodtoclose = modelHodDrop.predict(finaldf)       
    predicted_eodvolume = modelEodVolume.predict(finaldf)
    predicted_closedred =  modelClosedRed.predict(finaldf)
    predicted_closedred = ['Yes' if predicted_closedred[0] == 1 else 'No' ]
    
    priceOpen = finaldf.open
    priceHod = priceOpen*(1+predicted_openpush[0]/100)
    priceClose = priceHod*(1-abs(predicted_hodtoclose[0]/100))
    pricePattern = pd.DataFrame({
            'index': [0,1,2],
            'price': [float(priceOpen),float(priceHod),float(priceClose)]
        })    
    
    ## Display
    st.header(":green[:chart_with_upwards_trend: Prediction :chart_with_upwards_trend:]",divider="green")
    
    with st.container():
        #st.dataframe(finaldf)
        col1, col2 = st.columns([1,1])
        with col1:
            st.text(f"Open Push : {float(predicted_openpush[0]):.2f}%")
            st.text(f"Hod to Close : {float(predicted_hodtoclose[0]):.2f}%")
            st.text(f"Eod Volume : {int(predicted_eodvolume[0]):,}")
            st.text(f"Closed Red : {predicted_closedred[0]}")
        with col2:
            st.text(f"Hod Around : ${float(priceHod):.2f}")
            st.text(f"Close Around : ${float(priceClose):.2f}")
    

        st.subheader("Predcted Price Pattern")
        st.line_chart(pricePattern,y='price', use_container_width= True)
    
    st.markdown('---')
    
    
    st.header("Technical Skills")
    st.write("**LANGUAGES:** Utilize Python (Pandas, NumPy, Seaborn) and SQL effectively")
    st.write("**ANALYTICS/DATA VISUALIZATION:** Proficient in Microsoft Excel, Tableau, Matplotlib, and Plotly")
    st.write("**DATA TECHNIQUES:** Apply Sklearn (sklearn), TensorFlow, Statistical Modeling, Machine Learning Algorithms,Data Cleaning, Data Manipulation, and Hypothesis Testing")
    st.write('___')
    
    st.header("Experience")
    st.subheader("**Data Science Fellow | March/2024 – Present**")
    st.subheader("**Springboard | Remote**")

    st.subheader(f" [● Built a Safety Gear Detection application](https://github.com/karma-gits/springboard/tree/main/Capstone%20Three)")
    st.write("""
             - Utilized Python, OpenCV, TensorFlow, and YOLO to develop a system that detects and tracks various types of safety gear in construction sites with high accuracy.
             - Enhanced safety protocols and reduced risk of accidents by 80% through accurate detection and timely notification.""")
    
    st.subheader(f" [● Constructed a Product Recommendation System](https://github.com/karma-gits/springboard/tree/main/capstone%20two)") 
    st.write("""
             -  Used Python, Pandas, Sklearn, and Matplotlib to devise a system that recommends relevant items based on user interactions and historical purchase data.
             - Enhanced user experience and engagement.""")

    st.subheader(f" [● Developed Dynamic Pricing Strategy Model](https://github.com/karma-gits/DataScienceGuidedCapstone)")
    st.write("""
            -  Created a model using data-driven techniques in Python, Pandas, and Sklearn to optimize pricing based on competitor analysis.
            -  Aimed for a +5% revenue increase.""")

    st.write('___')
    
    # Education
    st.header("Education")
    st.write("**Data Science Certification**, Springboard, Jun2024")
    st.write("**BS, Computer Science**, Western Governors University, Dec 2023")

    st.header("Certifications")
    st.write("**ITIL Foundation** - PeopleCert - Nov 2023")
    st.write("**Linux Essentials** - LPI - Oct 2023")
    st.write("**Python For Everybody** - University of Michigan - Dec 2022")
    st.write("**Google Data Analytics** - Google Career Certificates - Dec 2022")