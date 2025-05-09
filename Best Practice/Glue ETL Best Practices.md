## Glue ETL Best Practices


## Overview of Glue ETL
1. Serverless no extra infra setup needed fully managed by AWS. Less time to spin workflow.
2. Good fit for the use cases that are small to medium kind of workload.
3. Cost of processing is depending on the number of dpu's, worker type used and time spent to complete the job. See the cost breakdown section down below.
4. Support different type of job setup.
   1. Glue Python shell -- for small pure python application that doesn't require distributed computing platform.
   2. Glue ETL (Spark) -- distributed computing model using spark.
   3. Glue Ray -- distributed computed model that can be used for different usecases uses pure pythonic programming [refer](https://www.ray.io/)
5. For distributed computing applications like Spark and Ray there are different type of workers can be used and each of the worker type is associated below resources.
   - **G.1X** --
     1. 1 worker(executor) = 1 DPU(Data Processing Unit)
     2. Cores    =   4 vCPU
     3. Memory   =   16 Gig
     4. Disk Space = 64 Gig
   - **G.2X** -- 
     1. 1 worker(executor) = 2 DPU(Data Processing Unit)
     2. Cores              = 8 vCPU
     3. Memory             = 32 Gig
     4. Disk Space         = 128 Gig
   - **G.4X** --
     1. 1 worker(executor) = 4 DPU(Data Processing Unit)
     2. Cores              = 16 vCPU
     3. Memory             = 64 Gig
     4. Disk Space         = 256 Gig
   - **G.8X** --
     1. 1 worker(executor) = 8 DPU(Data Processing Unit)
     2. Cores              = 32 vCPU
     3. Memory             = 128 Gig
     4. Disk Space         = 512 Gig

6. Glue ETL (spark) had different version associated to spark versions.
   - **Glue 2.0** -- spark 2.4, scala 2, python 3
   - **Glue 3.0** -- spark 3.1, scala 2, python 3
   - **Glue 4.0** -- spark 3.3, scala 2. python 3
   
7. Glue has different connectors that connect to various sources and sinks.
   - **Sources** -- S3, JDBC, Redshift, DynamoDB, MongoDB, Kafka, Kinesis, etc.
   - **Sinks** -- S3, JDBC, Redshift, DynamoDB, MongoDB, Kafka, Kinesis, etc.
    

### Job level best practices 
When setting up the glue job make sure below are followed.
**NOTE** please have these tried on the build account first.

1. Set the glue **version  3.0** or above.
2. **autoscaling** is enabled on the new job/updates by default, however, there are some experiences enaling autoscaling when upgrading the job from Glue 2.0 to 3.0 seen performance degradation so make sure benchmark the upgrade in build with autoscaling enabled and have it productionalized if you don't see a performance hit.
   - To enable autoscaling the job should be upgraded to glue 3.0 or above.
   **note** Autoscaling doesn't mean it would reduce the cost of the etl, it really depends on how your etl workload is distributed and how the workers are being utilized at each stage, so if spark decides it has to use the MAX workers it was set it will use all the workers regardless.
   - You would see the cost reduction in case of overprovisioned job where it can scale down the resources if not needed.
   - Make sure autoscaling is throughly tested for your usecase with existing workers set.
3. Deciding on the number of workers 
   - There is no concrete formula defining it, as each etl has the logic and transformations differs etl to etl. 
   - For simple and generic use cases where etl is reading a 1 gig data and applying **narrow transformations(filter,map, flatten etc)**,can start with **2 workers**.
   - Other cases please try with **5 workers** and see how the job performs. To check how many 
   - refer [capacity planning](https://docs.aws.amazon.com/glue/latest/dg/monitor-debug-capacity.html) 
4. When working on the build **enable job metrics** by selecting the below options and add sparkui log path pointing to glue temp bucket and specific job prefix. This would help determine how many executors effectively being used.
![img.png](img.png)
   1. To spin up spark ui follow steps [spark-ui](https://git.rockfin.com/Data-Intelligence/glue-etl-jobs-deployments/blob/master/docs/Setup/enable-spark-ui-metrics/enable-metrics.md)
   2. When job metrics are enabled each run will give metric insight similar to below.
      1. examples refer [job-metrics](https://docs.aws.amazon.com/glue/latest/dg/monitor-profile-debug-straggler.html) 
![img_1.png](img_1.png)
5. Use FLEX execution for non-urgent etl's that don't have tight SLA for data to be available. Some of the workload category tha can be potentially be a fit are. 
   - Nightly ETL jobs, or jobs that run over weekends for processing workloads
   - One-time bulk data ingestion jobs
   - Jobs running in test environments or pre-production workloads
   - Time-insensitive workloads where it’s acceptable to have variable start and end times
   - refer [flex-execution](https://aws.amazon.com/blogs/big-data/introducing-aws-glue-flex-jobs-cost-savings-on-etl-workloads/)

### ETL best practices

1. When reading the data from source make sure to use the **pushdown predicate** to filter the data.
   - This will reduce the amount of data being read and will reduce the cost of processing.
   - Example: 
     - If the source is s3 and the data is partitioned by date, then use the pushdown predicate to filter the data by date.
    ```python
   # reading s3 as source 
   spark.read.parquet("s3://bucket/path").filter("date = '2021-01-01'")
   # reading glue catalog as the source
    spark.table("db.table").filter("date = '2021-01-01'")
   # reading glue catalog as the source using sql
   spark.sql("select * from db.table where date = '2021-01-01'")
 
2. If the source is columnar format like parquet/orc, then use the **column pruning** to reduce the amount of data being read.
   - Example: If the source has 100 columns and the etl is using only 10 columns, then use the column pruning to read only 10 columns.
   
3. Make sure to use the **narrow transformations** as much as possible before applying the joins.
   - Example: filter, map, flatten, etc.
   ```python
     # Example of narrow transformation
     df.filter("date = '2021-01-01'").map(lambda x: x+1).flatten()
   ```
   
4. Apply Broadcast join if the data is small and can fit in the memory of the worker which avoid data shuffle.
   - Example: If the data is 1 gig and the worker has 16 gig memory, then broadcast join can be used.
     ```python 
     # Example of broadcast join
     df.join(broadcast(df1), df.id == df1.id, "inner")**
     # Example of broadcast join using sql
     spark.sql("select /*BROADCAST(df1)*/ * from df inner join df1 on df.id = df1.id")
     ```
   1. To verify broadcast join is working or not, check the spark ui and check shuffle read is 0.
      ```python
           df.explain()
           spark.sql("explain select /*BROADCAST(df1)*/ * from df inner join df1 on df.id = df1.id")
       ```
      spark explain output looks like below.
      1. **Broadcast join**
         1. **BroadcastExchange**
            1. Exchange
               1. Project
                  1. Filter
                     1. Scan
                        1. FileScan
                      
      - If the table size is less than 10 MB then spark will automatically broadcast the table.
      - If the table size is more than 10 MB and  want to broadcast the table then we can use the below property.
      **spark.sql.autoBroadcastJoinThreshold =  <appropriatesize> MB**  that can fit into the memory of the worker. 
   

5. If the data is skewed and joins are taking time use below approaches
   1. Use spark adaptive query execution to reduce the data skewness
        - example 
        ```python
        spark.conf.set("spark.sql.adaptive.enabled", "true")
        spark.conf.set("spark.sql.adaptive.skewJoin.enabled", "true")
        spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionFactor", "5")
        spark.conf.set("spark.sql.adaptive.skewJoin.skewedPartitionThresholdInBytes", "256MB")
      ```
       - refer [spark-adaptive-query-execution](https://spark.apache.org/docs/latest/sql-performance-tuning.html#adaptive-query-execution)
   2. Use the **broadcast join** if possible to avoid the skew joins see above point 4.

   3. Use the **skew join** to reduce the data skewness.
   - Example: 
   ```python
         spark.sql("select /*+ SKEWJOIN(b) */ * from a join b on a.id = b.id")
   ```
   4. Use repartition the data after all the transformations are applied to avoid the large data shuffles
      Example: 
         ```python
            # repartitioning the data
            df.repartition(10)
            # repartitioning the data using column, this column should be used in the join
            df.repartition("id", 10)
         ```
   5. Use salting technique to avoid the data skewness.
      - Example: 
         ```python
            # salting the data
            df.withColumn("salt", concat(lit(randint(0, 9)), col("id"))).repartition("salt", 10)
         ```
   6. While writing the data to the target use the **bucketing** to avoid the data skewness to avoid further .
      - Example: 
         ```python
            # bucketing the data
            df.write.bucketBy(10, "id").saveAsTable("db.table")
         ```

6. Avoid using collect() and collect_list() functions in prod as they will bring all the data to the driver and will cause the out of memory error unless the final data set is really small.
   - Example: 
      ```python
         # collect() function
         df.collect()
         # collect_list() function
         df.groupBy("id").agg(collect_list("name"))
      ```

7. Alternatively for collect use head() function to get the sample data.
   - Example: 
      ```python
         # head() function
         df.head()
      ```
8. Avoid using user defined functions(udf) as they are black box to spark and spark cannot optimize them. If possible use the spark sql functions for example if you want to add 1 to the id column then use the spark sql function. 
   - Example: 
      ```python
         # udf function
         def add_one(x):
            return x+1
         spark.udf.register("add_one", add_one)
         spark.sql("select add_one(id) from df")
         
         # spark sql function
         spark.sql("select id+1 from df")
      ```
9. Use the **spark sql** as much as possible as spark can optimize the sql queries based on cost based optimizer.
    - Example: 
       ```python
          # spark sql
          spark.sql("select id+1 from df")
       ```

10. Use **cache** and **persist** to avoid the recomputation of the data. For example if the dataframe is used in multiple places then cache/persist the data.
    - Example: 
      ```python
         # cache by default memory only
         df.cache()
         # persist
         df.persist()
         # persist with storage level
            df.persist(StorageLevel.MEMORY_AND_DISK)
      ```

11. Use kyro serialization to reduce the size of the data being transferred over the network. For example if the data is 1 gig and kyro serialization reduces the data size to 100 MB then it will reduce the network traffic by 90%.
    - Example: 
      ```python
         # kyro serialization
         spark.conf.set("spark.serializer", "org.apache.spark.serializer.KryoSerializer")
      ```


    
### Cost break down for the spark job with different worker types and workers
**Note - minimum billing hours is 0.0166 hours**
- **G.1X** -- 
  - Standard:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 1) = 10 dpus
    - 10 DPUs x 1.00 hours x 0.44 USD per DPU-Hour = 4.40 USD 
    - ETL jobs cost : 4.40 USD
  - FLEX:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 1) = 10 dpus
    - 10 DPUs x 1.00 hours x 0.29 USD per DPU-Hour = 2.90 USD (Apache Spark ETL job with Flex execution option cost)
    - ETL jobs with Flex execution option cost : 2.90 USD

- **G.2X** -- 
  - Standard:
      - ran with 10 Workers, ran about 1 hr
      - 10 workers * number of dpus (10 * 2) = 20 dpus
      - 20 DPUs x 1.00 hours x 0.44 USD per DPU-Hour = 8.80 USD (Apache Spark ETL job cost)
      - ETL jobs cost : 8.80 USD
  - FLEX:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 2) = 20 dpus
    - 20 DPUs x 1.00 hours x 0.29 USD per DPU-Hour = 5.80 USD (Apache Spark ETL job with Flex execution option cost)
    - ETL jobs with Flex execution option cost : 5.80 USD
  
- **G.4X** --
  - Standard:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 4) = 40 dpus
    - 40 DPUs x 1.00 hours x 0.44 USD per DPU-Hour = 17.60 USD (Apache Spark ETL job cost)
    - ETL jobs cost : 17.60 USD
  - FLEX:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 4) = 40 dpus
    - 40 DPUs x 1.00 hours x 0.29 USD per DPU-Hour = 11.60 USD (Apache Spark ETL job with Flex execution option cost)
    - ETL jobs with Flex execution option cost : 11.60 USD

- **G.8X** --
  - Standard:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 8) = 80 dpus
    - 80 DPUs x 1.00 hours x 0.44 USD per DPU-Hour = 35.20 USD (Apache Spark ETL job cost)
    - ETL jobs cost : 35.20 USD
  - FLEX:
    - ran with 10 Workers, ran about 1 hr
    - 10 workers * number of dpus (10 * 8) = 80 dpus
    - 80 DPUs x 1.00 hours x 0.29 USD per DPU-Hour = 23.20 USD (Apache Spark ETL job with Flex execution option cost)
    - ETL jobs with Flex execution option cost : 23.20 USD

    