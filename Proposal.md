# Final Project Proposal

### Problem Space 
Early in the morning on January 28, 2022, a Pittsburgh bridge collapsed “requiring rescuers to rappel down a ravine and form a human chain to reach a few occupants of a municipal bus that plummeted along with the span. No deaths were reported”. Three years prior, a routine inspection had shown the bridge’s condition as “poor”, but no maintenance was performed to update or improve its condition. Much has been debated and discussed around the topic with President Biden even arriving later in the day in Pittsburgh to promote an infrastructure bill including over $1 billion for Pennsylvania bridge maintenance. Our team is interested in looking at the condition of bridges in Pennsylvania and the distribution of infrastructure spending over the last 20 years to understand if enough funding is going toward fixing existing structures that desperately need it, or if it is instead being funneled mostly into new infrastructure projects. A 2019 Curbed article titled “U.S. addiction to building new roads eating up the money needed for maintenance” hypothesizes similarly. The article discusses how the increased spending on road widening and new lanes can simply lead to “induced demand”, where more people drive and transit issues worsen despite the appearance of progress. Instead of investing in existing infrastructure to make it safer or putting government funding toward boosting our train and bus systems, we observe that the US tends to favor new construction despite historic evidence that this does not solve the problem at hand. 

### Goal, Scope, and Target Audience 
Our goal is to add agency and awareness towards infrastructure integrity in Pennsylvania, and the resources that are being allocated towards its maintenance. We are targeting community advocates that seek to make actionable change within their surrounding neighborhoods. These users should have a working knowledge of public policy surrounding infrastructure, and understand relevant terminology. Tasks and key takeaways we plan to design include allowing users to analyze resource allocation towards bridge construction and maintenance in Pennsylvania, observing resource change over time, parse data on the structural integrity of Pennsylvania bridges, and make comparisons between bridge improvements and the resources allocated. While these preliminary tasks may adapt as we enter the design phase, we strive to allow our audience to find insights into whether funding is a contributing factor for bridge disrepair. 

### Dataset and Implementation of Solution 
We will attempt to use both national and state-level databases to help us address this problem and tell our story. We have already identified several different databases that give us the types of information we are seeking: the US Department of Transportation (USDOT)’s Federal Highway Administration has a National Bridge Inventory (NBI) that provides information on the nation’s bridges, including pertinent information such as inspection frequencies and bridge improvement costs. On a state level for Pennsylvania, the PA Open Data Portal provides annual budget program measures for statewide transportation infrastructure. The GoErie database also breaks down the number of bridges that are structurally deficient, needing repair, and rated poorly by the USDOT for the state of Pennsylvania. Using these databases and an interactive narrative format, we will be able to visualize the severity of the issues regarding bridge infrastructure in the country as well as at a local state level and determine if enough resources have been dedicated to fixing these problems. We can hopefully also propose possible future steps of improvement given the data at hand.

### Conclusion 
As students who reside in the Pittsburgh area, we believe that this project could be impactful due to its connection to recent events in the community. There is a huge opportunity to bring awareness and uncover insights that would be relevant for future infrastructure planning policy. This problem space also could yield novel exploration that will offer surprises and new knowledge for our team. 

## Data Processing and Sketches

### Data Processing 

When exploring our datasets, we found that there will be minimal cleanup or preprocessing necessary since we are gaining them from governement departmental websites, and there are no null values found. We plan to filter the categories such as condition, county, bridge type, improvement type, average daily traffic, cost and budget, etc. We are executing our prepocessing using python and pandas library. 

<img width="641" alt="image" src="https://user-images.githubusercontent.com/25258772/163445536-49c660bb-d161-4dd5-b59c-d1b62e93d9c0.png">

<img width="555" alt="image" src="https://user-images.githubusercontent.com/25258772/163446441-b6ddb1d7-c8d4-4433-8fcd-a24f8ee77bd0.png">

<img width="596" alt="image" src="https://user-images.githubusercontent.com/25258772/163448895-f816c41f-203d-48f3-bbe4-16b89b1b64b9.png">

<img width="602" alt="image" src="https://user-images.githubusercontent.com/25258772/163449024-d607ae90-0957-414e-a0d7-cfbb030b28f4.png">


### Sketches

The skecthes below showcase who we plan on structuring our project. The current structure will be (1) Introduction to problem space and visualization of scale of bridge conditions and improvements in PA, (2) Display of budge allocation, raod repair, etc. and how PA compares to others states, and (3) reveal any spatial patterns by visualizing bridge condition among PA counties. We plan for it to be interactive, and allow users to filter categories and see an updated visualization. 

<img width="957" alt="image" src="https://user-images.githubusercontent.com/25258772/163446764-a7630762-0c76-4a4c-baad-d46073b7016c.png">

<img width="1269" alt="image" src="https://user-images.githubusercontent.com/25258772/163448790-c5e11db7-3bfb-415f-90d0-74914a87922a.png">

<img width="549" alt="image" src="https://user-images.githubusercontent.com/25258772/163448948-236b7e4f-f040-4cac-8768-87a1529f13fa.png">

