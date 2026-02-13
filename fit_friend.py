from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
import os

load_dotenv()

class wellnessBot:
    def __init__(self):
        self.llm = ChatGroq(
            temperature=0,
            model_name="llama-3.3-70b-versatile",
            groq_api_key=os.getenv("GROQ_API_KEY")
        )

    def give_healthy_recipe(self, user_text):
        try:
            system_template = """
            You are an expert chef and wellness coach. 
            Based on the ingredient that the user is giving you, suggest a healthy cake or cookie.
    
            Provide response in this format:
            1. **Type of the food**: set a creative name for it.
            2. **Recipe**: Explain the recipe in max 1 paragraph in English.
            3. **Nutrition**: calories, protein and .....
            
            If the user asked for the adjustment, try to replace some items and come up with the new recipe.
            """

            prompt_template = ChatPromptTemplate.from_messages([
                ("system", system_template),
                ("user", "{text}")
            ])

            chain = prompt_template | self.llm
            response = chain.invoke({"text": user_text})
            return response.content

        except Exception as e:
            return f"Error connecting to the coach: {str(e)}"

    def give_workout_plan(self, user_text):
        try:
            system_template = """ You are an expert in weight training and health.
            You can help the user create a workout plan based on the equipment and body part they want to focus on.
            Provide the answer in this format:
            
            1. **Program Name**: Be creative is finding a name for the plan
            
            2. **Description**: Description of the program and number of sets and reps.
            
            3. **Estimated Time and Calories Burned**: Average calories burned and time required
            """
            prompt_template = ChatPromptTemplate.from_messages([
                ("system", system_template),
                ("user", "{text}")
                ])
            chain = prompt_template | self.llm
            response = chain.invoke({"text": user_text})
            return response.content

        except Exception as e:
            return f"Error connecting to the coach: {str(e)}"


