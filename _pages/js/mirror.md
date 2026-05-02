---
title: "镜像"
description: "文本的镜像翻转实现，可指定方向"
permalink: "/js/mirror/"
redirect_from:
  - "/js/flip/"
---

镜像方向：
<select id="mode" onchange="compute()">
  <option value="left">镜像左半</option>
  <option value="right" selected>镜像右半</option>
</select>

中心字符：
<select id="center" onchange="compute()">
  <option value="skip" selected>不重复</option>
  <option value="keep">重复</option>
</select>

原始文本：<input type="text" id="input" oninput="compute()" autofocus>

结果：<input type="text" id="output" readonly> <button onclick="copyText()">复制</button>

<script>
  function compute() {
    const s = document.getElementById('input').value;
    const isLeft = document.getElementById('mode').value === 'left';
    const keepCenter = document.getElementById('center').value === 'keep';
    let result = '';
    if (s.length > 0) {
      const reversed = s.split('').reverse().join('');
      if (isLeft) {
        result = s + (keepCenter ? reversed : reversed.slice(1));
      } else {
        result = (keepCenter ? reversed : reversed.slice(0, -1)) + s;
      }
    }
    document.getElementById('output').value = result;
  }
  function copyText() {
    const text = document.getElementById('output').value;
    navigator.clipboard.writeText(text);
  }
</script>
