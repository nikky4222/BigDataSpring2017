

import org.apache.spark.{SparkContext, SparkConf}


object SparkWordCount {

  def main(args: Array[String]) {


    val sparkConf = new SparkConf().setAppName("SparkWordCount").setMaster("local[1]")

    val sc=new SparkContext(sparkConf)

    val input=sc.textFile("input").flatMap(x=>x.split(" "))
   val counts = input.map(word => (word, 1)).reduceByKey{case (x, y) => x + y}
   counts.saveAsTextFile("keyvalue")
   val ccc=counts.sortBy(_._2,false)
    ccc.saveAsTextFile("sort")
   val i2=ccc.first()
   val i3=ccc.take(3)
   println("Word that occured the most"+i2)
   println("The top 3 words")
   i3.foreach{ println }
   val numAs = input.filter(line => line.contains("a")).count()

   println("Lines with a: %s".format(numAs))

   val input1=sc.textFile("input1").flatMap(x=>x.split(" "))
   val input2=sc.textFile("input2").flatMap(x=>x.split(" "))


    val ac=input.map(_.toUpperCase)
    val bc=input.flatMap(_.toUpperCase)
    ac.saveAsTextFile("uppermap")
    bc.saveAsTextFile("upperflatmap")



     val d=input1.union(input2)
    val e=input1.intersection(input2)
    val i1=e.count()
    println(i1)
    val f=input1.distinct()

    println("Union:" +d.collect().mkString(","))
    println("Intersection:" + e.collect().mkString(","))
    println("Distinct:" + f.collect().mkString(","))





  }

}
