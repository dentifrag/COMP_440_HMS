create table doctors
(
    doctor_id    int auto_increment
        primary key,
    name         varchar(255) not null,
    specialty    varchar(255) not null,
    contact_info varchar(255) null,
    room_number  varchar(50)  null,
    availability varchar(255) null
);

create fulltext index name
    on doctors (name);

