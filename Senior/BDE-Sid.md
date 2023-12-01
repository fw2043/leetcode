# Portfolio for Senior BDE - Siddartha Rao Chennur
## About Me
Joined Quicken Loans as a Big Data Engineer in November 2020. I worked on various projects in the past 3 years with Rocket Companies. 
I am passionate BDE always willing to learn, execute and embrace any challenge presented to me during my tenure.
I am involved in various impactful projects all across platform. 
Further I have always enabled my fellow engineers to have an quick, simple and highly efficient solutions to their data problems.

## Portfolio
### Glue Partition Management
My initial project Glue Partition Management is still widely used, highly robust and fault tolerant across platform both RM/RKT. 
This project is one of the key data enablers in the platform as it silently keeps all data partitions updated in a timely manner.
Its one of the project which I delivered in a short span of 2 months but has been impactful ever since. 

From the initial project itself, my major focus has been to have a scalable solution.
The Glue Partition Management process with Parent/Child Lambda concept provides such scalability as it has been able to deal with our ever expanding data catalog within the limitations of AWS Lambda like 15 min timeouts.

### Qtweets Ingestion into Datalake
Next, project that comes to my mind will be 300+ Qtweets Ingestion/Processing into our Cloud Platform. I have initially worked on developing an ETL pipeline which can backfill large amount of Qtweet data as well as do a ongoing data processing.  
First challenge I faced during the backfill was the common large number of small files problem. Some of our Qtweets had more than million files (>1.3 million) per day.
This caused GLUE ETL to fail with various memory issues. 

One of the solutions I proposed was to fix the source of the problem. I got that oppportunity where I worked on creating a new process for  Qtweets Streaming from Kafka to RAW.   

Here I proposed multiple enhancements to existing process, which includes merging files while moving data into RAW which avoids small file problems, adding Kafka Triggers under VPC setup to enable direct reads from Kafka Queues, Setting up a direct ingestion into RAW instead of using S3 connector which avoided data duplication and multiple hops across accounts.  

This helped reduce file numbers in S3 from millions to < 1000 files , increase the efficiency of the Qtweet process to more real time streaming setup for more than 300+ Qtweets.
This also helped reduce costs of the downstream Glue processes by 10 folds as well.