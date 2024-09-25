from db import update_data
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
import pandas as pd

# Function to create nitial suggestion message generated using LangChain and OpenAI
def show_suggestion(user_data,external_data):

    # Define the model
    llm = ChatOpenAI(model="gpt-4o", temperature=0.5)

    # Define the prompt template
    prompt = ChatPromptTemplate.from_messages(
        [
            (
                "system",
                "You are a helpful assistant that suggest a motivational 'transport of the day' quote  (not use double quotations for the quote and use emojis) which suggest how to save CO2 on user's way to work, respecting his usual transportation habits {user_data} and factoring in his environment {external_data}. Consider that when using bikes the user credits increase.",
            )
        ]
    )

    # Create the chain
    chain = prompt | llm

    # Generate response
    response = chain.invoke(
        {
            "user_data": user_data,
            "external_data": external_data
        }
    )

    return response.content

# Function to create a custom HTML progress bar for credits
def get_credit_progress_html(user_data):

    # Calculate the percentage of credit left
    percentage_left = (user_data["credit_left"] / user_data["max_credit"]) * 100

    return f"""
    <div style="width: 100%; background-color: lightgray; border-radius: 10px;">
        <div style="width: {percentage_left}%; background-color: green; height: 20px; border-radius: 10px;"></div>
    </div>
    <p>{user_data['credit_left']} / {user_data['max_credit']} Credits Remaining</p>
    """

# Function to generate a CO2 produced message
def get_co2_accumulated_html(user_data):
    co2_value = user_data['co2_produced']
    return f"""
    <div style="text-align: center;">
        <div style="font-size: 30px; font-weight: bold; color: black;">
            {co2_value} kg
        </div>
    </div>
    """

# Function to convert commute history into a pandas DataFrame for table display
def get_commute_history_df(user_data):
    return pd.DataFrame(user_data["commute_history"])

# Function to update the user's data
def update(user_data, transport_data, accepted, mode="bike"):

    if accepted == "Yes":
        user_data = update_data(user_data, transport_data, mode)

    return get_credit_progress_html(user_data), get_co2_accumulated_html(user_data), get_commute_history_df(user_data)

