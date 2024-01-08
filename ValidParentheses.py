class Solution(object):
    def isValid(self, s):
        myMap = {'(':')', '[':']', '{':'}'} 
        stack = []

        # Loop through string s
        for i in s:
            # If it's an opening bracket
            if i in myMap: 
                stack.append(i)
            # If it's a closing bracket
            else:
                if not stack or myMap[stack.pop()] != i:
                    return False
        
        # Return True if the stack is empty, False otherwise
        return not stack  
    

# Test the isValid function with an example string
example_string = "{[()]}"
print(f"The result for the example string {example_string} is: {Solution().isValid(example_string)}")