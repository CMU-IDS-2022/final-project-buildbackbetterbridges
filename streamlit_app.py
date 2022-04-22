import streamlit as st
import pandas as pd
import altair as alt

st.title("On the morning of January 28, 2022, Pittsburgh's Forbes Avenue Bridge collapsed just hours before President Joe Biden's visit to the city to promote his infrastructure plan.")
st.title("This led us to wonder, what is the current status of Pennsylvania's bridges?")

def load_data_ARTBA():
    artba_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/ARTBA_Bridge_Report.csv"
    data = pd.read_csv(artba_url, thousands=r',').rename(columns={"2021 State Data":"State"})
    data["SD Bridges as % of Inventory"] = data["SD Bridges as % of Inventory"].str[:-1].astype(float)
    return data

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

# st.write(df_artba)

# selection = alt.selection_multi(fields=['Number of SD bridges'], bind='legend')

hist_artba = alt.Chart(df_artba).mark_bar(
    tooltip=True
).encode(
	y = alt.Y('Number of SD bridges:Q'),
	x = alt.X('State:N', sort='-y', axis = alt.Axis(title="Top 5 States – Number of Structurally Deficient Bridges")),
	color=alt.condition(
        alt.datum.State == "Pennsylvania",  # If the rating is 80 it returns True,
        alt.value('orange'),      # and the matching bars are set as green.
        # and if it does not satisfy the condition 
        # the color is set to steelblue.
        alt.value('steelblue')
    )
).properties(
	width=325
).transform_window(
	rank='rank(Number of SD bridges)',
	sort=[alt.SortField('Number of SD bridges', order='descending')]
).transform_filter(
	(alt.datum.rank < 6)
)

hist_artba_2 = alt.Chart(df_artba).mark_bar(
    tooltip=True
).encode(
	y = alt.Y('SD Bridges as % of Inventory:Q'),
	x = alt.X('State:N', sort='-y', axis = alt.Axis(title="Top 5 States – Percent of Structurally Deficient Bridges")),
	color=alt.condition(
        alt.datum.State == "Pennsylvania",  # If the rating is 80 it returns True,
        alt.value('orange'),      # and the matching bars are set as green.
        # and if it does not satisfy the condition 
        # the color is set to steelblue.
        alt.value('steelblue')
    )
).properties(
	width=325
).transform_window(
	rank='rank(SD Bridges as % of Inventory)',
	sort=[alt.SortField('SD Bridges as % of Inventory', order='descending')]
).transform_filter(
	(alt.datum.rank < 6)
)

national_compare = alt.hconcat(hist_artba, hist_artba_2)
st.write(national_compare)

st.write("Here, we see that Pennsylvania ranks in the top 5 states for both number of structurally deficient bridges in the state as well as percentage of the state's bridges that are structurally defcient. As defined by the Pennsylvania Department of Transportation (PennDOT),a structurally deficient bridge means that deterioration has occurred to one or more of the bridge's major components (deck, superstructure, or substructure). ")

st.header("Next, let's have a high-level overview on the condition of PA bridges.")

state_source_count = pd.DataFrame({"Condition": ["Good", "Fair", "Poor"], "Percentage": ["34.43", "55.95", "9.55"]})
state_source_deckArea = pd.DataFrame({"category": ["Good Condition", "Fair Condition", "Poor Condition"], "Percentage": ["29.84%", "64.24", "5.85%"]})

pie_chart_state = alt.Chart(state_source_count).mark_arc(
	tooltip=True,
	innerRadius=50
).encode(
    theta=alt.Theta(field="Percentage", type="quantitative"),
    color=alt.Color(field="Condition", type="nominal"),
).properties(
	title="Conditions of Bridges on State Route System"
)


st.write(pie_chart_state)

st.header("What types of bridges need the most help?")

st.header("How much funding do we need to fix and repair these bridges?")


