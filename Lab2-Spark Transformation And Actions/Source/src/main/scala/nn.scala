/**
  * Created by nikky on 2/1/2017.
  */
import org.apache.spark.{SparkContext, SparkConf}

object nn {


  /**
    * Created by Mayanka on 09-Sep-15.
    */


    def main(args: Array[String]) {


      val sparkConf = new SparkConf().setAppName("SparkWordCount").setMaster("local[*]")

      val sc = new SparkContext(sparkConf)

      val input = sc.textFile("input").flatMap(line => {line.split(" ")})
      val input11 = sc.textFile("input11").flatMap(line => {line.split(" ")})
      println("input text file is divided into strings = ")
     input11.saveAsTextFile("outppp")


      val a= input.map(x=>(x,x.length.toDouble))//make a key value pair of (word , length of word)
      a.saveAsTextFile("out22")
      val asize=a.count()
      val b= input11.map(x=>(x,x.length.toDouble))
      val bsize=b.count()
      println( "input.txt contain " + asize + "words , input1.txt contain " + bsize + "words ")

      val a_3=a.filter{case (x, y) => y == 3}//three letter Words
      val a1=a.sortBy(_._2,false).take(5)//top 5 words in length
      val unique_words  = input.intersection(input11)
      unique_words.foreach(println)
      unique_words.saveAsTextFile("output20")
      val unique_word_count = unique_words.count()
      println("total unique words "+ unique_word_count)



    }



}
