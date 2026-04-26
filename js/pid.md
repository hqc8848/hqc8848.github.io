---
title: PID
description: 快速将pixiv PID转化为实际的网页链接
permalink: /js/pid/
---

页面类型：
<select id="type" onchange="generate()">
  <option value="artworks">作品 (artworks)</option>
  <option value="users" selected>用户 (users)</option>
  <option value="tags">标签 (tags)</option>
  <option value="novel/show.php?id=">小说 (novel)</option>
  <option value="novel/series/">小说系列 (series)</option>
</select>

数字 ID：<input type="text" id="pid" oninput="generate()" autofocus>

自动跳转：
<select id="jump">
  <option value="no" selected>否</option>
  <option value="yes">是</option>
</select>

链接：<input type="text" id="result" readonly style="width:360px"> <button onclick="copyLink()">复制</button> <button onclick="openLink()">打开</button>

<script>
  function generate() {
    var type = document.getElementById('type').value;
    var pid = document.getElementById('pid').value.trim();
    var url = '';
    if (pid) {
      if (type.indexOf('?') !== -1) {
        url = 'https://www.pixiv.net/' + type + pid;
      } else {
        url = 'https://www.pixiv.net/' + type + '/' + pid;
      }
    }
    document.getElementById('result').value = url;
    if (url && document.getElementById('jump').value === 'yes') {
      window.open(url, '_blank');
    }
  }
  function copyLink() {
    var text = document.getElementById('result').value;
    if (text) navigator.clipboard.writeText(text);
  }
  function openLink() {
    var url = document.getElementById('result').value;
    if (url) window.open(url, '_blank');
  }
</script>
