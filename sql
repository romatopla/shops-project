-- public.sales определение

-- Drop table

-- DROP TABLE public.sales;

CREATE TABLE public.sales (
	doc_id varchar NULL,
	shop_num int2 NULL,
	cash_num int2 NULL,
	item varchar NULL,
	category varchar NULL,
	amount int4 NULL,
	price numeric NULL,
	discount numeric NULL
);