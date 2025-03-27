import unittest
import json
import os
from solution import removeAllConflicts
import builtins

class TestJSONOutput(unittest.TestCase):
    def setUp(self):

        self.input_file = "temp_input.json"
        self.output_file = "temp_output.json"
    
        test_content = '''{
<<<<<<< branchA
    "key": "valueA",
=======
    "key": "valueB",
>>>>>>> branchB
    "another_key": "another_value"
}'''
        with open(self.input_file, "w") as f:
            f.write(test_content)
    
    def tearDown(self):
        for file in [self.input_file, self.output_file]:
            if os.path.exists(file):
                os.remove(file)
    
    def test_output_is_valid_json(self):
        original_input = builtins.input
        try:
            builtins.input = lambda prompt: "branchA" if "name of your branch" in prompt else "branchB"
            removeAllConflicts(self.input_file, self.output_file)
        finally:
            builtins.input = original_input

        with open(self.output_file, "r") as f:
            try:
                data = json.load(f)
            except json.JSONDecodeError as e:
                self.fail(f"Output file is not valid JSON: {e}")

if __name__ == "__main__":
    test_program = unittest.main(exit=False)

    if test_program.result.wasSuccessful():
        print("\nAll Test Cases Passed")
        print("Enter your information: ")
        print()
        removeAllConflicts("./bin/input.txt", "./bin/output.txt")
        

