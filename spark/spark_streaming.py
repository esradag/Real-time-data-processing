from pyspark.sql import SparkSession
from pyspark.sql.functions import from_json, col
from pyspark.sql.types import StructType, StringType, DoubleType

spark = SparkSession.builder.appName("CryptoStreaming").getOrCreate()

schema = StructType() \
    .add("id", StringType()) \
    .add("current_price", DoubleType()) \
    .add("market_cap", DoubleType()) \
    .add("price_change_percentage_24h", DoubleType())

df = spark.readStream \
    .format("kafka") \
    .option("kafka.bootstrap.servers", "localhost:9092") \
    .option("subscribe", "crypto-topic") \
    .load()

crypto_df = df.selectExpr("CAST(value AS STRING)") \
    .select(from_json(col("value"), schema).alias("data")) \
    .select("data.*")

crypto_df.writeStream \
    .foreachBatch(lambda batch_df, _: batch_df.write \
                  .format("jdbc") \
                  .option("url", "jdbc:postgresql://localhost:5432/crypto_db") \
                  .option("dbtable", "crypto_prices") \
                  .option("user", "postgres") \
                  .option("password", "password") \
                  .mode("append") \
                  .save()) \
    .start() \
    .awaitTermination()
