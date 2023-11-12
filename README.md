# About

- Author: Pradeep Yenkuwale
- Contact: pradeep1yenkuwale@gmail.com
- Description: This AI model specializes in recommending budget-friendly trips to various cities, taking into account both financial constraints and preferred travel seasons.
- Python 3.10.5, pip 23.3.1.
- Packages: langchain, openai, chromadb, tiktoken

# Installation

- Download [Python 3.10.5](https://www.python.org/ftp/python/3.10.5/python-3.10.5-amd64.exe)
- To clone the repository use `git clone https://github.com/theTechie93/assignment-app.git`
- Install supporting packages: `pip install angchain openai chromadb tiktoken`
- Make sure the `constants.py` file has the openai key updated => `API_KEY = "sk-<OpenAI_API_Key>"` [Get Key here](https://platform.openai.com/api-key)
- To run the script - Run: `python script.py`

# Data to be trained to the model

- Reference File: `data/data.json`
- Within this file, you'll find response data tailored for customer queries.
- The data is structured as a JSON object, specifically an array of objects.
- Each object comprehensively captures city details, including the country name, travel budget, and the most favorable season to visit.
- When a user inquires about travel trips, the model will extract information from this JSON file.

# Sample Runs

## Run 1:

PS D:\my_personal\Repositories\open-ai\Python\assignment-app> python script.py

Ask me a trip suggestion: Suggest me a trip

Here are some suggestions for trips:

1. For a trip to India during the monsoon season, you could consider visiting cities like Manali and Shimla. The budget for this trip would be between Rs 60,000 and Rs. 80,000.

2. If you're interested in visiting France, a trip to Paris during the winter season could be a great choice. The budget for this trip would be between $4,000 and $10,000.

3. Another option is to visit New York City in the USA during the winter season. The budget for this trip would be between $2,000 and $6,000.

Please note that these are just a few suggestions based on the given information. You can explore other destinations and seasons based on your preferences and budget.
Ask me a trip suggestions:

## Run 2

PS D:\my_personal\Repositories\open-ai\Python\assignment-app> python script.py

Ask me a trip suggestion: Get a trip details for Dubai

For a trip to Dubai, the estimated budget is between Dhs 8,000 and Dhs 12,000. Dubai is located in the United Arab Emirates and is known
for its luxurious hotels, shopping malls, and iconic landmarks like the Burj Khalifa. The best time to visit Dubai is during the summer season.

Ask me a trip suggestion: When i can travel to paris

The best time to travel to Paris is during the winter season.

Ask me a trip suggestion: What is the budget for paris trip

The estimated budget for a trip to Paris is between $4,000 and $10,000.
Ask me a trip suggestion:

## Run 3

PS D:\my_personal\Repositories\open-ai\Python\assignment-app> python script.py

Ask me a trip suggestion: suggest me a trip for $6000

Some suggested trips that can be planned within a budget of $6,000 are:

1. Dallas, USA: Visit the vibrant city of Dallas, explore its museums, enjoy live music, and indulge in Texan cuisine.

2. Dubai, United Arab Emirates: Experience the luxury and glamour of Dubai, visit iconic landmarks like the Burj Khalifa, go shopping in the famous malls, and enjoy the city's vibrant nightlife.

Please note that these are just a few suggestions based on the given budget. There are many other destinations to consider within this budget.

Ask me a trip suggestion: suggest me a trip for SAR 10000

Based on the provided information, here are some suggested trips that can be planned within a budget of SAR 10,000:

1. Riyadh, Saudi Arabia: You can explore the capital city and visit attractions like the Kingdom Centre Tower and the National Museum. The budget should be sufficient for accommodation, transportation, and meals.

2. Jeddah, Saudi Arabia: Jeddah offers a mix of historical sites and modern attractions like the King Fahd Fountain and the Old Town. The budget should cover your expenses for a short trip.

Please note that the information provided is based on the given context, and prices may vary depending on factors such as travel dates, accommodation choices, and personal expenses. It is always recommended to research and plan your trip in advance to get accurate cost estimates.
Ask me a trip suggestion:
