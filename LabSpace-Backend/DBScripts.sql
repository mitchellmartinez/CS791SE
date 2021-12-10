-- Creation of Person table
CREATE SEQUENCE person_id_seq;
CREATE TABLE Person ( 
  PersonId integer NOT NULL DEFAULT nextval('user_id_seq') primary KEY,
  FirstName varchar(200),
  LastName varchar(200),
  Netid VARCHAR(200),
  NSHEID VARCHAR(200), 
  CreatedOn TIMESTAMP,
  ModifiedOn TIMESTAMP,
  IsDeleted BIT,
  IsActive BIT
);
--ALTER TABLE Person ALTER PersonId SET DEFAULT NEXTVAL('person_id_seq');
--ALTER TABLE Person ALTER COLUMN CreatedOn TYPE TIMESTAMP;
--ALTER TABLE Person ALTER COLUMN ModifiedOn TYPE TIMESTAMP;
--ALTER TABLE Person ALTER COLUMN IsDeleted TYPE BOOLEAN;

-- Creation of Class table
CREATE SEQUENCE class_id_seq;
CREATE TABLE Class ( 
  ClassId integer NOT NULL DEFAULT nextval('class_id_seq') primary KEY,
  ClassName varchar(100),
  ClassNumber varchar(50),
  ClassCode VARCHAR(50),
  ClassMaxSize INT, 
  ClassCurrentSize INT, 
  CreatedOn TIMESTAMP,
  ModifiedOn TIMESTAMP,
  IsDeleted BIT,
  IsActive BIT
);

-- Creation of Session table
CREATE SEQUENCE session_id_seq;
CREATE TABLE Session ( 
  SessionId integer NOT NULL DEFAULT nextval('session_id_seq') PRIMARY KEY,
  ClassId integer NOT NULL references Class(ClassId),
  SessionNumber varchar(50),
  SessionCurrentSize INT, 
  StartTime TIMESTAMP,
  EndTime TIMESTAMP,
  CreatedOn TIMESTAMP,
  ModifiedOn TIMESTAMP,
  IsDeleted BIT,
  IsActive BIT
);

-- Creation of PersonSession table
CREATE SEQUENCE personsession_id_seq;
CREATE TABLE PersonSession ( 
  PersonSessionId integer NOT NULL DEFAULT nextval('personsession_id_seq') primary KEY,
  SessionId integer NOT NULL references Session(SessionId),
  PersonId integer NOT NULL references Person(PersonId),
  TokenIdentifier varchar(200),
  AttendanceFlag BIT, 
  JoinDate TIMESTAMP,
  DisconnectDate TIMESTAMP,
  CreatedOn TIMESTAMP,
  ModifiedOn TIMESTAMP,
  IsDeleted BIT,
  IsActive BIT
);


INSERT INTO Person (FirstName,LastName,Netid,NSHEID,CreatedOn,ModifiedOn,IsDeleted,IsActive) 
VALUES (pgp_sym_encrypt('Vinh', 'longsecretencryptionkey'), pgp_sym_encrypt('Le', 'longsecretencryptionkey'), 
pgp_sym_encrypt('vle', 'longsecretencryptionkey'), pgp_sym_encrypt('1005355129', 'longsecretencryptionkey'), NOW(),NOW(), '0', '1');

INSERT INTO Person (FirstName,LastName,Netid,NSHEID,CreatedOn,ModifiedOn,IsDeleted,IsActive) 
VALUES (pgp_sym_encrypt('Mitchell', 'longsecretencryptionkey'), pgp_sym_encrypt('Martinez', 'longsecretencryptionkey'), 
pgp_sym_encrypt('mitchellmartinez', 'longsecretencryptionkey'), pgp_sym_encrypt('9119119119', 'longsecretencryptionkey'), NOW(),NOW(), '0', '1');

SELECT pgp_sym_decrypt(FirstName::bytea, 'longsecretencryptionkey') AS FirstName, pgp_sym_decrypt(lastname::bytea, 'longsecretencryptionkey') AS LastName,
   pgp_sym_decrypt(netid::bytea, 'longsecretencryptionkey') AS NetId,  pgp_sym_decrypt(nsheid::bytea, 'longsecretencryptionkey')AS NSHE,
   to_char(CreatedOn, 'HH12:MI:SS') createdon, to_char(modifiedon, 'HH12:MI:SS') modifiedon, IsDeleted, IsActive FROM Person