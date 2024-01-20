import re  # needed to extract number and title (regular expression)
from CLASS_Document import Document


class Sonnet(Document):
    def __init__(self, title, lines):
        super().__init__(lines)
        self.title = self.extract_sonnet_title(title)
        self.id = self.extract_sonnet_id(title)

    # extract the id from every title by cutting off the rest, make sure it is an integer
    @staticmethod
    def extract_sonnet_id(title) -> int:
        match = re.match(r'Sonnet (\d+): (.+)', title)
        sonnet_id = int(match.group(1)) if match else None
        return sonnet_id

    # extract the title only from every title in the dictionary by cutting off the prefix
    # make sure it is a string
    @staticmethod
    def extract_sonnet_title(title) -> str:
        match = re.match(r'Sonnet \d+: (.+)', title)
        cleaned_title = match.group(1) if match else title
        return cleaned_title

    # how to print a sonnet
    def __str__(self):
        lines_str = '\n'.join(['  ' + line for line in self.lines])
        return f"Sonnet {self.id}: {self.title}\n{lines_str}\n"
