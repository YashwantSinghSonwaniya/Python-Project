"""
AI Chatbot with FAQ Answering and Text Summarization
A modular chatbot using OpenAI API for intelligent conversations.
Author: Your Name
Date: October 2025
"""

import os
import json
from datetime import datetime
from openai import OpenAI
import sys

# ============================================================================
# CONFIGURATION
# ============================================================================

class Config:
    """Configuration class to store API settings and application constants"""
    
    # OpenAI API key - should be set as environment variable
    API_KEY = os.getenv("OPENAI_API_KEY")
    
    # Model to use (gpt-4 or gpt-3.5-turbo)
    MODEL = "gpt-3.5-turbo"
    
    # Maximum tokens for responses
    MAX_TOKENS = 500
    
    # Temperature (0-2, lower = more focused, higher = more creative)
    TEMPERATURE = 0.7
    
    # Chat history file location
    HISTORY_FILE = "chat_history.json"
    
    # System prompts for different modes
    FAQ_SYSTEM_PROMPT = """You are a helpful FAQ assistant. Answer questions 
    clearly, concisely, and accurately. If you don't know the answer, say so."""
    
    SUMMARIZE_SYSTEM_PROMPT = """You are a text summarization expert. Provide 
    clear, concise summaries that capture the main points of the given text."""


# ============================================================================
# CHATBOT CLASS
# ============================================================================

class AIChatbot:
    """Main chatbot class handling all AI interactions and conversation flow"""
    
    def __init__(self):
        """Initialize the chatbot with OpenAI client and conversation history"""
        
        # Check if API key is set
        if not Config.API_KEY:
            raise ValueError(
                "OpenAI API key not found! Please set OPENAI_API_KEY "
                "environment variable."
            )
        
        # Initialize OpenAI client
        self.client = OpenAI(api_key=Config.API_KEY)
        
        # Initialize conversation history
        self.conversation_history = []
        
        # Current mode (faq or summarize)
        self.current_mode = None
        
        print("✓ AI Chatbot initialized successfully!")
    
    # ------------------------------------------------------------------------
    # CORE API FUNCTIONS
    # ------------------------------------------------------------------------
    
    def send_to_openai(self, user_message, system_prompt=None):
        """
        Send a message to OpenAI API and get a response
        
        Args:
            user_message (str): The user's input message
            system_prompt (str): Optional system prompt to set behavior
            
        Returns:
            str: The AI's response text
            
        Raises:
            Exception: If API call fails
        """
        try:
            # Prepare messages for API call
            messages = []
            
            # Add system prompt if provided
            if system_prompt:
                messages.append({
                    "role": "system",
                    "content": system_prompt
                })
            
            # Add user message
            messages.append({
                "role": "user",
                "content": user_message
            })
            
            # Make API call to OpenAI
            response = self.client.chat.completions.create(
                model=Config.MODEL,
                messages=messages,
                max_tokens=Config.MAX_TOKENS,
                temperature=Config.TEMPERATURE
            )
            
            # Extract and return the response text
            ai_response = response.choices[0].message.content.strip()
            
            # Save to conversation history
            self._save_to_history(user_message, ai_response, self.current_mode)
            
            return ai_response
            
        except Exception as e:
            # Handle API errors gracefully
            error_message = f"Error communicating with OpenAI API: {str(e)}"
            print(f"\n❌ {error_message}")
            return None
    
    # ------------------------------------------------------------------------
    # MODE-SPECIFIC FUNCTIONS
    # ------------------------------------------------------------------------
    
    def answer_faq(self, question):
        """
        Answer a FAQ question using OpenAI API
        
        Args:
            question (str): The user's question
            
        Returns:
            str: The AI's answer
        """
        self.current_mode = "FAQ"
        print("\n🤖 Processing your question...")
        
        # Send to OpenAI with FAQ system prompt
        response = self.send_to_openai(
            user_message=question,
            system_prompt=Config.FAQ_SYSTEM_PROMPT
        )
        
        return response
    
    def summarize_text(self, text):
        """
        Summarize a long text using OpenAI API
        
        Args:
            text (str): The text to summarize
            
        Returns:
            str: The summarized text
        """
        self.current_mode = "SUMMARIZE"
        print("\n📝 Generating summary...")
        
        # Create a summarization prompt
        prompt = f"Please provide a clear and concise summary of the following text:\n\n{text}"
        
        # Send to OpenAI with summarization system prompt
        response = self.send_to_openai(
            user_message=prompt,
            system_prompt=Config.SUMMARIZE_SYSTEM_PROMPT
        )
        
        return response
    
    # ------------------------------------------------------------------------
    # HISTORY MANAGEMENT
    # ------------------------------------------------------------------------
    
    def _save_to_history(self, user_input, ai_response, mode):
        """
        Save conversation to local history file
        
        Args:
            user_input (str): What the user asked/input
            ai_response (str): The AI's response
            mode (str): The mode used (FAQ or SUMMARIZE)
        """
        # Create a conversation entry
        entry = {
            "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "mode": mode,
            "user_input": user_input[:200] + "..." if len(user_input) > 200 else user_input,
            "ai_response": ai_response[:200] + "..." if len(ai_response) > 200 else ai_response
        }
        
        # Add to in-memory history
        self.conversation_history.append(entry)
        
        # Load existing history from file
        try:
            if os.path.exists(Config.HISTORY_FILE):
                with open(Config.HISTORY_FILE, 'r', encoding='utf-8') as f:
                    history = json.load(f)
            else:
                history = []
        except Exception as e:
            print(f"Warning: Could not load history file: {e}")
            history = []
        
        # Append new entry
        history.append(entry)
        
        # Save back to file
        try:
            with open(Config.HISTORY_FILE, 'w', encoding='utf-8') as f:
                json.dump(history, f, indent=2, ensure_ascii=False)
        except Exception as e:
            print(f"Warning: Could not save to history file: {e}")
    
    def view_history(self):
        """Display the conversation history from the current session"""
        if not self.conversation_history:
            print("\n📭 No conversation history yet in this session.")
            return
        
        print("\n" + "="*60)
        print("CONVERSATION HISTORY (Current Session)")
        print("="*60)
        
        for i, entry in enumerate(self.conversation_history, 1):
            print(f"\n[{i}] {entry['timestamp']} - Mode: {entry['mode']}")
            print(f"User: {entry['user_input']}")
            print(f"AI: {entry['ai_response']}")
            print("-" * 60)


# ============================================================================
# USER INTERFACE FUNCTIONS
# ============================================================================

def display_welcome():
    """Display welcome message and instructions"""
    print("\n" + "="*60)
    print("🤖 AI CHATBOT - FAQ Answering & Text Summarization")
    print("="*60)
    print("\nWelcome! This chatbot can help you with:")
    print("  1. Answering frequently asked questions")
    print("  2. Summarizing long texts")
    print("\nAll conversations are saved to 'chat_history.json'")
    print("="*60 + "\n")


def display_menu():
    """Display the main menu options"""
    print("\n" + "-"*60)
    print("MAIN MENU")
    print("-"*60)
    print("1. Ask a FAQ Question")
    print("2. Summarize Text")
    print("3. View Conversation History")
    print("4. Exit")
    print("-"*60)


def get_user_choice():
    """
    Get and validate user's menu choice
    
    Returns:
        str: User's choice (1-4)
    """
    while True:
        choice = input("\nEnter your choice (1-4): ").strip()
        if choice in ['1', '2', '3', '4']:
            return choice
        print("❌ Invalid choice. Please enter 1, 2, 3, or 4.")


def get_multiline_input(prompt):
    """
    Get multi-line input from user (for long text)
    
    Args:
        prompt (str): Prompt to display to user
        
    Returns:
        str: User's input (potentially multiple lines)
    """
    print(f"\n{prompt}")
    print("(Press Enter twice to finish, or type 'CANCEL' to go back)\n")
    
    lines = []
    empty_line_count = 0
    
    while True:
        line = input()
        
        if line.upper() == 'CANCEL':
            return None
        
        if line == '':
            empty_line_count += 1
            if empty_line_count >= 2:
                break
        else:
            empty_line_count = 0
            lines.append(line)
    
    return '\n'.join(lines).strip()


def format_response(response):
    """
    Format and display the AI's response nicely
    
    Args:
        response (str): The AI's response to format
    """
    if response:
        print("\n" + "="*60)
        print("🤖 AI RESPONSE:")
        print("="*60)
        print(f"\n{response}\n")
        print("="*60)
    else:
        print("\n❌ Failed to get a response. Please try again.")


# ============================================================================
# MAIN APPLICATION FLOW
# ============================================================================

def main():
    """Main function to run the chatbot application"""
    
    # Display welcome message
    display_welcome()
    
    # Initialize chatbot
    try:
        chatbot = AIChatbot()
    except ValueError as e:
        print(f"\n❌ {e}")
        print("\nTo set your API key:")
        print("  Windows: set OPENAI_API_KEY=your_api_key_here")
        print("  Mac/Linux: export OPENAI_API_KEY=your_api_key_here")
        print("\nOr add it to a .env file in the project directory.")
        sys.exit(1)
    
    # Main application loop
    while True:
        # Display menu
        display_menu()
        
        # Get user choice
        choice = get_user_choice()
        
        # Handle user choice
        if choice == '1':
            # FAQ Mode
            print("\n" + "="*60)
            print("FAQ MODE - Ask Your Question")
            print("="*60)
            question = input("\nYour question: ").strip()
            
            if question:
                response = chatbot.answer_faq(question)
                format_response(response)
            else:
                print("❌ Question cannot be empty!")
        
        elif choice == '2':
            # Summarize Mode
            print("\n" + "="*60)
            print("SUMMARIZATION MODE - Enter Text to Summarize")
            print("="*60)
            text = get_multiline_input("Paste or type the text you want to summarize:")
            
            if text:
                response = chatbot.summarize_text(text)
                format_response(response)
            elif text is None:
                print("❌ Cancelled.")
            else:
                print("❌ Text cannot be empty!")
        
        elif choice == '3':
            # View History
            chatbot.view_history()
        
        elif choice == '4':
            # Exit
            print("\n" + "="*60)
            print("👋 Thank you for using AI Chatbot!")
            print(f"💾 Your chat history has been saved to '{Config.HISTORY_FILE}'")
            print("="*60 + "\n")
            break
        
        # Ask if user wants to continue
        if choice in ['1', '2', '3']:
            input("\nPress Enter to continue...")


# ============================================================================
# ENTRY POINT
# ============================================================================

if __name__ == "__main__":
    main()