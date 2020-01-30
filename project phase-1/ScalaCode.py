val data = sc.textFile("hdfs://localhost:9000/Users⁩/saiaravindreddymannem⁩/⁨Documents⁩/⁨workspaces/⁨python_workspaces⁩/twitter-datastream⁩/⁨hadoop_files⁩/twitter_healthandhashtags.txt")
val data1 = data.flatMap(_.split("\\s+"))
val Out_file = data1.map(w => (w, 1)).reduceByKey(_ + _)
Out_file.saveAsTextFile("README1.count")