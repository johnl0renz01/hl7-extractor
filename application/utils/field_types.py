# String types
string_set = {"ST", "ID", "IS", "FT", "TX"}

# Numeric types
numeric_set = {"NM", "SI"}

# Datetime types
datetime_set = {"DT", "TM", "DTM", "TS"}

# Extend String types
hierarchical_set = {"HD", "EI", "PT", "VID", "CWE", "XON", "MSG", "CX", "XPN", "XAD", "XTN"}
custom_set = {"CWE", "EI", "HD", "XON", "CX", "XPN", "XAD", "XTN"}

# string_set.update(datetime_set)
string_set.update(hierarchical_set)
string_set.update(custom_set)