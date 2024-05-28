# Databricks notebook source
DATABRICKS_HOST=''
DATABRICKS_TOKEN=''
DATABRICKS_SQL_WAREHOUSE_ID=''
CATALOG='central_platform_config'
SCHEMA='system_tables_config'
TABLE='workspace_to_identity_access_mapping'
SQL_STATEMENT=f"""INSERT INTO {CATALOG}.{SCHEMA}.{TABLE} (workspace_id, workspace_name, bu_name, identity_name) VALUES ('4488299099255398', 'ws1', 'bu1', 'tarun.dalke@databricks.com');"""


# COMMAND ----------

# MAGIC %pip install databricks-sdk --upgrade
# MAGIC dbutils.library.restartPython()
# MAGIC %pip show databricks-sdk | grep -oP '(?<=Version: )\S+'

# COMMAND ----------

from databricks.sdk import WorkspaceClient
w = WorkspaceClient()

response = w.statement_execution.execute_statement(SQL_STATEMENT,DATABRICKS_SQL_WAREHOUSE_ID)
print(response)
print(type(response.status.state))
