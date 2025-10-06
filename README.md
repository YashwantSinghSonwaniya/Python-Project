# AI Chatbot - FAQ Answering & Text Summarization

A professional, modular Python chatbot powered by OpenAI's GPT API. Perfect for learning AI integration and showcasing on your resume!

## 🌟 Features

- **FAQ Answering**: Get intelligent answers to your questions
- **Text Summarization**: Automatically summarize long texts
- **Chat History**: All conversations saved locally in JSON format
- **Error Handling**: Robust error handling for API failures
- **Clean Architecture**: Modular, well-commented code structure
- **Beginner-Friendly**: Easy to understand and extend

## 📋 Prerequisites

- Python 3.8 or higher
- OpenAI API key (get one at https://platform.openai.com/api-keys)
- Basic knowledge of command line

## 🚀 Installation & Setup

### Step 1: Clone or Download the Project

Download all project files to a folder on your computer:
- `chatbot.py` (main script)
- `requirements.txt`
- `README.md` (this file)

### Step 2: Install Python Dependencies

Open your terminal/command prompt in the project folder and run:

```bash
pip install -r requirements.txt
```

Or install packages individually:

```bash
pip install openai python-dotenv
```

### Step 3: Set Up Your OpenAI API Key

You need to set your OpenAI API key as an environment variable.

#### Option A: Set Environment Variable (Temporary)

**Windows (Command Prompt):**
```cmd
set OPENAI_API_KEY=your_api_key_here
```

**Windows (PowerShell):**
```powershell
$env:OPENAI_API_KEY="your_api_key_here"
```

**Mac/Linux:**
```bash
export OPENAI_API_KEY=your_api_key_here
```

#### Option B: Use a .env File (Recommended)

1. Create a file named `.env` in the project folder
2. Add this line (replace with your actual key):
   ```
   OPENAI_API_KEY=your_api_key_here
   ```
3. Modify the chatbot.py to load from .env (add at the top):
   ```python
   from dotenv import load_dotenv
   load_dotenv()
   ```

### Step 4: Run the Chatbot

```bash
python chatbot.py
```

## 📖 How to Use

1. **Start the chatbot**: Run `python chatbot.py`
2. **Choose a mode**:
   - Option 1: Ask a FAQ question
   - Option 2: Summarize text (paste long text, press Enter twice to finish)
   - Option 3: View conversation history
   - Option 4: Exit

3. **View history**: All conversations are automatically saved to `chat_history.json`

## 💡 Example Usage

### FAQ Example:
```
Your question: What is machine learning?

🤖 AI RESPONSE:
Machine learning is a subset of artificial intelligence that enables 
computers to learn from data and improve their performance over time 
without being explicitly programmed...
```

### Summarization Example:
```
Paste or type the text you want to summarize:
(Press Enter twice to finish)

[Paste long article here]

🤖 AI RESPONSE:
The article discusses three main points: 1) The rise of AI technology...
```

## 🏗️ Project Structure

```
ai-chatbot/
│
├── chatbot.py           # Main application file
├── requirements.txt     # Python dependencies
├── README.md           # This file
├── chat_history.json   # Auto-generated conversation log
└── .env               # API key (you create this)
```

## 🔧 Code Structure

The code is organized into clear sections:

1. **Configuration Class**: Stores all settings and API parameters
2. **AIChatbot Class**: Main chatbot logic
   - `send_to_openai()`: Core API communication
   - `answer_faq()`: FAQ answering mode
   - `summarize_text()`: Text summarization mode
   - `_save_to_history()`: Conversation logging
3. **UI Functions**: Menu display and user input handling
4. **Main Flow**: Application entry point and loop

## 🎨 Customization Tips

### Change the AI Model
In `chatbot.py`, modify the `Config` class:
```python
MODEL = "gpt-4"  # Use GPT-4 for better responses (costs more)
# or
MODEL = "gpt-3.5-turbo"  # Faster and cheaper
```

### Adjust Response Length
```python
MAX_TOKENS = 1000  # Longer responses
```

### Make Responses More Creative
```python
TEMPERATURE = 1.5  # Higher = more creative (range: 0-2)
```

## 🚀 Professional Improvements (Future Features)

Here are ideas to make this project even more impressive:

### Easy Improvements:
1. **Add a GUI**: Use `tkinter` or `streamlit` for a graphical interface
2. **Web Deployment**: Deploy as a Flask/FastAPI web app
3. **Database Storage**: Replace JSON with SQLite for better data management
4. **Export History**: Add options to export chat history as PDF/CSV
5. **Multi-language Support**: Add translation capabilities

### Intermediate Improvements:
1. **Conversation Context**: Make the chatbot remember previous messages in the same session
2. **Document Upload**: Allow users to upload PDF/DOCX files for summarization
3. **Custom Knowledge Base**: Add RAG (Retrieval Augmented Generation) with vector database
4. **User Authentication**: Add user accounts and personal chat histories
5. **Sentiment Analysis**: Detect user emotion and adjust responses

### Advanced Improvements:
1. **Voice Integration**: Add speech-to-text and text-to-speech
2. **Multi-Modal**: Process images along with text using GPT-4 Vision
3. **API Rate Limiting**: Implement token counting and cost tracking
4. **A/B Testing**: Compare different prompts/models for best results
5. **Production Ready**: Add logging, monitoring, and error alerting

## 🐛 Troubleshooting

### "OpenAI API key not found" Error
- Make sure you set the environment variable correctly
- Check that there are no extra spaces in your API key
- Try using the .env file method instead

### "Module not found" Error
- Run `pip install -r requirements.txt` again
- Make sure you're in the correct project directory
- Try `pip3` instead of `pip` if on Mac/Linux

### API Timeout or Connection Errors
- Check your internet connection
- Verify your API key is valid at https://platform.openai.com/api-keys
- Check if you have API credits/quota remaining

### Rate Limit Errors
- You may have exceeded OpenAI's rate limits
- Wait a few minutes and try again
- Consider upgrading your OpenAI plan

## 💰 API Costs

Using this chatbot costs money based on OpenAI's pricing:
- **GPT-3.5-turbo**: ~$0.0015 per 1000 tokens (very cheap)
- **GPT-4**: ~$0.03 per 1000 tokens (more expensive but smarter)

A typical conversation costs less than $0.01 with GPT-3.5-turbo.

## 📝 Resume Tips

When adding this to your resume/portfolio:

**Project Description Example:**
> *Developed a production-ready AI chatbot using Python and OpenAI's GPT API with modular architecture, featuring FAQ answering and text summarization capabilities. Implemented error handling, conversation logging, and a user-friendly CLI interface.*

**Skills Demonstrated:**
- API Integration (OpenAI)
- Python Programming
- Error Handling & Exception Management
- File I/O and JSON handling
- Object-Oriented Programming
- User Interface Design
- Code Documentation

## 📄 License

This is a learning project - feel free to use, modify, and share!

## 🤝 Contributing

Want to improve this project? Feel free to:
1. Fork the repository
2. Make your changes
3. Test thoroughly
4. Submit suggestions

## 📧 Questions?

If you run into issues, check:
1. OpenAI API documentation: https://platform.openai.com/docs
2. Python documentation: https://docs.python.org/3/

---

**Happy Coding! 🎉**

Built with ❤️ for AI enthusiasts and Python learners