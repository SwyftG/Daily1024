> 1024是一个好网站

***首先，此次实战系列的前提是您能科学的找到1024网站！我这里并不提供网站地址，特此声明，这里只是用计算机科学的态度和方法，来分析一个问题。和1024网站没有任何关联。***

在1024网站上，不知道你是否和我一样，平时爱逛技术讨论区，爱看一些每日资讯总结的帖子，那么会不会因为板块的主题帖子是按照回复时间排序而找不到自己喜欢看的帖子而心烦意乱呢？是不是为了找自己今天没看过的帖子，而一遍又一遍的重新从头开始翻呢？

别怕，我都被这些问题困扰过！社区人口众多，帖子刷的很快，为了看到每天发布的帖子，板块的排版不得不让我每次进来都得从头开始找，看看哪个帖子今儿没看过。而且是左边看标题，右边看发布时间，好累啊。这样我不喜欢，有些浪费时间。

作为一个程序员，我觉得，这些问题，都是可以自己手动写一个Python爬虫来解决。

#### 我感觉这个虫子全网***最方便***，***最牛逼***，***最便捷***，***最能解决实际问题***的虫子！活学活用，***真正的让代码方便我的生活，这才是我编写程序索要达到的目的***。

##我们现在遇到的问题：
论坛的帖子排序是按照回帖时间排序的，为了能够看到每天最新发布的帖子，总是得从头开始看整个论坛，很烦，浪费时间。

![技术讨论区帖子按照回帖时间排序](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZTIVrsljhFE2owaiclJFick1HAf0lcszsYepW9wgfxzVjjiaWxQByUOmQglpgCNAwrlAM3uaTYDh2ncA/0?wx_fmt=png)

## 我们希望变成的样子
论坛的帖子按照时间发布顺序排列，这样看每天的新内容就很省事儿。

如果我们要写一个爬虫来解决的话，大致结构应该如下：

![Daily1024结构](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZTIVrsljhFE2owaiclJFick1HNyicjUXHsLJgeicdVKcaMBD9fAdhyQSf4WOHnXzarEq3DWJh3PN2iacYw/0?wx_fmt=png)

这里有几个部分：
- **config.json**: 这个算是配置文件，目前需要填入的信息有：
  1.1024网站的的URL
  2.爬虫结果输出的的文件位置
  3.爬虫需要爬的最大page num
  4.板块信息，指论坛的板块名称（*这个可以自定义*）和板块的fid
- **Url_manager**: 管理备爬取的URL。
- **Html_downloade**r: 爬虫获取网页信息。
- **Html_parser**: 爬虫的网页解析器。
- **Html_output**: 爬虫输出结果。

上面的结构很简单，那么简单的流程就是：*我们先配置好本地的config.json文件，然后启动程序，爬虫会自动根据配置好的信息，然后抓取各个板块前几页的内容，根据帖子发帖时间，筛选爬出出来信息，随后，将获取到的信息按照时间排序，最后输出成html格式的文件，使用本地的网页浏览器打开。浏览器里面可以看到帖子的id，帖子的标题以及帖子的发布时间。通过点击帖子的标题，可以跳转到社区的帖子。*

这样，内容丰富的小草网站，就直接变成了我们本地写的最简单的***html***文件。

我们整理后的网站首页：
![Daily1024的index](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZTIVrsljhFE2owaiclJFick1HgDfFZRu2iahHaHLIHficicx2GTSOpbJKxia3yWY45Qib0GibMu9pQJVicGEFA/0?wx_fmt=png)
  
新整理后板块长这个样子：

![Daily1024的技术讨论板块](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZTIVrsljhFE2owaiclJFick1Hc7aiagTtvdXhdia5l83klmfwQEuRQfElmYgXAty2M0nE9hRvHqlDphRw/0?wx_fmt=png)



![Daily1024的技术讨论板块，按照时间顺序排列](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZTIVrsljhFE2owaiclJFick1HaAPVFIOYn3YOEL0S9JhzJMNHibluXmIMoiawmiaIicBy8ZtoSl6o0hFQzg/0?wx_fmt=png)

这样看上去，就简单和舒服的多了，不再需要像之前那样一个一个的找了。而且，我们看过哪个帖子，都是有不同颜色区分的。这样节省好多好多时间。下面就简单的说一下工程中运用到的技术点吧。

### 技术梳理
虽然现在网络上有很多成熟的爬虫框架，比如`Scrapy`，我之前也用过`Scrapy`，`Scrapy`确实强大，但是感觉这样体会不到爬虫的乐趣。所以干脆自己从零搭建一个爬虫。从零距离感受爬虫，感受`Python`的乐趣。

#### 整体技术
- `python 3.6`
- `requests`
- `BeautifulSoup4`
- `webbrowser`
- `json`

#### Config.json
这个是配置文件，将需要一些基本参数写在这个json文件中。先关的读取类是`config_utils`中的`configreader`。

![config.json](https://mmbiz.qpic.cn/mmbiz_png/jA4Qc7C9IZTIVrsljhFE2owaiclJFick1HOYhZiaf45XdCaaSCF2g7oP1ETJ2W1IWcSQrKYU4v3jWmL7Yv74ddjrw/0?wx_fmt=png)

#### Url_manager
通过一个`dict`来存储板块名称和对应的板块`URL`，提供一些简答的方法来操作`URL`。

#### Html_download
通过使用`requests`模块来进行网页的访问。从而拿到网页数据，为后面步骤的解析提供基础。  
这里进行网络请求的时候，由于`1024网站`做了反爬处理，我添加了不同的`HTTP header`。目前还算比较好用。表头信息在`user_agents`文件中。

#### Html_parser
通过`BeautifulSoup`来对`html`做解析处理。每一个帖子都是有一个*唯一id*的。帖子都封装到`CaoliuItem`中，然后将结果输出到`html_outputer`中。这里是通过`html`的`tag`来做的寻找，并不是通过正则表达式。可能有点*僵*。

#### Html_outputer
这个是将之前收集到的爬虫解析结果，整理成`html`文件的类。最终结果有一个`index`页面，每个版块还有自己的页面。他们之间相互链接在一起，点击起来爽爽的，炒鸡方便。

### 需要改进的地方 TODO
- 整体结构虽然清晰，但是整体结构还需要优化。要做到像`Scrapy`那样强大的虫子，得一步一步来。
 - 目前爬虫能力比较弱，没有用到多线程爬虫。下一个版本可以加入多线程，这样既能提升速度，又能提升质量。
- `parser`的解析还是太依赖网站的布局。若是网站布局发生改变，`parser`就得修改。这个问题是所有爬虫的通病，我还在想办法把这里做的更活一些，不要这么死板。
- `output`的`html`文件美观度不够。
- 下一版本，想将解析出来的东西，能够和`MongoDB`联动，算是本地保存一份吧。因为这样就能够看到之前的帖子信息。
- 接下来应该最好是针对每个帖子，再爬一层，可以做到自动将图片或者种子文件下载下来。这个下载图片和种子的虫子我之前用`Scrapy`的时候做过，但是还是需要结合自己写的虫子比较好。
- 最好能够将爬虫扩展到其他网站，比如微博啊，V2ex啊，之类的资讯网站。感觉每天来回逛这几个网站，打开这个打开那个，确实有时候挺浪费时间的，倒不如把它们每天更新的东西都整合成在一起，通过一个网站，一次看个够。这样多爽。
- 最终的版本就是把这个程序做成一个后台服务，然后部署到服务器上，每天通过访问，能够看到当天各个网站的更新内容。做到***"访问一个，就可以访问全部"***的效果。

这个项目源码，通过***阅读原文***即可查阅。

最后来一波福利，关注公众号：**皮克啪的铲屎官**，回复“1024”，能够找到你需要的东西哦~
![关注并回复 1024 有惊喜](https://mmbiz.qpic.cn/mmbiz_jpg/jA4Qc7C9IZS5CU8Eicxw9K4kIY8BibzDJX6QiahNQ0wDC2HLheXWp6CpITXBWcxt6E4SRlxHJyrxNO6v6TlKMgeUg/0?wx_fmt=jpeg)



