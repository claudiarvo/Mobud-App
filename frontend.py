import gradio as gr
from db import init_data
from backend import *

# Function that handles user feedback and updates the relevant data
def handle_update(response):
    return update(user_data, transport_data, response)

# Function for creating the Gradio interface for the application
def interface():

    # Create the Gradio Interface
    with gr.Blocks(theme=gr.themes.Monochrome(),  css="footer{display:none !important}") as demo:

        # Add a title to the interface
        gr.Markdown("<h1 style='text-align: center;'>Corporate Mobility Budget</h1>")

        # Display the suggestion automatically
        gr.Markdown("### Today's Transport Suggestion")
        suggestion_output = gr.Textbox(value=show_suggestion(user_data,external_data), label="", interactive=False)

        # Add Yes/No radio buttons for user feedback
        response_input = gr.Radio(choices=["Yes", "No"], label="Do you accept this suggestion?")

        # Display user credit and CO2 emitted
        with gr.Row():
            with gr.Column(scale=1):
                gr.Markdown("<h3 style='text-align: center;'>Mobility Credit Left</h3>")
                credit_progress = gr.HTML(get_credit_progress_html(user_data))

            with gr.Column(scale=1):
                gr.Markdown("<h3 style='text-align: center;'>CO2 Produced</h3>")
                Co2 = gr.HTML(get_co2_accumulated_html(user_data))

        # Display Commute History
        gr.Markdown("### Commutes History")
        commute_history_df = get_commute_history_df(user_data)
        commute_history_table = gr.DataFrame(value=commute_history_df)

        # When user feedback is Yes, update data and refresh
        response_input.change(handle_update, inputs=[response_input],
                          outputs=[credit_progress, Co2, commute_history_table])

    return demo

# Initialize data
user_data, transport_data, external_data = init_data()

# Create demo interface
demo = interface()

# Launch the demo
demo.launch()


