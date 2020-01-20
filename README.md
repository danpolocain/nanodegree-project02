#PROJECT 02 - UDACITY STREAMING NANODEGREE
**How did changing values on the SparkSession property parameters affect the throughput and latency of the data?**.

I've notice that changing some SparkSession properties, it increases the performance of throughput and latency. Specially in rows per second and decreasing speed to process jobs.

**What were the 2-3 most efficient SparkSession property key/value pairs? Through testing multiple variations on values, how can you tell these were the most optimal?**

spark.default.parallelism:18 and spark.serializer:org.apache.spark.serializer.KryoSerializer. The first one is used to increase num. of tasks per core and the second one is to set the serializer to use Kryo library that is about 10x compact than java serializer.