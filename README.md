<div id="top"></div>
<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/Mhackiori/LLM-SysAdmin/">
    <img src="https://i.postimg.cc/7YCB9YZN/network.png" alt="Logo" width="150" height="150">
  </a>

  <h1 align="center">Can LLMs Understand Computer Networks?</h1>

  <p align="center">
    Towards a Virtual System Administrator
    <br />
    <a href="https://github.com/Mhackiori/LLM-SysAdmin/"><strong>Paper in progress »</strong></a>
    <br />
    <br />
    <a href="">Anonymous Authors</a>
  </p>
</div>

<!-- TABLE OF CONTENTS -->
<details>
  <summary><strong>Table of Contents</strong></summary>
  <ol>
    <li>
      <a href="#abstract">Abstract</a>
    </li>
    <li>
      <a href="#usage">Usage</a>
    </li>
  </ol>
</details>

<div id="abstract"></div>

## 🧩 Abstract

>Recent advancements in Artificial Intelligence, and particularly Large Language Models (LLMs), offer promising prospects for aiding system administrators in managing the complexity of modern networks. However, despite this potential, a significant gap exists in the literature regarding the extent to which LLMs can understand computer networks. Without empirical evidence, system administrators might rely on these models without assurance of their efficacy in performing network-related tasks accurately. In this paper, we are the first to conduct an exhaustive study on LLMs' comprehension of computer networks. We formulate several research questions to determine whether LLMs can provide correct answers when provided with a network topology and questions on it. To assess them, we developed a thorough framework for evaluating LLMs' capabilities in various network-related tasks. We evaluate our framework on multiple computer networks employing private (e.g., GPT4) and open-source (e.g., Llama2) models. Our findings demonstrate promising results, with the best model achieving an average accuracy of 79.3%. Private LLMs achieve noteworthy results in small and medium networks, while challenges persist in comprehending complex network topologies, particularly for open-source models. Moreover, we provide insight into how prompt engineering can enhance the accuracy of some tasks.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="usage"></div>

## ⚙️ Usage

To access the NetJSONs and the prompts we use in our study, clone the repository using the following command.

```bash
git clone https://github.com/Mhackiori/LLM-SysAdmin/
cd LLM-SysAdmin
```
<sup>NOTE: if you're accessing this data from the anonymized repository, the above command might not work.</sup>

<p align="right"><a href="#top">(back to top)</a></p>
