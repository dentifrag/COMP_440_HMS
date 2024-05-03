create table patients
(
    patient_id              int auto_increment
        primary key,
    name                    varchar(255) not null,
    date_of_birth           date         not null,
    gender                  varchar(50)  not null,
    contact_info            varchar(255) null,
    address                 varchar(255) null,
    email                   varchar(255) null,
    emergency_contact_name  varchar(255) null,
    emergency_contact_phone varchar(255) null
);

create fulltext index name
    on patients (name);

