create table appointments
(
    appointment_id   int auto_increment
        primary key,
    patient_id       int      not null,
    doctor_id        int      not null,
    appointment_date datetime not null,
    purpose          text     null,
    constraint appointments_ibfk_1
        foreign key (patient_id) references patients (patient_id)
            on delete cascade,
    constraint appointments_ibfk_2
        foreign key (doctor_id) references doctors (doctor_id)
);

create index doctor_id
    on appointments (doctor_id);

