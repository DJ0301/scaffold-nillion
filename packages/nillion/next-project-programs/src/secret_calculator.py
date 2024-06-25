from nada_dsl import *

def nada_main():
    # Create a party (just like in your example)
    calculator_party = Party(name="Secret Calculator 🧮")

    # Define two secret integers as inputs
    secret_int_1 = SecretInteger(Input(name="input_1", party=calculator_party))
    secret_int_2 = SecretInteger(Input(name="input_2", party=calculator_party))

    # Perform arithmetic operation (addition in this case)
    result = secret_int_1 + secret_int_2

    # Return the result as an output
    return [Output(result, "output_result", calculator_party)]

# Example usage:
if __name__ == "__main__":
    outputs = nada_main()
    print(outputs)
