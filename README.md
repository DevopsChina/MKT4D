## DevOps Tools live show | 工具鉴宝活动

>Must know DevOps Tools for Developer [codename = *MKT4D*]

Welcome to the DevOps China code live show! This lab is a collection of hands-on, self-paced exercises that will help you gain practical experience with various DevOps concepts and tools. The exercises are designed to be simple, straightforward, and easy to follow, with step-by-step instructions.

Season one playlist 
* [Bilibili](https://space.bilibili.com/370989874/channel/collectiondetail?sid=338624) 
* [YouTube](https://www.youtube.com/watch?v=XBglZDywiXk&list=PLbiCRAJeBtFucYb2W_autUr8G5OGAUFAU&ab_channel=DevOpsChina)

Season two is now open for summit a new idea at [MKT4D issues](https://github.com/DevopsChina/mkt4d/issues)

Each code live show is a separate directory in this repository, and each directory contains a README file with detailed instructions, along with any necessary configuration files or sample code. Whether you're new to DevOps or an experienced practitioner, this lab will help you take your skills to the next level and give you the confidence to tackle real-world challenges.

### 第二季鉴宝活动的鉴宝人火热招募中，请提交你的分享思路到：[MKT4D issues](https://github.com/DevopsChina/MKT4D/issues/new?assignees=martinliu&labels=&template=%F0%9F%9A%80-%E6%8A%A5%E5%90%8Ddevops%E5%B7%A5%E5%85%B7%E9%89%B4%E5%AE%9D%E5%88%86%E4%BA%AB-%F0%9F%92%A0%F0%9F%AA%95%F0%9F%92%8E-.md&title=)

## 活动简介

大家想要获取DevOps的理念和技术，收获深刻的理解；社区建议的途径是示例项目实操。这里是直播节目的代码仓库。我们用 DevOps 工具鉴宝的直播方式，请各路实战经验丰富的工程师给社区分享一些列有趣有料的Codelab，并在直播过程中进行生动的讲解和互动问答。

"DevOps鉴宝活动“的目标是：公开面向社区的所有人，征集DevOps工具链中各种工具的实战操作技能。

相关的 DevOps 工具应该包含，但不仅限于以下分类。

- 软件仓库 | code – 管理软件版本的工具–目前使用最广泛的是Git。
- 构建工具 | build – 有些软件在打包或使用前需要编译，传统的构建工具包括Make、Ant、Maven和MSBuild。
- 持续集成工具 | ci – 在配置好以后，每次将代码提交到存储库中时，它都会对软件进行构建、部署和测试。这通常可以提高软件质量和上市时间。这个市场上最流行的工具是 Jenkins、Travis、TeamCity和Bamboo。
- 代码分析/审查工具 | verify – 这些工具可以查找代码中的错误，检查代码格式和质量，以及测试覆盖率。这些工具因编程语言而异。SonarQube是这个领域的一个流行工具，还有其他各种 “轻量的 “工具。
- 配置管理 | config – 配置管理工具和数据库通常存储所有关于你的硬件和软件项目的信息，以及提供一个脚本和/或模板系统，用于自动化常见任务。在这个领域似乎有很多玩家。传统的玩家是Chef、Puppet和Salt Stack。
- 部署工具 | deploy – 这些工具有助于软件的部署。许多CI工具也是CD（持续部署）工具，它们协助软件的部署。传统上在Ruby语言中，Capistrano工具被广泛使用；在Java语言中，Maven被很多人使用。所有的编排工具也都支持某种形式的部署。
- 编排工具 | release – 这些工具配置、调度和管理计算机系统和软件。它们通常将 “自动化 “和 “工作流 “作为其服务的一部分。Kubernetes是一个非常流行的编排工具，它专注于容器。Terraform是一个非常流行的编排工具，它的关注点更广，包括云编排。另外，每个云提供商都有自己的一套工具（CloudFormation、GCP Deployment Manager, 和ARM）。
- 监控工具 | monitor - 这些工具允许监控硬件和软件。通常，它们包括监控代理程序，用于监视进程和日志文件，以确保系统的健康。Nagios是一种流行的监控工具。
- 测试工具 | test - 测试工具用于管理测试，以及测试自动化，包括性能和负载测试等。

![devops tool chain](https://elasticstack-1300734579.cos.ap-nanjing.myqcloud.com/2021-04-02-1-wTp-r9QJvF-DXGZDZUHmbA.jpeg)

## 学习清单

以下是所有 DevOps 鉴宝活动直播内容的回放清单，请大家根据需求学习打卡。社区也欢迎你在视频中发表弹幕和留言，分享你对 DevOps 工具的见解。

### code


### build


### test


### verify


### 持续集成 - ci

- 第一季：第 3 集 恐龙级CI/CD工具 Jenkins [【Codelab】](ci/lab03-jenkins) - [【B 站视频】](https://www.bilibili.com/video/BV1MA4y1Z7Fk)
- 第一季：第 5 集 云原生 CI 中的强者 Tekton [【Codelab】](ci/lab05-tekton) - [【B 站视频】](https://www.bilibili.com/video/BV1e94y117tY)
- 第一季：第 6 集 云开发者可快速上手的 TeamCity [【Codelab】](ci/lab06-teamcity) - [【B 站视频】](https://www.bilibili.com/video/BV1pY4y17754)

### 配置管理

- 第一季： 第 1 集 配置管理神器 Ansible - 新手入门指南 [【Codelab】](config/lab01-ansible) - [【B 站视频】](https://www.bilibili.com/video/BV1Uv4y1K7u9)
- 第一季： 第 7 集 数据库变更版本管理利器 Liquibase [【Codelab】](database/lab06-liquibase) - [【B 站视频】](https://www.bilibili.com/video/BV1iT411E7Fk)
- 第一季：第 9 集 - 基础架构自动化编排工具 Terraform [【Codelab】](config/lab09-terraform) - [【B 站视频】](https://www.bilibili.com/video/BV1HU4y1e7wZ)


### 部署 - deploy

- 第一季：第 4 集 GitOps 的不二之选 ArgoCD [【Codelab】](deploy/lab04-argocd) -[【B 站视频】](https://www.bilibili.com/video/BV11a411L7f5)

### 编排 - Orchestration

- 第一季：第 10 集 品鉴极简风格的容器平台 K3S [【Codelab】](orchestration/lab10-k3s) -[【B 站视频】](https://www.bilibili.com/video/BV11e411g7qx)

### 监控 - monitor

### 平台 - platform

- 第一季：第 2 集 - 全能级 DevOps 平台 GitLab [【Codelab】](platform/lab02-jihu-gitlab) - [【B 站视频】](https://www.bilibili.com/video/BV1hR4y1c75b)
- 第一季：第 9 集 - 品鉴 Atlassian 的 DevOps 全家桶的妙用 [【Codelab】](platform/lab09-atlassian) - [【B 站视频】](https://www.bilibili.com/video/BV1vG4y1a7ph)




## 贡献说明

### 目录结构

通过创建 PR 的方式，在以上分类目录中，按编号创建一个新的文件夹，用于容纳一个独立lab的所有相关代码。必须包含清晰的 readme 文件，在 readme 文件中清晰概要的描述相关技术知识要点，不能有意无意的包含任何产品市场宣传的内容。

```sh
├── README.md
├── build
├── ci
├── code
├── config
│   └── lab01-ansible
│       └── readme.md
├── deploy
├── monitor
├── release
├── test
└── verify
└── platform
```

### 参与贡献过程

本代码库面向所有社区朋友开放。为了让大家能够顺利的参与贡献，请参考以下参与流程。

1. 在代码库的 issue 列表中，用模板创建一个新 issue，简单描述 codelab 的内容，必须包含工具、技术、开发语言和难度级别等，让其他人更清晰的了解知识的范围。
2. Issue 的沟通和确认阶段，社区评审同学和提议者在 issue 的评论区完成讨论确认过程。
3. 进入 codelab 代码的 PR 提交阶段，请创建符合规则的分支名称 【 分类 - 编号  - 工具名称】，例如： code-lab01-git 
4. 进入 PR 搞了确认，社区评审同学会进行评审和测试，并提出修改建议。
5. 提交 PR 的合并请求，本代码库的维护同学审批 MR ，代码正式纳入主干。
6. 进入 Codelab 的学习和宣传阶段，Codelab的提交者和其他鉴宝人，用线上直播的方式演示整个 codelab 的操作过程，并将录播视频在 B 站分享给大家。
7. 关闭 issue 。
8. Codelab 的 readme 文件内容和 B 站视频 会分享给社区的所有人。

## 鸣谢

### 赞助商福利资源

* Red Hat ：欢迎免费注册[红帽开发者账号](https://developers.redhat.com/)，可以免费获得开发者个人订阅的详情[「点这里」](https://www.redhat.com/wapps/tnc/viewterms/72ce03fd-1564-41f3-9707-a09747625585?extIdCarryOver=true&intcmp=701f2000001OMHaAAO&sc_cid=701f2000001OH7YAAW)；订阅中包含了 16 个物理/虚拟机上 RHEL 操作系统的开发者使用订阅，并且可以访问几乎红帽所有产品的安装包和源代码。官方微信公众号「红帽支持与服务」
* 极狐 GitLab ：欢迎[免费注册使用极狐GitLab SaaS](https://gitlab.cn/)。凡是通过 DevOps 社区鉴宝活动注册的用户，可以发邮件至 marketing@gitlab.cn，申请超长（超 1 个月以上）时间的旗舰版试用（发邮件是为了方便获取需要延长旗舰版试用的 Group 等信息）。
* Elastic：欢迎[免费注册 Elastic Cloud 超长（30 天）试用账号](https://info.elastic.co/elasticsearch-service-trial-community-showcase.html?ultron=community-martin&hulk=30d)，只需要邮箱，无需输入信用卡号，直接体验当前最新版本的 Elastic Stack 技术栈。官方微信公众号「Elastic搜索」
* JetBrains TeamCity Cloud 平台焕然一新，CI/CD 本色依旧，[免费试用](https://www.jetbrains.com/zh-cn/teamcity/cloud/)DevOps社区成员亮明身份还可通过链接获取[更长试用时间](https://www.jetbrains.com/zh-cn/teamcity/get-in-touch/) 官方微信号「JetBrainsChina」
* 阿里云云起实验室：由阿里云提供的面向个人和企业开发者的零门槛云上实践平台，让开发者能够在“做中学”。实验室提供详细的实验手册指导和免费的实验云资源，一键生成预置实验环境，让开发者能够快速体验云计算、大数据、人工智能等云服务实验场景和解决方案，帮助开发者快速提升使用云服务的能力。[免费体验](https://developer.aliyun.com/adc/?utm_content=g_1000342863)
* Rancher：Rancher 是一个开源的企业级 Kubernetes 管理平台，实现了 K8s 集群在混合云+本地数据中心的集中部署与管理。关注「Rancher 微信公众号」，第一时间了解 Rancher 中文论坛精选内容，公众号后台回复「工具鉴宝」还能免费解锁 K8s 安全防护终极指南哦～


### 赞助商参与

#### 第一季

第一期：

* Red Hat & 极狐GitLab 赞助了直播抽奖礼品
* JetBrains 赞助鉴宝人礼品

第二期：

* Elastc & 极狐GitLab 赞助了直播抽奖礼品
* JetBrains 赞助鉴宝人礼品

第三期：

* 阿里云云起实验室 & Elastc 赞助了直播抽奖礼品
* JetBrains 赞助鉴宝人礼品

第四期：

* 阿里云云起实验室 & Elastc 赞助了直播抽奖礼品
* JetBrains 赞助鉴宝人礼品

第五期：

* 阿里云云起实验室 & Elastc 赞助了直播抽奖礼品
* JetBrains 赞助鉴宝人礼品

第六期：

* 阿里云云起实验室 & Elastc 赞助了直播抽奖礼品

第七期：

* 阿里云云起实验室 & Elastc 赞助了直播抽奖礼品

第八期：

- 阿里云云起实验室、中国DevOps社区

第九期：

- 阿里云云起实验室 &Rancher

第十期：

- 阿里云云起实验室 &Rancher

## 行为准则

本项目是面向所有社区参与者的共创学习项目，请任何参与者遵守[《中国DevOps社区行为规范》](https://www.devopschina.org/codeofconduct/)
