import streamlit as st
import openai
from io import BytesIO
import base64

st.title("Camera Interaction App (OpenAI Vision on Streamlit)")

# Sidebar for secure API key entry
openai_api_key = st.sidebar.text_input("OpenAI API Key", type="password")
openai_model = "gpt-4o"  # Or gpt-4-vision-preview

# Camera input (returns photo as bytes)
image_data = st.camera_input("Take a photo with your webcam")

instruction = st.text_area("Instruction", value="What do you see?")
submit = st.button("Send to OpenAI")

if submit and not openai_api_key:
    st.error("Please enter your OpenAI API key in the sidebar.")
elif submit and image_data:
    # Convert image bytes to base64 string as expected by OpenAI
    image_bytes = image_data.getvalue()
    image_base64 = base64.b64encode(image_bytes).decode("utf-8")
    image_url = f"data:image/jpeg;base64,{image_base64}"

    # Prepare OpenAI API call payload
    payload = {
        "model": openai_model,
        "max_tokens": 256,
        "messages": [{
            "role": "user",
            "content": [
                {"type": "text", "text": instruction},
                {"type": "image_url", "image_url": {"url": image_url}}
            ]
        }]
    }

    # Call OpenAI API using openai package
    try:
        openai.api_key = openai_api_key
        resp = openai.chat.completions.create(**payload)
        # Try both access patterns for compatibility
        try:
            output_text = resp.choices[0].message.content
        except AttributeError:
            output_text = resp.choices[0]['message']['content']
        st.success("OpenAI Response:")
        st.write(output_text)
    except Exception as e:
        st.error(f"API error: {e}")

elif submit and not image_data:
    st.warning("Please take a photo before submitting.")

