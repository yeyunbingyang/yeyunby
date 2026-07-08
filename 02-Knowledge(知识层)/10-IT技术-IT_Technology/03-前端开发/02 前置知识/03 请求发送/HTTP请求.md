# HTTP 请求

## 1) 请求组成

请求由三部分组成

1. 请求行

2. 请求头

3. 请求体

### **请求行（Request Line）**：

当一个客户端（例如，浏览器）向服务器发送HTTP请求时，请求的第一行就是请求行。请求行包括以下三个部分：

1. **请求方法**：这是一个动词，如 `GET`、`POST`、`PUT`、`DELETE` 等，它告诉服务器要执行什么样的操作。

2. **请求的URL路径**：这是请求的目标资源的路径。

3. **HTTP协议版本**：这表示客户端使用的HTTP协议的版本。

下面是一个请求行的例子：

```
GET /index.html HTTP/1.1
```

在这个例子中：

- `GET` 是请求方法，表示客户端希望获取资源。

- `/index.html` 是请求的URL路径，表示客户端希望获取的资源。

- `HTTP/1.1` 是HTTP协议版本，表示客户端使用的是HTTP 1.1版本的协议。

### **请求头（Request Headers）**：

- 请求头包含关于请求的元数据，如用户代理、所需的内容类型、所接受的内容类型等。

- 请求头是由键值对组成的列表，每个键值对之间使用冒号分隔，键和值之间使用空格分隔。

- 例如，一个包含常见请求头的请求可能是这样的：

```
bashCopy codeHost: www.example.com
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9
```

#### Content-Type【内容】

`Content-Type` 是一个 HTTP 头部信息，用于**定义网络文件的类型和网页的编码**，决定浏览器将以什么形式、什么编码读取这个文件。它在响应中，向客户端提供返回内容的实际内容类型。

`Content-Type` 的语法格式如下：

```
Content-Type: media-type; charset=character-set
```

其中：

- `media-type` [是资源或数据的 MIME 类型](https://www.runoob.com/http/http-content-type.html)[1](https://www.runoob.com/http/http-content-type.html)。

- `charset` [是字符编码标准](https://www.runoob.com/http/http-content-type.html)

常见的`Content-Type`值包括：

1. **application/x-www-form-urlencoded**：【表单默认】

- 这是用于HTML表单数据的默认编码类型。

- 表单数据会以键值对的形式编码，并使用`&`符号分隔。

- 例如：`key1=value1&key2=value2`

2. **multipart/form-data**：

- 这是用于在HTML表单中上传文件或二进制数据的编码类型。

- 表单数据会被划分为多个部分，并以多个部分的形式发送到服务器。

- 这种编码类型允许在表单中包含文件上传字段。

- 例如，一个包含文件上传的表单提交的请求可能使用multipart/form-data编码。

3. **application/json**：

- 这是表示JSON数据的媒体类型。

- 当客户端向服务器发送JSON格式的数据时，通常会使用这种类型。

- 例如：`{"key": "value"}`

4. **text/plain**：

- 这是纯文本数据的媒体类型。

- 当实体主体包含普通文本时，可以使用这种类型。

- 例如：普通文本消息或文本文件。

5. **application/xml**：

- 这是表示XML数据的媒体类型。

- 当客户端向服务器发送XML格式的数据时，通常会使用这种类型。

- 例如：`<xml><key>value</key></xml>`

6. **image/jpeg、image/png等**：

- 这些是表示图像数据的媒体类型。

- 当实体主体包含图像数据时，会使用对应的图像媒体类型。

`Content-Type`字段的值告诉服务器如何解析请求的实体主体数据，以及如何格式化响应的实体主体数据。正确设置`Content-Type`对于正确解析和处理HTTP请求和响应非常重要。

### **请求体（Request Body）**：

- 请求体包含实际发送到服务器的数据，通常用于POST请求或其他需要发送数据的请求。

- 请求体的格式取决于请求的内容类型，例如，对于表单提交，请求体可能是经过URL编码或者多部分形式的数据。

- 例如，对于一个包含表单数据的POST请求，请求体可能是这样的：

```
makefileCopy code
username=user&password=pass
```

或者对于包含JSON数据的POST请求，请求体可能是这样的：

```
jsonCopy code
{"username": "user", "password": "pass"}
```

这三部分组成了一个完整的HTTP请求，客户端通过发送这些信息到服务器来请求资源或执行某些操作。

可以用 telnet 程序测试

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864249-431332e2-377b-4d90-b74b-58d1d843a25c.png "null")

## 2) 请求方式与数据格式

### get 请求示例

```
GET /test2?name=%E5%BC%A0&age=20 HTTP/1.1
Host: localhost
```

- %E5%BC%A0 是【张】经过 URL 编码后的结果

- GET请求用于向服务器请求特定资源，通常用于获取数据。

- 请求参数是以URL查询字符串的形式附加在URL之后，以`?`开始，参数之间用`&`分隔。

- GET请求的请求体为空。

- GET请求的格式示例：

```
GET /path/to/resource?param1=value1&param2=value2 HTTP/1.1
Host: www.example.com
```

### post 请求示例

```
POST /test2 HTTP/1.1
Host: localhost
Content-Type: application/x-www-form-urlencoded
Content-Length: 21

name=%E5%BC%A0&age=18
```

- POST请求用于向服务器提交数据，通常用于向服务器发送数据并创建新的资源。

- 请求参数通常包含在请求体中，而不是URL中。

- POST请求的请求体的格式通常取决于请求的内容类型，可以是经过URL编码的表单数据，也可以是JSON格式的数据等。

- POST请求的格式示例（以表单数据为例）：

- 如果POST请求的内容是JSON格式的数据，则请求头中的Content-Type可能是application/json：

```
makefileCopy codePOST /path/to/resource HTTP/1.1
Host: www.example.com
Content-Type: application/x-www-form-urlencoded

param1=value1&param2=value2
```

```
bashCopy codePOST /path/to/resource HTTP/1.1
Host: www.example.com
Content-Type: application/json
            
{"param1": "value1", "param2": "value2"}
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864341-4c84946d-081a-44cb-8acf-942d6e901eab.png "null")

application/x-www-form-urlencoed 格式细节：

- 参数分成名字和值，中间用 = 分隔

- 多个参数使用 & 进行分隔

- 【张】等特殊字符需要用 encodeURIComponent() 编码为 【%E5%BC%A0】后才能发送

url：utf-8编码规则：每个字节转为16进制

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864400-8b06f4bc-e5a8-4956-a272-c117e8374dcf.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864460-86cd4119-5079-4c69-99ba-097300242962.png "null")

### json 请求示例

```
POST /test3 HTTP/1.1
Host: localhost
Content-Type: application/json
Content-Length: 25//发送字节长度

{"name":"zhang","age":18}
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864530-4e9604bb-3ca4-41e2-9d37-d24942cd8742.png "null")

0代表接收完毕

json 对象格式

```
{"属性名":属性值}
```

其中属性值可以是

- 字符串 ""

- 数字

- true, false

- null

- 对象

- 数组

json 数组格式

```
[元素1, 元素2, ...]
```

### multipart 请求示例

可以上传文件

分隔符,划分为多部分

```
POST /test2 HTTP/1.1
Host: localhost
Content-Type: multipart/form-data; boundary=123
Content-Length: 125

--123
Content-Disposition: form-data; name="name"

lisi
--123
Content-Disposition: form-data; name="age"

30
--123--
```

- boundary=123 用来定义分隔符

- 起始分隔符是 `--分隔符`

- 结束分隔符是 `--分隔符--`

Content-Length: 125

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864602-551dbcd4-aad2-436e-807f-a4b64d84d3a3.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864656-8d053e74-58bc-4498-ba04-330c295d8ee8.png "null")

http中换行是/r/n，少计算了/r 9个字符

### 数据格式小结

**客户端发送**

- 编码

- application/x-www-form-urlencoded ：url 编码 ，将特殊字符进行编码后发送

- application/json：utf-8 编码

- multipart/form-data：每部分编码可以不同

- 表单只支持以 application/x-www-form-urlencoded 和 multipart/form-data 格式发送数据

- 文件上传需要用 multipart/form-data 格式

- js 代码可以支持任意格式发送数据

**服务端接收**

- 对 application/x-www-form-urlencoded 和 multipart/form-data 格式的数据，Spring 接收方式是统一的，只需要用 java bean 的属性名对应请求参数名即可

- 对于 applicaiton/json 格式的数据，Spring 接收需要使用 @RequestBody 注解 + java bean 的方式

- 对于multipart/form-data格式的数据MultipartFile类型接收

## 3) 会话跟踪技术

Http 无状态，有会话

- 无状态是指，请求之间相互独立，第一次请求的数据，第二次请求不能重用

- 有会话是指，客户端和服务端都有相应的技术，可以暂存数据，让数据在请求间共享

什么是会话？

- 在我们日常生活当中，会话指的就是谈话、交谈。

- 在web开发当中，会话指的就是浏览器与服务器之间的一次连接，我们就称为一次会话。

在用户打开浏览器第一次访问服务器的时候，这个会话就建立了，直到有任何一方断开连接，此时会话就结束了。在一次会话当中，是可以包含多次请求和响应的。

比如：打开了浏览器来访问web服务器上的资源（浏览器不能关闭、服务器不能断开）

- 第1次：访问的是登录的接口，完成登录操作

- 第2次：访问的是部门管理接口，查询所有部门数据

- 第3次：访问的是员工管理接口，查询员工数据

**只要浏览器和服务器都没有关闭，以上3次请求都属于一次会话当中完成的。**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864718-fb917e45-9e3c-4781-8f12-57015d63423e.png "null")

需要注意的是：会话是和浏览器关联的，当有三个浏览器客户端和服务器建立了连接时，就会有三个会话。同一个浏览器在未关闭之前请求了多次服务器，这多次请求是属于同一个会话。比如：1、2、3这三个请求都是属于同一个会话。当我们关闭浏览器之后，这次会话就结束了。而如果我们是直接把web服务器关了，那么所有的会话就都结束了。

知道了会话的概念了，接下来我们再来了解下会话跟踪。

会话跟踪：一种维护浏览器状态的方法，服务器需要**识别多次请求是否来自于同一浏览器**，以便在同一次会话的多次请求间共享数据。

服务器会接收很多的请求，但是服务器是需要识别出这些请求是不是同一个浏览器发出来的。比如：1和2这两个请求是不是同一个浏览器发出来的，3和5这两个请求不是同一个浏览器发出来的。**如果是同一个浏览器发出来的，就说明是同一个会话**。如果是不同的浏览器发出来的，就说明是不同的会话。而识别多次请求是否来自于同一浏览器的过程，我们就称为会话跟踪。

我们使用会话跟踪技术就是要完成在同一个会话中，多个请求之间进行共享数据。

为什么要共享数据呢？

由于HTTP是无状态协议，在后面请求中怎么拿到前一次请求生成的数据呢？此时就需要在一次会话的多次请求之间进行数据共享

### **Cookie**原理【浏览器会话跟踪】

cookie 是**客户端会话跟踪技术**，它是存储在客户端浏览器的，我们使用 cookie 来跟踪会话，我们就可以在浏览器第一次发起请求来请求服务器的时候，我们**在服务器端来设置一个cookie**。

比如第一次请求了登录接口，登录接口执行完成之后，我们就可以设置一个cookie，在 cookie 当中我们就可以来存储用户相关的一些数据信息。比如我可以**在 cookie 当中来存储当前登录用户的用户名，用户的ID**。

服务器端在给客户端在响应数据的时候，会**自动**的将 cookie 响应给浏览器，浏览器接收到响应回来的 cookie 之后，会**自动**的将 cookie 的值存储在浏览器本地。接下来在后续的每一次请求当中，都会将浏览器本地所存储的 cookie **自动**地携带到服务端。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864778-8453980e-2784-4a18-80d8-2930e0859a4e.png "null")

接下来在服务端我们就可以获取到 cookie 的值。我们可以去判断一下这个 cookie 的值是否存在，如果不存在这个cookie，就说明客户端之前是没有访问登录接口的；如果存在 cookie 的值，就说明客户端之前已经登录完成了。这样我们就可以基于 cookie 在同一次会话的不同请求之间来共享数据。

我刚才在介绍流程的时候，用了 3 个自动：

- 服务器会 **自动** 的将 cookie 响应给浏览器。

- ![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864854-84001914-c32a-4d2d-b182-3e7399f157ee.png "null")

- 浏览器接收到响应回来的数据之后，会 **自动** 的将 cookie 存储在浏览器本地。

- 在后续的请求当中，浏览器会 **自动** 的将 cookie 携带到服务器端。![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864924-46f8ace3-b8e3-43a5-8070-6a9bb4d35dae.png "null")

**为什么这一切都是自动化进行的？**

是因为 **cookie 它是 HTP 协议当中所支持的技术**，而各大浏览器厂商都支持了这一标准。在 HTTP 协议官方给我们提供了一个响应头和请求头：

- 响应头 Set-Cookie ：设置Cookie数据的

- 请求头 Cookie：携带Cookie数据的

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432864982-f03da0c2-8e52-4945-9d3d-6a7c73487894.png "null")

**代码测试**

```
@Slf4j
@RestController
public class SessionController {

    //设置Cookie
    @GetMapping("/c1")
    public Result cookie1(HttpServletResponse response){
        response.addCookie(new Cookie("login_username","itheima")); //设置Cookie/响应Cookie
        return Result.success();
    }
    
    //获取Cookie
    @GetMapping("/c2")
    public Result cookie2(HttpServletRequest request){
        Cookie[] cookies = request.getCookies();
        for (Cookie cookie : cookies) {
            if(cookie.getName().equals("login_username")){
                System.out.println("login_username: "+cookie.getValue()); //输出name为login_username的cookie
            }
        }
        return Result.success();
    }
}    
```

A. 访问c1接口，设置Cookie，[http://localhost:8080/c1](http://localhost:8080/c1)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865059-29f6e519-2997-4031-a29c-6ce637f33cb3.png "null")

我们可以看到，设置的cookie，通过**响应头Set-Cookie**响应给浏览器，并且浏览器会将Cookie，存储在浏览器端。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865125-dd69ab9e-648d-420d-8bc1-6aebe6ab32cf.png "null")

B. 访问c2接口 [http://localhost:8080/c2，此时浏览器会自动的将Cookie携带到服务端，是通过**请求头Cookie**，携带的。](http://localhost:8080/c2，此时浏览器会自动的将Cookie携带到服务端，是通过**请求头Cookie**，携带的。)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865240-c4de854e-faa6-44ab-90d3-4d7737c53fe5.png "null")

**优缺点**

- 优点：HTTP协议中支持的技术（像Set-Cookie 响应头的解析以及 Cookie 请求头数据的携带，都是浏览器自动进行的，是无需我们手动操作的）

- 缺点：

- 移动端APP(Android、IOS)中无法使用Cookie

- 不安全，用户可以自己禁用Cookie

- Cookie不能跨域

Cookie 技术实现身份验证

服务器在用户登录后设置了一个包含用户信息的 Cookie，并在后续的请求中检查这个 Cookie。

sequenceDiagram  
participant Client  
participant L as LoginController  
participant i as CookieInterceptor  
participant C as Cookie  
rect rgb(200, 223, 255)  
Client ->> +L : 登录请求  
L ->> L : 检查用户名，密码，验证通过  
L ->> +C : 设置包含用户名的Cookie  
C -->> -L:   
L -->> -Client: 登录成功，返回包含Cookie的响应  
end  
rect rgb(200, 190, 255)  
Client ->> +i : 其它请求，请求中包含Cookie  
i ->> +C : 获取Cookie中的用户名  
C -->> -i :   
i ->> i: 用户名存在，放行  
i -->> -Client :   
end

在这个序列图中：

- 当客户端发送登录请求时，`LoginController` 检查用户名和密码。如果验证通过，`LoginController` 会设置一个包含用户名的 Cookie。

- 在后续的请求中，`CookieInterceptor` 会获取请求中的 Cookie，并检查其中的用户名。如果用户名存在，请求被放行。

### session 原理【单体架构】

服务器端会话跟踪技术，所以它是存储在服务器端的。而 Session 的底层其实就是**基于我们刚才所介绍的 Cookie 来实现的**。

- 获取Session![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865301-9239669f-e411-4647-abc0-0718e26288f2.png "null") 如果我们现在要基于 Session 来进行会话跟踪，浏览器在第一次请求服务器的时候，我们就可以直接在服务器当中来获取到会话对象Session。如果是第一次请求Session ，会话对象是不存在的，这个时候服务器会自动的创建一个会话对象Session 。而**每一个会话对象Session ，它都有一个ID**（示意图中Session后面括号中的1，就表示ID），我们称之为 Session 的ID。

- 响应Cookie (JSESSIONID)![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865356-14d0fe61-7e78-4d9c-afb5-ed9ea7d35bcd.png "null") 接下来，服务器端在给浏览器响应数据的时候，它会将 Session 的 ID 通过 Cookie 响应给浏览器。其实在响应头当中增加了一个 Set-Cookie 响应头。这个 Set-Cookie 响应头对应的值是不是cookie？ cookie 的名字是固定的 JSESSIONID 代表的服务器端会话对象 Session 的 ID。浏览器会自动识别这个响应头，然后自动将Cookie**存储在浏览器本地。**

- 查找Session![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865424-ce1d0cf3-6d42-45a2-be7d-2c7b22a50d5d.png "null") 接下来，在后续的每一次请求当中，都会将 Cookie 的数据获取出来，并且携带到服务端。接下来服务器拿到JSESSIONID这个 Cookie 的值，也就是 Session 的ID。拿到 ID 之后，就会从众多的 Session 当中来找到当前请求对应的会话对象Session。

- 这样我们是不是就可以通过 Session 会话对象在同一次会话的多次请求之间来共享数据了？好，这就是基于 Session 进行会话跟踪的流程。

**代码测试**

```
@Slf4j
@RestController
public class SessionController {

    @GetMapping("/s1")
    public Result session1(HttpSession session){
        log.info("HttpSession-s1: {}", session.hashCode());

        session.setAttribute("loginUser", "tom"); //往session中存储数据
        return Result.success();
    }

    @GetMapping("/s2")
    public Result session2(HttpServletRequest request){
        HttpSession session = request.getSession();
        log.info("HttpSession-s2: {}", session.hashCode());

        Object loginUser = session.getAttribute("loginUser"); //从session中获取数据
        log.info("loginUser: {}", loginUser);
        return Result.success(loginUser);
    }
}
```

A. 访问 s1 接口，[http://localhost:8080/s1](http://localhost:8080/s1)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865532-999837ad-44ff-49cb-b798-21781d337e2b.png "null")

请求完成之后，在响应头中，就会看到有一个Set-Cookie的响应头，里面响应回来了一个Cookie，就是JSESSIONID，这个就是服务端会话对象 Session 的ID。

B. 访问 s2 接口，[http://localhost:8080/s2](http://localhost:8080/s2)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865600-7336b167-a101-4429-b4ca-3e0f047ed909.png "null")

接下来，在后续的每次请求时，都会将Cookie的值，携带到服务端，那服务端呢，接收到Cookie之后，会自动的根据JSESSIONID的值，找到对应的会话对象Session。

那经过这两步测试，大家也会看到，在控制台中输出如下日志：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865677-8274db3d-1e8e-4e65-8cba-ee720e60dff7.png "null")

两次请求，获取到的Session会话对象的hashcode是一样的，就说明是同一个会话对象。而且，第一次请求时，往Session会话对象中存储的值，第二次请求时，也获取到了。 那这样，我们就可以通过Session会话对象，在同一个会话的多次请求之间来进行数据共享了。

**优缺点**

- 优点：Session是存储在服务端的，安全

- 缺点：

- 服务器集群环境下无法直接使用Session

- 移动端APP(Android、IOS)中无法使用Cookie

- 用户可以自己禁用Cookie

- Cookie不能跨域

PS：Session 底层是基于Cookie实现的会话跟踪，如果Cookie不可用，则该方案，也就失效了。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865747-47c9e424-5991-46df-b1af-72496063b4bd.png "null")

服务器集群环境为何无法使用Session？（在负载均衡服务器中，访问到的服务器不是一致的，获取到的不是同一个会话对象）

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866660-9eea909f-9265-45fd-ae7b-c8f5c4f15551.png)

- 首先第一点，我们现在所开发的项目，一般都不会只部署在一台服务器上，因为一台服务器会存在一个很大的问题，就是单点故障。所谓单点故障，指的就是一旦这台服务器挂了，整个应用都没法访问了。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865822-07287f7c-ca9e-4bd3-9399-968936e14db8.png "null")

- 所以在现在的企业项目开发当中，最终部署的时候都是以集群的形式来进行部署，也就是同一个项目它会部署多份。比如这个项目我们现在就部署了 3 份。

- 而用户在访问的时候，到底访问这三台其中的哪一台？其实用户在访问的时候，他会访问一台前置的服务器，我们叫负载均衡服务器，我们在后面项目当中会详细讲解。目前大家先有一个印象负载均衡服务器，它的作用就是将前端发起的请求均匀的分发给后面的这三台服务器。![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865899-a27ec961-ad86-42cf-93f2-2a0b6bde0fef.png "null")

- 此时假如我们通过 session 来进行会话跟踪，可能就会存在这样一个问题。用户打开浏览器要进行登录操作，此时会发起登录请求。登录请求到达负载均衡服务器，将这个请求转给了第一台 Tomcat 服务器。Tomcat 服务器接收到请求之后，要获取到会话对象session。获取到会话对象 session 之后，要给浏览器响应数据，最终在给浏览器响应数据的时候，就会携带这么一个 cookie 的名字，就是 JSESSIONID ，下一次再请求的时候，是不是又会将 Cookie 携带到服务端？好。此时假如又执行了一次查询操作，要查询部门的数据。这次请求到达负载均衡服务器之后，负载均衡服务器将这次请求转给了第二台 Tomcat 服务器，此时他就要到第二台 Tomcat 服务器当中。根据JSESSIONID 也就是对应的 session 的 ID 值，要找对应的 session 会话对象。我想请问在第二台服务器当中有没有这个ID的会话对象 Session， 是没有的。此时是不是就出现问题了？我同一个浏览器发起了 2 次请求，结果获取到的不是同一个会话对象，这就是Session这种会话跟踪方案它的缺点，在服务器集群环境下无法直接使用Session。

服务端使用了 session 技术来暂存数据

存

```
GET /s1?name=zhang HTTP/1.1
Host: localhost
```

取

```
GET /s2 HTTP/1.1
Host: localhost
Cookie: JSESSIONID=560FA845D02AE09B176E1BC5D9816A5D
```

每次请求会根据用户信息（有无）创建session对象，并生成唯一的id，返回给用户端，

下一次请求会携带这个id访问，帮助服务器定位

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432865974-59878948-67a2-4b45-b7d0-a8df9cd678c4.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866079-8bd91183-e402-46d6-bc08-46380c58ca5c.png "null")

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866143-d31377b5-e1bd-4b03-9074-5685e530dcf8.png "null")

session 技术实现身份验证

sequenceDiagram  
participant Client  
participant L as LoginController  
participant i as LoginInterceptor  
participant Session  
rect rgb(200, 223, 255)  
Client ->> +L : 登录请求  
L ->> L : 检查用户名，密码，验证通过  
L ->> +Session : 存入用户名  
Session -->> -L:   
L -->> -Client: 登录成功  
end  
rect rgb(200, 190, 255)  
Client ->> +i : 其它请求  
i ->> +Session : 获取用户名  
Session -->> -i :   
i ->> i: 用户名存在，放行  
i -->> -Client :   
end

### jwt 原理【分布式】

WT全称：JSON Web Token （官网：[https://jwt.io/）](https://jwt.io/）)

- 定义了一种**简洁的、自包含的格式**，用于在通信双方**以json数据格式**安全的传输信息。由于**数字签名**的存在，这些信息是可靠的。

简洁：是指jwt就是一个简单的字符串。可以在请求参数或者是请求头当中直接传递。

自包含：指的是jwt令牌，看似是一个随机的字符串，但是我们是可以根据自身的需求在jwt令牌中存储自定义的数据内容。如：**可以直接在jwt令牌中存储用户的相关信息。**

简单来讲，jwt就是将原始的json数据格式进行了安全的封装，这样就可以直接基于jwt在通信双方安全的进行信息传输了。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866217-c96e6bfc-cd21-4197-9af0-60f6f2b201dc.png "null")

JWT的组成： （JWT令牌由三个部分组成，三个部分之间使用英文的点来分割）

- 第一部分：Header(头）， 记录令牌类型、签名算法等。 例如：{"alg":"HS256","type":"JWT"}

- 第二部分：Payload(有效载荷），携带一些自定义信息、默认信息等。 例如：{"id":"1","username":"Tom"}

- 第三部分：Signature(签名），防止Token被篡改、确保安全性。将header、payload融入，并加入指定秘钥，通过指定签名算法计算而来。

签名的目的就是为了防jwt令牌被篡改，而正是因为jwt令牌最后一个部分数字签名的存在，所以整个jwt 令牌是非常安全可靠的。一旦jwt令牌当中任何一个部分、任何一个字符被篡改了，整个令牌在校验的时候都会失败，所以它是非常安全可靠的。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866303-570456f0-dfa5-490c-981c-b183c2921bc3.png "null")

JWT是如何将原始的JSON格式数据，转变为字符串的呢？

其实在生成JWT令牌时，**会对JSON格式的数据进行一次编码：进行base64编码**

Base64：是一种基于64个可打印的字符来表示二进制数据的编码方式。既然能编码，那也就意味着也能解码。所使用的64个字符分别是A到Z、a到z、 0- 9，一个加号，一个斜杠，加起来就是64个字符。任何数据经过base64编码之后，最终就会通过这64个字符来表示。当然还有一个符号，那就是等号。等号它是一个补位的符号

**需要注意的是Base64是编码方式，而不是加密方式。**

**jwt 技术实现身份验证**

sequenceDiagram  
participant Client  
participant L as LoginController  
participant i as LoginInterceptor  
  
rect rgb(200, 223, 255)  
Client ->> +L : 登录请求  
L ->> L : 检查用户名，密码，验证通过  
L -->> -Client : 登录成功，返回token  
end  
  
rect rgb(150, 190, 155)  
Client ->> +i : 其它请求，携带token  
i ->> i : 校验token，校验无误，放行  
i -->> -Client :   
end

生成 token

```
GET /j1?name=zhang&pass=123 HTTP/1.1
Host: localhost
```

校验 token

```
GET /j2 HTTP/1.1
Host: localhost
Authorization: eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJhZG1pbiJ9._1-P_TLlzQPb1_lCyGwplMZaKQ8Mcw_plBbYPZ3OX28
```

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866376-a2bbda47-cfde-4fd6-b90c-8d19c7189583.png "null")

token详解：

前俩个片段是json数据，无加密，可以进行解码

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866475-6278a369-db95-455e-ab44-e7e1a56d62c7.png "null")

防止篡改

前俩部分和服务器的秘钥加密算法生成签名，

可以根据对比生成的签名

**jwt 和session的区别**  
JWT（JSON Web Token）和会话（Session）是用于在Web应用程序中管理用户身份验证和状态的两种不同的机制，它们有一些重要的区别：

1. **存储位置**:

- JWT: JWT是一种无状态的身份验证机制，它将用户的身份验证信息（例如用户ID、权限等）存储在加密的令牌中，并将该令牌发送给客户端。客户端在之后的请求中将该令牌发送给服务器，服务器解析令牌并验证用户的身份。

- 会话: 会话是一种有状态的机制，它将用户的状态信息（例如用户ID、会话ID、权限等）存储在服务器端。服务器在会话中维护用户的状态，并将会话标识符（session ID）发送给客户端。客户端在每个请求中将会话标识符发送给服务器，服务器使用该标识符来检索和更新用户的状态信息。

2. **存储方式**:

- JWT: JWT令牌是基于JSON格式的数据结构，并且通常是使用Base64编码和签名算法进行加密的。因此，JWT令牌可以存储在客户端的Cookie中或通过其他方式存储在客户端的本地存储中。

- 会话: 会话数据通常存储在服务器的内存中或持久化到数据库或文件系统中。服务器根据会话标识符来管理和检索会话数据。

3. **状态管理**:

- JWT: JWT是无状态的，服务器不需要在内存中维护任何会话状态。所有的用户身份验证信息都包含在JWT令牌中，并且客户端负责将令牌发送到服务器以进行验证。

- 会话: 会话是有状态的，服务器需要在内存或持久化存储中维护会话数据。服务器使用会话标识符来识别和关联用户的请求，并根据需要更新会话数据。

4. **适用场景**:

- JWT: 适用于无状态的API认证和跨域认证等场景，特别是在微服务架构中更为常见。

- 会话: 适用于需要在服务器端维护用户状态的传统Web应用程序，例如基于浏览器的Web应用程序。

总的来说，JWT和会话都是用于在Web应用程序中管理用户身份验证和状态的机制，它们各自具有不同的特点和适用场景。选择JWT还是会话取决于应用程序的需求、架构和安全考虑等因素。

### 总结

|   |   |   |   |   |
|---|---|---|---|---|
|会话技术|存储位置|生命周期|安全性|大小限制|
|**Cookie**|客户端（浏览器）|可设置过期时间，如果不设置，生命周期为浏览器会话期间|可以被用户编辑或伪造，相对不安全|Cookie的大小上限为4KB|
|**Session**|服务器|一般情况下，当用户关闭浏览器时，Session就会失效|相对较安全，因为数据存储在服务器端|一般没有大小限制|
|**JWT**|客户端（浏览器）|可设置过期时间，如果不设置，生命周期为浏览器会话期间|相对较安全，因为 JWT 是数字签名的|一般没有大小限制|

## 4）跨域

跨域介绍：

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866769-cec49ea6-b148-4245-bec9-247b0c19c7c8.png)

- 现在的项目，大部分都是前后端分离的，前后端最终也会分开部署，前端部署在服务器 192.168.150.200 上，端口 80，后端部署在 192.168.150.100上，端口 8080

- 我们打开浏览器直接访问前端工程，访问url：[http://192.168.150.200/login.html](http://192.168.150.200/login.html)

- 然后在该页面发起请求到服务端，而服务端所在地址不再是localhost，而是服务器的IP地址192.168.150.100，假设访问接口地址为：[http://192.168.150.100:8080/login](http://192.168.150.100:8080/login)

- 那此时就存在跨域操作了，因为我们是在 [http://192.168.150.200/login.html](http://192.168.150.200/login.html) 这个页面上访问了[http://192.168.150.100:8080/login](http://192.168.150.100:8080/login) 接口

- 此时如果服务器设置了一个Cookie，这个Cookie是不能使用的，因为Cookie无法跨域

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1739432866586-93e1b351-3954-44c3-bffd-4ae25c70aa29.png "null")

区分跨域的维度：

- 协议

- IP/协议

- 端口

只要上述的三个维度有任何一个维度不同，那就是跨域操作

举例：

[http://192.168.150.200/login.html](http://192.168.150.200/login.html) ----------> [https://192.168.150.200/login](https://192.168.150.200/login) [协议不同，跨域]

[http://192.168.150.200/login.html](http://192.168.150.200/login.html) ----------> [http://192.168.150.100/login](http://192.168.150.100/login) [IP不同，跨域]

[http://192.168.150.200/login.html](http://192.168.150.200/login.html) ----------> [http://192.168.150.200:8080/login](http://192.168.150.200:8080/login) [端口不同，跨域]

[http://192.168.150.200/login.html](http://192.168.150.200/login.html) ----------> [http://192.168.150.200/login](http://192.168.150.200/login) [不跨域]

## 拓展

`param` 和 `query` 是前后端开发中用于从请求中获取数据的两种常见方式，分别指代 **路径参数** 和 **查询参数**。它们的区别主要在于 URL 中数据的传递方式。

在后端开发中，`param` 和 `query` 通常用来指代 URL 请求中的两种传参方式：

---

### 1. **Path Param (路径参数)**

- **概念**：路径参数是 URL 路径中的一部分，通常用来标识资源。

- 特点：

- 参数值嵌入到 URL 的路径中。

- 更直观且适用于 RESTful API 中的资源标识。

- 示例：

```
GET /users/{id}
```

如果

```
id=123
```

，请求 URL 可能是：

```
GET /users/123
```

- 优点：

- 更符合 RESTful 设计。

- 表意清晰，参数是资源的一部分。

- 适用场景：

- 资源标识，例如用户 ID、产品 ID 等。
- 查一个具体资源（如某个订单）

---

### 2. **Query Param (查询参数)**

- **概念**：查询参数是 URL 路径后以 `?` 开始的键值对，多个参数用 `&` 分隔。

- 特点：

- 用于传递非必须的、附加的信息。

- 不影响资源路径。

- 示例：

```
GET /users?id=123&sort=asc
```

- 优点：

- 灵活性高，适合可选参数或过滤条件。

- 易于扩展，支持多个参数。

- 适用场景：

- 筛选条件、分页参数、排序规则等。

---

### 对比总结：

|   |   |   |
|---|---|---|
|**特性**|**Path Param**|**Query Param**|
|**位置**|URL 路径的一部分|URL 的 `?` 后面|
|**用途**|标识资源|传递可选条件或附加数据|
|**格式**|`/resource/{param}`|`?key=value&key2=value2`|
|**RESTful 风格**|更符合 RESTful 设计|较适合动态参数|
|**适合场景**|资源 ID|筛选条件、分页、搜索参数|

---

### **使用建议**：

1. 标识性资源用 Path Param，例如：

```
GET /orders/{order_id}
```

2. 非必要参数用 Query Param，例如：

```
GET /products?category=clothes&price_range=100-200
```

这样设计会让你的 API 更具可读性和易用性。