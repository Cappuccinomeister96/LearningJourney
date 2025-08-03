import json
import matplotlib.pyplot as plt
import tiktoken

def load_cost_data(file_path):
    """Load LLM cost data from a JSON file."""
    with open(file_path, 'r') as file:
        return json.load(file)

def calculate_tokens(input_text, model):
    """Calculate the number of tokens for a given input text and model."""
    try:
        encoding = tiktoken.encoding_for_model(model)
    except KeyError:
        print(f"Model '{model}' not recognized. Using default tokenizer.")
        encoding = tiktoken.get_encoding("cl100k_base")  # Default tokenizer
    return len(encoding.encode(input_text))

def calculate_cost(tokens, cost_per_token):
    """Calculate the cost based on the number of tokens and cost per token."""
    return tokens * cost_per_token

def plot_cost_comparison(models, costs, cost_type):
    """Plot a bar chart comparing costs for different models."""
    plt.bar(models, costs, color='skyblue')
    plt.xlabel('Model')
    plt.ylabel(f'Cost (USD) - {cost_type}')
    plt.title(f'Token {cost_type} Comparison')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.show()

def main():
    # Load cost data
    cost_data = load_cost_data('./01_Vorteile_Nachteile_LLM_APIs/vergleich.json')

    # Hardcoded input texts
    input_texts = [
        "Sag Hallo Welt!",
        "Dies ist ein längerer Text, um Tokenzählung zu demonstrieren. Wie viele Tokens werden verwendet?",
        "In der OpenAI-API findest du im Response-Objekt das Feld 'usage', das genaue Zahlen liefert."
    ]

    # Calculate costs for all models and texts
    for input_text in input_texts:
        print(f"\nText: '{input_text}'")
        models = []
        input_costs = []
        output_costs = []

        for model_data in cost_data:
            model_name = model_data['model']
            input_cost_per_token = model_data['input_cost_usd_per_1000_tokens'] / 1000
            output_cost_per_token = model_data['output_cost_usd_per_1000_tokens'] / 1000

            # Calculate tokens and costs
            tokens = calculate_tokens(input_text, model_name)
            input_cost = calculate_cost(tokens, input_cost_per_token)
            output_cost = calculate_cost(tokens, output_cost_per_token)

            models.append(model_name)
            input_costs.append(input_cost)
            output_costs.append(output_cost)

            print(f"Model: {model_name}, Tokens: {tokens}, Input Cost: ${input_cost:.4f}, Output Cost: ${output_cost:.4f}")

        # Plot cost comparison for the current text
        plot_cost_comparison(models, input_costs, "Input Cost")
        plot_cost_comparison(models, output_costs, "Output Cost")

if __name__ == "__main__":
    main()
