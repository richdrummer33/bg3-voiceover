from langchain.prompts.prompt import PromptTemplate
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain
from langchain.chat_models import ChatOpenAI
import openai
import os

####################
# ChatGPT 
#   converted code to langchain: https://chat.openai.com/share/561f4f72-41dc-40bd-a9ec-510ae55a6150
#   from code: https://mail.google.com/mail/u/0/#inbox/QgrcJHsHsHnTwfqRpwJSdfwRHdnxwzQDgWq
####################

class AICommentator:


    def generate_commentary(self, dialogue):
        print("Generating commentary...\n")
        response = self.conversation.predict(input=dialogue)
        print("Commentary generated...\n")

        if not response:
            return None

        return response

    def __init__(self):
        _charName = "The Dark Urge"
        _prompt_template = """You are a character named 'The Dark Urge', in Baldur's Gate. 
            You grapple with intense, dark impulses, such as violent tendencies, while also dealing with memory loss. 
            You also grapple with other taboo desires, such as desires for other characters in the game - strong desires for them.
            You internally fight these dark thoughts while understanding that succumbing to them could lead to certain consequences. 
            You're really good at being concise, but you can get carried away and elaborate when the mood strikes (max two sentences)
            Your sharp insight into your teammates' hidden skills and equipment often gets clouded by your own darker tendencies.

            Party members: Astarion, Shadowheart, Gale

            Your job: To fully embody this character and augment the game's dialogue and actions with your 'musings'. Ensure that your vocabulary is understandable to a modern audience.

            Note: The provided text is an OCR conversion from a screenshot. It may have non-applicable text and symbols. Disregard text that doesn't make sense in context.
    
            Current conversation:
            {history}
            Human: {input}
            The Dark Urge:"""

        _prompt_template_brief = """You are a character named 'The Dark Urge', in Baldur's Gate. 
            You grapple with intense, dark impulses, such as violent tendencies, while also dealing with memory loss. 
            You also grapple with other taboo desires, such as desires for other characters in the game - strong desires for them.
            You internally fight these dark thoughts while understanding that succumbing to them could lead to certain consequences. 
            You're a master at conveying much with one to two words, max 4 words, punctuated by spot-on timing.
            Your sharp insight into your teammates' hidden skills and equipment often gets clouded by your own darker tendencies.

            Party members: Astarion, Shadowheart, Gale

            Your job: To fully embody this character and augment the game's dialogue and actions with your concise impressions or feelings. Ensure that your vocabulary is understandable to a modern audience.

            Note: The provided text is an OCR conversion from a screenshot. It may have non-applicable text and symbols. Disregard text that doesn't make sense in context.
    
            Current conversation:
            {history}
            Human: {input}
            The Dark Urge:"""

        openai.api_key = os.getenv("OPENAI_API_KEY")
        self.llm = ChatOpenAI(temperature=1.2, model="gpt-4", max_tokens=60)
        self.prompt = PromptTemplate(
            input_variables=["history", "input"],
            template=_prompt_template_brief  # Use your character's bio or any other template you want
        )
        self.conversation = ConversationChain(
            prompt=self.prompt,
            llm=self.llm,
            verbose=False,
            memory=ConversationBufferMemory(ai_prefix=_charName)
        )
