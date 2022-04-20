import streamlit as st
import pandas as pd
import altair as alt

st.title("On the morning of January 28, 2022, Pittsburgh's Forbes Avenue Bridge collapsed just hours before President Joe Biden's visit to the city to promote his infrastructure plan.")
st.title("This led us to wonder, what is the current status of Pennsylvania's bridges?")

def load_data_ARTBA():
    artba_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/ARTBA_Bridge_Report.csv"
    return pd.read_csv(artba_url)

def load_data_BIPA():
    bipa_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Bridge_Inventory_PA.csv"
    return pd.read_csv(bipa_url)

def load_data_PBW():
    pbw_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Proposed_Bridge_Work.csv"
    return pd.read_csv(pbw_url)

def load_data_RASP():
    rasp_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Report_A2_STATE_PUBLIC.csv"
    return pd.read_csv(rasp_url)

def load_data_RBLP():
    rblp_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Report_B2_LOCAL_PUBLIC.csv"
    return pd.read_csv(rblp_url)

st.header("Let's first take a look at how Pennsylvania compares to the rest of the country.")

df_artba = load_data_ARTBA()
df_bipa = load_data_BIPA()
df_pbw = load_data_PBW()
df_rasp = load_data_RASP()
df_rblp = load_data_RBLP()

st.write(df_artba)

st.header("Let's have a high-level overview on the condition of PA bridges.")

st.header("What types of bridges need the most help?")

st.header("How much funding do we need to fix and repair these bridges?")


