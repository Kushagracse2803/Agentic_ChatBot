from configparser import ConfigParser

class Config:
    def __init__(self, config_file_path='./src/langgraph_agent/ui/uiconfigfile.ini') -> None:
        self.config = ConfigParser()
        self.config.read(config_file_path)

    def get_llm_options(self):
        options_str = self.config["DEFAULT"].get('LLM_OPTIONS') or "Groq"
        return [opt.strip() for opt in options_str.split(',')]
    
    def get_usecase_options(self):
        options_str = self.config["DEFAULT"].get('USECASE_OPTIONS') or "Chatbot, AI News"
        return [opt.strip() for opt in options_str.split(',')]
    
    def get_groq_model_options(self):
        options_str = self.config["DEFAULT"].get('GROQ_MODEL_OPTIONS') or "llama3-70b-8192, llama3-8b-8192"
        return [opt.strip() for opt in options_str.split(',')]
    
    def get_page_title(self):
        return self.config["DEFAULT"].get('PAGE_TITLE') or "LangGraph Agentic AI"