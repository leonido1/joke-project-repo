"""
Configuration file for Raspberry Pi Home Assistant
"""

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# OpenAI API Configuration
# Get your API key from: https://platform.openai.com/api-keys
# You can set it here directly, or use environment variable, or .env file
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY", "")

# Assistant Configuration
ASSISTANT_NAME = "Paublo"

# System prompt for ChatGPT
SYSTEM_PROMPT = """You are a helpful home assistant running on a Raspberry Pi. 
You help users with daily tasks, answer questions, and provide useful information.
Be concise, friendly, and helpful. If asked about Raspberry Pi or home automation,
provide relevant and practical advice."""


