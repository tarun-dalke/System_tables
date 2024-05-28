# Databricks notebook source
# MAGIC %sh
# MAGIC DATABRICKS_HOST=''
# MAGIC DATABRICKS_TOKEN=''
# MAGIC DATABRICKS_SQL_WAREHOUSE_ID=''
# MAGIC CATALOG='central_platform_config'
# MAGIC SCHEMA='system_tables_config'
# MAGIC TABLE='workspace_to_identity_access_mapping'
# MAGIC SQL_STATEMENT="INSERT INTO $CATALOG.$SCHEMA.$TABLE (workspace_id, workspace_name, bu_name, identity_name) VALUES ('2352924812459863', 'ws2', 'bu2', 'user');"

# COMMAND ----------

# MAGIC %sh
# MAGIC curl --request POST \
# MAGIC https://${DATABRICKS_HOST}/api/2.0/sql/statements/ \
# MAGIC --header "Authorization: Bearer ${DATABRICKS_TOKEN}" \
# MAGIC --header "Content-Type: application/json" \
# MAGIC --data '{
# MAGIC   "warehouse_id": "'"$DATABRICKS_SQL_WAREHOUSE_ID"'",
# MAGIC   "catalog": "'"$CATALOG"'",
# MAGIC   "schema": "'"$SCHEMA"'",
# MAGIC   "table": "'"$SCHEMA"'",
# MAGIC   "statement": "'"$SQL_STATEMENT"'",
# MAGIC   "parameters": [
# MAGIC     { "name": "extended_price", "value": "60000", "type": "DECIMAL(18,2)" },
# MAGIC     { "name": "ship_date", "value": "1995-01-01", "type": "DATE" },
# MAGIC     { "name": "row_limit", "value": "2", "type": "INT" }
# MAGIC   ]
# MAGIC }' 
# MAGIC
