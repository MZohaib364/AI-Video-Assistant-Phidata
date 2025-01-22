import streamlit as st
from phi.agent import Agent
from phi.model.google import Gemini
from phi.tools.duckduckgo import DuckDuckGo
from phi.tools.youtube_tools import YouTubeTools
import google.generativeai as genai
from google.generativeai import upload_file, get_file

import time
from pathlib import Path

import tempfile

from dotenv import load_dotenv
load_dotenv()

import os

API_KEY = os.getenv("GOOGLE_API_KEY")
if API_KEY:
    genai.configure(api_key=API_KEY)

st.set_page_config(
    page_title="Multimodal AI Agent - Video Assistant",
    layout = "wide"

)

st.title("Phidata AI Video Assistant Agent")
st.header("Powered by Gemini 2.0 Flash Exp")

@st.cache_resource
def initialize_agent():

    youtube_agent = Agent(
        name = "Youtube Link Handling Agent",
        model = Gemini(id="gemini-2.0-flash-exp"),
        tools = [YouTubeTools()],
        instructions = ["You are a YouTube agent. Obtain the captions of a YouTube video and answer questions."],
        show_tools_calls = True,
        markdown = True
    )

    upload_agent = Agent(
        name = "Local Video Handling Agent",
        model = Gemini(id="gemini-2.0-flash-exp"),
        markdown =True,
        tools = [DuckDuckGo()]
    )
    return Agent(
        name = "AI Video Assistant",
        team = [youtube_agent, upload_agent],
        model = Gemini(id="gemini-2.0-flash-exp"),
        markdown =True
    )

# Initialize the agents as a multiagent
Multimodal_Agent = initialize_agent()

# Input for YouTube video URL
youtube_url = st.text_input(
    "Enter YouTube video URL",
    placeholder="https://www.youtube.com/watch?v=VIDEO_ID",
    help="Provide the URL of the YouTube video you want to analyze."
)

# File uploader for local video files
video_file = st.file_uploader(
    "Or upload a video file",
    type=["mp4", "mov", "avi"],
    help="Upload a video for AI Assistant Analysis."
)

# Function to analyze YouTube video
def analyze_youtube_video(url, query):
    try:
        with st.spinner("Processing YouTube video and gathering insights..."):
            # Generate the prompt for analysis
            analysis_prompt = (
                f"Analyze the YouTube video at {url}.\n"
                f"Respond to the following query using video insights and supplementary web research:\n"
                f"{query}\n\n"
                "Provide a detailed, user-friendly, and actionable response."
            )

            # AI agent processing
            response = Multimodal_Agent.run(analysis_prompt)

        # Display the response
        st.subheader("Analysis Result")
        st.markdown(response.content)

    except Exception as error:
        st.error(f"An error occurred during analysis: {error}")

# Function to analyze uploaded local video
def analyze_uploaded_video(file_path, query):
    try:
        with st.spinner("Processing video and gathering insights..."):
            # Upload and process the video file
            process_video = upload_file(file_path)
            while process_video.state.name == "PROCESSING":
                time.sleep(2)
                process_video = get_file(process_video.name)

            # Generate the prompt for analysis
            analysis_prompt = (
                f"Analyze the uploaded video for content and context.\n"
                f"Respond to the following query using video insights and supplementary web research:\n"
                f"{query}\n\n"
                "Provide a detailed, user-friendly, and actionable response."
            )

            # AI agent processing
            response = Multimodal_Agent.run(analysis_prompt, videos=[process_video])

        # Display the response
        st.subheader("Analysis Result")
        st.markdown(response.content)

    except Exception as error:
        st.error(f"An error occurred during analysis: {error}")
    finally:
        # Clean up the temporary video file
        Path(file_path).unlink(missing_ok=True)

# Handling YouTube URL input
if youtube_url:
    user_query = st.text_area(
        "What insights are you seeking from this YouTube video?",
        placeholder="Ask anything about the video content",
        help="Provide specific questions or insights you want from the video"
    )

    if st.button("Analyze YouTube Video", key="analyze_youtube_video_button"):
        if not user_query:
            st.warning("Please provide a query to analyze the video")
        else:
            analyze_youtube_video(youtube_url, user_query)

# Handling local video file upload
elif video_file:
    with tempfile.NamedTemporaryFile(delete=False, suffix='.mp4') as temp_video:
        temp_video.write(video_file.read())
        video_path = temp_video.name

    st.video(video_path, format='video/mp4', start_time=0)

    user_query = st.text_area(
        "What insights are you seeking from this video?",
        placeholder="Ask anything about the video content",
        help="Provide specific questions or insights you want from the video"
    )

    if st.button("Analyze Uploaded Video", key="analyze_uploaded_video_button"):
        if not user_query:
            st.warning("Please provide a query to analyze the video")
        else:
            analyze_uploaded_video(video_path, user_query)

else:
    st.info("Enter a YouTube video URL or upload a video file to begin analysis")

# Customize text area height
st.markdown(
    """
    <style>
    .stTextArea textarea{
        height: 100px;
    }
    </style>
    """,
    unsafe_allow_html=True
)
