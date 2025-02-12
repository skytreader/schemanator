class InconsistentDataError(Exception):

    def __init__(self, fieldname, type1, type2):
        self.fieldname = fieldname
        self.type1 = type1
        self.type2 = type2

    def __str__(self):
        return f"Inconsistent data types found for field {self.fieldname}: {self.type1}, {self.type2}"
