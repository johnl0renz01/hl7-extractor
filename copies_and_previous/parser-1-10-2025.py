from .segment import msh_dict, pid_dict, pv1_dict, orc_dict, obr_dict, obx_dict, populateSegment

from . import db
from .models import MSH_Model, PID_Model, PV1_Model, ORC_Model, OBR_Model, OBX_Model


from hl7apy.parser import parse_message

# ORU^R01 prevent from reading, replace it to anything, ex (BLANK) to read.

def parseData(data, msg_id):
    if "|ORU" in data:
        data = data.replace("|ORU","|OR_")

    hl7_message = f"""{data}"""

    segments = hl7_message.split('\n')
    segments = list(filter(lambda txt: txt != "", segments))

    segment_data = {}

    for segment in segments:
        pipe_idx = segment.index('|')
        key = segment[0:pipe_idx].lower()
        segment_data[key] = ''

    
    hl7_message = "\r".join(segments)
    message = parse_message(hl7_message)


    def segmentChecker(obj, segment, segment_str, segment_model): # check if the current segment is repeated ex. pid 1, pid 2

        def exportSegment(data): # put the segment into database
            segment_content = segment_model(**data['key'],unparsed_msg_id=msg_id)
            db.session.add(segment_content)
            db.session.commit()


        if len(segment) == 0:
            segment_data[segment_str] = ''
            return
        
        segment_obj = obj


        
        if len(segment) > 1: # if the current segment are many
            data_arr = []
            for current_segment in segment:
                output = populateSegment(segment_obj, current_segment, segment_str)
                data_arr.append(output)

                data = {"key": output}
                exportSegment(data)

            segment_data[segment_str] = data_arr
        else:
            output = populateSegment(segment_obj, segment, segment_str)

            segment_data[segment_str] = output

            data = {"key": output}
            exportSegment(data)

            

    segmentChecker(msh_dict(), message.msh, "msh", MSH_Model)
    segmentChecker(pid_dict(), message.pid, "pid", PID_Model)
    segmentChecker(pv1_dict(), message.pv1, "pv1", PV1_Model)
    segmentChecker(orc_dict(), message.orc, "orc")
    segmentChecker(obr_dict(), message.obr, "obr")
    segmentChecker(obx_dict(), message.obx, "obx")

    return segment_data



