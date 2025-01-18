def msh_dict():
    return {
        "field_separator": None,                              # MSH-1: Field Separator
        "encoding_characters": None,                          # MSH-2: Encoding Characters
        "sending_application": None,                          # MSH-3: Sending Application
        "sending_facility": None,                             # MSH-4: Sending Facility
        "receiving_application": None,                        # MSH-5: Receiving Application
        "receiving_facility": None,                           # MSH-6: Receiving Facility
        "date_time_of_message": None,                         # MSH-7: Date/Time of Message
        "security": None,                                     # MSH-8: Security
        "message_type": None,                                 # MSH-9: Message Type
        "message_control_id": None,                           # MSH-10: Message Control ID
        "processing_id": None,                                # MSH-11: Processing ID
        "version_id": None,                                   # MSH-12: Version ID
        "sequence_number": None,                              # MSH-13: Sequence Number
        "continuation_pointer": None,                         # MSH-14: Continuation Pointer
        "accept_acknowledgment_type": None,                   # MSH-15: Accept Acknowledgment Type
        "application_acknowledgment_type": None,              # MSH-16: Application Acknowledgment Type
        "country_code": None,                                 # MSH-17: Country Code
        "character_set": None,                                # MSH-18: Character Set
        "principal_language_of_message": None,                # MSH-19: Principal Language of Message
        "alternate_character_set_handling_scheme": None,      # MSH-20: Alternate Character Set Handling Scheme
        "message_profile_identifier": None,                   # MSH-21: Message Profile Identifier
        "sending_responsible_organization": None,             # MSH-22: Sending Responsible Organization
        "receiving_responsible_organization": None,           # MSH-23: Receiving Responsible Organization
        "sending_network_address": None,                      # MSH-24: Sending Network Address
        "receiving_network_address": None                     # MSH-25: Receiving Network Address
    }

def pid_dict():
    return {
        "set_id": None,                                  # PID-1: Set ID - PID
        "patient_id": None,                              # PID-2: Patient ID
        "patient_identifier_list": None,                 # PID-3: Patient Identifier List
        "alternate_patient_id": None,                    # PID-4: Alternate Patient ID - PID
        "patient_name": None,                            # PID-5: Patient Name
        "mothers_maiden_name": None,                     # PID-6: Mother's Maiden Name
        "date_time_of_birth": None,                      # PID-7: Date/Time of Birth
        "administrative_sex": None,                      # PID-8: Administrative Sex
        "patient_alias": None,                           # PID-9: Patient Alias
        "race": None,                                    # PID-10: Race
        "patient_address": None,                         # PID-11: Patient Address
        "county_code": None,                             # PID-12: County Code
        "phone_number_home": None,                       # PID-13: Phone Number - Home
        "phone_number_business": None,                   # PID-14: Phone Number - Business
        "primary_language": None,                        # PID-15: Primary Language
        "marital_status": None,                          # PID-16: Marital Status
        "religion": None,                                # PID-17: Religion
        "patient_account_number": None,                  # PID-18: Patient Account Number
        "ssn_number_patient": None,                      # PID-19: SSN Number - Patient
        "drivers_license_number_patient": None,          # PID-20: Driver's License Number - Patient
        "mothers_identifier": None,                      # PID-21: Mother's Identifier
        "ethnic_group": None,                            # PID-22: Ethnic Group
        "birth_place": None,                             # PID-23: Birth Place
        "multiple_birth_indicator": None,                # PID-24: Multiple Birth Indicator
        "birth_order": None,                             # PID-25: Birth Order
        "citizenship": None,                             # PID-26: Citizenship
        "veterans_military_status": None,                # PID-27: Veterans Military Status
        "nationality": None,                             # PID-28: Nationality
        "patient_death_date_and_time": None,             # PID-29: Patient Death Date and Time
        "patient_death_indicator": None,                 # PID-30: Patient Death Indicator
        "identity_unknown_indicator": None,              # PID-31: Identity Unknown Indicator
        "identity_reliability_code": None,               # PID-32: Identity Reliability Code
        "last_update_date_time": None,                   # PID-33: Last Update Date/Time
        "last_update_facility": None,                    # PID-34: Last Update Facility
        "taxonomic_classification_code": None,           # PID-35: Taxonomic Classification Code
        "breed_code": None,                              # PID-36: Breed Code
        "strain": None,                                  # PID-37: Strain
        "production_class_code": None,                   # PID-38: Production Class Code
        "tribal_citizenship": None,                      # PID-39: Tribal Citizenship
        "patient_telecommunication_information": None    # PID-40: Patient Telecommunication Information
    }

def pv1_dict():
    return {
        "set_id": None,                                 # PV1-1: Set ID - PV1
        "patient_class": None,                          # PV1-2: Patient Class
        "assigned_patient_location": None,              # PV1-3: Assigned Patient Location
        "admission_type": None,                         # PV1-4: Admission Type
        "preadmit_number": None,                        # PV1-5: Preadmit Number
        "prior_patient_location": None,                 # PV1-6: Prior Patient Location
        "attending_doctor": None,                       # PV1-7: Attending Doctor
        "referring_doctor": None,                       # PV1-8: Referring Doctor
        "consulting_doctor": None,                      # PV1-9: Consulting Doctor
        "hospital_service": None,                       # PV1-10: Hospital Service
        "temporary_location": None,                     # PV1-11: Temporary Location
        "preadmit_test_indicator": None,                # PV1-12: Preadmit Test Indicator
        "re_admission_indicator": None,                 # PV1-13: Re-admission Indicator
        "admit_source": None,                           # PV1-14: Admit Source
        "ambulatory_status": None,                      # PV1-15: Ambulatory Status
        "vip_indicator": None,                          # PV1-16: VIP Indicator
        "admitting_doctor": None,                       # PV1-17: Admitting Doctor
        "patient_type": None,                           # PV1-18: Patient Type
        "visit_number": None,                           # PV1-19: Visit Number
        "financial_class": None,                        # PV1-20: Financial Class
        "charge_price_indicator": None,                 # PV1-21: Charge Price Indicator
        "courtesy_code": None,                          # PV1-22: Courtesy Code
        "credit_rating": None,                          # PV1-23: Credit Rating
        "contract_code": None,                          # PV1-24: Contract Code
        "contract_effective_date": None,                # PV1-25: Contract Effective Date
        "contract_amount": None,                        # PV1-26: Contract Amount
        "contract_period": None,                        # PV1-27: Contract Period
        "interest_code": None,                          # PV1-28: Interest Code
        "transfer_to_bad_debt_code": None,              # PV1-29: Transfer to Bad Debt Code
        "transfer_to_bad_debt_date": None,              # PV1-30: Transfer to Bad Debt Date
        "bad_debt_agency_code": None,                   # PV1-31: Bad Debt Agency Code
        "bad_debt_transfer_amount": None,               # PV1-32: Bad Debt Transfer Amount
        "bad_debt_recovery_amount": None,               # PV1-33: Bad Debt Recovery Amount
        "delete_account_indicator": None,               # PV1-34: Delete Account Indicator
        "delete_account_date": None,                    # PV1-35: Delete Account Date
        "discharge_disposition": None,                  # PV1-36: Discharge Disposition
        "discharged_to_location": None,                 # PV1-37: Discharged to Location
        "diet_type": None,                              # PV1-38: Diet Type
        "servicing_facility": None,                     # PV1-39: Servicing Facility
        "bed_status": None,                             # PV1-40: Bed Status
        "account_status": None,                         # PV1-41: Account Status
        "pending_location": None,                       # PV1-42: Pending Location
        "prior_temporary_location": None,               # PV1-43: Prior Temporary Location
        "admit_date_time": None,                        # PV1-44: Admit Date/Time
        "discharge_date_time": None,                    # PV1-45: Discharge Date/Time
        "current_patient_balance": None,                # PV1-46: Current Patient Balance
        "total_charges": None,                          # PV1-47: Total Charges
        "total_adjustments": None,                      # PV1-48: Total Adjustments
        "total_payments": None,                         # PV1-49: Total Payments
        "alternate_visit_id": None,                     # PV1-50: Alternate Visit ID
        "visit_indicator": None,                        # PV1-51: Visit Indicator
        "other_healthcare_provider": None,              # PV1-52: Other Healthcare Provider
        "service_episode_description": None,            # PV1-53: Service Episode Description
        "service_episode_identifier": None              # PV1-54: Service Episode Identifier
    }

def orc_dict():
    return {
        "order_control": None,                              # ORC-1: Order Control
        "placer_order_number": None,                        # ORC-2: Placer Order Number
        "filler_order_number": None,                        # ORC-3: Filler Order Number
        "placer_group_number": None,                        # ORC-4: Placer Group Number
        "order_status": None,                               # ORC-5: Order Status
        "response_flag": None,                              # ORC-6: Response Flag
        "quantity_timing": None,                            # ORC-7: Quantity/Timing
        "parent": None,                                     # ORC-8: Parent
        "date_time_of_transaction": None,                   # ORC-9: Date/Time of Transaction
        "entered_by": None,                                 # ORC-10: Entered By
        "verified_by": None,                                # ORC-11: Verified By
        "ordering_provider": None,                          # ORC-12: Ordering Provider
        "enterer's_location": None,                         # ORC-13: Enterer's Location
        "call_back_phone_number": None,                     # ORC-14: Call Back Phone Number
        "order_effective_date_time": None,                  # ORC-15: Order Effective Date/Time
        "order_control_code_reason": None,                  # ORC-16: Order Control Code Reason
        "entering_organization": None,                      # ORC-17: Entering Organization
        "entering_device": None,                            # ORC-18: Entering Device
        "action_by": None,                                  # ORC-19: Action By
        "advanced_beneficiary_notice_code": None,           # ORC-20: Advanced Beneficiary Notice Code
        "ordering_facility_name": None,                     # ORC-21: Ordering Facility Name
        "ordering_facility_address": None,                  # ORC-22: Ordering Facility Address
        "ordering_facility_phone_number": None,             # ORC-23: Ordering Facility Phone Number
        "ordering_provider_address": None,                  # ORC-24: Ordering Provider Address
        "order_status_modifier": None,                      # ORC-25: Order Status Modifier
        "advanced_beneficiary_notice_override_reason": None,# ORC-26: Advanced Beneficiary Notice Override Reason
        "fillers_expected_availability_date_time": None,    # ORC-27: Filler's Expected Availability Date/Time
        "confidentiality_code": None,                       # ORC-28: Confidentiality Code
        "order_type": None,                                 # ORC-29: Order Type
        "enterer_authorization_mode": None,                 # ORC-30: Enterer Authorization Mode
        "parent_universal_service_identifier": None,        # ORC-31: Parent Universal Service Identifier
        "advanced_beneficiary_notice_date": None,           # ORC-32: Advanced Beneficiary Notice Date
        "alternate_placer_order_number": None,              # ORC-33: Alternate Placer Order Number
        "order_workflow_profile": None                      # ORC-34: Order Workflow Profile
    }

def obr_dict():
    return {
        "set_id_obr": None,                                # OBR-1: Set Id - Obr
        "placer_order_number": None,                       # OBR-2: Placer Order Number
        "filler_order_number": None,                       # OBR-3: Filler Order Number
        "universal_service_identifier": None,              # OBR-4: Universal Service Identifier
        "priority": None,                                  # OBR-5: Priority
        "requested_date_time": None,                       # OBR-6: Requested Date/Time
        "observation_date_time": None,                     # OBR-7: Observation Date/Time
        "observation_end_date_time": None,                 # OBR-8: Observation End Date/Time
        "collection_volume": None,                         # OBR-9: Collection Volume
        "collector_identifier": None,                      # OBR-10: Collector Identifier
        "specimen_action_code": None,                      # OBR-11: Specimen Action Code
        "danger_code": None,                               # OBR-12: Danger Code
        "relevant_clinical_information": None,             # OBR-13: Relevant Clinical Information
        "specimen_received_date_time": None,               # OBR-14: Specimen Received Date/Time
        "specimen_source": None,                           # OBR-15: Specimen Source
        "ordering_provider": None,                         # OBR-16: Ordering Provider
        "order_callback_phone_number": None,               # OBR-17: Order Callback Phone Number
        "placer_field_1": None,                            # OBR-18: Placer Field 1
        "placer_field_2": None,                            # OBR-19: Placer Field 2
        "filler_field_1": None,                            # OBR-20: Filler Field 1
        "filler_field_2": None,                            # OBR-21: Filler Field 2
        "results_rpt_status_chng_date_time": None,         # OBR-22: Results Rpt/Status Chng - Date/Time
        "charge_to_practice": None,                        # OBR-23: Charge To Practice
        "diagnostic_serv_sect_id": None,                   # OBR-24: Diagnostic Serv Sect Id
        "result_status": None,                             # OBR-25: Result Status
        "parent_result": None,                             # OBR-26: Parent Result
        "quantity_timing": None,                           # OBR-27: Quantity/Timing
        "result_copies_to": None,                          # OBR-28: Result Copies To
        "parent": None,                                    # OBR-29: Parent
        "transportation_mode": None,                       # OBR-30: Transportation Mode
        "reason_for_study": None,                          # OBR-31: Reason For Study
        "principal_result_interpreter": None,              # OBR-32: Principal Result Interpreter
        "assistant_result_interpreter": None,              # OBR-33: Assistant Result Interpreter
        "technician": None,                                # OBR-34: Technician
        "transcriptionist": None,                          # OBR-35: Transcriptionist
        "scheduled_date_time": None,                       # OBR-36: Scheduled Date/Time
        "number_of_sample_containers": None,               # OBR-37: Number Of Sample Containers
        "transport_logistics_of_collected_sample": None,   # OBR-38: Transport Logistics Of Collected Sample
        "collector_comment": None,                         # OBR-39: Collector's Comment
        "transport_arrangement_responsibility": None,      # OBR-40: Transport Arrangement Responsibility
        "transport_arranged": None,                        # OBR-41: Transport Arranged
        "escort_required": None,                           # OBR-42: Escort Required
        "planned_patient_transport_comment": None,         # OBR-43: Planned Patient Transport Comment
        "procedure_code": None,                            # OBR-44: Procedure Code
        "procedure_code_modifier": None,                   # OBR-45: Procedure Code Modifier
        "placer_supplemental_service_information": None,   # OBR-46: Placer Supplemental Service Information
        "filler_supplemental_service_information": None,   # OBR-47: Filler Supplemental Service Information
        "medically_necessary_duplicate_procedure_reason": None, # OBR-48: Medically Necessary Duplicate Procedure Reason
        "result_handling": None,                           # OBR-49: Result Handling
        "parent_universal_service_identifier": None,       # OBR-50: Parent Universal Service Identifier
        "observation_group_id": None,                      # OBR-51: Observation Group Id
        "parent_observation_group_id": None,               # OBR-52: Parent Observation Group Id
        "alternate_placer_order_number": None,             # OBR-53: Alternate Placer Order Number
        "parent_order": None                                # OBR-54: Parent Order
    }

def obx_dict():
    return {
        "set_id_obx": None,                                # OBX-1: Set Id - Obx
        "value_type": None,                                # OBX-2: Value Type
        "observation_identifier": None,                    # OBX-3: Observation Identifier
        "observation_sub_id": None,                        # OBX-4: Observation Sub-id
        "observation_value": None,                         # OBX-5: Observation Value
        "units": None,                                     # OBX-6: Units
        "reference_range": None,                           # OBX-7: References Range
        "interpretation_codes": None,                      # OBX-8: Interpretation Codes
        "probability": None,                               # OBX-9: Probability
        "nature_of_abnormal_test": None,                   # OBX-10: Nature Of Abnormal Test
        "observation_result_status": None,                 # OBX-11: Observation Result Status
        "effective_date_of_reference_range": None,         # OBX-12: Effective Date Of Reference Range
        "user_defined_access_checks": None,                # OBX-13: User Defined Access Checks
        "date_time_of_the_observation": None,              # OBX-14: Date/Time Of The Observation
        "producers_id": None,                              # OBX-15: Producer's Id
        "responsible_observer": None,                      # OBX-16: Responsible Observer
        "observation_method": None,                        # OBX-17: Observation Method
        "equipment_instance_identifier": None,             # OBX-18: Equipment Instance Identifier
        "date_time_of_the_analysis": None,                 # OBX-19: Date/Time Of The Analysis
        "observation_site": None,                          # OBX-20: Observation Site
        "observation_instance_identifier": None,           # OBX-21: Observation Instance Identifier
        "mood_code": None,                                 # OBX-22: Mood Code
        "performing_organization_name": None,              # OBX-23: Performing Organization Name
        "performing_organization_address": None,           # OBX-24: Performing Organization Address
        "performing_organization_medical_director": None,  # OBX-25: Performing Organization Medical Director
        "patient_results_release_category": None,          # OBX-26: Patient Results Release Category
        "root_cause": None,                                # OBX-27: Root Cause
        "local_process_control": None                      # OBX-28: Local Process Control
    }


def populateSegment(obj, segment, segment_str):
    if len(segment) == 0:
        return ''

    for index, key in enumerate(obj.keys()): # iterate on all keys 
        try:
            curr_segment = f"{segment_str}_{index + 1}" # get the current segment to parse
            val = getattr(segment, curr_segment).value # get the value
            if '^' in val and val != '^~\&': # if current component has caret
                total_subcomponents = val.count('^') + 1
                temp_val = []
                for i in range (total_subcomponents):
                    i = i + 1
                    temp_curr_segment = f"{curr_segment}_{i}" 
                    temp_val.append(getattr(getattr(segment, curr_segment),temp_curr_segment).value) #store in array 

                obj[key] = temp_val #assign array to current segment key
            else:
                try:
                    if len(getattr(segment, curr_segment)) > 1: # if the segment is greater than 1
                        if type(getattr(segment, curr_segment)) != str: # if the segment is list
                            val = [segment_field.value for segment_field in getattr(segment, curr_segment)] # split all elements and put in array
                            val = list(filter(lambda txt: txt != "", val)) # remove empty
                except Exception:
                    pass
                
                obj[key] = val

        except Exception:
            break
    return obj    