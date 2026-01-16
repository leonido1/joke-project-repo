#!/usr/bin/env python3
"""
Home Assistant for Raspberry Pi using ChatGPT
"""

import os
import sys
from openai import OpenAI
from config.local import OPENAI_API_KEY, ASSISTANT_NAME, SYSTEM_PROMPT


class HomeAssistant:
    """Basic home assistant using ChatGPT"""
    
    def __init__(self):
        """Initialize the home assistant"""
        if not OPENAI_API_KEY:
            print("Error: OPENAI_API_KEY not set in config.py")
            sys.exit(1)
        
        self.client = OpenAI(api_key=OPENAI_API_KEY)
        self.conversation_history = []
        self.assistant_name = ASSISTANT_NAME
        
    def chat(self, user_input):
        """Send message to ChatGPT and get response"""
        try:
            # Add user message to history
            self.conversation_history.append({"role": "user", "content": user_input})
            
            # Prepare messages with system prompt
            messages = [{"role": "system", "content": SYSTEM_PROMPT}]
            messages.extend(self.conversation_history)
            
            # Get response from ChatGPT
            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=500,
                temperature=0.7
            )
            
            assistant_response = response.choices[0].message.content
            
            # Add assistant response to history
            self.conversation_history.append({"role": "assistant", "content": assistant_response})
            
            return assistant_response
            
        except Exception as e:
            return f"Error: {str(e)}"
    
    def run(self):
        """Main conversation loop"""
        print(f"{self.assistant_name} is ready! Type 'exit' or 'quit' to stop.")
        print("-" * 50)
        
        while True:
            try:
                user_input = input("\nYou: ").strip()
                
                if not user_input:
                    continue
                
                if user_input.lower() in ['exit', 'quit', 'bye']:
                    print(f"\n{self.assistant_name}: Goodbye!")
                    break
                
                print(f"\n{self.assistant_name}: ", end="", flush=True)
                response = self.chat(user_input)
                print(response)
                
            except KeyboardInterrupt:
                print(f"\n\n{self.assistant_name}: Goodbye!")
                break
            except Exception as e:
                print(f"Error: {str(e)}")


def main():
    """Main function"""
    assistant = HomeAssistant()
    assistant.run()


if __name__ == "__main__":
    main()

