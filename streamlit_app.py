import streamlit as st
import pandas as pd
import altair as alt

from urllib.request import urlopen
import json
import plotly
import plotly.express as px
import pandas as pd

st.title("On the morning of January 28, 2022, Pittsburgh's Forbes Avenue Bridge collapsed just hours before President Joe Biden's visit to the city to promote his infrastructure plan.")
st.title("This led us to wonder, what is the current status of Pennsylvania's bridges?")

def load_data_ARTBA():
    artba_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/ARTBA_Bridge_Report.csv"
    data = pd.read_csv(artba_url, thousands=r',').rename(columns={"2021 State Data":"State"})
    data["SD Bridges as % of Inventory"] = data["SD Bridges as % of Inventory"].str[:-1].astype(float)
    return data

def load_data_BIPA():
    bipa_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Bridge_Inventory_PA.csv"
    data = pd.read_csv(bipa_url, thousands=r',')
    data = data[:-1]
    return data

def load_data_PBW():
    pbw_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Proposed_Bridge_Work.csv"
    data = pd.read_csv(pbw_url, thousands=r',')
    data = data[:-1]
    return data

def load_data_RASP():
    rasp_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Report_A2_STATE_PUBLIC.csv"
    return pd.read_csv(rasp_url)

def load_data_RBLP():
    rblp_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Report_B2_LOCAL_PUBLIC.csv"
    return pd.read_csv(rblp_url)

def load_data_FED():
    fed_url = "https://raw.githubusercontent.com/CMU-IDS-2022/final-project-buildbackbetterbridges/main/data/Fed_Funding.csv"
    return pd.read_csv(fed_url)

st.header("Let's first take a look at how Pennsylvania's bridges compare to the rest of the country.")

df_artba = load_data_ARTBA()
df_bipa = load_data_BIPA()
df_pbw = load_data_PBW()
df_rasp = load_data_RASP()
df_rblp = load_data_RBLP()
df_fed = load_data_FED()

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

st.write("Here, we see that Pennsylvania ranks in the top 5 states for both number of structurally deficient bridges in the state as well as percentage of the state's bridges that are structurally defcient. As defined by the Pennsylvania Department of Transportation (PennDOT), a structurally deficient bridge means that deterioration has occurred to one or more of the bridge's major components (deck, superstructure, or substructure). ")

st.header("Next, let's have a high-level overview on the condition of PA bridges.")

state_source_count = pd.DataFrame({"Condition": ["Good", "Fair", "Poor"], "Percentage": ["34.43", "55.95", "9.55"]})
state_source_deckArea = pd.DataFrame({"Condition": ["Good", "Fair", "Poor"], "Percentage": ["29.84", "64.24", "5.85"]})
local_source_count = pd.DataFrame({"Condition": ["Good", "Fair", "Poor"], "Percentage": ["25.08", "48.96", "25.74"]})
local_source_deckArea = pd.DataFrame({"Condition": ["Good", "Fair", "Poor"], "Percentage": ["25.65", "52.98", "20.97"]})

source_state = pd.DataFrame({"Condition": ["Good", "Fair", "Poor", "Good", "Fair", "Poor"], "Percentage": ["34.43", "55.95", "9.55", "29.84", "64.24", "5.85"], "Method": ["Count", "Count", "Count", "DeckArea", "DeckArea", "DeckArea"]})
source_local = pd.DataFrame({"Condition": ["Good", "Fair", "Poor", "Good", "Fair", "Poor"], "Percentage": ["25.08", "48.96", "25.74", "25.65", "52.98", "20.97"], "Method": ["Count", "Count", "Count", "DeckArea", "DeckArea", "DeckArea"]})

select_box = alt.binding_select(name="Method of Measure ", options=list(source_state["Method"].unique()))
selection = alt.selection_single(fields=['Method'], bind=select_box)

pie_chart_state = alt.Chart(source_state).mark_arc(
	tooltip=True,
	innerRadius=50
).encode(
    theta=alt.Theta(field="Percentage", type="quantitative"),
    color=alt.Color(field="Condition", type="nominal"),
).properties(
	title="Conditions of Bridges on State Route System",
	width=325
).add_selection(
	selection
).transform_filter(
    selection
)

pie_chart_local = alt.Chart(source_local).mark_arc(
	tooltip=True,
	innerRadius=50
).encode(
    theta=alt.Theta(field="Percentage", type="quantitative"),
    color=alt.Color(field="Condition", type="nominal"),
).properties(
	title="Conditions of Bridges on Local Route System",
	width=325
).add_selection(
	selection
).transform_filter(
    selection
)

road_compare = alt.hconcat(pie_chart_state, pie_chart_local)
st.write(road_compare)

st.write("By count, roughly 6% of bridges on the State Route System are in poor condition, while roughly 1 in 4 bridges on the Local Route System are in poor condition. If measured by deck area, 21% of bridges in the Local Route System are in poor condition. A bridge that is considered to be in poor condition received a rating of 4 or below by state-certified bridge inspectors during each inspection of the bridge:")

st.markdown("4 = Poor, deterioration of primary structural elements has advanced.")
st.markdown("3 = Serious, deterioration has seriously affected the primary structural components.")
st.markdown("2 = Critical, deterioration of primary structural components has advanced and bridge will be closely monitored, or closed, until corrective action can be taken.")
st.markdown("1 = Imminent failure, major deterioration in critical structural components. Bridge is closed but corrective action may put the bridge back into light service.")
st.markdown("0 = Failed, bridge is out of service and beyond corrective action.")

st.header("What types of bridges need the most help?")

bridge_types = alt.Chart(df_bipa).mark_circle(size=60).encode(
    x=alt.X('Daily Crossings on All Bridges:Q', scale=alt.Scale(domain=(0, 60000000))),
    y=alt.Y('Number of Structurally Deficient Bridges:Q', scale=alt.Scale(domain=(0, 1800))),
    color='Type of Bridge',
    tooltip=['Type of Bridge', 'Number of Bridges', 'Number of Structurally Deficient Bridges', 'Daily Crossings on All Bridges']
).properties(
	height=350,
	width=800
).interactive()

st.write(bridge_types)

st.write("It appears that the bridges that need the most help are not necessarily those that are used the most. Here, we can see that bridges on rural local roads have been especially neglected.")


#SECTION TWO: MAP 
st.header("How is the county and bridge condition related?")

st.write('When exploring the condition of bridges throughout the counties, you can see that, while majority of the counties have high numbers of good or fair bridge conditions, there are some counties that have a concentration of poor condition bridges. These causes one to wonder, what why do some counties have more bridges in poor condition than others?')

#plotly map of PA
with urlopen('https://raw.githubusercontent.com/plotly/datasets/master/geojson-counties-fips.json') as response:
 counties = json.load(response)

data_url = 'data/fip_county.csv'
df = pd.read_csv(data_url)

select_box = alt.binding_select(name="Method of Measure ", options=list(source_state["Method"].unique()))
selection = alt.selection_single(fields=['Method'], bind=select_box)

conditions = ['# of poor', '# of fair', '# of good']
condition_selection = st.selectbox("Select Bridge Condition:", conditions, 0)

fig = px.choropleth(df, geojson=counties, locations='fip', color=condition_selection,
 color_continuous_scale='GnBu',
 range_color=(df[condition_selection].min(), df[condition_selection].max()),
 scope='usa',
 hover_name='counties',
 labels={'counties':'County Name:'}
 )
fig.update_layout(margin={'r':0,'t':0,'l':0,'b':0})
fig.update_geos(fitbounds='locations', visible=False)

#breakdown
counties_breakdown = alt.Chart(df).mark_bar(tooltip=True).encode(
    x=alt.X(condition_selection + ':Q'),
    y=alt.Y("counties:N", sort="-x"),
).properties(
	width=700
)

#population 
#Total bridges 

st.write(fig)
with st.expander ('Click to see county breakdown' + condition_selection): 
    st.write(counties_breakdown)
















st.header("How much funding do we need to fix and repair these bridges?")

funding_types = alt.Chart(df_pbw).mark_bar(tooltip=True).encode(
    x=alt.X('Cost to Repair (in millions):Q'),
    y=alt.Y("Type of Work:N", sort="-x"),
).properties(
	width=700
)

st.write(funding_types)

funding_stacked = alt.Chart(df_pbw).mark_bar().encode(
    x=alt.X('sum(Cost to Repair (in millions)):Q',scale=alt.Scale(domain=(0, 18522))),
    color='Type of Work',
    tooltip=['Cost to Repair (in millions)', 'Type of Work', 'Number of Bridges']
).properties(
	width=700,
	height=80
)

st.write(funding_stacked)

st.write("As seen above, it would take around 18.5 billion dollars to complete all the work needed on bridges in Pennsylvania alone, with most (~13 billion) of the needed funding going to rehabilitation of the bridge structure.")

st.header("How does Pennsylvania's transportation funding compare to the rest of the country?")

st.write("In the chart below we can see that Pennsylvania is fifth in the country for repair funding allocation. Yet, the other states in the top 5 - with the exception of Illinois - are not in the top five of places with the most structurally deficient bridges. ")

hist_fed = alt.Chart(df_fed).mark_bar(
    tooltip=True
).encode(
	y = alt.Y('Repair_Funding:Q'),
	x = alt.X('State:N', axis = alt.Axis(title="Top 5 States – Transportation Repair Funding")),
	color=alt.condition(
        alt.datum.State == "Pennsylvania",  # If the rating is 80 it returns True,
        alt.value('orange'),      # and the matching bars are set as green.
        # and if it does not satisfy the condition 
        # the color is set to steelblue.
        alt.value('steelblue')
    )
).properties(
	width=800
).transform_window(
	rank='rank(Repair_Funding)',
	sort=[alt.SortField('Repair_Funding', order='descending')]
).transform_filter(
	(alt.datum.rank < 6)
)

st.write(hist_fed)


