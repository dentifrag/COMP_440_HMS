create table billing
(
    bill_id        int auto_increment
        primary key,
    patient_id     int            not null,
    amount         decimal(10, 2) not null,
    bill_date      date           not null,
    payment_status varchar(255)   null,
    constraint billing_ibfk_1
        foreign key (patient_id) references patients (patient_id)
            on delete cascade
);

