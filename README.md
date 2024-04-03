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

>The complexity of modern networks necessitates efficient comprehension and management by system administrators. Thanks to the advancements of Artificial Intelligence and, in particular, Large Language Models (LLMs), there is a promising prospect of employing these systems to assist humans in addressing network operations and navigating their architectures. However, despite this potential, a significant gap exists in the literature regarding the extent to which LLMs can understand computer networks. Without empirical evidence, system administrators might rely on these models without assurance of their efficacy in performing network-related tasks accurately. In this paper, we address this gap by introducing the problem of LLMs' understanding of computer networks. We propose a comprehensive framework designed to assess the capabilities of LLMs in comprehending various aspects of computer network topologies. We define multiple networks representing different scenarios, such as web servers and more complex architectures. We then formalize different research questions to determine whether LLMs can provide correct answers on the networks' topology and help system administrators in various tasks. Our framework comprises several state-of-the-art and open-source LLMs. Our findings highlight how these models represent a promising solution, as they can perform well in most tasks regardless of the network size. Despite their results, complex topologies are still challenging for LLMs to understand. Our evaluation also emphasizes the superiority of private LLMs with respect to local models, which have limited capabilities. Furthermore, we provide an analysis of prompt engineering techniques, aiding system administrators in obtaining the best results from LLMs.

<p align="right"><a href="#top">(back to top)</a></p>
<div id="usage"></div>

## ⚙️ Usage

To access the NetJSONs and the prompts we use in our study, start clone the repository with the following command.

```bash
git clone https://github.com/Mhackiori/LLM-SysAdmin/
cd LLM-SysAdmin
```
<sup>NOTE: if you're accessing this data from the anonymized repository, the above command might not work.</sup>

<p align="right"><a href="#top">(back to top)</a></p>