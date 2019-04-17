## 格式化代码几个基础大概的概念


1、 Pylint

Pylint 是一个 Python 代码分析工具，它分析 Python 代码中的错误，查找不符合代码风格标准（Pylint 默认使用的代码风格是 PEP 8）和有潜在问题的代码。 。它与几个流行的编辑器和IDE很好地集成，也可以从命令行运行。

要安装，请运行 pip install pylint 。

要从命令行运行 Pylint，请运行 pylint [options] path/to/dir 或 pylint [options] path/to/module.py 。Pylint 会向控制台输出不符合代码风格标准以及错误代码的地方

你还可以调用 pylintrc 配置文件来自定义 Pylint 检查的错误。（项目地址： https://www.pylint.org/ ）

2、Flake8

Flake8是一个“Python工具，它将PEP8，Pyflakes（类似于Pylint），McCabe（代码复杂性检查器）和第三方插件集合在一起，以检查某些Python代码的风格和质量。”

要使用Flake8，要先运行 pip install flake8 。然后运行 flake8 [options] path/to/dir 或 flake8 [options] path/to/module.py 查看其错误和警告。

与Pylint一样，Flake8允许对配置文件检查的内容进行一些自定义。它有非常清晰的文档，包括一些有用的Commit，可以作为开发工作流程的一部分自动检查代码。

Flake8能够与流行的编辑器和IDE集成，但这些指令通常在文档中并没有说明。要将Flake8与你喜欢的编辑器或IDE集成，可以在线搜索插件（例如 Sublime Text的Flake8插件）。（项目地址： http://flake8.pycqa.org/en/latest/ ）

3、Isort

isort 可自动对 Python的 import语句进行排序和分段。可将大量的 import结构转成非常适合阅读的排版。（例如，标准库导入，第三方库导入，从你自己的项目导入等），这样可以提高可读性，而且如果你导入的库较多，还能快速找到各个库

安装 isort pip install isort ，然后运行 isort path/to/module.py 。文档中提供了许多配置选项。例如，你可以配置 isort如何处理.isort.cfg文件来执行一个库的多行导入。

与Flake8和Pylint一样，isort还提供了将其与流行的编辑器和IDE集成的插件。（项目地址： https://github.com/timothycrosley/isort ）

分享你的代码风格

记住从命令行手动为每个文件运行linters是一件很痛苦的事情，你可能也不太喜欢通过运行 IDE 中某个插件来实现这个功能。另外，您的同事可能更喜欢别的方式，或者可能他们最喜欢的编辑器的没有这个插件，或者你检查代码不够细致，久而久之，你们共享的代码库将变得混乱并且难以阅读。

一个很好的解决方案是使用一个库，自动将代码重新按照PEP 8规范进行格式化。我们推荐的三个库都有不同的自定义级别来控制如何格式化代码，像pylint的和Flake8，你要先测试，看看它是否存在你接受不了却无法更改的默认配置。 

4、 Autopep8

Autopep8可以自动格式化你指定的模块中的代码。它将重新缩进行，修复缩进，删除无关的空白，并重构常见的比较错误（如布尔和None值）。你可以在它的文档中查看完整的更改列表

安装Autopep8，需要先运行 pip install --upgrade autopep8 。要重新格式化代码，请运行 pip install --upgrade autopep8  。然后执行autopep8 --in-place --aggressive --aggressive  就可以重新格式化你的代码。该aggressive标志（和它们的数量），表明autopep8对你的代码风格有多少控制权。（项目地址： https://github.com/hhatto/autopep8 ）

5、 Yapf

Yapf是重新格式化代码的另一种选择，它带有自己的配置选项列表。它与autopep8的不同之处在于它不仅仅解决了违反PEP 8规范的问题。它还重新格式化了没有违反PEP 8规范的代码，但没有一致地设置样式，可能是为了可读性而格式化得更好。

要安装Yapf，需要运行 pip install yapf 。要重新格式化代码，要运行 yapf [options] path/to/dir 或 yapf [options] path/to/module.py 。（项目地址： https://github.com/google/yapf ）

6、 Black

在所有的代码检查工具中，Black算是比较新的一个。它与autopep8和Yapf类似，但限制比较多，它很少有自定义选项，这是重点，这意味着你无法自定义代码风格。

Black支持Python 3.6+以上的版本，但可以

格式化Python 2代码。要使用Black，请运行 pip install black 。要美化您的代码，请运行： black path/to/dir或black path/to/module.py 。（项目地址： https://github.com/ambv/black ）

检查代码的测试覆盖率

假如你正在编写测试，你需要确保对代码库提交的新代码进行测试，并且不会降低代码的测试覆盖率。虽然测试覆盖率的百分比不是衡量测试有效性和充分性的唯一指标，但它是确保项目中遵循基本测试标准的一种方法。为了测量测试覆盖率，我们有一个建议：使用 Coverage 这个库。

7、Coverage

Coverage有多种向你报告测试覆盖率的方式，包括将结果输出到控制台或HTML页面，并提示哪些行号没有覆盖到。你可以设置配置文件以自定义Coverage检查的内容并使其更便于运行。

要安装Coverage，请运行 pip install coverage 。要运行程序并查看其输出，请运行 coverage run [path/to/module.py] [args] ，接着你将看到程序的输出。要查看哪些代码行没有被覆盖，请运行 coverage report -m 。（项目地址：https://coverage.readthedocs.io/en/latest/ ）

持续集成工具

持续集成(CI)是在合并和部署代码之前，自动检查代码风格错误和测试最小覆盖率的一系列过程。有许多免费或付费的工具可以自动化这个过程，本文这里就不详细介绍了。但是，由于设置CI过程是将代码块删除为更易于阅读和维护的重要步骤，因此，你不得不重视。