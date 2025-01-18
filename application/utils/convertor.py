
# ORU^R01 or other message types prevent from parsing, replace it to anything, ex (BLANK) to read.

def convertMessage(string_data):
    counter = 0
    startIndex = 0
    for i in range(len(string_data)):
        if "|" == string_data[i]:
            counter += 1
            if counter == 8:
                startIndex = i+1
        
        if counter == 9:
            msg_type = string_data[startIndex:i]
            msh_message_type = msg_type
            
            string_data = string_data.replace(msg_type, "")
            return [string_data, msh_message_type]