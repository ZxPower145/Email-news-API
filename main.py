import requests as req
import send_email as se
import streamlit as st

api_key = "79d1f6c78da344299c31ce709ef97daf"

body = ""

# UI
st.header("Sign up for a free newsletter :")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address: ")
    topic = st.selectbox('Select a topic for the newsletter: ', ('Tesla', 'Business', 'Entertainment',
                                                                 'General', 'Health', 'Science', 'Sports',
                                                                 'Technology'))

# The url for the news API
    url = f"https://newsapi.org/v2/everything?q={topic.lower()}&" \
          "from=2023-04-21&" \
          "sortBy=publishedAt&" \
          f"apiKey={api_key}&" \
          "language=en"

    # made a request
    request = req.get(url)

    # Get a dictionary with data
    content = request.json()

    sub_btn = st.form_submit_button("Send")
    for article in content["articles"][:20]:
        if article["title"] is not None:
            body = body + article["title"] + "\n" \
                   + article["description"] + "\n" \
                   + article["url"] + 2 * "\n"

    message = f"""\
    Subject: {topic.capitalize()} News Letter

    {body}

    """
    message = message.encode("utf-8")
    if sub_btn:
        se.send_email(user_email, message)
        st.info("Email sent successfully!")

