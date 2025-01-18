from . import db
from sqlalchemy.sql import func
from sqlalchemy import Column, Integer, String, DateTime, Text, TIMESTAMP, ForeignKey, Boolean, Float
from sqlalchemy.dialects.postgresql import ARRAY


class Unparsed(db.Model):
    __tablename__ = 'unparsed_hl7'

    id = Column(Integer, primary_key=True)
    content = Column(Text, nullable=False)
    msh_model = db.relationship('MSH_Model', backref='unparsed', lazy=True, cascade="all, delete-orphan")
    pid_model = db.relationship('PID_Model', backref='unparsed', lazy=True, cascade="all, delete-orphan")
    pv1_model = db.relationship('PV1_Model', backref='unparsed', lazy=True, cascade="all, delete-orphan")
    orc_model = db.relationship('ORC_Model', backref='unparsed', lazy=True, cascade="all, delete-orphan")
    obr_model = db.relationship('OBR_Model', backref='unparsed', lazy=True, cascade="all, delete-orphan")
    obx_model = db.relationship('OBX_Model', backref='unparsed', lazy=True, cascade="all, delete-orphan")
    date_created = Column(DateTime(timezone=True),server_default=func.now())

    def __repr__(self):
        return '<Unparsed Data %r>' % self.id
    
class MSH_Model(db.Model):
    __tablename__ = 'msh'

    id = Column(Integer, primary_key=True)
    unparsed_msg_id = Column(Integer, ForeignKey('unparsed_hl7.id'))
    field_separator = Column(String(1), nullable=True)  # MSH-1
    encoding_characters = Column(String(5), nullable=True)  # MSH-2
    sending_application = Column(String, nullable=True)  # MSH-3
    sending_facility = Column(String, nullable=True)  # MSH-4
    receiving_application = Column(String, nullable=True)  # MSH-5
    receiving_facility = Column(String, nullable=True)  # MSH-6
    date_time_of_message = Column(TIMESTAMP(timezone=True), nullable=True)  # MSH-7 
    security = Column(String, nullable=True)  # MSH-8
    message_type = Column(String, nullable=True)  # MSH-9
    message_control_id = Column(String(199), nullable=True)  # MSH-10
    processing_id = Column(String, nullable=True)  # MSH-11
    version_id = Column(String, nullable=True)  # MSH-12
    sequence_number = Column(Integer, nullable=True)  # MSH-13
    continuation_pointer = Column(String, nullable=True)  # MSH-14
    accept_acknowledgment_type = Column(String(2), nullable=True)  # MSH-15
    application_acknowledgment_type = Column(String(2), nullable=True)  # MSH-16
    country_code = Column(String(3), nullable=True)  # MSH-17
    character_set = Column(ARRAY(String), nullable=True)  # MSH-18
    principal_language_of_message = Column(String, nullable=True)  # MSH-19
    alternate_character_set_handling_scheme = Column(String(13), nullable=True)  # MSH-20
    message_profile_identifier = Column(ARRAY(String), nullable=True)  # MSH-21
    sending_responsible_organization = Column(String, nullable=True)  # MSH-22
    receiving_responsible_organization = Column(String, nullable=True)  # MSH-23
    sending_network_address = Column(String, nullable=True)  # MSH-24
    receiving_network_address = Column(String, nullable=True)  # MSH-25
    date_created = Column(DateTime(timezone=True), server_default=func.now())  # Auto-created timestamp


    def __repr__(self):
        return f"<MSH Message ID: {self.message_control_id}>"
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'unparsed_msg_id': self.unparsed_msg_id,
            'field_separator': self.field_separator,
            'encoding_characters': self.encoding_characters,
            'sending_application': self.sending_application,
            'sending_facility': self.sending_facility,
            'receiving_application': self.receiving_application,
            'receiving_facility': self.receiving_facility,
            'date_time_of_message': self.date_time_of_message.isoformat() if self.date_time_of_message else None,
            'security': self.security,
            'message_type': self.message_type,
            'message_control_id': self.message_control_id,
            'processing_id': self.processing_id,
            'version_id': self.version_id,
            'sequence_number': self.sequence_number,
            'continuation_pointer': self.continuation_pointer,
            'accept_acknowledgment_type': self.accept_acknowledgment_type,
            'application_acknowledgment_type': self.application_acknowledgment_type,
            'country_code': self.country_code,
            'character_set': self.character_set,
            'principal_language_of_message': self.principal_language_of_message,
            'alternate_character_set_handling_scheme': self.alternate_character_set_handling_scheme,
            'message_profile_identifier': self.message_profile_identifier,
            'sending_responsible_organization': self.sending_responsible_organization,
            'receiving_responsible_organization': self.receiving_responsible_organization,
            'sending_network_address': self.sending_network_address,
            'receiving_network_address': self.receiving_network_address,
            'date_created': self.date_created.isoformat() if self.date_created else None,
        }


class PID_Model(db.Model):
    __tablename__ = 'pid'

    id = Column(Integer, primary_key=True)
    unparsed_msg_id = Column(Integer, ForeignKey('unparsed_hl7.id'))
    set_id = Column(Integer, nullable=True)  # PID-1
    patient_id = Column(String, nullable=True)  # PID-2
    patient_identifier_list = Column(ARRAY(String), nullable=True)  # PID-3
    alternate_patient_id = Column(String, nullable=True)  # PID-4
    patient_name = Column(ARRAY(String), nullable=True)  # PID-5
    mothers_maiden_name = Column(ARRAY(String), nullable=True)  # PID-6
    date_time_of_birth = Column(DateTime, nullable=True)  # PID-7
    administrative_sex = Column(String, nullable=True)  # PID-8
    patient_alias = Column(String, nullable=True)  # PID-9
    race = Column(ARRAY(String), nullable=True)  # PID-10
    patient_address = Column(ARRAY(String), nullable=True)  # PID-11
    county_code = Column(String, nullable=True)  # PID-12
    phone_number_home = Column(ARRAY(String), nullable=True)  # PID-13
    phone_number_business = Column(ARRAY(String), nullable=True)  # PID-14
    primary_language = Column(String, nullable=True)  # PID-15
    marital_status = Column(String, nullable=True)  # PID-16
    religion = Column(String, nullable=True)  # PID-17
    patient_account_number = Column(String, nullable=True)  # PID-18
    ssn_number_patient = Column(String, nullable=True)  # PID-19
    drivers_license_number_patient = Column(String, nullable=True)  # PID-20
    mothers_identifier = Column(ARRAY(String), nullable=True)  # PID-21
    ethnic_group = Column(ARRAY(String), nullable=True)  # PID-22
    birth_place = Column(String, nullable=True)  # PID-23
    multiple_birth_indicator = Column(String, nullable=True)  # PID-24 # Boolean
    birth_order = Column(Integer, nullable=True)  # PID-25
    citizenship = Column(ARRAY(String), nullable=True)  # PID-26
    veterans_military_status = Column(String, nullable=True)  # PID-27
    nationality = Column(String, nullable=True)  # PID-28
    patient_death_date_and_time = Column(DateTime, nullable=True)  # PID-29
    patient_death_indicator = Column(String, nullable=True)  # PID-30 # Boolean
    identity_unknown_indicator = Column(String, nullable=True)  # PID-31
    identity_reliability_code = Column(ARRAY(String), nullable=True)  # PID-32 # Boolean
    last_update_date_time = Column(DateTime, nullable=True)  # PID-33
    last_update_facility = Column(String, nullable=True)  # PID-34
    taxonomic_classification_code = Column(String, nullable=True)  # PID-35
    breed_code = Column(String, nullable=True)  # PID-36
    strain = Column(String, nullable=True)  # PID-37
    production_class_code = Column(ARRAY(String), nullable=True)  # PID-38
    tribal_citizenship = Column(ARRAY(String), nullable=True)  # PID-39
    patient_telecommunication_information = Column(ARRAY(String), nullable=True)  # PID-40
    date_created = Column(DateTime(timezone=True), server_default=func.now())  # Auto-created timestamp

    def __repr__(self):
        return f"<PID Patient ID: {self.patient_id}>"
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}

class PV1_Model(db.Model):
    __tablename__ = 'pv1'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unparsed_msg_id = Column(Integer, ForeignKey('unparsed_hl7.id'))
    set_id = Column(Integer, nullable=True)  # PV1-1
    patient_class = Column(String, nullable=True)  # PV1-2
    assigned_patient_location = Column(Text, nullable=True)  # PV1-3
    admission_type = Column(String, nullable=True)  # PV1-4
    preadmit_number = Column(String, nullable=True)  # PV1-5
    prior_patient_location = Column(Text, nullable=True)  # PV1-6
    attending_doctor = Column(ARRAY(Text), nullable=True)  # PV1-7
    referring_doctor = Column(ARRAY(Text), nullable=True)  # PV1-8
    consulting_doctor = Column(ARRAY(Text), nullable=True)  # PV1-9
    hospital_service = Column(String, nullable=True)  # PV1-10
    temporary_location = Column(Text, nullable=True)  # PV1-11
    preadmit_test_indicator = Column(String, nullable=True)  # PV1-12
    re_admission_indicator = Column(String, nullable=True)  # PV1-13
    admit_source = Column(String, nullable=True)  # PV1-14
    ambulatory_status = Column(ARRAY(Text), nullable=True)  # PV1-15
    vip_indicator = Column(String, nullable=True)  # PV1-16
    admitting_doctor = Column(ARRAY(Text), nullable=True)  # PV1-17
    patient_type = Column(String, nullable=True)  # PV1-18
    visit_number = Column(String, nullable=True)  # PV1-19
    financial_class = Column(ARRAY(Text), nullable=True)  # PV1-20
    charge_price_indicator = Column(String, nullable=True)  # PV1-21
    courtesy_code = Column(String, nullable=True)  # PV1-22
    credit_rating = Column(String, nullable=True)  # PV1-23
    contract_code = Column(ARRAY(Text), nullable=True)  # PV1-24
    contract_effective_date = Column(DateTime, nullable=True)  # PV1-25
    contract_amount = Column(Float, nullable=True)  # PV1-26
    contract_period = Column(Float, nullable=True)  # PV1-27
    interest_code = Column(String, nullable=True)  # PV1-28
    transfer_to_bad_debt_code = Column(String, nullable=True)  # PV1-29
    transfer_to_bad_debt_date = Column(DateTime, nullable=True)  # PV1-30
    bad_debt_agency_code = Column(String, nullable=True)  # PV1-31
    bad_debt_transfer_amount = Column(Float, nullable=True)  # PV1-32
    bad_debt_recovery_amount = Column(Float, nullable=True)  # PV1-33
    delete_account_indicator = Column(String, nullable=True)  # PV1-34
    delete_account_date = Column(DateTime, nullable=True)  # PV1-35
    discharge_disposition = Column(String, nullable=True)  # PV1-36
    discharged_to_location = Column(Text, nullable=True)  # PV1-37
    diet_type = Column(String, nullable=True)  # PV1-38
    servicing_facility = Column(String, nullable=True)  # PV1-39
    bed_status = Column(String, nullable=True)  # PV1-40
    account_status = Column(String, nullable=True)  # PV1-41
    pending_location = Column(Text, nullable=True)  # PV1-42
    prior_temporary_location = Column(Text, nullable=True)  # PV1-43
    admit_date_time = Column(DateTime, nullable=True)  # PV1-44
    discharge_date_time = Column(DateTime, nullable=True)  # PV1-45
    current_patient_balance = Column(Float, nullable=True)  # PV1-46
    total_charges = Column(Float, nullable=True)  # PV1-47
    total_adjustments = Column(Float, nullable=True)  # PV1-48
    total_payments = Column(Float, nullable=True)  # PV1-49
    alternate_visit_id = Column(String, nullable=True)  # PV1-50
    visit_indicator = Column(String, nullable=True)  # PV1-51
    other_healthcare_provider = Column(String, nullable=True)  # PV1-52
    service_episode_description = Column(Text, nullable=True)  # PV1-53
    service_episode_identifier = Column(String, nullable=True)  # PV1-54

    def __repr__(self):
        return f"<PV1(id={self.id}, set_id={self.set_id}, patient_class={self.patient_class})>"
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
class ORC_Model(db.Model):
    __tablename__ = 'orc'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unparsed_msg_id = Column(Integer, ForeignKey('unparsed_hl7.id'))
    order_control = Column(String, nullable=True)  # ORC-1
    placer_order_number = Column(Text, nullable=True)  # ORC-2
    filler_order_number = Column(Text, nullable=True)  # ORC-3
    placer_group_number = Column(Text, nullable=True)  # ORC-4
    order_status = Column(String, nullable=True)  # ORC-5
    response_flag = Column(String, nullable=True)  # ORC-6
    quantity_timing = Column(ARRAY(Text), nullable=True)  # ORC-7
    parent = Column(Text, nullable=True)  # ORC-8
    date_time_of_transaction = Column(DateTime, nullable=True)  # ORC-9
    entered_by = Column(ARRAY(Text), nullable=True)  # ORC-10
    verified_by = Column(ARRAY(Text), nullable=True)  # ORC-11
    ordering_provider = Column(ARRAY(Text), nullable=True)  # ORC-12
    enterers_location = Column(Text, nullable=True)  # ORC-13
    call_back_phone_number = Column(ARRAY(Text), nullable=True)  # ORC-14
    order_effective_date_time = Column(DateTime, nullable=True)  # ORC-15
    order_control_code_reason = Column(Text, nullable=True)  # ORC-16
    entering_organization = Column(Text, nullable=True)  # ORC-17
    entering_device = Column(Text, nullable=True)  # ORC-18
    action_by = Column(ARRAY(Text), nullable=True)  # ORC-19
    advanced_beneficiary_notice_code = Column(Text, nullable=True)  # ORC-20
    ordering_facility_name = Column(ARRAY(Text), nullable=True)  # ORC-21
    ordering_facility_address = Column(ARRAY(Text), nullable=True)  # ORC-22
    ordering_facility_phone_number = Column(ARRAY(Text), nullable=True)  # ORC-23
    ordering_provider_address = Column(ARRAY(Text), nullable=True)  # ORC-24
    order_status_modifier = Column(Text, nullable=True)  # ORC-25
    advanced_beneficiary_notice_override_reason = Column(Text, nullable=True)  # ORC-26
    fillers_expected_availability_date_time = Column(DateTime, nullable=True)  # ORC-27
    confidentiality_code = Column(Text, nullable=True)  # ORC-28
    order_type = Column(Text, nullable=True)  # ORC-29
    enterer_authorization_mode = Column(Text, nullable=True)  # ORC-30
    parent_universal_service_identifier = Column(Text, nullable=True)  # ORC-31
    advanced_beneficiary_notice_date = Column(DateTime, nullable=True)  # ORC-32
    alternate_placer_order_number = Column(ARRAY(Text), nullable=True)  # ORC-33
    order_workflow_profile = Column(ARRAY(Text), nullable=True)  # ORC-34

    def __repr__(self):
        return f"<ORC(id={self.id}, order_control={self.order_control})>"
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
class OBR_Model(db.Model):
    __tablename__ = 'obr'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unparsed_msg_id = Column(Integer, ForeignKey('unparsed_hl7.id'))
    set_id_obr = Column(Integer, nullable=True)  # OBR-1
    placer_order_number = Column(Text, nullable=True)  # OBR-2
    filler_order_number = Column(Text, nullable=True)  # OBR-3
    universal_service_identifier = Column(Text, nullable=True)  # OBR-4
    priority = Column(String, nullable=True)  # OBR-5
    requested_date_time = Column(String, nullable=True)  # OBR-6
    observation_date_time = Column(DateTime, nullable=True)  # OBR-7
    observation_end_date_time = Column(DateTime, nullable=True)  # OBR-8
    collection_volume = Column(String, nullable=True)  # OBR-9
    collector_identifier = Column(ARRAY(Text), nullable=True)  # OBR-10
    specimen_action_code = Column(String, nullable=True)  # OBR-11
    danger_code = Column(Text, nullable=True)  # OBR-12
    relevant_clinical_information = Column(ARRAY(Text), nullable=True)  # OBR-13
    specimen_received_date_time = Column(String, nullable=True)  # OBR-14
    specimen_source = Column(String, nullable=True)  # OBR-15
    ordering_provider = Column(ARRAY(Text), nullable=True)  # OBR-16
    order_callback_phone_number = Column(ARRAY(Text), nullable=True)  # OBR-17
    placer_field_1 = Column(String, nullable=True)  # OBR-18
    placer_field_2 = Column(String, nullable=True)  # OBR-19
    filler_field_1 = Column(String, nullable=True)  # OBR-20
    filler_field_2 = Column(String, nullable=True)  # OBR-21
    results_rpt_status_chng_date_time = Column(DateTime, nullable=True)  # OBR-22
    charge_to_practice = Column(Text, nullable=True)  # OBR-23
    diagnostic_serv_sect_id = Column(String, nullable=True)  # OBR-24
    result_status = Column(String, nullable=True)  # OBR-25
    parent_result = Column(Text, nullable=True)  # OBR-26
    quantity_timing = Column(ARRAY(Text), nullable=True)  # OBR-27
    result_copies_to = Column(ARRAY(Text), nullable=True)  # OBR-28
    parent = Column(Text, nullable=True)  # OBR-29
    transportation_mode = Column(String, nullable=True)  # OBR-30
    reason_for_study = Column(ARRAY(Text), nullable=True)  # OBR-31
    principal_result_interpreter = Column(Text, nullable=True)  # OBR-32
    assistant_result_interpreter = Column(ARRAY(Text), nullable=True)  # OBR-33
    technician = Column(ARRAY(Text), nullable=True)  # OBR-34
    transcriptionist = Column(ARRAY(Text), nullable=True)  # OBR-35
    scheduled_date_time = Column(DateTime, nullable=True)  # OBR-36
    number_of_sample_containers = Column(Integer, nullable=True)  # OBR-37
    transport_logistics_of_collected_sample = Column(ARRAY(Text), nullable=True)  # OBR-38
    collector_comment = Column(ARRAY(Text), nullable=True)  # OBR-39
    transport_arrangement_responsibility = Column(Text, nullable=True)  # OBR-40
    transport_arranged = Column(String, nullable=True)  # OBR-41
    escort_required = Column(String, nullable=True)  # OBR-42
    planned_patient_transport_comment = Column(ARRAY(Text), nullable=True)  # OBR-43
    procedure_code = Column(Text, nullable=True)  # OBR-44
    procedure_code_modifier = Column(ARRAY(Text), nullable=True)  # OBR-45
    placer_supplemental_service_information = Column(ARRAY(Text), nullable=True)  # OBR-46
    filler_supplemental_service_information = Column(ARRAY(Text), nullable=True)  # OBR-47
    medically_necessary_duplicate_procedure_reason = Column(Text, nullable=True)  # OBR-48
    result_handling = Column(Text, nullable=True)  # OBR-49
    parent_universal_service_identifier = Column(Text, nullable=True)  # OBR-50
    observation_group_id = Column(Text, nullable=True)  # OBR-51
    parent_observation_group_id = Column(Text, nullable=True)  # OBR-52
    alternate_placer_order_number = Column(ARRAY(Text), nullable=True)  # OBR-53
    parent_order = Column(Text, nullable=True)  # OBR-54

    def __repr__(self):
        return f"<OBR(id={self.id}, set_id_obr={self.set_id_obr})>"
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
class OBX_Model(db.Model):
    __tablename__ = 'obx'

    id = Column(Integer, primary_key=True, autoincrement=True)
    unparsed_msg_id = Column(Integer, ForeignKey('unparsed_hl7.id'))
    set_id_obx = Column(Integer, nullable=True)  # OBX-1: Set Id - Obx
    value_type = Column(String, nullable=True)  # OBX-2: Value Type
    observation_identifier = Column(Text, nullable=True)  # OBX-3: Observation Identifier
    observation_sub_id = Column(String, nullable=True)  # OBX-4: Observation Sub-id
    observation_value = Column(ARRAY(Text), nullable=True)  # OBX-5: Observation Value
    units = Column(Text, nullable=True)  # OBX-6: Units
    reference_range = Column(String, nullable=True)  # OBX-7: References Range
    interpretation_codes = Column(ARRAY(Text), nullable=True)  # OBX-8: Interpretation Codes
    probability = Column(Float, nullable=True)  # OBX-9: Probability
    nature_of_abnormal_test = Column(ARRAY(Text), nullable=True)  # OBX-10: Nature Of Abnormal Test
    observation_result_status = Column(String, nullable=True)  # OBX-11: Observation Result Status
    effective_date_of_reference_range = Column(DateTime, nullable=True)  # OBX-12: Effective Date Of Reference Range
    user_defined_access_checks = Column(String, nullable=True)  # OBX-13: User Defined Access Checks
    date_time_of_the_observation = Column(DateTime, nullable=True)  # OBX-14: Date/Time Of The Observation
    producers_id = Column(Text, nullable=True)  # OBX-15: Producer's Id
    responsible_observer = Column(ARRAY(Text), nullable=True)  # OBX-16: Responsible Observer
    observation_method = Column(ARRAY(Text), nullable=True)  # OBX-17: Observation Method
    equipment_instance_identifier = Column(ARRAY(Text), nullable=True)  # OBX-18: Equipment Instance Identifier
    date_time_of_the_analysis = Column(DateTime, nullable=True)  # OBX-19: Date/Time Of The Analysis
    observation_site = Column(ARRAY(Text), nullable=True)  # OBX-20: Observation Site
    observation_instance_identifier = Column(Text, nullable=True)  # OBX-21: Observation Instance Identifier
    mood_code = Column(Text, nullable=True)  # OBX-22: Mood Code
    performing_organization_name = Column(Text, nullable=True)  # OBX-23: Performing Organization Name
    performing_organization_address = Column(Text, nullable=True)  # OBX-24: Performing Organization Address
    performing_organization_medical_director = Column(Text, nullable=True)  # OBX-25: Performing Organization Medical Director
    patient_results_release_category = Column(String, nullable=True)  # OBX-26: Patient Results Release Category
    root_cause = Column(Text, nullable=True)  # OBX-27: Root Cause
    local_process_control = Column(ARRAY(Text), nullable=True)  # OBX-28: Local Process Control

    def __repr__(self):
        return f"<OBX(id={self.id}, set_id_obx={self.set_id_obx})>"
    
    def as_dict(self):
        return {column.name: getattr(self, column.name) for column in self.__table__.columns}
    
    def serialize(self):
        """Return object data in easily serializable format"""
        return {
            'id': self.id,
            'unparsed_msg_id': self.unparsed_msg_id,
            'set_id_obx': self.set_id_obx,
            'value_type': self.value_type,
            'observation_identifier': self.observation_identifier,
            'observation_sub_id': self.observation_sub_id,
            'observation_value': self.observation_value,
            'units': self.units,
            'reference_range': self.reference_range,
            'interpretation_codes': self.interpretation_codes,
            'probability': self.probability,
            'nature_of_abnormal_test': self.nature_of_abnormal_test,
            'observation_result_status': self.observation_result_status,
            'effective_date_of_reference_range': self.effective_date_of_reference_range.isoformat() if self.effective_date_of_reference_range else None,
            'user_defined_access_checks': self.user_defined_access_checks,
            'date_time_of_the_observation': self.date_time_of_the_observation.isoformat() if self.date_time_of_the_observation else None,
            'producers_id': self.producers_id,
            'responsible_observer': self.responsible_observer,
            'observation_method': self.observation_method,
            'equipment_instance_identifier': self.equipment_instance_identifier,
            'date_time_of_the_analysis': self.date_time_of_the_analysis.isoformat() if self.date_time_of_the_analysis else None,
            'observation_site': self.observation_site,
            'observation_instance_identifier': self.observation_instance_identifier,
            'mood_code': self.mood_code,
            'performing_organization_name': self.performing_organization_name,
            'performing_organization_address': self.performing_organization_address,
            'performing_organization_medical_director': self.performing_organization_medical_director,
            'patient_results_release_category': self.patient_results_release_category,
            'root_cause': self.root_cause,
            'local_process_control': self.local_process_control,
        }