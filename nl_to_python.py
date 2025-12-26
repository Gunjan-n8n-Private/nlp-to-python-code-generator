
import re

class NLPToPython:
    """
    A simple rule-based NLP to Python code generator.
    Parses natural language instructions and converts them into valid Python code.
    """

    def __init__(self):
        
        self.rules = [
            (r"print\s+(?:numbers\s+)?from\s+(\d+)\s+to\s+(\d+)", self._handle_range_loop),
            (r"print\s+['\"](.+)['\"]", self._handle_print_string),
            (r"print\s+(.+)", self._handle_print_variable_or_expression),
            (r"create\s+function\s+(\w+)\s+that\s+prints\s+['\"](.+)['\"]", self._handle_create_function),
            (r"set\s+(\w+)\s+to\s+(.+)", self._handle_assignment),
            (r"add\s+(\d+)\s+and\s+(\d+)", self._handle_addition),
            (r"subtract\s+(\d+)\s+from\s+(\d+)", self._handle_subtraction),
            (r"multiply\s+(\d+)\s+by\s+(\d+)", self._handle_multiplication),
            (r"divide\s+(\d+)\s+by\s+(\d+)", self._handle_division),
        ]

    def translate(self, instruction: str) -> str:
        """
        Translates a single line of natural language instruction to Python code.
        """
        instruction = instruction.strip().lower()
        
        for pattern, handler in self.rules:
            match = re.search(pattern, instruction, re.IGNORECASE)
            if match:
                return handler(match)
        
        return f"# Could not understand instruction: {instruction}"

    def _handle_range_loop(self, match):
        start = int(match.group(1))
        end = int(match.group(2))
        
        return f"for i in range({start}, {end + 1}):\n    print(i)"

    def _handle_print_string(self, match):
        content = match.group(1)
        return f"print('{content}')"

    def _handle_print_variable_or_expression(self, match):
        content = match.group(1)
        
        return f"print({content})"

    def _handle_create_function(self, match):
        func_name = match.group(1)
        print_content = match.group(2)
        return f"def {func_name}():\n    print('{print_content}')"

    def _handle_assignment(self, match):
        var_name = match.group(1)
        value = match.group(2)
        return f"{var_name} = {value}"

    def _handle_addition(self, match):
        n1, n2 = match.groups()
        return f"print({n1} + {n2})"

    def _handle_subtraction(self, match):
        n1, n2 = match.groups()
        return f"print({n2} - {n1})"

    def _handle_multiplication(self, match):
        n1, n2 = match.groups()
        return f"print({n1} * {n2})"

    def _handle_division(self, match):
        n1, n2 = match.groups()
        return f"print({n1} / {n2})"

if __name__ == "__main__":
    converter = NLPToPython()
    
    print("AI/ML Assignment: text-to-python-code")
    print("Type 'exit' to quit.\n")
    
    while True:
        try:
            user_input = input("Enter instruction: ")
            if user_input.lower() == 'exit':
                break
            
            code = converter.translate(user_input)
            print(f"Generated Code:\n{code}\n")
            
        except KeyboardInterrupt:
            break
        except Exception as e:
            print(f"Error: {e}")
