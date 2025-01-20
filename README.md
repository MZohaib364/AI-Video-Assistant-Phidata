# AI Video Assistant with Phidata and Gemini 2.0

## 📊 Overview

This project is a Multimodal AI Video Assistant built with Phidata, Gemini 2.0 Flash Exp, and Streamlit. The AI agent analyzes uploaded video files and provides detailed insights based on user queries, leveraging web search tools for supplementary information.

## 🛠️ Features

- **🎥 Video Upload & Playback**: Upload `.mp4`, `.mov`, or `.avi` files and preview them.

- **🔗 YouTube Link Analysis**: Enter a YouTube video URL for analysis.

- **🧰 AI-Powered Analysis**: Analyze video content based on user-provided queries.

- **🔍 Web Research Integration**: Uses DuckDuckGo to enrich video insights.

- **📃 User-Friendly Interface**: Simple UI built with Streamlit.

## 📝 Requirements

- Python 3.x

- Streamlit

- Phidata

- Google Generative AI (google.generativeai)

- DuckDuckGo Tool

- dotenv

## 📁 Project Structure

AI-Video-Assistant-Phidata/
├── env/                   # Virtual environment
├── app.py                # Streamlit application
├── requirements.txt      # Python dependencies
├── assets/               # Images, videos, or other media
├── .env                 # API keys configuration
└── README.md             # Project documentation

## 🛠️ Setup Instructions

1. Clone the Repository

git clone https://github.com/MZohaib364/AI-Video-Assistant-Phidata.git
cd AI-Video-Assistant-Phidata

2. Create and Activate Virtual Environment

python -m venv env
./env/Scripts/activate  # Windows
source env/bin/activate # macOS/Linux

3. Install Dependencies

pip install -r requirements.txt

4. Configure API Keys

Create a .env file in the root directory:

touch .env

Add your Google API key to the .env file:

GOOGLE_API_KEY=your_google_api_key_here

Set the environment variable:

Option 1:

setx GOOGLE_API_KEY your_google_api_key_here  # Windows
export GOOGLE_API_KEY=your_google_api_key_here  # macOS/Linux

Option 2: (Temporary for session)

$env:GOOGLE_API_KEY="your_google_api_key_here"  # PowerShell

5. Run the Application

python app.py

## 🔄 Workflow

1. **Upload a Video or Enter a YouTube Link**:
   - **Upload**: Use the file uploader to select a video file.
   - **YouTube Link**: Enter the URL of the YouTube video.

2. **Enter a Query**: Provide a question or insight you're seeking about the video content.

3. **Analyze**: Click the "Analyze Video" button.

4. **View Results**: The AI-generated insights and analysis will be displayed.

## 📅 Future Improvements

Support for more video formats.

Summarization of long videos.

## 💪 Contributing

Fork the repository.

Create a new branch: git checkout -b feature-name.

Commit your changes: git commit -m "Add feature".

Push to the branch: git push origin feature-name.

Open a pull request.

## 💎 Acknowledgements

Phidata

Google Generative AI

DuckDuckGo API

----------------------------------------------------------

**Developed by Muhammad Zohaib**  
[LinkedIn](https://www.linkedin.com/in/muhammad-zohaib-a1b027280/) | [GitHub](https://github.com/MZohaib364)

