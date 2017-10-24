SET SQL_SAFE_UPDATES = 0;
DELETE FROM yzservice.organization WHERE name like 'AUTO机构%';
DELETE FROM yzservice.package WHERE name like 'AUTO套餐%';
DELETE FROM yzservice.examine_project WHERE examine_project_name like 'AUTO%';
DELETE FROM yzservice.package2organization WHERE org_name like 'AUTO机构%';
DELETE FROM yzservice.package_examines WHERE name like 'AUTO%';

DELETE FROM yzservice.package_recommend WHERE city_name = '常州市';
DELETE FROM yzservice.package_recommend WHERE city_name = '上海市';
DELETE FROM yzservice.package_recommend WHERE city_name = '无锡市';

DELETE FROM yzservice.promotion_code WHERE code = '0123456789';
DELETE FROM yzservice.promotion_code WHERE code = '0000000000';
DELETE FROM yzservice.order_promotion_code WHERE promotion_code = '0123456789';
DELETE FROM yzservice.order_promotion_code WHERE promotion_code = '0000000000';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '12912345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '12912345678');
DELETE FROM member WHERE mobile_phone = '12912345678';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '13012345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '13012345678');
DELETE FROM member WHERE mobile_phone = '13012345678';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '13112345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '13112345678');
DELETE FROM member WHERE mobile_phone = '13112345678';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '13212345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '13212345678');
DELETE FROM member WHERE mobile_phone = '13212345678';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '13312345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '13312345678');
DELETE FROM member WHERE mobile_phone = '13312345678';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '13412345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '13412345678');
DELETE FROM member WHERE mobile_phone = '13412345678';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '123456abc'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '123456abc');
DELETE FROM member WHERE mobile_phone = '123456abc';

DELETE FROM yzservice.order_promotion_code WHERE order_id IN (SELECT id FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM yzservice.member WHERE mobile_phone = '18012345678'));
DELETE FROM yzservice.commodity_order WHERE member_id = (SELECT id FROM member WHERE mobile_phone = '18012345678');
DELETE FROM member WHERE mobile_phone = '18012345678';