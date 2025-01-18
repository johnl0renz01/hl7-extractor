from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

import os
import psycopg2
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
url = os.getenv("DATABASE_URL")
connection = psycopg2.connect(url)


from hl7apy.parser import parse_message

# hl7_message = """
# MSH|^~\&|GHH_ADT||||20080115153000||ADT^A01^ADT_A01|0123456789|P|2.5||||AL
# EVN||20080115153000||AAA|AAA|20080114003000
# PID|1|25366|25366||DOE^JANE^VARAS||19770219000000.0000+08:00|F|||B13 L24 ROYALE^Bulihan^Malolos City^Bulacan|||||||25128
# NK1|1|NUCLEAR^NELDA^W|SPO|2222 HOME STREET^^ANN ARBOR^MI^^USA
# """

# ORU^R01 prevent from reading, replace it to anything, ex (BLANK) to read.

hl7_message = """
MSH|^~\&|NovaRAD|Radiology Dept|Mirth|PHI-SSH|20240322230242.0000+08:00||BLANK|346GRE633FGZ@%@#$@#sdfdssd|P|2.3
PID|1|25366|25366||DOE^JANE^VARAS||19770219000000.0000+08:00|F|||B13 L24 ROYALE^Bulihan^Malolos City^Bulacan|||||||25128
PV1|1|E|||||310^Rosales MD, FPCR Lic. No. 45646^Jesse-Lim|247^DOE^DOCTOR|||||||||||807427
ORC|RE|FEA|35497||||^^5^20240322194100.0000+08:00^20240322194600.0000+08:00||20240322213344.0000+08:00|3^ACCOUNT^SYSTEM||247^DOE^DOCTOR
OBR|1|FEA|35497||||20240322214731.0000+08:00|||||||||||7788106||||||CR|F||^^5^20240322194100.0000+08:00^20240322194600.0000+08:00^S|||||310^Rosales MD, FPCR Lic. No. 45646^Jesse-Lim||||||||||||XRY00015^CERVICAL AP/LATERAL^^^CERVICAL AP/LATERAL
OBX|1|TX|^35510.16309.Report Text||FINDINGS:~~Limited study due to non-visualization of the lower cervical vertebrae.~~There is reversal of the normal cervical curvature which may be due to muscle spasm.~~There is no evidence of fracture seen. ~~Vertebral bodies and intervertebral space are well maintained.  ~~Laminae and pedicles are intact. ~~CT scan correlation is suggested if clinically warranted~~||http://192.168.1.15/NovaWeb/WebViewer/Account/ValidateUserFromUrl?key=01phe1vPyq9Ltkasd4QRSqf3uyJDReqd9G714WGusqdaE1YDFdTKLJvd7vMNBzFf6qv3qwcvC6Z6D7uX3vZsgP9Fe8HqyUQ6VfPXk6jN2JhsFV5e4YmfmJ6W|||||||||||
"""


segments = hl7_message.split('\n')
segments = list(filter(lambda txt: txt != "", segments))

segment_keys = {}

for segment in segments:
    pipe_idx = segment.index('|')
    key = segment[0:pipe_idx].lower()
    segment_keys[key] = ''

# print(segment_keys)


hl7_message = "\r".join(segments)
message = parse_message(hl7_message)


msh_dict = {
    "field_separator": None,                # MSH-1: Field Separator
    "encoding_characters": None,            # MSH-2: Encoding Characters
    "sending_application": None,            # MSH-3: Sending Application
    "sending_facility": None,               # MSH-4: Sending Facility
    "receiving_application": None,          # MSH-5: Receiving Application
    "receiving_facility": None,             # MSH-6: Receiving Facility
    "datetime_of_message": None,            # MSH-7: Date/Time of Message
    "security": None,                       # MSH-8: Security
    "message_type": None,                   # MSH-9: Message Type
    "message_control_id": None,             # MSH-10: Message Control ID
    "processing_id": None,                  # MSH-11: Processing ID
    "version_id": None,                     # MSH-12: Version ID
    "sequence_number": None,                # MSH-13: Sequence Number
    "continuation_pointer": None,           # MSH-14: Continuation Pointer
    "accept_acknowledgment_type": None,     # MSH-15: Accept Acknowledgment Type
    "application_acknowledgment_type": None, # MSH-16: Application Acknowledgment Type
    "country_code": None,                   # MSH-17: Country Code
    "character_set": None,                  # MSH-18: Character Set
    "principal_language_of_message": None,  # MSH-19: Principal Language of Message
    "alternate_character_set_handling_scheme": None, # MSH-20: Alternate Character Set Handling Scheme
    "message_profile_identifier": None      # MSH-21: Message Profile Identifier
}

pid_dict = {
    "set_id": None,                           # PID-1: Set ID
    "patient_id": None,                       # PID-2: Patient ID
    "patient_identifier_list": None,          # PID-3: Patient Identifier List
    "alternate_patient_id": None,             # PID-4: Alternate Patient ID
    "patient_name": None,                     # PID-5: Patient Name
    "mothers_maiden_name": None,              # PID-6: Mother's Maiden Name
    "datetime_of_birth": None,                # PID-7: Date/Time of Birth
    "administrative_sex": None,               # PID-8: Administrative Sex
    "patient_alias": None,                    # PID-9: Patient Alias
    "race": None,                             # PID-10: Race
    "patient_address": None,                  # PID-11: Patient Address
    "country_code": None,                     # PID-12: Country Code
    "phone_number_home": None,                # PID-13: Phone Number - Home
    "phone_number_business": None,            # PID-14: Phone Number - Business
    "primary_language": None,                 # PID-15: Primary Language
    "marital_status": None,                   # PID-16: Marital Status
    "religion": None,                         # PID-17: Religion
    "patient_account_number": None,           # PID-18: Patient Account Number
    "ssn_number_patient": None,               # PID-19: SSN Number - Patient
    "drivers_license_number_patient": None,   # PID-20: Driver's License Number - Patient
    "mothers_identifier": None,               # PID-21: Mother's Identifier
    "ethnic_group": None,                     # PID-22: Ethnic Group
    "birth_place": None,                      # PID-23: Birth Place
    "multiple_birth_indicator": None,         # PID-24: Multiple Birth Indicator
    "birth_order": None,                      # PID-25: Birth Order
    "citizenship": None,                      # PID-26: Citizenship
    "veterans_military_status": None,         # PID-27: Veterans Military Status
    "nationality": None,                      # PID-28: Nationality
    "patient_death_date_and_time": None,      # PID-29: Patient Death Date and Time
    "patient_death_indicator": None           # PID-30: Patient Death Indicator
}


def populateSegment(obj, segment, segment_str):    
    for index, key in enumerate(obj.keys()):
        try:
            curr_segment = f"{segment_str}_{index + 1}"
            val = getattr(segment, curr_segment).value
            if '^' in val and val != '^~\&':
                total_subcomponents = val.count('^') + 1
                temp_val = []
                for i in range (total_subcomponents):
                    i = i + 1
                    temp_curr_segment = f"{curr_segment}_{i}" 
                    temp_val.append(getattr(getattr(segment, curr_segment),temp_curr_segment).value)

                obj[key] = temp_val
            else:
                obj[key] = val

        except Exception:
            break
    return obj    

msh_dict = populateSegment(msh_dict, message.msh, "msh")
segment_keys['msh'] = msh_dict

pid_dict = populateSegment(pid_dict, message.pid, "pid")
segment_keys['pid'] = pid_dict





@app.route('/', methods=['POST', 'GET'])
def index():
    return render_template('index.html', msh_dict=msh_dict, pid_dict=pid_dict)


if __name__ == "__main__":
    app.run(debug=True)
