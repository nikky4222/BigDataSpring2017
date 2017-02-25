name := "Image_Classification"

version := "1.0"

scalaVersion := "2.11.8"

scalacOptions ++= Seq(
  "-optimize",
  "-unchecked",
  "-deprecation"
)

classpathTypes += "maven-plugin"

libraryDependencies ++= Seq(
  "org.apache.spark" %% "spark-core" % "1.6.0" % "provided",
  "org.apache.spark" %% "spark-streaming" % "1.6.0",
  "org.apache.spark" %% "spark-mllib" % "1.6.0",
  "org.scalatest" %% "scalatest" % "2.2.1" % "test",
  "org.bytedeco" % "javacpp" % "0.11",
  "org.bytedeco"% "javacv" % "0.11",
  "net.databinder" %% "unfiltered-filter" % "0.8.3",
  "net.databinder" %% "unfiltered-jetty" % "0.8.3",
  "net.databinder" %% "unfiltered-directives" % "0.8.3",
  "com.levigo.jbig2" % "levigo-jbig2-imageio" % "1.6.5",
  "org.bytedeco.javacpp-presets" % "opencv" % "2.4.11-0.11",
  "org.bytedeco.javacpp-presets" % "opencv" % "2.4.11-0.11" classifier "linux-x86",
  "org.bytedeco.javacpp-presets" % "opencv" % "2.4.11-0.11" classifier "linux-x86_64",
  "org.bytedeco.javacpp-presets" % "opencv" % "2.4.11-0.11" classifier "macosx-x86_64",
  "org.bytedeco.javacpp-presets" % "opencv" % "2.4.11-0.11" classifier "windows-x86",
  "org.bytedeco.javacpp-presets" % "opencv" % "2.4.11-0.11" classifier "windows-x86_64"
)


resolvers ++= Seq(
  "Akka Repository" at "http://repo.akka.io/releases/",
  "scala-tools" at "https://oss.sonatype.org/content/groups/scala-tools",
  "Typesafe repository" at "http://repo.typesafe.com/typesafe/releases/",
  "Second Typesafe repo" at "http://repo.typesafe.com/typesafe/maven-releases/",
  "JavaCV maven repo" at "http://maven2.javacv.googlecode.com/git/",
  "JavaCPP maven repo" at "http://maven2.javacpp.googlecode.com/git/",
  "ImageIO" at "https://mvnrepository.com/artifact/com.levigo.jbig2/levigo-jbig2-imageio",
  Resolver.sonatypeRepo("public")
)
