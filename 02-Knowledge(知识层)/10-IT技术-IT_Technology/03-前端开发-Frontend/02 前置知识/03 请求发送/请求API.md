**- `**XMLHttpRequest**`：

- **回调函数**：通过 `onload`、`onerror` 等回调函数处理请求结果。
- **缺点**：代码冗长，容易产生回调地狱，缺乏直接的错误处理机制。
- **低级别 API**：需要手动处理请求的生命周期，适用范围较广，但代码复杂。

- `**Promise**`：【异步】

- **异步操作**：`Promise` 提供了异步操作的更优雅方式，避免了回调地狱。
- **链式调用**：`.then()` 和 `.catch()` 方法使得代码更加简洁和可维护。
- **状态**：三种状态：`pending`（待定）、`fulfilled`（已成功）、`rejected`（已失败）。

- `**Fetch API**`：

- **基于** `**Promise**`：`Fetch` 是基于 `Promise` 的现代化接口，简化了 `XMLHttpRequest` 的操作。
- **缺点**：需要手动检查 HTTP 错误（如 404、500），默认不会抛出异常。
- **响应解析**：`Fetch` 需要开发者手动解析响应数据（如 `.json()`）。

- `**Axios**`：⭐

- **封装** `**Fetch**` **和** `**XMLHttpRequest**`：`Axios` 封装了复杂的请求和响应处理。
- **自动解析 JSON**：返回的响应会自动解析为 JSON 对象，减少了开发者的操作。
- **请求拦截器和响应拦截器**：可以在请求和响应阶段进行处理，如统一处理错误、设置请求头等。
- **并发请求**：`Axios` 支持并发请求，通过 `axios.all()` 进行多个请求的并行处理。

## `XMLHttpRequest` (XHR)

`XMLHttpRequest`（简称 `XHR`）是浏览器内置的一个 JavaScript API，用于在不重新加载整个页面的情况下，与服务器进行交互。它是 Ajax 技术的核心之一，广泛应用于动态加载数据和进行异步请求。虽然现在 `Fetch API` 提供了更简洁和现代化的方式来处理 HTTP 请求，但 `XMLHttpRequest` 依然被一些旧的应用和兼容性要求所使用。

### **核心特点：**

1. **异步操作**：

- `XMLHttpRequest` 支持异步和同步请求，默认情况下是异步的。
- 异步请求允许浏览器继续处理用户交互，而不阻塞 UI 线程。

2. **回调函数**：

- 由于是异步请求，`XMLHttpRequest` 使用回调函数（如 `onload`、`onreadystatechange` 等）来处理请求的结果。
- 开发者需要处理 `onload`（请求成功）、`onerror`（请求失败）等回调。

3. **请求状态**：

- `XMLHttpRequest` 请求有 5 个不同的状态，具体为：

- **0 (UNSENT)**: 请求未初始化。
- **1 (OPENED)**: 已调用 `open()`，但未发送请求。
- **2 (HEADERS_RECEIVED)**: 收到响应头。
- **3 (LOADING)**: 正在接收响应体。
- **4 (DONE)**: 请求完成，响应已返回。

4. **同步与异步**：

- **异步请求**：最常用的方式，浏览器会在后台发起请求，UI 可以继续交互。
- **同步请求**：阻塞浏览器，直到请求完成才会继续执行后续代码，不推荐使用，因为它会导致界面冻结。

5. **支持各种 HTTP 请求方法**：

- 支持 `GET`、`POST`、`PUT`、`DELETE`、`PATCH` 等 HTTP 请求方法。

### **基本使用方法：**

1. **创建** `**XMLHttpRequest**` **实例**：

```
const xhr = new XMLHttpRequest();
```

2. **初始化请求**： 使用 `open()` 方法初始化请求，指定请求方法和 URL：

```
xhr.open('GET', 'https://api.example.com/data', true);  // 第三个参数为 true 表示异步请求
```

3. **设置请求头（可选）**： 可以通过 `setRequestHeader()` 方法设置请求头，例如设置 `Content-Type`：

```
xhr.setRequestHeader('Content-Type', 'application/json');
```

4. **定义回调函数**： 使用 `onreadystatechange` 或 `onload` 来指定回调函数，在请求完成后执行：

```
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4 && xhr.status === 200) {
    const data = JSON.parse(xhr.responseText); // 解析响应数据
    console.log(data);
  }
};
```

5. **发送请求**： 使用 `send()` 方法发送请求。对于 `GET` 请求，不需要传递参数；对于 `POST` 请求，可以传递数据：

```
xhr.send();
```

对于 `POST` 请求：

```
const data = JSON.stringify({ key: 'value' });
xhr.send(data);
```

### **完整示例：**

```
const xhr = new XMLHttpRequest();
xhr.open('GET', 'https://api.example.com/data', true);  // 异步请求

// 设置请求头（可选）
xhr.setRequestHeader('Accept', 'application/json');

// 定义请求完成后的回调
xhr.onreadystatechange = function() {
  if (xhr.readyState === 4) {
    if (xhr.status === 200) {
      const data = JSON.parse(xhr.responseText);
      console.log(data);  // 处理成功的响应数据
    } else {
      console.error('Request failed with status', xhr.status);  // 错误处理
    }
  }
};

// 发送请求


xhr.send();
```

### **常见属性和方法：**

1. **属性**：

- `xhr.readyState`：表示请求的状态。
- `xhr.status`：响应的 HTTP 状态码（如 200 表示成功，404 表示找不到资源）。
- `xhr.responseText`：响应的文本数据。
- `xhr.responseXML`：响应的 XML 数据（如果响应是 XML 格式）。
- `xhr.statusText`：响应的状态文本（如 "OK"）。
- `xhr.responseType`：指定响应的类型，如 `'json'`、`'text'` 等。

2. **方法**：

- `xhr.open(method, url, async)`：初始化请求，指定 HTTP 方法、URL 和是否异步。
- `xhr.setRequestHeader(header, value)`：设置请求头。
- `xhr.send(data)`：发送请求数据。
- `xhr.abort()`：中止请求。

### **回调事件**：

- `onreadystatechange`：每次 `readyState` 改变时都会触发，用于跟踪请求的状态变化。
- `onload`：请求成功完成时触发。
- `onerror`：请求失败时触发（如网络错误）。
- `onprogress`：可以用于跟踪请求进度。
- `ontimeout`：请求超时时触发。

### **优缺点：**

#### 优点：

- **广泛兼容**：几乎所有浏览器都支持 `XMLHttpRequest`。
- **灵活性高**：可以用于处理复杂的 HTTP 请求，支持多种请求方法、请求头、响应类型等。

#### 缺点：

- **回调地狱**：多次嵌套的回调函数使得代码复杂且难以维护。
- **API 繁琐**：需要手动处理很多细节（如解析响应、处理错误等），代码比较冗长。
- **不支持流式处理**：相较于 `Fetch API`，`XMLHttpRequest` 对流处理的支持较差。

### **总结**：

虽然 `XMLHttpRequest` 是早期前端开发中进行 HTTP 请求的主要方式，但它的代码冗长和回调地狱问题在现代 JavaScript 开发中被 `Promise` 和 `Fetch API` 取代。即使如此，`XMLHttpRequest` 仍然是许多遗留系统中的常见工具，且在浏览器兼容性方面具有优势。

## Promise API

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1736676927546-a01ab473-837e-4e07-b205-734647c03fd8.png)

在 JavaScript 中，**Promise** 是一个用于处理异步操作的对象，它代表了一个可能还未完成的操作的结果。通过 Promise，JavaScript 可以更清晰地处理异步操作，避免传统回调函数的“回调地狱”问题。Promise 是 ES6（ECMAScript 2015）引入的标准。

### Promise 的基本概念

一个 **Promise** 对象表示一个异步操作的最终完成（或失败）及其结果值。一个 Promise 对象有三种状态：

1. **Pending（等待中）**：初始状态，表示异步操作还没有完成。
2. **Resolved/Fulfilled（已完成）**：表示异步操作成功完成，且提供了结果。
3. **Rejected（已拒绝）**：表示异步操作失败，且提供了原因（错误信息）。

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1736677036525-10521095-704d-440f-9706-c06ff14a20c0.png)

### Promise 的基本用法

#### 1. 创建一个 Promise 对象

```
let promise = new Promise((resolve, reject) => {
  let success = true; // 模拟成功或失败的条件

  if (success) {
    resolve("操作成功！");  // 成功时执行 then接受
  } else {
    reject("操作失败！");   // 失败时执行 catch接受
  }
});
```

#### 2. 使用 `.then()` 处理成功和失败的回调

`then()` 方法用于指定成功和失败的回调函数。它返回一个新的 Promise，因此你可以链式调用多个 `.then()`。

```
promise
  .then(result => {
    console.log(result); // 成功时的处理逻辑
  })
  .catch(error => {
    console.log(error);  // 失败时的处理逻辑
  });
```

#### 3. `.then()` 链式调用

可以解决回调地狱

Promise 的 `.then()` 方法是链式调用的，它会在当前 Promise 被处理（fulfilled 或 rejected）后，返回一个新的 Promise。

```
promise
  .then(result => {
    console.log(result); // 操作成功，打印成功消息
    return "继续操作";   // 返回一个新的值
  })
  .then(newResult => {
    console.log(newResult); // 打印 "继续操作"
  })
  .catch(error => {
    console.log(error);  // 错误处理
  });
```

#### 4. 使用 `.catch()` 捕获错误

如果在链中的任何一个 Promise 被拒绝，或者抛出错误，`.catch()` 将会捕获并处理这个错误。

```
let anotherPromise = new Promise((resolve, reject) => {
  reject("发生错误！");
});

anotherPromise
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.error(error);  // 捕获错误
  });
```

#### 5. 使用 `.finally()` 方法

`finally()` 方法用于指定无论操作成功还是失败都会执行的回调。它通常用于清理工作，比如关闭加载指示器等。

```
promise
  .then(result => {
    console.log(result);
  })
  .catch(error => {
    console.log(error);
  })
  .finally(() => {
    console.log("无论成功还是失败，都会执行");
  });
```

### 回调函数地狱⭐

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1736677789652-de1c17e1-55a7-4bd2-b973-4231ea82cdda.png)

#### promise`.then()` 链式调用

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1736677997386-573174e5-6112-45b3-a23a-0cef817cbc39.png)

#### async 函数和 await

- async进行函数声明
- await 等待 请求结果
- **使用try catch 捕获 错误**

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1736678401643-249ec9fa-9d2a-45fb-b788-088b73953172.png)

![](https://cdn.nlark.com/yuque/0/2025/png/40487410/1736678612480-f734f986-496e-4af4-8946-dd6ccbb9849a.png)

### 总结

- **Promise** 使得异步操作的代码更加清晰和易于管理，避免了回调函数的嵌套和“回调地狱”问题。
- `**then()**` 用于处理成功的结果，`**catch()**` 用于捕获错误，`**finally()**` 用于执行清理任务。
- 静态方法如 `**Promise.all()**`、`**Promise.race()**`、`**Promise.allSettled()**` 和 `**Promise.any()**` 提供了处理多个 Promise 的便利。

Promise 是现代 JavaScript 中非常重要的异步编程工具，它支持链式调用、错误处理和多 Promise 操作，广泛应用于 AJAX 请求、定时任务等场景。

## fetch API

`Fetch API` 是现代 JavaScript 提供的一个用于进行网络请求的接口，它替代了传统的 `XMLHttpRequest`，提供了更简单、更强大、更灵活的功能。`fetch` 是基于 Promise 的，因此它支持链式调用和异步操作，使得处理异步请求更加简洁和易于理解。

### 1. 基本语法

`fetch` 方法的基本语法如下：

```
fetch(url, options)
  .then(response => response.json())  // 解析 JSON 响应
  .then(data => console.log(data))    // 使用响应数据
  .catch(error => console.error('Error:', error)); // 错误处理
```

- `**url**`：请求的 URL 地址。
- `**options**`（可选）：配置对象，用于指定请求的方法、请求头、请求体等。

`fetch` 默认使用 `GET` 方法，因此如果你只是进行简单的 GET 请求，可以只传入 URL 参数；如果是其他 HTTP 方法（如 `POST`、`PUT`、`DELETE` 等），则需要传入 `options` 配置。

### 2. 主要参数和配置

`fetch` 方法接收两个参数：

1. `**url**`：请求的 URL，必须。
2. `**options**`：请求的配置对象，包含以下常用属性：

- `**method**`：指定 HTTP 请求的方法（如 `GET`、`POST`、`PUT`、`DELETE` 等）。
- `**headers**`：指定请求的头部信息（如 `Content-Type`、`Authorization` 等）。
- `**body**`：发送的请求体，通常在 `POST` 或 `PUT` 请求中使用。
- `**mode**`：设置跨域请求的模式，通常使用 `cors`、`no-cors` 或 `same-origin`。
- `**credentials**`：设置请求时是否携带凭证（cookies），可以是 `same-origin`、`include` 或 `omit`。
- `**cache**`：指定缓存模式（如 `default`、`no-store` 等）。

#### 示例：使用 POST 请求发送数据

```
fetch('https://example.com/api', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({
    username: 'user1',
    password: 'password123',
  }),
})
  .then(response => response.json())  // 解析 JSON 响应
  .then(data => console.log(data))    // 使用返回的数据
  .catch(error => console.error('Error:', error)); // 错误处理
```

### 3. 处理响应

`fetch` 返回的是一个 `**Promise**`，它会解析服务器的响应。当请求完成时，返回的 `Promise` 会返回一个 `Response` 对象。你可以使用该对象的方法来获取响应数据。

- `**response.json()**`：解析响应体为 JSON 对象。
- `**response.text()**`：解析响应体为字符串。
- `**response.blob()**`：解析响应体为 Blob 对象，适用于图片、文件等。
- `**response.formData()**`：解析响应体为 `FormData` 对象。

例如，解析 JSON 响应：

```
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {
      throw new Error('Network response was not ok');
    }
    return response.json();  // 解析为 JSON
  })
  .then(data => console.log(data))
  .catch(error => console.error('Fetch error:', error));
```

### 4. 错误处理

`fetch` 只会在网络错误或请求无法完成时（例如：无法连接到服务器）触发 `catch`，它不会因 HTTP 错误状态（如 404 或 500）而触发 `catch`。因此，你需要显式地检查响应的 `status` 字段，判断请求是否成功。

```
fetch('https://api.example.com/data')
  .then(response => {
    if (!response.ok) {  // 如果响应状态码不是 200-299，抛出错误
      throw new Error('Request failed with status ' + response.status);
    }
    return response.json();
  })
  .then(data => console.log(data))
  .catch(error => console.error('Fetch error:', error));
```

### 5. 使用 `async/await`

由于 `fetch` 返回一个 Promise，可以结合 `async/await` 使用，使得代码更加简洁和易读。

#### 示例：使用 `async/await` 获取数据

```
async function fetchData() {
  try {
    const response = await fetch('https://api.example.com/data');
    
    if (!response.ok) {  // 检查响应状态码
      throw new Error('Network response was not ok');
    }
    
    const data = await response.json();  // 解析 JSON 响应
    console.log(data);
  } catch (error) {
    console.error('Fetch error:', error);
  }
}

fetchData();
```

### 6. `fetch` 与跨域请求（CORS）

`fetch` 支持跨域请求（CORS，Cross-Origin Resource Sharing）。如果你需要跨域访问其他服务器的资源，确保服务器端支持 CORS，并在请求中设置 `mode` 属性为 `cors`。

例如，进行跨域请求：

```
fetch('https://api.example.com/data', {
  method: 'GET',
  mode: 'cors',  // 开启跨域请求
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Fetch error:', error));
```

### 7. `fetch` 的其他常用功能

- **设置请求头（Headers）**：使用 `headers` 属性可以设置请求头。例如，设置 `Authorization` 头来进行身份验证。

```
fetch('https://api.example.com/data', {
  method: 'GET',
  headers: {
    'Authorization': 'Bearer your_token_here',
  },
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Fetch error:', error));
```

- **设置请求体（Body）**：使用 `body` 属性可以发送数据。在 `POST` 或 `PUT` 请求中通常使用 `body`，它可以是 JSON、`FormData` 或其他类型的内容。

```
fetch('https://api.example.com/data', {
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
  },
  body: JSON.stringify({ key: 'value' }),
})
  .then(response => response.json())
  .then(data => console.log(data))
  .catch(error => console.error('Fetch error:', error));
```

### 8. 总结

- `**fetch**` 是一种基于 Promise 的现代方法，用于处理 HTTP 请求，比传统的 `XMLHttpRequest` 更简洁、更强大。
- `fetch` 默认执行 **GET** 请求，支持所有 HTTP 方法（如 POST、PUT、DELETE 等）。
- `fetch` 支持 **JSON**、**text**、**blob** 等不同类型的响应处理。
- 与 `async/await` 配合使用时，代码更加简洁和易于理解。
- 需要注意，`fetch` 不会自动处理 HTTP 错误状态码，需要手动检查响应的状态。

`fetch` 是一个非常强大的工具，广泛用于现代 Web 开发中处理网络请求。如果你正在进行前端开发，它将是你处理异步操作的首选方法之一。

## Axios API

`Axios` 是一个基于 **Promise** 的 HTTP 客户端，用于浏览器和 Node.js 中发送 HTTP 请求。它提供了比原生的 `fetch` 更加丰富和简便的功能，且拥有对请求和响应的拦截器、请求取消、请求超时、并发请求等高级特性，因此广泛应用于前端开发中。

### 1. 安装 Axios

如果你使用的是 **Node.js** 环境或前端框架（如 React、Vue），可以通过以下方式安装 `axios`：

- **NPM 安装**

```
npm install axios
```

- **Yarn 安装**

```
yarn add axios
```

### 2. 基本用法

`Axios` 用法非常简单，可以使用它发送常见的 HTTP 请求（如 `GET`、`POST`、`PUT`、`DELETE` 等）。下面是一些常见的示例：

#### 发送 GET 请求

```
const axios = require('axios'); // 如果是 Node.js 中使用，前端直接在 script 标签引入即可

axios.get('https://api.example.com/data')
  .then(response => {
    console.log(response.data);  // 服务器返回的数据
  })
  .catch(error => {
    console.error('Error:', error);  // 错误处理
  });
```

#### 发送 POST 请求

```
axios.post('https://api.example.com/data', {
  username: 'user1',
  password: 'password123',
})
  .then(response => {
    console.log(response.data);  // 服务器返回的数据
  })
  .catch(error => {
    console.error('Error:', error);  // 错误处理
  });
```

### 3. 请求配置

`Axios` 提供了丰富的配置选项，允许你在发送请求时自定义请求头、请求超时、响应类型等。

```
axios({
  method: 'get',
  url: 'https://api.example.com/data',
  headers: {
    'Authorization': 'Bearer your_token_here',
  },
  timeout: 5000,  // 设置请求超时时间，单位是毫秒
})
  .then(response => {
    console.log(response.data);  // 服务器返回的数据
  })
  .catch(error => {
    console.error('Error:', error);  // 错误处理
  });
```

### 4. 响应处理

`Axios` 的响应对象包含以下几个重要属性：

- `**data**`：响应体中的数据。
- `**status**`：HTTP 状态码。
- `**statusText**`：HTTP 状态文本。
- `**headers**`：响应头。
- `**config**`：请求的配置。
- `**request**`：原生的请求对象。

例如：

```
axios.get('https://api.example.com/data')
  .then(response => {
    console.log('Response data:', response.data);  // 返回的数据
    console.log('HTTP Status:', response.status);  // 返回的状态码
    console.log('Response Headers:', response.headers);  // 返回的响应头
  })
  .catch(error => {
    console.error('Error:', error);  // 错误处理
  });
```

### 5. 错误处理

`Axios` 的错误处理非常强大，可以根据错误类型做出相应的处理。常见的错误类型包括网络错误、请求超时、服务器错误等。

```
axios.get('https://api.example.com/data')
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    if (error.response) {
      // 服务器返回了状态码，但状态码超出了 2xx 的范围
      console.error('Response Error:', error.response.data);
    } else if (error.request) {
      // 请求已发出，但没有收到响应
      console.error('Request Error:', error.request);
    } else {
      // 其他错误
      console.error('Error:', error.message);
    }
  });
```

### 6. 使用 `async/await`

`Axios` 完全支持 `async/await`，让异步代码看起来像同步代码一样简洁易读。

```
async function fetchData() {
  try {
    const response = await axios.get('https://api.example.com/data');
    console.log(response.data);
  } catch (error) {
    console.error('Error:', error);
  }
}

fetchData();
```

### 7. 请求和响应拦截器

`Axios` 支持 **请求拦截器**和 **响应拦截器**，可以在请求发送之前和接收到响应之后对请求或响应进行处理。这对于添加认证令牌、日志记录、错误处理等非常有用。

#### 请求拦截器

```
axios.interceptors.request.use(
  config => {
    // 在发送请求之前做一些处理
    console.log('Request Interceptor:', config);
    config.headers['Authorization'] = 'Bearer your_token';
    return config;
  },
  error => {
    // 请求错误处理
    return Promise.reject(error);
  }
);
```

#### 响应拦截器

```
axios.interceptors.response.use(
  response => {
    // 对响应数据做一些处理
    console.log('Response Interceptor:', response);
    return response;
  },
  error => {
    // 响应错误处理
    console.error('Response Error:', error);
    return Promise.reject(error);
  }
);
```

### 8. 并发请求

`Axios` 提供了 `axios.all()` 和 `axios.spread()` 方法来并行发送多个请求，并在所有请求完成后一起处理它们。

```
axios.all([
  axios.get('https://api.example.com/data1'),
  axios.get('https://api.example.com/data2'),
])
  .then(axios.spread((response1, response2) => {
    console.log('Response 1:', response1.data);
    console.log('Response 2:', response2.data);
  }))
  .catch(error => {
    console.error('Error:', error);
  });
```

### 9. 请求取消

`Axios` 支持取消请求，通过使用 `CancelToken`。

```
const CancelToken = axios.CancelToken;
let cancel;

axios.get('https://api.example.com/data', {
  cancelToken: new CancelToken(function executor(c) {
    cancel = c;  // 保存取消请求的方法
  })
})
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    if (axios.isCancel(error)) {
      console.log('Request canceled:', error.message);
    } else {
      console.error('Error:', error);
    }
  });

// 取消请求
cancel('Request canceled by user.');
```

### 10. 设置默认配置

你可以为所有的请求设置默认配置，避免重复配置每个请求。

```
axios.defaults.baseURL = 'https://api.example.com';
axios.defaults.timeout = 5000;
axios.defaults.headers['Authorization'] = 'Bearer your_token';
```

### 11. 请求超时

你可以设置请求的超时时间（单位：毫秒），超过这个时间，`Axios` 会自动中止请求。

```
axios.get('https://api.example.com/data', {
  timeout: 1000  // 设置请求超时时间为 1 秒
})
  .then(response => {
    console.log(response.data);
  })
  .catch(error => {
    if (error.code === 'ECONNABORTED') {
      console.error('Request timeout');
    } else {
      console.error('Error:', error);
    }
  });
```

### 12. 其他高级功能

- **自定义请求头**
- **设置请求基础路径 (**`**baseURL**`**)**
- **处理跨域请求（CORS）**
- **上传文件**

### 总结

`Axios` 是一个功能强大的 HTTP 客户端，提供了比原生 `fetch` 更多的功能，如请求拦截、响应拦截、请求取消、并发请求等。它简单易用，且能够轻松处理 HTTP 请求中的各种复杂场景。

如果你需要更复杂的 HTTP 请求操作，或者需要更细粒度的错误处理、拦截等功能，`Axios` 无疑是一个更好的选择。**