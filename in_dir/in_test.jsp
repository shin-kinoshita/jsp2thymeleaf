<html>
   <%-- this is comment --%>
   <head>
      <title> Tag Example</title>
   </head>

   <body>
      <p>${f:h(evaluation)}</p>
      <p id="${f:h(evaluation)}"></p>
      <p id="${f:h(evaluation)}">${f:h(evaluation)} is good</p>
      <p>${hello1}</p>
      <p value=${test}>hello2</p>
      <c:if test="${count != null}">
        <c:if test="${count != null}">
          <p>count is not null</p>
        </c:if>
      </c:if>
      <c:if test="${count != null}">
        <p>count2 is not null</p>
      </c:if>
      <c:forEach var="i" begin="1" end="5">
         Item1 <c:out value="${i}"/><p>
      </c:forEach>
      <c:forEach var="i" begin="1" end="5">
         Item2 <c:out value="${i}"/><p>
      </c:forEach>
      <c:foreach>Item3</c:foreach>
      <c:forEach var="item" items="${list}">
        Item4
        <c:out value="${item}" />
      </c:forEach>
      <c:if test="${count != null}">
        <p>count3 is not null</p>
      </c:if>
      <c:set var="data" value="this is test">
        <p>${data}</p>
      </c:set>
      <c:set var="data" value="123">
        <p>${data}</p>
      </c:set>
   </body>
</html>