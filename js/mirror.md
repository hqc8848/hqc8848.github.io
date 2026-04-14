---
title: 镜像
description: 文本的镜像翻转实现，可指定方向
permalink: /js/mirror/
redirect_from:
  - /js/flip/
---

镜像方向：
<select id="mode">
  <option value="left">镜像左半</option>
  <option value="right" selected>镜像右半</option>
</select>

原始文本：<input type="text" id="input" oninput="compute()" autofocus>

结果：<input type="text" id="output" readonly> <button onclick="copyText()">复制</button>

<script>
  function compute() {
    const s = document.getElementById('input').value;
    const isLeft = document.getElementById('mode').value === 'left';
    let result = '';
    if (s.length > 0) {
      if (isLeft) {
        result = s + s.split('').reverse().join('').slice(1);
      } else {
        result = s.slice(1).split('').reverse().join('') + s;
      }
    }
    document.getElementById('output').value = result;
  }
  function copyText() {
    const input = document.getElementById('myInput');
    input.select();
    document.execCommand('copy');
  }
  document.getElementById('mode').addEventListener('change', compute);
</script>
