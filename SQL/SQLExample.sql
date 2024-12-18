DROP TABLE IF EXISTS StudentModuleLink
DROP TABLE IF EXISTS Module
DROP TABLE IF EXISTS Student
DROP TABLE IF EXISTS PAT

CREATE TABLE PAT(
	PATCode int NOT NULL,
	PATName varchar(25),
	PATRoom varchar(5),
	CONSTRAINT PKPat PRIMARY KEY (PATCode)
)

CREATE TABLE Student(
	EnrolNo int NOT NULL PRIMARY KEY,
	Surname varchar(25),
	Forename varchar(25),
	Gender char,
	Dob date,
	PATCode int,
	CONSTRAINT FKPatCODE FOREIGN KEY (PATCode) REFERENCES PAT(PATCode)
)

CREATE TABLE Module(
	ModuleNo int NOT NULL PRIMARY KEY,
	ModuleTitle varchar(25)
)

CREATE TABLE StudentModuleLink(
	EnrolNo int NOT NULL,
	ModuleNo int NOT NULL,
	ModuleMark int,
	ModuleResult varchar(3),
	CONSTRAINT PK_SML PRIMARY KEY (EnrolNo,ModuleNo),
	CONSTRAINT FK_EnrolNo FOREIGN KEY (EnrolNo) REFERENCES Student(EnrolNo),
	CONSTRAINT FK_ModuleNo FOREIGN KEY (ModuleNo) REFERENCES Module(ModuleNo)
)

INSERT INTO PAT (PATCode, PATName)
VALUES (1, 'Richard'),
(2, 'Mike'),
(3, 'Andrew')

INSERT INTO Student (EnrolNo, Surname, Forename, Gender, Dob, PATCode )
VALUES(1,'Fisher','Jack','M','10-02-2000', 1),
(2,'Smith','John','M','11-02-2005', 1),
(3,'Jones','Samantha','F','5-06-2002', 2)

INSERT INTO Module
VALUES(4222,'Databases'),
(4225,'Programming'),
(4126, 'Web')

INSERT INTO StudentModuleLink(EnrolNo,ModuleNo,ModuleMark,ModuleResult)
VALUES (1,4222,56,'PAS'),
(1,4225,65,'PAS'),
(1,4126,35,'FAI')

