
import java.io.{File, ByteArrayInputStream}
import java.nio.file.{Files, Paths}
import javax.imageio.{ImageWriteParam, IIOImage, ImageIO}

import unfiltered.Cycle

//import java.util.Base64
import sun.misc.BASE64Decoder;
import _root_.unfiltered.request.Body
import _root_.unfiltered.request.Path
import unfiltered.response.{Ok, ResponseHeader, ResponseString}
import unfiltered.filter.Plan
import unfiltered.jetty.SocketPortBinding
import unfiltered.request._
/**
  * Created by sudhakar on 2/10/17.
  */

object SimplePlan extends Plan {
  def intent = {
    case req@GET(Path("/get")) => {
      Ok ~> ResponseString(IPApp.testImage("data3/test/elephant/image_0011.jpg"))
    }

      case req@POST(Path("/get_custom")) => {
        val imageByte = (new BASE64Decoder()).decodeBuffer(Body.string(req));
        val bytes = new ByteArrayInputStream(imageByte)
        val image = ImageIO.read(bytes)
        ImageIO.write(image, "png", new File("image.png"))
      }
        Ok ~> ResponseString(IPApp.testImage("image.png"))
  }
}
object SimpleServer extends App {
  val bindingIP = SocketPortBinding(host = "127.0.0.1", port = 8080)
  unfiltered.jetty.Server.portBinding(bindingIP).plan(SimplePlan).run()
}
