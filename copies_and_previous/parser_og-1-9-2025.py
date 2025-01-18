from hl7apy.parser import parse_message

# ORU^R01 prevent from reading, replace it to anything, ex (BLANK) to read.

def parseData(data):
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

    from .segment import msh_dict, pid_dict, pv1_dict, orc_dict, obr_dict, obx_dict, populateSegment
    from .data import HL7Object


    def segmentChecker(obj, segment, segment_str): # check if the current segment has
        pass

    msh_dict_obj = msh_dict()
    current_data = populateSegment(msh_dict_obj, message.msh, "msh")
    segment_data['msh'] = current_data

    pid_dict_obj = pid_dict()
    current_data = populateSegment(pid_dict_obj, message.pid, "pid")
    segment_data['pid'] = current_data

    pv1_dict_obj = pv1_dict()
    current_data = populateSegment(pv1_dict_obj, message.pv1, "pv1")
    segment_data['pv1'] = current_data

    orc_dict_obj = orc_dict()
    current_data = populateSegment(orc_dict_obj, message.orc, "orc")
    segment_data['orc'] = current_data

    obr_dict_obj = obr_dict()
    current_data = populateSegment(obr_dict_obj, message.obr, "obr")
    segment_data['obr'] = current_data

    obx_dict_obj = obx_dict()
    current_data = populateSegment(obx_dict_obj, message.obx, "obx")
    segment_data['obx'] = current_data

    return segment_data



