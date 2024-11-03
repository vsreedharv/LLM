import openai

# Set your OpenAI API key here
openai.api_key = "your-api-key-here"

def query_llm(prompt, model="gpt-3.5-turbo", temperature=0.7, max_tokens=100):
    try:
        response = openai.ChatCompletion.create(
            model=model,
            messages=[{"role": "user", "content": prompt}],
            temperature=temperature,
            max_tokens=max_tokens,
        )
        return response.choices[0].message["content"].strip()
    except Exception as e:
        print(f"Error querying the model: {e}")
        return None

def main():
    # Get user input
    prompt = input("Enter your prompt: ")
    
    # Query the LLM
    response = query_llm(prompt)
    
    if response:
        print("Response from LLM:")
        print(response)
    else:
        print("Failed to get a response.")

if __name__ == "__main__":
    main()
