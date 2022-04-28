# Databricks notebook source
# MAGIC %md
# MAGIC # Learning DBFS
# MAGIC * Also learning about creating Markdown cell
# MAGIC 
# MAGIC The below cell to list the folders from the DBFS. Use %fs to start with for any command. This is for bash environment, then enter the command. In below case, executing ls command on the root

# COMMAND ----------

# MAGIC %fs ls /FileStore/tables

# COMMAND ----------

# MAGIC %fs mkdirs /tmp/my_cloud_dir

# COMMAND ----------

# MAGIC %sql
# MAGIC drop table if exists employeedata;
# MAGIC create table employeedata using csv options (path "/FileStore/tables/employeedata.csv", header "true")

# COMMAND ----------

# MAGIC %sql
# MAGIC select * from employeedata

# COMMAND ----------

# MAGIC %sql
# MAGIC select gender, sum(salary) as totalsalary from employeedata group by gender order by gender desc

# COMMAND ----------

# MAGIC %md
# MAGIC Both the statements below brings back the same result

# COMMAND ----------

# MAGIC %fs ls /

# COMMAND ----------

display(dbutils.fs.ls('/'))

# COMMAND ----------

df1 = spark.read.format("csv").option("header", "true").load("dbfs:/FileStore/datafiles/employeedata.csv")

# COMMAND ----------

display(df1)

# COMMAND ----------

dbutils.help()

# COMMAND ----------

dbutils.fs.help()

# COMMAND ----------

dbutils.notebook.help()

# COMMAND ----------

dbutils.widgets.help()

# COMMAND ----------

dbutils.secrets.help()

# COMMAND ----------

dbutils.fs.help('cp')

# COMMAND ----------

dbutils.widgets.text("Something","GoodJob")


# COMMAND ----------

something = dbutils.widgets.get("Something")
print(something)

# COMMAND ----------

dbutils.widgets.removeAll()
