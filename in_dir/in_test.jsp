<html>
   <head>
      <title><c:forEach> Tag Example</title>
   </head>

   <body>
      <p>hello1</p>
      <p>hello2</p>
      <c:if = test="${count != null}">
        <p>count is not null</p>
      </c:if>
      <c:foreach>Item3</c:foreach>
      <c:forEach var = "i" begin = "1" end = "5">
         Item1 <c:out value = "${i}"/><p>
      </c:forEach>
      <c:forEach var = "i" begin = "1" end = "5">
         Item2 <c:out value = "${i}"/><p>
      </c:forEach>
   </body>
</html>