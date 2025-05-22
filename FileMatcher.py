class FileMatcher:
    patterns: dict

    def __init__(self, patterns: dict):
        self.set_patterns(patterns)


    def set_patterns(self, patterns: dict):
        if (not isinstance(patterns, dict)):
            raise ValueError("patterns must be a dictionary")

        if (len(patterns) == 0):
            raise ValueError("patterns must not be empty")

        self.patterns = patterns

    def match(self, file_name: str) -> str | None:
        file_name_extension = file_name.split(".")[-1]

        if ( "." + file_name_extension in self.patterns):
            return self.patterns[ "." + file_name_extension]
        else:
            return None