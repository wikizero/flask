
### Vue 基础
- Vue是响应式的；
-  v-bind : 绑定元素特性，元素节点的特性有title、attr、src等；
```html
<div id="app-2">
  <input v-bind:value="message">
</div>

<script>
    var app = new Vue({
        el: '#app-2',
        data: {
            message: 'Value:' + new Date().toLocaleString()
        }
    })
</script>
```

- v-if 、v-else-if、 v-else

```html
<div id="app">
  <p v-if="seen">现在你看到我了</p>
</div>

var app = new Vue({
  el: '#app',
  data: {
    seen: true
  }
})
```

- v-for 
```html
<div id="app-4">
  <ol>
    <li v-for="todo in todos">
      {{ todo.text }}
    </li>
  </ol>
</div>

var app4 = new Vue({
  el: '#app-4',
  data: {
    todos: [
      { text: '学习 JavaScript' },
      { text: '学习 Vue' },
      { text: '整个牛项目' }
    ]
  }
})
```

- v-on 添加事件监听器，事件包括很多例如：click、submit、keyUp...
```html
<div id="app-2">
    <p>{{ msg }}</p>
    <button v-on:click="nowDate">click to update datetime</button>
</div>

<script>
    var app = new Vue({
        el: '#app-2',
        data: {
            msg: 'Value:' + new Date().toLocaleString()
        },
        methods:{
            nowDate: function () {
                this.msg = new Date().toLocaleString()
            }
        }
    })
</script>
```

- v-model 轻松实现表单输入和应用状态之间的双向绑定
```html
<div id="app-6">
  <p>{{ message }}</p>
  <input v-model="message">
</div>

var app6 = new Vue({
  el: '#app-6',
  data: {
    message: 'Hello Vue!'
  }
})
```

- v-once 一次性地插值，当数据改变时，插值处的内容不会更新
```html
<span v-once>这个将不会改变: {{ msg }}</span>
```

- v-html 解析html，而非显示文本内容
```html
<span v-html="rawHtml"></span>
```

- 数据绑定支持JavaScript表达式 
```html
{{ number + 1 }}

{{ ok ? 'YES' : 'NO' }}

{{ message.split('').reverse().join('') }}

<div v-bind:id="'list-' + id"></div>

// 下面是错误例子
<!-- 这是语句，不是表达式 -->
{{ var a = 1 }}

<!-- 流控制也不会生效，请使用三元表达式 -->
{{ if (ok) { return message } }}
```

- v-bind 缩写
```html
<!-- 完整语法 -->
<a v-bind:href="url">...</a>

<!-- 缩写 -->
<a :href="url">...</a>
```

- v-on 缩写
```html
<!-- 完整语法 -->
<a v-on:click="doSomething">...</a>

<!-- 缩写 -->
<a @click="doSomething">...</a>
```

- 计算属性（computed）, 计算属性会缓存而方法则不会，方法每次调用都会重新执行
```html
<div id="example">
    <p>Original message: "{{ message }}"</p>
    <p>Computed reversed message: "{{ reversedMessage }}"</p>
</div>

var vm = new Vue({
    el: '#example',
    data: {
        message: 'Hello'
    },
    computed: {
        // 计算属性的 getter
        reversedMessage: function () {
            // `this` 指向 vm 实例
            return this.message.split('').reverse().join('')
        }
    }
})
```

- [Class 与 Style 绑定 - 官方文档](https://cn.vuejs.org/v2/guide/class-and-style.html)