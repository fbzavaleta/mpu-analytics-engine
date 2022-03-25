CREATE TABLE giroscope_mpu_on (
                id  INT NOT NULL AUTO_INCREMENT,
                x FLOAT NOT NULL,
                y FLOAT NOT NULL,
                z FLOAT NOT NULL,
                date_mpu  VARCHAR(250) NOT NULL,       
                time_mpu  VARCHAR(250) NOT NULL,  
                time_float FLOAT NOT NULL,                                        
                PRIMARY KEY (id)
);

CREATE TABLE giroscope_mpu_off (
                id  INT NOT NULL AUTO_INCREMENT,
                x FLOAT NOT NULL,
                y FLOAT NOT NULL,
                z FLOAT NOT NULL,
                date_mpu  VARCHAR(250) NOT NULL,       
                time_mpu  VARCHAR(250) NOT NULL,  
                time_float FLOAT NOT NULL,                                        
                PRIMARY KEY (id)
);

CREATE TABLE giroscope_mpu_live (
                id  INT NOT NULL AUTO_INCREMENT,
                x FLOAT NOT NULL,
                y FLOAT NOT NULL,
                z FLOAT NOT NULL,
                date_mpu  VARCHAR(250) NOT NULL,       
                time_mpu  VARCHAR(250) NOT NULL,  
                time_float FLOAT NOT NULL,                                        
                PRIMARY KEY (id)
);