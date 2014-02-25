CREATE SCHEMA "教育部臺灣閩南語常用詞辭典";

SET search_path = "教育部臺灣閩南語常用詞辭典", pg_catalog;

--
-- Name: 例句; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "例句" (
    "流水號" integer,
    "主編號" integer,
    "釋義編號" integer,
    "例句順序" integer,
    "例句" character varying,
    "標音" character varying,
    "例句翻譯" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."例句" OWNER TO "臺灣言語工具";

--
-- Name: 又音; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "又音" (
    "流水號" integer,
    "主編號" integer,
    "屬性" character varying,
    "又音" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."又音" OWNER TO "臺灣言語工具";

--
-- Name: 反義詞對應; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "反義詞對應" (
    "流水號" integer,
    "主編號" integer,
    "反義詞" integer,
    "另注音讀" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."反義詞對應" OWNER TO "臺灣言語工具";

--
-- Name: 屬性對照; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "屬性對照" (
    "屬性" integer,
    "屬性內容" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."屬性對照" OWNER TO "臺灣言語工具";

--
-- Name: 詞彙方言差; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "詞彙方言差" (
    "編號" integer NOT NULL,
    "詞彙編號" character varying,
    "華語" character varying,
    "鹿港" character varying,
    "三峽" character varying,
    "臺北" character varying,
    "宜蘭" character varying,
    "臺南" character varying,
    "高雄" character varying,
    "金門" character varying,
    "馬公" character varying,
    "新竹" character varying,
    "臺中" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."詞彙方言差" OWNER TO "臺灣言語工具";

--
-- Name: 詞性對照; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "詞性對照" (
    "詞性" integer,
    "詞性內容" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."詞性對照" OWNER TO "臺灣言語工具";

--
-- Name: 詞目總檔; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "詞目總檔" (
    "主編號" integer NOT NULL,
    "屬性" integer,
    "詞目" character varying,
    "音讀" character varying,
    "文白俗替" character varying,
    "部首" character varying,
    "部首序" character varying,
    "方言差" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."詞目總檔" OWNER TO "臺灣言語工具";

--
-- Name: 語音方言差; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "語音方言差" (
    "編號" integer,
    "字號" character varying,
    "字目" character varying,
    "鹿港" character varying,
    "三峽" character varying,
    "臺北" character varying,
    "宜蘭" character varying,
    "臺南" character varying,
    "高雄" character varying,
    "金門" character varying,
    "馬公" character varying,
    "新竹" character varying,
    "臺中" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."語音方言差" OWNER TO "臺灣言語工具";

--
-- Name: 近義詞對應; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "近義詞對應" (
    "流水號" integer,
    "主編號" integer,
    "近義詞對應" integer,
    "另注音讀" character varying
);



--
-- Name: 造字集; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "造字集" (
    "統一碼" character varying(5),
    "組字式" character varying(200)
);


--
-- Name: 釋義; Type: TABLE; Schema: 教育部臺灣閩南語常用詞辭典; Owner: 臺灣言語工具; Tablespace: 
--

CREATE TABLE "釋義" (
    "流水號" integer,
    "主編號" integer,
    "義項順序" integer,
    "詞性" integer,
    "釋義" character varying
);


ALTER TABLE "教育部臺灣閩南語常用詞辭典"."釋義" OWNER TO "臺灣言語工具";

COPY "教育部臺灣閩南語常用詞辭典"."造字集" ("統一碼", "組字式") FROM stdin;
e0a0	⿰金森
e35a	⿰口霧
e35c	⿱相同
e35d	⿰月席
e700	⿰恩
e701	⿰因
e702	⿰勿愛
e703	⿰立在
e705	⿰百
e711	⿰口尢
e725	⿰虫念
e72c	⿴丁
e76f	⿴皮卜
f5e7	⿴疒哥
f5e8	⿱向上
f5e9	⿰彥
f5ea	⿰甩
f5ee	⿰回
f5ef	⿰寒
\.

