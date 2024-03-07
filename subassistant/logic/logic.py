import sys, os

class ProcessSubtitles(object):
    def __init__(self, input_file: str, output_file: str) -> None:
        self.input_file = input_file
        self.output_file = output_file

    def process_file(self) -> None:
        with open(self.input_file, 'r', encoding='utf-8') as infile, open(self.output_file, 'w', encoding='utf-8') as outfile:
            for line in infile:
                modified_line = self.process_line(line)
                outfile.write(modified_line)

    def process_line(self, line: str) -> str:
        raise NotImplementedError



class RemoveComments(ProcessSubtitles):
    def process_line(self, line: str) -> str:
        modified_line = ''
        inside_braces = False

        for i, char in enumerate(line):
            if char == '{' and line[i + 1] != '\\':
                inside_braces = True
            elif char == '}' and inside_braces:
                inside_braces = False
            elif not inside_braces:
                modified_line += char

        return modified_line
    
    def process_file(self) -> None:
        super().process_file()
        print("Text within {} removed and written to", self.output_file)

class CommentDialogue(ProcessSubtitles):
    def process_line(self, line: str) -> str:
        if not line.startswith("Dialogue"):
            return line
        
        modified_line = ''
        inside_braces = False
        comma_count = 0 
        str_buffer = ''

        for i, char in enumerate(line.strip()):
            if char == ',':
                comma_count += 1
                if comma_count == 9: 
                    modified_line += char
                    continue

            # Check if the text part has started
            if comma_count >= 9:
                # Don't comment out the text if it's a formatting tag
                if char == '{':
                    # But if the opening brace was preceeded by dialog, we want to comment that part out
                    inside_braces = True
                    if str_buffer != '':
                        modified_line += f"{{{str_buffer}}}"
                    modified_line += char
                elif char == '}':
                    inside_braces = False
                    modified_line += char

                # Buffer the text outside of the braces to comment out later    
                elif not inside_braces:
                    str_buffer += char
                
                # We don't want to modify the line until the actual text part
                else:
                    modified_line += char
    
            else:
                modified_line += char

        if str_buffer != '':
            modified_line += f"{{{str_buffer}}}"

        return f"{modified_line}\n" 

    def process_file(self) -> None:
        super().process_file()
        print("Subtitle successfully commented and saved to ", self.output_file)

