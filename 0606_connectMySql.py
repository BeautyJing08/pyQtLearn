# 現在要用這個連線看看mysql
import mysql.connector

mydb = mysql.connector.connect(
    host= "localhost",
    user= "root",
    password = "5321",
    database = "sql_tutorial"

)

cursor = mydb.cursor()
cursor.execute("SELECT * FROM member_table")

result = cursor.fetchall()
for row in result:
    print(row)

cursor.close()
mydb.close()

#################### 這是設定member_Table

# SELECT * FROM sql_tutorial.member_table;
# DESCRIBE `member_table`;
# # CHANGE [`mem_id`] `mem_id` `mem_id`
# #UPDATE [`mem_id`] SET [`mem_id`] =  AUTO_INCREMENT
# ALTER TABLE `member_table` MODIFY `mem_id` INT AUTO_INCREMENT;
#
# SELECT * FROM `member_table`;
#
# INSERT INTO `member_table` (`mem_name`,`mem_isMale`, `mem_phone`) VALUES ("小白","女","098765432");
# UPDATE `member_table` SET `mem_isMale` = "男" where mem_id = 2;
#
# UPDATE `member_table` SET `mem_phone` = "0987654321" where mem_id = 2;

##################### 這是設定booking_table

# SELECT * FROM sql_tutorial.booking_table;
# INSERT INTO `booking_table` (`TIME_start`,`TIME_end`,`Net_height`, `place_name`) VALUES ("2023-06-06 08:00","2023-06-06 12:00", "243男網", "場地A");
# INSERT INTO `booking_table` (`TIME_start`,`TIME_end`,`Net_height`, `place_name`) VALUES ("2023-06-06 13:00","2023-06-06 17:00", "224女網", "場地A");
# ALTER TABLE `booking_table` RENAME COLUMN `TIME_emd` TO `TIME_end`;
#
# UPDATE `booking_table` SET `Net_height` = "243男網" where `booking_num` = 1;


################## 這是新的資料表 booking_table

# SELECT * FROM sql_tutorial.booking_table;
# DESCRIBE TABLE `booking_table`;
# INSERT INTO `booking_table` (`TIME_start`,`TIME_end`,`Net_height`, `place_name`) VALUES ("2023-06-06 08:00","2023-06-06 12:00", "243男網", "場地A");
# INSERT INTO `booking_table` (`TIME_start`,`TIME_end`,`Net_height`, `place_name`) VALUES ("2023-06-06 13:00","2023-06-06 17:00", "224女網", "場地A");
# ALTER TABLE `booking_table` RENAME COLUMN `TIME_emd` TO `TIME_end`;
#
# UPDATE `booking_table` SET `Net_height` = "243男網" where `booking_num` = 1;
#
# ALTER TABLE `booking_table` ADD COLUMN `booking_list` VARCHAR(30);
# ALTER TABLE `booking_table` ADD COLUMN `allOrMix` VARCHAR(30);