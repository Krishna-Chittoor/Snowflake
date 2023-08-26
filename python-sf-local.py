import snowflake.connector

ctx = snowflake.connector.connect(
    user="krishnade1",
    password=,
    account="zodwstr-qm55433",
    warehouse="compute_wh",
    database="snowflake_sample_data",
    schema="TPCH_SF1",
    role='ACCOUNTADMIN',
    session_parameters={
        'TIMEZONE':'UTC',
    }
)

cs=ctx.cursor()

try:
    wh_sql=""" USE WAREHOUSE compute_wh """
    cs.execute(wh_sql)
    sql = """ select * from SNOWFLAKE_SAMPLE_DATA.TPCH_SF1.LINEITEM limit 10 """
    cs.execute(sql)
    all_rows=cs.fetchall()
    print(all_rows)

finally:
    cs.close()

ctx.close()



