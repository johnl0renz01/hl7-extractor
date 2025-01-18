from .segment import msh_dict, pid_dict, pv1_dict, orc_dict, obr_dict, obx_dict, populateSegment

from .. import db
from ..models import MSH_Model, PID_Model, PV1_Model, ORC_Model, OBR_Model, OBX_Model


from hl7apy.parser import parse_message
from .convertor import convertMessage


def parseData(data, msg_id):
    validate = convertMessage(data)
    data, msh_message_type = validate[0], validate[1]

    hl7_message = f"""{data}"""

    segments = hl7_message.split('\n')
    segments = list(filter(lambda txt: txt != "", segments))

    hl7_message = "\r".join(segments)
    message = parse_message(hl7_message)


    def segmentChecker(obj, segment, segment_str, segment_model): # check if the current segment is repeated ex. pid 1, pid 2
        if len(segment) <= 0:
            return

        def exportSegment(data): # put the segment into database
            segment_content = segment_model(**data['key'],unparsed_msg_id=msg_id)
            db.session.add(segment_content)
            db.session.commit()

        segment_obj = obj

        if len(segment) > 1: # if the current segment are many
            for current_segment in segment:
                output = populateSegment(segment_obj, current_segment, segment_str, msh_message_type)
                data = {"key": output}
                exportSegment(data)
        else:
            output = populateSegment(segment_obj, segment, segment_str, msh_message_type)
            data = {"key": output}
            exportSegment(data)


    segmentChecker(msh_dict(), message.msh, "msh", MSH_Model)
    segmentChecker(pid_dict(), message.pid, "pid", PID_Model)
    segmentChecker(pv1_dict(), message.pv1, "pv1", PV1_Model)
    segmentChecker(orc_dict(), message.orc, "orc", ORC_Model)
    segmentChecker(obr_dict(), message.obr, "obr", OBR_Model)
    segmentChecker(obx_dict(), message.obx, "obx", OBX_Model)



