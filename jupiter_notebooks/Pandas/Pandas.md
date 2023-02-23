{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1dedba8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import matplotlib.pyplot as plt\n",
    "import ssl\n",
    "\n",
    "%matplotlib inline\n",
    "ssl._create_default_https_context = ssl._create_unverified_context\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7cfe3868",
   "metadata": {},
   "outputs": [],
   "source": [
    "np.zeros(15)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0a0e4183",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "f = pd.read_csv('zoo1.csv', names=['animal', 'uniq_id', 'water_need'], index_col='uniq_id')\n",
    "df = pd.DataFrame(f)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4a3d1870",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "69ef31ee",
   "metadata": {},
   "outputs": [],
   "source": [
    "\"\"\"\n",
    "data = {'A': list(range(1, 6)), 'B': list(range(10, 15)), 'C': list(range(11, 16)), 'D': list(range(20, 25))}\n",
    "df = pd.DataFrame(data)\n",
    "df2 = df.assign(E=[25, 26, 27, 28, 29])\n",
    "print(df)\n",
    "print(df2)\n",
    "\n",
    "\"\"\"\n",
    "df1 = pd.DataFrame(np.zeros(25).reshape(5,5))\n",
    "df2 = pd.DataFrame(np.ones(25).reshape(5,5))\n",
    "df2 / df1\n",
    "\n",
    "# Рассмотрим DataFrame:\n",
    "# df  A\n",
    "# 0 AbCd\n",
    "# 1 Efg\n",
    "# 2 HIG\n",
    "# 3 klm\n",
    "# Заполните пропуски в коде чтобы преобразовать все значения в столбце A к нижнему регистру:\n",
    "\n",
    "# df = pd.DataFrame({'A':['AbCd','Efg','HIG','klm']})\n",
    "# df['A'] = df['A'].str.lower()\n",
    "# df\n",
    "\n",
    "\n",
    "# Дисперсия всех рядов \n",
    "# print(df.var())\n",
    "\n",
    "# Какие из следующих способов являются правильными для выбора строк на основе списка индексных меток?\n",
    "# + df[df.index.isin([1, 2, 4])] \n",
    "# - df.get_row(df.index.isin([1, 2, 4]))\n",
    "# - df.where(df.index.isin([1, 2, 4]))\n",
    "# - df.query(df.index.isin([1, 2, 4]))\n",
    "# + df.loc[df.index.isin([1, 2, 4])]\n",
    "\n",
    "\n",
    "# Какой из следующих способов является правильным для создания точечной диаграммы?\n",
    "\n",
    "# + df.plot.scatter(x='A', y='B')\n",
    "# + df.plot(kind='scatter', x='A', y='B')\n",
    "# - df.scatter(x='A', y='B')\n",
    "# - df.scatterplot(x='A', y='B')\n",
    "# - df.plot_scatter(x='A', y='B')\n",
    "\n",
    "# Какие из следующих способов являются правильными для выбора строк на основе нескольких условий?\n",
    "# + df[(df.A == 5) & (df.B >= 11)]\n",
    "# - df[df.A == 5 and df.B == 11]\n",
    "# + df.loc[(df.A >= 3) & (df.B >= 10)]\n",
    "# - df.loc[df.A >= 1 and df.B >= 10]\n",
    "# - df.get_rows((df.column_name_1 == 5) & (df.column_name_2 == 6))\n",
    "\n",
    "\n",
    "# Определите какая серия будет создана в результате выполнения следующего кода:\n",
    "# data = {'a': 15, 'b': 10, 'c': 12}\n",
    "# pd.Series(data=data, index=['x', 'y', 'z'])\n",
    "\n",
    "# Вариант С\n",
    "# x   NaN\n",
    "# y   NaN\n",
    "# z   NaN\n",
    "# dtype: float64\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ef91ba13",
   "metadata": {},
   "source": [
    "### Функция DataFrame.cut() - разбивка на интервалы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "58790db2",
   "metadata": {},
   "outputs": [],
   "source": [
    "ages = [18, 20, 25, 22, 33, 35, 30, 40, 42, 45, 50, 53, 55, 62, 65, 70, 80, 90, 95]\n",
    "bins = [18, 26, 36, 46, 60, 100]\n",
    "names = ['от 18 до 25 лет', 'от 26 до 35 лет', 'от 36 до 45 лет', 'от 46 до 60 лет', 'от 61 и старше']\n",
    "res = pd.cut(ages, bins, right=False, labels=names)\n",
    "# res.categories\n",
    "# res.codes\n",
    "pd.value_counts(res, sort=False)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3cc1370c",
   "metadata": {},
   "source": [
    "#### Автоматическое разбиение списка значений на интервалы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f517ffc3",
   "metadata": {},
   "outputs": [],
   "source": [
    "ages = [18, 20, 25, 22, 33, 35, 30, 40, 42, 45, 50, 53, 55, 62, 65, 70, 80, 90, 95]\n",
    "res = pd.cut(ages, 4, precision=0)\n",
    "print(pd.value_counts(res, sort=False))\n"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "ddb0c4d4",
   "metadata": {},
   "source": [
    "### 5.3.2\n",
    "Сегодня наш друг Николай (владелец сети кинотеатров) просит нас о помощи. Николай хочет запустить в прокат новый индийский фильм с известным актером, но пока не понимает на сколько фильм может быть успешен. Для этого он собрал группу из 50 человек и устроил для них закрытый показ. После закрытого показа каждый зритель поставил оценку от 0 до 10, где 0 - совсем плохо, 10 - отлично. Николай начинал проходить курс по основам Pandas, но остановился где-то на сериях, поэтому он подготовил серию в которой хранятся все оценки зрителей:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "(на скрине первые 10 оценок)\n",
    "\n",
    "И теперь он хочет разбить все оценки на три группы:\n",
    "0-4 - Плохо\n",
    "5-7 - Так себе\n",
    "8-10 - Отлично\n",
    "А потом посчитать по каждой группе количество оценок. Помогите Николаю посчитать результаты) \n",
    "Ваша функция solution должна вернуть серию в которой будут лежать названия групп (индекс) и количество оценок (значения).\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6a5a24ca",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = [8, 9, 2, 0, 3, 8, 3, 9, 6, 5, 7, 0, 3, 0, 6, 7, 3, 9, 3, 5, 1, 4, 6, 5, 7, 5, 7, 6, 4, 6, 6, 1, 9, 1, 5, 8, 4, 6,\n",
    "      8, 5, 9, 5, 7, 9, 9, 1, 1, 0, 1, 0]\n",
    "\n",
    "grades = ['Плохо', 'Так себе', 'Отлично']\n",
    "bins = [-1, 4, 7, 10]\n",
    "pd.cut(s1, bins, labels=grades).value_counts()\n"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "caa790eb",
   "metadata": {},
   "source": [
    "### 5.3.4 \n",
    "\n",
    "Костя, один из студентов нашего курса, кажется все понял про функцию map и решил применить свою функцию get_sklad_number к значениям из серии s1:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "Функция вытаскивает из названия склада его номер. Но у него что-то пошло не так и код не запускается. \n",
    "Помогите Косте исправить ошибки в коде.\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a0bef0bb",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = pd.Series(['Sklad 26', 'Sklad 18','Sklad 36','Sklad 5'])\n",
    "# s1.map(lambda n: int(n.split()[1]))\n",
    "\n",
    "\n",
    "def solution(s1: str) -> int:\n",
    "    \"\"\"Принимает строку вида <имя_склада номер> и возвращает целое число - номер склада \"\"\"\n",
    "    return s1.map(lambda n: int(n.split()[1]))\n",
    "\n",
    "\n",
    "solution(s1)\n",
    "               "
   ]
  },
  {
   "cell_type": "markdown",
   "id": "20242149",
   "metadata": {},
   "source": [
    "### 5.3.6 \n",
    "На вход функции подается датафрейм с наиболее популярными веб-сайтами за последний месяц в мире. У некоторых веб-сайтов не верно записано доменное имя: вместо .com -> .cm или .om, а вместо .ru -> рф. По всей видимости данные в систему вносил человек, который не очень знаком с интернетом. Замените значения в ячейках на корректные:"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1684ce3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_ = pd.DataFrame({'Веб-сайт': ['google.com', 'youtube.com', 'facebook.cm',\n",
    "                  'twitter.com', 'instagram.com', 'baidu.com', 'wikipedia.org',\n",
    "                   'yandex.рф', 'yahoo.cm', 'whatsapp.om']})\n",
    "\n",
    "\n",
    "def solution(df: pd.DataFrame) -> pd.DataFrame:\n",
    "    \"\"\"Принимает dataframe (список веб-сайтов) и заменяет в нем значения .cm или .om на .com, рф на .ru\"\"\"\n",
    "    return df.replace({'\\.[co]m': '.com', '\\.рф': '.ru'}, regex=True)\n",
    "    #return df.replace(['\\.[co]m$', '\\.рф$'], ['.com', '.ru'], regex=True)\n",
    "\n",
    "    \n",
    "solution(df_)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "fc6670bb",
   "metadata": {},
   "source": [
    "### Выбросы"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "03512f3d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({'IZM_1' : [-1.63, 0.51, -1.33, -0.83, 0.27, 1.28, 0.36, 2.01, -0.43, -0.52],\n",
    "    'IZM_2' : [0.22, 0.41, -2.07, -0.74, -0.68, -0.62, 0.83, 0.30, -0.72, -0.14],\n",
    "    'IZM_3' : [-0.31, 0.41, 1.26, -0.41, -0.62, -0.76, 0.02, 0.42, -1.48, 0.71]}, \n",
    "     index = ['TEST#1', 'TEST#2', 'TEST#3', 'TEST#4', 'TEST#5', 'TEST#6', 'TEST#7', 'TEST#8', 'TEST#9', 'TEST#10'])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a85e88f7",
   "metadata": {},
   "outputs": [],
   "source": [
    "df2 = pd.DataFrame({'A1': ['43', '3', '80', '5'],\n",
    "                     'B1': ['B0', 'B1', 'B5', 'B3'],\n",
    "                     'C1': ['C4', 'C5', 'C6', 'C7'],\n",
    "                     'D1': ['D4', 'D5', 'D6', 'D7']})\n",
    "df1 = pd.DataFrame({'A': ['5', '87', '42', '43'],\n",
    "                     'B': ['B0', 'B1', 'B2', 'B3'],\n",
    "                     'C': ['C0', 'C1', 'C2', 'C3'],\n",
    "                     'D': ['D0', 'D1', 'D2', 'D3']})\n",
    "\n",
    "df2\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21ffa4b8",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f73784c3",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4d556d7",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "3c07fb71",
   "metadata": {},
   "source": [
    "#### Для одной серии "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e74415c7",
   "metadata": {},
   "outputs": [],
   "source": [
    "mask = np.abs(df['IZM_3']) > 1\n",
    "\n",
    "df[mask]['IZM_3']\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6eeced73",
   "metadata": {},
   "outputs": [],
   "source": [
    "mask = df['IZM_3'].between(-1, 1, inclusive='both')\n",
    "\n",
    "df[mask]['IZM_3']\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "763a9245",
   "metadata": {},
   "source": [
    "#### Для всего dataframe"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88bc1fe5",
   "metadata": {},
   "outputs": [],
   "source": [
    "mask = (np.abs(df) > 1).any(axis=1)\n",
    "\n",
    "df[mask]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9a981a84",
   "metadata": {},
   "source": [
    "#### Приводим выбросы к границам диапазона (-1,1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "688d0f87",
   "metadata": {},
   "outputs": [],
   "source": [
    "mask = (np.abs(df) > 1)\n",
    "\n",
    "# df[mask] = np.sign(df)\n",
    "\n",
    "print(df)\n",
    "print(df.describe())\n",
    "print()\n",
    "print(df_ := df.clip(-1, 1))\n",
    "\n",
    "df_.describe().T.drop(['std','25%', '50%', '75%'], axis=1).style.background_gradient(subset=['count', 'mean', 'min', 'max'], cmap='Blues')\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "5c7b4977",
   "metadata": {},
   "source": [
    "#### Вывод перемешанного df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4c65a8f",
   "metadata": {},
   "outputs": [],
   "source": [
    "idx = np.random.permutation(10)\n",
    "\n",
    "# df1.iloc[idx]\n",
    "\n",
    "df1.take(idx)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9190d978",
   "metadata": {},
   "source": [
    "#### Выбрать n случайных строк из df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f9acc7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df1.sample(n=3) # replace = True для вывода повторов строк"
   ]
  },
  {
   "attachments": {
    "image-2.png": {
     "image/png": "iVBORw0KGgoAAAANSUhEUgAAAIYAAADrCAYAAACsE+4VAAAXBklEQVR4nO2dTWsb19+Gbz08q+oD2MExkUzIpgSMF34rxUTQZVH+Y2yoTAiiy1JCSgmB2BGyZQimtJTyLP+IEKSCglWLLgsyplSyvTCG0E0okoItJH2A6XaexTkzc2b0m5FsjRQn/l0giDUzZ85o7vPmWHOFDMMwwDAu/ud9V4C5mnAwGBIOBkPCwWBIOBgMCQdDUt0KIRTaRtV843Aby7+2h3Oyw22EQiFsH15wv/M8lreqvocEhsF0c5YzNMDQ8q33XROFipEBDGxWRnK2axeMyiYMQL5WckbL8X7GqJg3wHzJG9HKa+Rx/ufJGOZtFMdrRu7MMIxqxgBgZKrqNvOc9jH2fi0jt9Jdb8/jAuB6BUO9Ia5ewXEj3T2G40b22XKrGTsIhryxZqA86+Eq2++8fscFwP+OZsC6WqwvhICqgV0j0df+1T/WAWQQmweABcQ2Abypo40FjHsdNB9DBuvY/bONxOdl7L4GtHzMc/9i4gaW0cKuYeDZBa7lssf14npNPue/Rm5F/HN9IdTfBBBt1N8AwDoWQ+KYxecAXtdR9z1OBKj4WxnVP3dRhIblz4lY3Ezg+03xz2LiBkKhUH+T3sse1yfXKxgYR6JgwDAMtPIaAGB9QVmJeBwTvQsAGVTE0Ctfz7DQ42wLX2SA17v44bcisLKM2E2P/TZkmdUMAKCY+Ab5895Xc9nj+uFaBaP96zJCoWXkz4Hxr/5P9B4rUUR7HLfwRQbAOsqHAFDFdiiEUD/LxvkYMiii+BrQ/uMxjKhL0vlnqGwCwAyiHiEa+Lh+CWy28oHgWJVYk0P3KkJZBVArgD5WJc7z2ecxDKPHqsR+372fXXdRT8/jAiBkGPzf7kw312ooCRrx21L61XtSe7XhHoMh4R6DIeFgMCQcDIaEg8GQcDAYEg4GQ9Lzf1dDodAo6sGMgIv8ZqJnMHRdH6gyzIcJDyUMCQeDIeFgMCQcDIaEg8GQcDAYEg4GQ/LhBeN4B4lCZ6AiOoUEwuGweL04cm5sFpDw2tbnfkcv5PvhBApNxxbsmMc8KKDTZ3lqfXeO+yxvQD6sYDQLSNxLD1zG49/vo6br0PUasn/HlKAdYedOEtP71DYV7/06hQRif2dF+fvTSN7ZgbjNHRQexHCarUHXdZQ/TWLKCoDPeY93MJWcRlnXob/N4vSeGTa/8gZnsGCoKXen2WubfF+9cHt7B4UHIv0Fq9WZH6z48EoASskp/9bsx8Qq8q9WMQYAGMPSl3GUag1Zt3c4RQpLs8q23w+6W6LPfo1aCfEvl0T5s0tIIY2DYwBooFGM4/5n4sxzsRSwdSCuzae8TuMU2FjCHABMLOG+VsLeXx3/8gJggGCIGwUzsRtA+p68ic0CEsq2WjaO9D13t+pDcQ94IFpIHGn8XOgAmMOTt1nEAcSzNehP5y5fdYsODn4vIT4VET82GyhpEcifMBaZBooNNNyHee7Xwbu/genImNwSQUQDThsdefOncWtCbpqIII5TvGv6n7dRU+qHMdz6FCLIfuUFwOWDcXyANJTEPtWh608wB6Dz1x5Kyrax1UdIoYTkq37zLC944hamAbtFB8nxDsLhKSSLKTxaFfXsNE77OtR7vwYaRY9NzQZKFy5PBO2i5QXBpYPh9yE2aiVATfNFUVrP0Jh9Al3Xoe8DMTlcjUWm+zrUez/RQ5BMRBC/cHmih7hoeUFw6WCIiymhQXRdkak4EGC3NlTULngigrgydHQap3RIPfcTN/K0Yc5KRA8yHRmTvZ/ymTQbKFk9o/d5I1PKHEj2IPGpiH95AXD5oWR2CSkA6bKccxcS1vJs7LP7iMOcJAGdws9II47sg7mu4eGoPOAq46Ic7ziWdp2/9lDS7mPJGrrMyaKcf5gTSRWf/SJTyoT1+ABpa1IZQUSzP5OjclqZVHqXNxaZViapB9izJpw+5QVBr6+q6bru/XqbNeLKV+RS+17b4kb2rb2tlo3bx2yklGNrRlaDAS1r1HTd0PWykQIMbJTlsXI71H0u/lLPD6SMstc1WefVjfIGjHi21nM/c1/quq3roervU57j89rvszziFehXFP/999+gMsi8Zz755JO+9/2wfsHFjAwOBkPCwWBIOBgMCQeDIeFgMCQcDIaEg8GQ8BN1GBLuMRgSDgZDwsFgSDgYDAkHgyHhYDAkHAyGhIPhxXkey9JU4L3dfES0U21hP0rafbw0F4RCCK3m0fYqz2U2ENYE6lHUPuUNCAeDpI38d2vw+iYAUMX25Bpmqqb75ASL8ma2f13G4pscWoYBozqDtUkzNG3kVxdxkm/BMAxU7q7hhhUAtbwWcm8WbSnN4TZuJGaEK+Ush5MFM2x+5QXAhf4QsAvTxZVTZG4ZoyJ1CnCbCJX33XI3py7CpYdYyRm5Tfq4YdDKa4a2mTE0t05CvQ4P/1hlU71m8fnYTjOlvGrG5WBzifVUHYZ1LvF52B40j/ICIJge43kd0YJp2lnH4o9RtAwDlU3FunOex/LCOrR8S7SKlXUsmt3f4bbdys5y0LButUAAwOtdIGlv+2FYPlSIen6TmMH3SW+9Tbt+Au123e7GQ3avUH8DzERNZU0U0RXgpN4Gzus4UUUzN6PQcIL6OYDzOoqKUGc8OmOpter/FKHdtrYgehco/lP3Ly8AggnGZkxooG5GocG2+URv29++aTu8YOOI/UezvWLzz2AUEqhvhRCapLpw+QHcjGIG8oMZEtXsGmaqvbVWxcQuomdiKKlsmkGuo/7a44DzuufQ1K6feG2RPraLlRcEI5tj1P8pAihibVK0shuJIiATbk6uFlGBYVSQcR/ch54qEA63sYgKns33se/m90jI1rrwRQZ4XkZV9hAkstFQjEdnvLZIH9vFyguCkQVD9B4acmeqcG4XiZttlH8rAis5tDZ6tdPhUv1jHXi+KIaHyTUUUcTaZPfKZDw6I/WabsSNPKmbW0QPMhMdl72d0tWf11FUekJNsTK26ydWY4je1pQeUvQg2u2of3kBMLJgjH++DA1F7P7ZhphRm0ss2SrkB9P+9Qesj6pSLiwroTXX0ZA727V6Bov5GDKvd1E2Vwc/rlvDafS2huJvZTl3KmPd8rVGEV0xr1+GUBmCZywZn2go5nA8Hp2RvRGA8zJ2X5vDsU95QTDY3NXPHuzSVhuG96pEHgcpsNMsq7HLcDxKv/lZzrEqca42XHV2yfPsFZZ7VaPowd3CPbU81/WpUjynEM+nvAHhP9RhSPgXXAwJB4Mh4WAwJBwMhoSDwZBwMBgSDgZDwsFgSHo60fhRSx8P/KglZmA4GAwJB4Mh4WAwJBwMhoSDwZBwMBiSKxmMoxde0hvpAAtQ8dR9btvK1Jd7rVlAwnSfuaxOXeVImxPlMPP2tEnrE2GRUutqm6CC4coFo1NIILb1nk5+vIMYysJjopcxnZxyyencdFB4mrSFMhOryOu6PF6Hvp8CIEU50ueW2te7HWbHO5hKAtm33U60oxdTSEI61lQnmqOuOsobacSujBNtABxpN1vP8Q6mkiUAJSTvyNbhsAseDLdSs08UpdYcljZU90g3ncJj7H2a8hDKdFD4JY3UvrA+Cb1VFg9nZekPsohL3YTwnj3C6gQAjGH125RUWwg/Sepb6XCbWMWjDamicNT1SjnRBuB4B7EtiNbzNot4MYnHBXGxtWwcQBzZtzqezJotMiUsgjFgdHaTIxxsqX4zF80CHien8eiBh4vp+CWSsINA4yP7oVxsEkoF5induSTvdShJ3wtjpym63/wqcQOaB9grAvHsQ9HqpDxn2IjxPoa05n1jj14lMW32Bt0liN7CbOmAtBgl8VIOTcIbJxCymp+teZUt9xHGpPQv5nxEhLWLZgGPk0D2xWq3dOeSvJ9gzD5EVn6NKn2PEs2+X8ZW88L++OUepijRrRzfn3j1Bs0D7BVNs5FkYhU/ZePW9T6uTSNuqqpmn6C8IYbPcDiMA6Ss1j/3tIxUMYmpcBjh8AGwAcWqCMtYOb2fl0NRMLynHmMMq690S70JKGpOgqFYFPvAS695VE4DWzEx77mTRAklJO/YK6nOX3soERoqM3C6riMfg0OpKSyU4vVw6hT49JZs/XN4Yk1oHyKi6juPdxC+s4f7b3XvkF6S9xIMhz9t9SfRe5BSuiXc12BPqo4PhjrH6BQSjqWil2dMvYnCDRtH9q3dYp2uVEmzgERYsTb/krZ9aw5P2xFeJktIxcRZj16oy92XSJo9UbOAxL1Tx3kDpdc3ki7jHOvnZXvDXO4wxQ0mHGSK92sj5XKkDbleimesy4nmcJmp7jPhbXO6ywgXm6dHzX0e5fqV8zi9bh5+N3aiMf3Af6jDDAwHgyHhYDAkHAyGhIPBkHAwGBIOBkPCwWBI+FFLDAn3GAwJB4Mh4WAwJBwMhoSDwZBwMBgSDgZDcvWCId1gy8OU1fRBdatHHYJ2mF0xJ9qAD5n/ODEfEu94qLxzD0VppeqoDEJpZT5o3rlfZVN9mHzQ5Q3OiHoMmeytvNBRmLqow22rJVit09Fj2PqK/BZtLAwWcb5FVFDZ9NntvI4TSzchbE2miqJdP1F0EzEsW+qIOuqWUkKV3wyhvAAY7VDSjzuNYmROtHEkCgaMXkKdoB1mH60TrV/6cKfRjM6J1g9BO8yutRNtIIbiRGsrw9rFJrtBO8yutRPt6iGHDam62v1qvPchJkE7zK6zE+2jImiH2RV0ovV8MjAjqG6F8MPtluxZFvDsLIflyRBCALBZgWH2OPPP0Mov40YoBADIVA0p2xtHolBBPXQDoQSENbJg3sagyxsc/kMdhoSHEoaEg8GQcDAYEg4GQ8LBYEg4GAwJB4Mh4WAwJOxEu0bwo5aYgeFgMCQcDIaEg8GQcDAYEg4GQ8LBYEiGHgxPb1eXP8x8er/iAFNVTsc7Q3WhUfX2dqI5PWUOv1nXdalWBel0I5xoTpOT8zpVX5pT3+FT3oAMNxiqyUivIasp3q5mAyVpMhJP8pdP0ZdmoNrbLOKW3KWDwi+nyD6gtTFBc/Qi7Otl6xQeY+/Lmqx3DVlIQxNgKa5qlkrClN10UHgQw2m21u1EwxF27iQxvd/tRBM6sGlheFKdaL7lDc5wgzH7BLpuujSErQeqB8wUuSiI9wFM3MK0+ebxSyQ/fTQc/YLz7Cg8CCOGMsob3nuNreYVI9MYlr6MS4eZrL/lGlFpoFGM4/5n0kKiOsya73AKU3xDlGeqMSaWcF+TTjS/8gJgdHOMZgE/b8HykjRqJQBpxFwKyrGIjEPzHURERtlbSMHO04udq1ErWWFo1Eq25Ebt+pvvcKo2hIkI4qYTrdlwSG1UgY7TfSIaV6nW8C8vAEYUDNFVlgApb5Fur42yZTkqmSrL2YfIIompO0mUNh5htSl7C9hj8FXSZInhMoXy0zlAWg/jsnvX91NIm11/s2FrOF1YvWT3Frz722OTT3lBMIJgiLEwDQBaFj+tjsHSOcmWOfbZfcRhqixtLZb+NGL1FkevkkC2hlo2rsjj3jPHOwjfO0X2rTmPEHW3hpnZh8iaXf9ExEPDqfSS3VvE8EvhU14QjGBVMoVkEQBSKL+6oOXPmlvYLcf7QxwtnUIC4XtAWe+tnpqOjMk5k9LVNxsomUPBRARxxb2mqjIjU3HFCSd7pKmIf3kBMJJVifCoqipKp4pbqCbtiZRAnVvYLce72x0h1krBrdc8wk5Y0Y+rDjNEELEmji7f2sQtTCONg2MA6ODg95LlSxPqTXOSeoA9a8LpU14Q9HqARnDeM5e3az/leL/LIbafcnrDFFca5RsbhhtNdZOpP5PXZfrTlHo6XG9uv5niW3Nfn9uXpvrPnNfuUx470Zh+4T/UYQaGg8GQcDAYEg4GQ8LBYEg4GAwJB4Mh4WAwJPyoJYaEewyGhIPBkHAwGBIOBkPCwWBIOBgMCQeDIRl6MKpbtvrB6ftSfF6hZUVio+giVDfY4XaXK2wU9fXUVfg4zOwyll1yHnaiSYS3i3J1VTZhYCVntMx/m96vaka83+X/Mv89/PoKN5kf3g6zVl6zrsvhM2Mnmkod9ddQ1E0mVZSfA7gbxTikz0tqGSzbj7QZAQAO/4u1u9/Lp+4Pu75ab+eHj8Os/o+tlMB8DBlLN8FONJvzOk4AFBM3nKI7+b4VGGnrOam3bduP3AdoI//jCXLJ4JQL/vUtYm2yR/fs6TATopmZqCnFiSK6Iq6LnWgK7T93UYSG3JkBw6ggg3Us9hoL579GDmu4MbmG4ub3SJzL3gL2GOwcZwPkvI4iMqgYBgyjJepBzGu8HWaih/Qum+baOdHGv9qFYezKIWABsU1YLcHnKFtJtRG1eotqdg3It9DKa1j/MeCJlsn8MxjGM2kJGkfiO7p79naYiR6ChJ1ofeC2Icr0212wxJpb2C3H+0McEpSoz9NhJm7kSd2MrehBZqLjH5wTbairklZeM2DNosXM25w5q6sSsZ85e7eOdqxEKptiBu6Y9Q+jvtbM3rU6cPDxr0pGs1w1vy3luKHqNmIpWs04L/QsZ2iynN7Lyctj6rsB5wdtBpOqj/uG2GW4r0s2jq7Pwr880XCoa/cpb0D4D3UYEv6VOEPCwWBIOBgMCQeDIeFgMCQcDIaEg8GQcDAYEnaiXSP4UUvMwHAwGBIOBkPCwWBIOBgMCQeDIeFgMCRDDYbTh+ZyhF1VJ9rxjl0nv/P5OMzs61YeOC+2sBMNAOaeml4wIXUBgHj2oXhC/lV0ojULSNw7lXVyuckceDvMOoUEYn9LJ9r+NJJ3TFkeO9EIOij8klZENlfUieZwfiiaqa79vB1mjZqtlMDsElKWboKdaN0cv0SyCKS+tUU2V9KJ5riRijTGjafDTBwzHTGvMoKIJs1N7ETr5qicBqwWAeDKOtHm8EQvA/fCCIen0PhW0VgpeMt0Gmh4fT2MnWhuzBCo9p0r6kQ73kE4fIAlOS9aKtMTUG/9lughSNiJ5uL4AGkAqdglhoIRO9Hc+ijPcdvTYSZupAg4YPYg7EQjEN1kHBFHha+mE80dhKNy2rpBDnwcZpEpe+IoGgU70ciX8Hm53WBX14mm+scsfxvhSPNzmNnONHaiMR8A/Ic6zMBwMBgSDgZDwsFgSDgYDAkHgyHhYDAkHAyGhB+1xJBwj8GQcDAYEg4GQ8LBYEg4GAwJB4Mh4WAwJBwMF6p/zNfB9pE70TgYKofbuJGAFO+0kHuz6CHLq2J7cg0z1e792r8uY/FNDi3DgFGdwdqktDqhjfzqIk7yLRiGgcpdVZLjXZ6o04yQ65zlcLJghs2vvAC48GPpL4ClpchnrL9Z1PIVxTqgqCjUp+/DrWUwfzaNBW6FRYD1VZ/8b4r73Due5QxNqYOqonBaClTdRMXIqDaCLt0EXZ63KsOnvAAYQY9RxC6+Fi1hBSgmFlH/TqRfwzoWt6oA2sh/Z7YYA5VNoJj4RrSM+WfWz9tb32DtNZCpmhaiEUAZmdiJFgSm6c/UOElboGpJlLqrZzfFOLv43FnCQjIHDUWsPy8CKzl8PT+cmo5HZ4DnP1jzguof6+R+7EQbGXISNbmL5TMDrbzr61w3E/h+U/wz810C490FBMP8M1Q2bYtiGRlSfcVOtFFxWMY6gEx1l3arHm5bvcj6wnZgblGKhQ0p6jMMfH37xHLDOrgGTrSrEQzFuwpU8d+E2klWsb2wDqzk0KoKce/isFTeh9vKsk/UI/MFMZu5GcWMJdpto/ybLeGN3rZluiLwpmg3iqgl05XDlCXa9S5PDG+muLeMXUvC61NeEAQ0iSVxyvJcqm5KnmeuSFY0y/9l+sBMF5jYb3g6b0c9FAcaO9EYBldlKGGuHBwMhoSDwZBwMBgSDgZDwsFgSDgYDAkHgyHhYDAkHAyG5P8BsHIiWbXAOOMAAAAASUVORK5CYII="
    },
    "image-3.png": {
     "image/png": "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"
    },
    "image-4.png": {
     "image/png": "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"
    },
    "image-5.png": {
     "image/png": "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"
    },
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "c13044bc",
   "metadata": {},
   "source": [
    "### 5.4.2\n",
    "Сегодня мы присоединились к стартапу, который разрабатывает сайт для бронирования отелей. Каждое посещение сайта записывается в базу данных с целью отслеживания динамики посещений. Нам поручили взять данные за январь 2022 года и дать короткий комментарий о ситуации с посещениями сайта в январе. Данные уже загружены в датафрейм _df:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "(на скриншоте первые 10 записей)\n",
    "\n",
    "Вы вызываете _df.describe() и видите статистику о наборе данных:\n",
    "\n",
    "![image-2.png](attachment:image-2.png)\n",
    "\n",
    "Первое, что вас насторожило - это количество значений:\n",
    "\n",
    "![image-3.png](attachment:image-3.png)\n",
    "\n",
    "Их всего 30, а количество дней в январе 2022 года: 31. \n",
    "Вы подозреваете, что есть пропуск и выполняете его поиск:\n",
    "\n",
    "![image-4.png](attachment:image-4.png)\n",
    "\n",
    "Отлично, есть пропуск с которым надо поработать, но это не всё! \n",
    "Вы также увидели, что минимальное значение для колонки с посещениями -1:\n",
    "\n",
    "![image-5.png](attachment:image-5.png)\n",
    "\n",
    "Как количество посещений за день может быть отрицательным? С этим вопросом вы подошли к разработчику Мише, который быстро посмотрел код счётчика посещений и сказал, что это баг. На самом деле -1 это тоже, что и 0 посещений.\n",
    "\n",
    "Только вот для нас это большая разница, если мы хотим правильно посчитать результаты. Чтобы правильно посчитать среднее количество посещений сайта за месяц, нам придется -1 заменить на 0.\n",
    "\n",
    "Задания:\n",
    "\n",
    "1) Миша сказал, что 17 января сайт не работал, поэтому NaN можно заменить на 0\n",
    "\n",
    "2) -1 тоже замените на 0\n",
    "\n",
    "3) Посчитайте среднее значение посещений за месяц\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1972fcbd",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df = pd.DataFrame(\n",
    "    {'site_visits': {'2022-01-01': 3.0, '2022-01-02': 8.0, '2022-01-03': 0.0, '2022-01-04': 9.0, '2022-01-05': 9.0,\n",
    "                     '2022-01-06': 2.0, '2022-01-07': 7.0, '2022-01-08': -1.0, '2022-01-09': 7.0, '2022-01-10': 5.0,\n",
    "                     '2022-01-11': 9.0, '2022-01-12': 1.0, '2022-01-13': 4.0, '2022-01-14': -1.0, '2022-01-15': 5.0,\n",
    "                     '2022-01-16': 5.0, '2022-01-17': None, '2022-01-18': 5.0, '2022-01-19': 6.0, '2022-01-20': 6.0,\n",
    "                     '2022-01-21': 8.0, '2022-01-22': 4.0, '2022-01-23': 1.0, '2022-01-24': 0.0, '2022-01-25': 1.0,\n",
    "                     '2022-01-26': 9.0, '2022-01-27': -1.0, '2022-01-28': 8.0, '2022-01-29': 9.0, '2022-01-30': 2.0,\n",
    "                     '2022-01-31': 8.0}})\n",
    "\n",
    "# 1\n",
    "#_df.fillna(0, inplace=True)\n",
    "#_df[_df < 0] = 0\n",
    "#_df['site_visits'].mean()\n",
    "\n",
    "# 2\n",
    "_df['site_visits'].fillna(0).replace(-1, 0).mean()\n",
    "\n",
    "# _df.mask(cond=_df['site_visits'].fillna(0).between(-1, 0), other=0).mean()\n",
    "\n",
    "# 3\n",
    "#_df['site_visits'].where(_df['site_visits'] >= 0, 0).mean()\n",
    "\n",
    "# Заменить все отрицательные числа нулями\n",
    "# _df[_df['site_visits'] < 0] = 0\n",
    "#_df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0eac40ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({\n",
    "   'pig': [20, 18, 489, 675, 1776],\n",
    "   'horse': [4, 25, 281, 600, 1900]\n",
    "   }, index=[1990, 1997, 2003, 2009, 2014])\n",
    "\n",
    "lines = df.plot.line()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "eecb8956",
   "metadata": {},
   "source": [
    "### 5.4.6\n",
    "\n",
    "Возвращаемся на завод в отдел контроля качества. За квартал было сделано 10 тестов, в каждом тесте по 3 измерения.\n",
    "Посчитайте % тестов, в которых нет ни одного выброса. Выбросом считать значения, которые меньше -1 или больше 1.\n",
    "Результат не округляйте и не добавляйте знак '%'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "4cd4c06a",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df = pd.DataFrame({'IZM_1': {'TEST #1': 0.02232427, 'TEST #2': 0.4057245, 'TEST #3': 1.43896697,\n",
    "                              'TEST #4': -0.08961166, 'TEST #5': 0.47942731, 'TEST #6': -0.1445852,\n",
    "                              'TEST #7': -1.60695384, 'TEST #8': -0.15509896, 'TEST #9': 0.59731408,\n",
    "                              'TEST #10': -0.38225769},\n",
    "                    'IZM_2': {'TEST #1': 0.06924143, 'TEST #2': -0.00535554, 'TEST #3': 0.1668628,\n",
    "                              'TEST #4': -1.19400875, 'TEST #5': -0.34500531, 'TEST #6': 0.50825417,\n",
    "                              'TEST #7': 1.92554085, 'TEST #8': -0.46557126, 'TEST #9': 1.03750377,\n",
    "                              'TEST #10': -1.02947651},\n",
    "                    'IZM_3': {'TEST #1': -0.8196085, 'TEST #2': 0.40953733, 'TEST #3': -0.34021751,\n",
    "                              'TEST #4': -0.91692505, 'TEST #5': -0.43249034, 'TEST #6': 0.07091598,\n",
    "                              'TEST #7': 1.26657643, 'TEST #8': -1.15994801, 'TEST #9': 1.31649045,\n",
    "                              'TEST #10': -0.6475169}})\n",
    "\n",
    "_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18b7a094",
   "metadata": {},
   "outputs": [],
   "source": [
    "# mask = (_df.abs() <= 1).all(axis=1)\n",
    "# float((_df[mask].count()[0] / _df.shape[0] * 100))\n",
    "\n",
    "float((_df.abs() <= 1).all(axis=1).mean() * 100)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5ba703d",
   "metadata": {},
   "source": [
    "### 5.5 Создаём матрицы фиктивных переменных"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f3f629c3",
   "metadata": {},
   "outputs": [],
   "source": [
    "cinema =  ({'Film': ['Анчартед', 'Доктор Стрендж', 'Соник 2', 'Одиннадцать мужчин', 'Тор', 'Мистер Нокаут', 'Я краснею'],\n",
    "            'Durations': [115, 126, 122, 121, 119, 118, 100],\n",
    "            'Genre': ['боевик', 'фантастика', 'боевик', 'драма', 'фантастика', 'спорт', 'приключения']})\n",
    "df = pd.DataFrame(cinema)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "48e3685d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a995bb6a",
   "metadata": {},
   "outputs": [],
   "source": [
    "m = pd.get_dummies(df['Genre'])\n",
    "m"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b8868e53",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[['Film', 'Durations']].join(m)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "93106753",
   "metadata": {},
   "outputs": [],
   "source": [
    "pd.get_dummies(df, prefix='Genre_', columns=['Genre'])"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "77c57918",
   "metadata": {},
   "source": [
    "#### Несколько жанров "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "572e7e13",
   "metadata": {},
   "outputs": [],
   "source": [
    "films = pd.DataFrame([['Анчартед', 115, 'боевик|приключения'], ['Доктор Стрэндж', 126, 'фантастика|боевик|приключения'],\n",
    "                      ['Соник', 122, 'боевик|приключения'], ['Одиннадцать', 121, 'драма|спорт'],\n",
    "                      ['Тор', 119, 'фантастика|боевик'],['Мистер нокаут', 118, 'спорт'], ['Я краснею', 100, 'приключения']],\n",
    "                      columns=['Film', 'Duration', 'Genre'])\n",
    "films\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4ad5e58",
   "metadata": {},
   "outputs": [],
   "source": [
    "genres = pd.unique('|'.join(films['Genre']).split('|'))\n",
    "genres"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b9a8d7a",
   "metadata": {},
   "outputs": [],
   "source": [
    "m = np.zeros((films.shape[0], len(genres)), dtype='int')\n",
    "matrix = pd.DataFrame(m, columns=genres)\n",
    "\n",
    "for i, g in enumerate(films['Genre']):\n",
    "    idx = matrix.columns.get_indexer(g.split('|'))\n",
    "    matrix.iloc[i, idx] = 1\n",
    "\n",
    "films[['Film', 'Duration']].join(matrix.add_prefix('genre_'))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0cc835fd",
   "metadata": {},
   "source": [
    "#### Разбитие на интервалы по Duration"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9709e2a2",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = pd.get_dummies(pd.qcut(films['Duration'], 2))\n",
    "\n",
    "films.join(d)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a784a9a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# - films.drop(column='Film')\n",
    "# + films.drop(columns=['Film'])\n",
    "# + films.drop('Film', axis=1)\n",
    "# - films.drop('Film', axis=0)\n",
    "# films"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c596fb0c",
   "metadata": {},
   "source": [
    "### Задание 5.5.1"
   ]
  },
  {
   "attachments": {
    "image-2.png": {
     "image/png": "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"
    },
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "f84efe2b",
   "metadata": {},
   "source": [
    "#### Сегодня мы работаем с данными некоторого онлайн-кинотеатра:\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "account - аккаунт пользователя\n",
    "lang - предпочитаемый язык озвучки фильма у пользователя\n",
    "tarif - активный тариф пользователя\n",
    "\n",
    "Постройте две матрицы фиктивных переменных: одну для lang, а вторую для tarif. Объедините их с исходным датафреймом. А затем удалите столбцы lang и tarif. \n",
    "\n",
    "<b>Результат:</b>\n",
    "\n",
    "![image-2.png](attachment:image-2.png)\n",
    "\n",
    "<b>Важные дополнения:<br></b>\n",
    "-Если у пользователя пропущен тариф, то установите тариф regular.\n",
    "-Добавьте префиксы чтобы было понятно откуда взялись фиктивные (дамми) переменные\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f6747de3",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df = pd.DataFrame({'account': ['ivan333@gmail.com', 'matvey443@mail.ru', 'jeck44@meil.ru', 'katy4443@mail.ru', 'roma443@mail.ru'],\n",
    "                   'lang': ['ru', 'en', 'jp', 'ru', 'kz'],'tarif': ['demo', 'demo', 'regular', 'regular', np.NaN]})\n",
    "_df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d11c152d",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df.fillna('regular',inplace=True)\n",
    "_df[['account']].join(pd.get_dummies(_df[['lang', 'tarif']]))\n",
    "\n",
    "# pd.get_dummies(_df, columns=['lang', 'tarif'])\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "13b66487",
   "metadata": {},
   "source": [
    "### Задание 5.5.3\n"
   ]
  },
  {
   "attachments": {
    "image-2.png": {
     "image/png": "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"
    },
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "9e642944",
   "metadata": {},
   "source": [
    "#### Датафрейм с прошлого задания немного усложнился:\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "теперь в столбце lang несколько языков. \n",
    "Доработайте алгоритм, который вы сделали для предыдущего задания, с учётом нескольких языков. \n",
    "\n",
    "<b>На выходе должен получиться датафрейм:</b>\n",
    "![image-2.png](attachment:image-2.png)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "33a2e3de",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df = pd.DataFrame({'account': {0: 'ivan111@gmail.com', 1: 'ivan000@mail.ru', 2: 'jack123@mail.ru', 3: 'petr432@yandex.ru', 4: 'jack000@yandex.ru', 5: 'andrey111@yandex.ru', 6: 'ivan000@gmail.com', 7: 'jack432@yandex.ru', 8: 'ivan123@yandex.ru', 9: 'jack432@mail.ru'}, \n",
    "                    'lang': {0: 'ru', 1: 'en,jp', 2: 'jp,en', 3: 'ru,en', 4: 'jp,ru', 5: 'en,kz', 6: 'en,jp', 7: 'ru,kz', 8: 'ru,en,kz', 9: 'kz,jp'}, \n",
    "                    'tarif': {0: 'demo', 1: 'demo', 2: 'regular', 3: 'regular', 4: 'demo', 5: 'premium', 6: 'premium', 7: 'premium', 8: 'regular', 9: 'regular'}})\n",
    "_df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5a6a00bd",
   "metadata": {},
   "outputs": [],
   "source": [
    "lang = _df['lang'].str.get_dummies(',').add_prefix('lang_')\n",
    "tarif = pd.get_dummies(_df['tarif'], prefix='tarif')\n",
    "\n",
    "_df[['account']].join([lang, tarif])\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "48687b25",
   "metadata": {},
   "source": [
    "### Задание 5.5.5"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "d94de640",
   "metadata": {},
   "source": [
    "#### Теперь всё наоборот! Преобразуйте матрицу dummy переменных в столбец tarif:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "На вход функции solution подается датафрейм слева, а должна вернуть датафрейм справа"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5f13b66f",
   "metadata": {},
   "outputs": [],
   "source": [
    "_dum = pd.DataFrame({'account': {0: 'ivan111@gmail.com', 1: 'ivan000@mail.ru', 2: 'jack123@mail.ru', 3: 'petr432@yandex.ru', 4: 'jack000@yandex.ru', 5: 'andrey111@yandex.ru', 6: 'ivan000@gmail.com', 7: 'jack432@yandex.ru', 8: 'ivan123@yandex.ru', 9: 'jack432@mail.ru'}, \n",
    "                     'tarif_demo': {0: 1, 1: 1, 2: 0, 3: 0, 4: 1, 5: 0, 6: 0, 7: 0, 8: 0, 9: 0}, \n",
    "                     'tarif_premium': {0: 0, 1: 0, 2: 0, 3: 0, 4: 0, 5: 1, 6: 1, 7: 1, 8: 0, 9: 0}, \n",
    "                     'tarif_regular': {0: 0, 1: 0, 2: 1, 3: 1, 4: 0, 5: 0, 6: 0, 7: 0, 8: 1, 9: 1}})\n",
    "_dum"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6bdb03e7",
   "metadata": {},
   "outputs": [],
   "source": [
    "# cols = [i[6:] for i in _dum.columns[1:]]\n",
    "# _dum['tarif'] = ['NaN'] * 10\n",
    "# for i, k in enumerate(_dum.columns[1:-1]):\n",
    "#     _dum.loc[(_dum[k] == 1), ['tarif']] = cols[i]\n",
    "# _dum.drop(['tarif_demo','tarif_premium','tarif_regular'], axis=1)\n",
    "\n",
    "_dum['tarif'] = [i[6:] for i in _dum.iloc[:,1:].idxmax(axis=1)]    \n",
    "_dum[['account', 'tarif']]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d3e71aee",
   "metadata": {},
   "outputs": [],
   "source": [
    "_dum[['account', 'tarif']][_dum['tarif'] == 'demo']"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "d216475c",
   "metadata": {},
   "source": [
    "### Задание 5.6.1 \n",
    "В этом уроке мы будем работать с данными одной автотранспортной компании:\n",
    "![image.png](attachment:image.png)\n",
    "<p>\n",
    "driver - ФИО водителя<br>\n",
    "car - номер транспортного средства<br>\n",
    "car_type - тип транспортного средства<br>\n",
    "fuel_rate - потребление топлива на 100 км.<br>\n",
    "</p>\n",
    "\n",
    "Отфильтруйте датафрейм так чтобы в нем остались водители, которые не были уволены.<br> \n",
    "Для этого выполните проверку на вхождение слова 'уволен' в столбце driver.<br> \n",
    "Для Орлова Б.А. уберите надпись 'Водитель'\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1c0e50c4",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {'driver': {0: 'Петров А.Б', 1: 'Скворцов М.В.', \n",
    "                2: 'Адреев Н.И.', 3: 'Водитель Орлов Б.А.',\n",
    "                4: 'Михайлов Д.В. (уволен 01.01.2022)',\n",
    "                5: 'Торетто Игорь Степанович (уволен за превышение скорости 01.01.2022)'},\n",
    "            'car': {0: 'Б432АВ', 1: 'М012ГД', 2: 'В122УВ', 3: 'А4212ЛД', 4: '432ЯАВ', 5: '432А'},\n",
    "            'car_type': {0: 'Грузовик', 1: 'Легковая', 2: 'Автобус', 3: 'Автокран', 4: '?', 5: '?'},\n",
    "            'fuel_rate': {0: '14.2', 1: '9,8', 2: '19.4', 3: '25,6', 4: '7.8', 5: '5.5'}}\n",
    "\n",
    "df = pd.DataFrame(d)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ae777da",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = df[~df.driver.str.contains('уволен')]\n",
    "df.driver = df.driver.str.replace('Водитель ', '')\n",
    "df\n"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "fc51c588",
   "metadata": {},
   "source": [
    "### Задание 5.6.2\n",
    "Продолжаем работу с датафреймом:\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "Выполните проверку ошибочных номеров.<br> \n",
    "Номер должен состоять из 6 символов, а первый обязательно буква.<br>\n",
    "Отсортируйте датафрейм так чтобы остались записи с ошибочными номерами.<br> \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8465449c",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {'driver': {0: 'Петров А.Б', 1: 'Скворцов М.В.', \n",
    "                2: 'Адреев Н.И.', 3: 'Водитель Орлов Б.А.',\n",
    "                4: 'Михайлов Д.В. (уволен 01.01.2022)',\n",
    "                5: 'Торетто Игорь Степанович (уволен за превышение скорости 01.01.2022)'},\n",
    "            'car': {0: 'Б432АВ', 1: 'М012ГД', 2: 'В122УВ', 3: 'А4212ЛД', 4: '432ЯАВ', 5: '432А'},\n",
    "            'car_type': {0: 'Грузовик', 1: 'Легковая', 2: 'Автобус', 3: 'Автокран', 4: '?', 5: '?'},\n",
    "            'fuel_rate': {0: '14.2', 1: '9,8', 2: '19.4', 3: '25,6', 4: '7.8', 5: '5.5'}}\n",
    "\n",
    "df = pd.DataFrame(d)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d54b890a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df[(df.car.str.len() != 6) | (~df.car.str[0].str.isalpha())]\n",
    "\n",
    "# regex\n",
    "#df[~df.car.str.contains(r'\\b[а-я][\\w]{5}\\b', case=False, regex=True)]\n"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "dc3c5a70",
   "metadata": {},
   "source": [
    "### Задание 5.6.3\n",
    "Продолжаем работу с датафреймом:\n",
    "![image.png](attachment:image.png)\n",
    "В столбце fuel_rate содержится информация о потреблении топлива.<br>\n",
    "Определите среднее потребление топлива. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "74ad045b",
   "metadata": {},
   "outputs": [],
   "source": [
    "d = {'driver': {0: 'Петров А.Б', 1: 'Скворцов М.В.', \n",
    "                2: 'Адреев Н.И.', 3: 'Водитель Орлов Б.А.',\n",
    "                4: 'Михайлов Д.В. (уволен 01.01.2022)',\n",
    "                5: 'Торетто Игорь Степанович (уволен за превышение скорости 01.01.2022)'},\n",
    "            'car': {0: 'Б432АВ', 1: 'М012ГД', 2: 'В122УВ', 3: 'А4212ЛД', 4: '432ЯАВ', 5: '432А'},\n",
    "            'car_type': {0: 'Грузовик', 1: 'Легковая', 2: 'Автобус', 3: 'Автокран', 4: '?', 5: '?'},\n",
    "            'fuel_rate': {0: '14.2', 1: '9,8', 2: '19.4', 3: '25,6', 4: '7.8', 5: '5.5'}}\n",
    "\n",
    "df = pd.DataFrame(d)\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5aea4142",
   "metadata": {},
   "outputs": [],
   "source": [
    "#df1 = df['fuel_rate'].map(lambda f: float(f.replace(',', '.'))).mean()\n",
    "\n",
    "df1 = df['fuel_rate'].str.replace(',','.').astype(float).mean()\n",
    "df1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6af55592",
   "metadata": {},
   "source": [
    "#### Создайте список индексов столбцов и строк для 3 самых больших значений в предлагаемом датафрейме.\n",
    "\n",
    "Sample Output:\n",
    "\n",
    "[(5, 7), (6, 4), (2, 5)]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9d223da0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(np.random.RandomState(30).randint(1, 101, size=(8, 8)))\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d2f29ab0",
   "metadata": {},
   "outputs": [],
   "source": [
    "#df.columns.to_list()\n",
    "#df.index.to_list()\n",
    "\n",
    "#df.unstack().nlargest(3).index.tolist()\n",
    "df.unstack().sort_values()[-3:].index.tolist()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3de58dbb",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({\"vals\": np.random.RandomState(31).randint(-30, 30, size=15), \n",
    "                   \"grps\": np.random.RandomState(31).choice([\"A\", \"B\"], 15)})\n",
    "\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0081afa4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['patched_vals'] = df.vals\n",
    "#df.groupby(['grps']).mean()\n",
    "# df = df.groupby(['A']).sum().squeeze()\n"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "939bb73c",
   "metadata": {},
   "source": [
    "### Определите имя столбца с наибольшим количеством строковых максимумов. \n",
    "![image.png](attachment:image.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e898c9d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(np.random.RandomState(30).randint(1,100, 40).reshape(10, -1))\n",
    "\n",
    "df.isin(df.max(axis=1)).sum().idxmax()\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e3d7fc9f",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "ef4dfe56",
   "metadata": {},
   "source": [
    "### Определите название станции, на которой было наибольшее количество входов за 4 квартал 2021 года"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "199455e0",
   "metadata": {},
   "outputs": [],
   "source": [
    "# header = 0:  первая строка в csv - english names \n",
    "# header = 1:  вторая строка в csv - russian names \n",
    "\n",
    "df = pd.DataFrame(pd.read_csv('Пассажиропоток_МосМетро_2.csv', sep=';', header=1))\n",
    "\n",
    "# max_vxod = df.loc[(df['Год'] == 2021) & (df['Квартал'] == 'IV квартал') & (df['Входы пассажиров'] == df['Входы пассажиров'].max())]\n",
    "# print(max_vxod[['Квартал','Станция метрополитена','Входы пассажиров']])\n",
    "\n",
    "# df.query(\"Год == 2021 & Квартал == 'IV квартал'\").sort_values('Входы пассажиров',ascending=False)[['Год','Квартал', 'Станция метрополитена', 'Входы пассажиров']]\n",
    "\n",
    "df.query(\"Год == 2021 & Квартал == 'IV квартал'\").sort_values('Входы пассажиров',ascending=False)[['Год','Квартал', 'Станция метрополитена', 'Входы пассажиров']].head(1)\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "016f64c9",
   "metadata": {},
   "source": [
    "### Определите сколько всего было входов по всем станциям за всё время (сумма по столбцу IncomingPassengers)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "acdb765d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "#df = pd.DataFrame(pd.read_csv('Пассажиропоток_МосМетро_3.csv', sep='|', skiprows = [0,1,2,3,4,6], nrows=920))\n",
    "#df = pd.DataFrame(pd.read_csv('Пассажиропоток_МосМетро_3.csv', sep='|', header=5, skiprows=[6,903,1380]))\n",
    "df = pd.DataFrame(pd.read_csv('Пассажиропоток_МосМетро_3.csv', sep='|', header=1, comment='#'))\n",
    "df['Входы пассажиров'].sum()\n",
    "#df\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3484f623",
   "metadata": {},
   "source": [
    "### В столбце IncomingPassengers присутствуют пропущенные значения: 0, NULL, None, не указано\n",
    "\n",
    "2) определите разделитель и загрузите данные в датафрейм. На этапе загрузки сконвертируйте 0, NULL, None, не указано в NaN\n",
    "\n",
    "В столбце OutgoingPassengers нули не должны сконвертироваться в NaN!\n",
    "\n",
    "3) С помощью функции pd.isnull определите количество записей, у которых пропущено значение в столбце IncomingPassengers\n",
    "\n",
    "В ответе укажите число строк в которых пропущено значение в столбце IncomingPassengers "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3ac8f81d",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "\n",
    "df = pd.DataFrame(pd.read_csv('Пассажиропоток_МосМетро_4.csv', sep='|', header=1, na_values={'Входы пассажиров': [0, 'NULL', None,'не указано'], 'Выходы пассажиров': ['NULL', None, 'не указано']}))\n",
    "\n",
    "df['Входы пассажиров'].isnull().sum()\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "raw",
   "id": "8f638703",
   "metadata": {},
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a7027912",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "\n",
    "#with pd.read_csv('Пассажиропоток_МосМетро_2.csv', sep=';', header = 0, skiprows=1, iterator=True) as reader:\n",
    "#    reader.get_chunk(100)\n",
    "\n",
    "r = pd.read_csv('Пассажиропоток_МосМетро_2.csv', sep=';', header = 0, skiprows=1, chunksize = 300) \n",
    "\n",
    "for df in r:\n",
    "    print(df[['Станция метрополитена', 'Линия', 'Год', 'Квартал','Входы пассажиров']])\n",
    "    input('--------------')\n",
    "\n",
    "    \n",
    "#f = pd.read_csv()\n",
    "\n",
    "#f[(f['Год'] == 2021) & (f['Станция метрополитена'] == 'Митино')]\n",
    "\n",
    "#f[(f['Год'] == 2021) & (f['Станция метрополитена'] == 'Митино') & (f['Квартал'].notnull())].to_csv('МосМетро_2.csv', columns=['Станция метрополитена', 'Линия', 'Год', 'Квартал', 'Входы пассажиров','Выходы пассажиров'], index=False)\n",
    "\n",
    "#print(f[['Год','Квартал','Станция метрополитена','Входы пассажиров','Выходы пассажиров']].value_counts(ascending=True), 'rows OK')\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "cc406b7a",
   "metadata": {},
   "source": [
    "### from IPython.core.display import display, HTML"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "425dc8ec",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "display(HTML('<h1>Hello !</h1>'))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "54d4ba3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(np.random.randn(2, 2))\n",
    "html = df.to_html(float_format=\"{0:.10f}\".format)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f7d6fe0",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "display(HTML(html))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "0b047442",
   "metadata": {},
   "source": [
    "### Вы оказались в аналитическом отделе некоторой социальной сети, которая объединяет людей занимающихся благотворительностью. Для вас подготовили выгрузку пользователей в формате csv. Загрузите файл в датафрейм и оставьте только пользователей женского пола. Сохраните датафрейм в формате csv без индекса и в кодировке utf8. Оставьте только две колонки: username и mail Разделитель значений: точка с запятой. Порядок записей не меняйте. Ответ загрузите на степик."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db545756",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "df = pd.read_csv('users.csv', sep=';', nrows = 50)\n",
    "\n",
    "\n",
    "df[df['sex'] == 'M'].shape[0]\n",
    "\n",
    "#(df['sex'] == 'M').sum()\n",
    "#df.query(\"'sex' == 'M'\")\n",
    "#df[df['sex'] == 'F'].to_csv('users_female.csv', sep=';', columns=['username', 'mail'], encoding='utf-8', index=False)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "9982e3ca",
   "metadata": {},
   "source": [
    "### Вася сделал для нас выгрузку в формате csv, но забыл рассказать про кодировку. Определите в какой кодировке сохранена выгрузка."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6e0b072e",
   "metadata": {},
   "outputs": [],
   "source": [
    "import chardet as chd\n",
    "f = open('Пассажиропоток_МосМетро.csv', 'rb')\n",
    "chd.detect(f.read(8192))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "63d2c193",
   "metadata": {},
   "outputs": [],
   "source": [
    "n = int(input())\n",
    "s = '*'\n",
    "\n",
    "for i in range(1, n + 1):\n",
    "    print(' ' * (n - i),  s * (i * 2 - 1), ' ' * (n - i))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cf31b4e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_csv('users.csv', sep=';')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ae4a68f4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "52466f32",
   "metadata": {},
   "source": [
    "Скачайте набор данных в формате JSON. Набор данных позволяет получить информацию о видах билетов и тарифах на проезд в метрополитене и монорельсе, наземном пассажирском транспорте и пригородном железнодорожном транспорте города Москвы.\n",
    "\n",
    "Источник данных: Портал открытых данных Правительства Москвы: Тарифы на проезд в городском пассажирском транспорте\n",
    "\n",
    "Скачайте файл JSON. Загрузите данные в датафрейм и определите самый дешевый тариф. Стоимость указана в столбце TicketCost, а наименование тарифа NameOfTariff\n",
    "\n",
    "В поле ответа вставьте значение из столбца NameOfTariff\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7b35893f",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://stepik.org/media/attachments/lesson/755302/data-399-2022-07-01.json'\n",
    "df = pd.read_json(url, encoding = 'Windows-1251')[['TicketCost', 'NameOfTariff', 'TypeOfTransport']]\n",
    "\n",
    "#df.iloc[df.TicketCost.idxmin()].NameOfTariff\n",
    "#df.NameOfTariff[df.TicketCost==df.TicketCost.min()]\n",
    "\n",
    "df.loc[df['TicketCost'].idxmin(), ['NameOfTariff', 'TicketCost', 'TypeOfTransport']]\n",
    "\n"
   ]
  },
  {
   "attachments": {
    "%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png": {
     "image/png": "iVBORw0KGgoAAAANSUhEUgAAAXAAAAI/CAYAAABu/4IbAAAgAElEQVR4XuydB3hUVfrGP0iAAAkhNGEltD9dpKgUwUW6ICBKQKQKgsKCoCgCBlCkt7UhICzFBaUqSKii1EWqtMAiRUpEMNQkQEJ6/vc97Bknk5nMzJk7uTOT7+zjA8vcc+fOe+793e++57vny3PmzJkM4uaUAlUr3c20/bYdd6hNi2IO78PZ7R3eMW/ICrACuUqBPAxw58ebAe68ZtyDFWAF9FeAAa6gqTMAv/JHDEVsPEbR1+MoJSWNnm5YmQoWLudUxK5wiNyFFWAFcoECDHCFQXYU4L/9dp2+XrGfEpNSTd/CAFcQnLuwAqyAVQW8HuCJiYn0n//8hzZv3kzXrl2j559vR6++2tetw+0owL9evp9Onb5Kj5QqQl3D6lPZR0PEcbEH7tbh4Z2zArlGAa8EeEZGBkVHR9O2bT/Qzp276MGDB6YB8xSAJyam0vyFO+nmrXv0SpeGVKvWo6ZjZIDnmuuLfygr4FYFvBLg9+/fp1mzZtGvv/5KJUuWpJ49e9LJkydp+/btHhOBJyQk0YJFe+h+fCL9443mVLxYIAPcracy75wVyH0KeCXAhQ2xbZs2KZhCLVu2pICAAPr3v7/SbJQtDPDcdw7zL2YFcq0CXgtwyxFjgOfac5h/OCuQaxVggCsMvSOTmLBQ5i/cTfHan2yhKIjMXVgBVsCuArke4AcOHMhWpEaNGmX53B7Ak5NSaNd/ztHuPWfob38Lodf7/Z3yF8jHHrjd05E3YAVYAWcUyPUAx2RoWloapab+lasNAf39/cnPz49GjBjhMMDPnoumb7S872TthZ28efNSqZJB9ErXBlS6dHCmfXAWijOnKG/LCrACthTI9QC/ePEinT9/niIjIzNpVLt2bapSpQpVqlRJGeDFixWml7s0oNCyD/O/ZWOA8wXJCrACeiiQ6wEeUKAAnT13jo4fP05//vmn0LRMmTJUt25dqla1qvYWZZLDAJcb3o17QOs2HNX2e53KlC5CA/s/yxaKHmcr74MVYAUyKZDrAZ4nTx4hSJIG6o0bN4q/d+jQgQpoYEfDS0OWzZ4Hju3jYhNonvYiT3JymuaBN9VuCkU5AueLjxVgBXRVINcDHGrCrwaoL126JMStWLEiAezp6elWxXYE4PJFnjt37lPP7k9r0XxpBriupy7vjBVgBRjg/zsHAOwC+fM/jMaTk61G3vJ0YYDzhcMKsAKeoIDXAly+uJOdiBUqVKDw8HAKDs6cBeKq8AxwVxXk/qwAK6CHAgxwBRUZ4AqicRdWgBXQXQGvBbjuSjixQwa4E2LxpqwAK+A2BRjgCtI6AnC8jblg8R4tNTGWXur0JD31ZAXTN3EeuILo3IUVYAWyKMAAVzgpHAE4dvvt2iP0y9FLVKRIAL3cuT5VrvyI+DYGuILo3IUVYAUY4HqcA5YA/8++WHqiThAVLuyXaffR0XG0ZNleitNe7JGt/pP/R6UeqUh/b/xXXrgex8T7YAVYgdynAEfgCmNuCfDzvyVQcmoGPVa9cJa93bh5lzZtiaSLl26KosbVqpWnZ55+jKpULqTwzdyFFWAFWIG/FGCAK5wNlgDHLg4fvUuFCvlRhdCALJE4Po+PT6PLVxIpISGN6j9RROFbuQsrwAqwApkVYIArnBHWAI7dIBKPvpFMDxKzvsFZMCAvlS6VnyNvBb25CyvAClhXgAGucGbYArjCrrgLK8AKsALKCjDAFaRjgCuIxl1YAVZAdwXyREdHZ11uT/ev8a0dPvLIw3RAbqwAK8AKGKkAA1xBfQa4gmjchRVgBXRXgAGuICkDXEE07sIKsAK6K8AAV5CUAa4gGndhBVgB3RVggCtIygBXEI27sAKsgO4KMMAVJGWAK4jGXVgBVkB3BRjgCpJ6CsCnTp1KX3zxBdWqVYsWzJ+vrbHyCI0aNYq+++47at++Pc2aNUtbSIvf+lQYYkO7PHjwwDSOLVq0EGOcmppKb7zxBh04cIAGDBhAH3zwAfn5ZV57x6iDPnnyJG3bto1u375FaWnp9NJLL1GjRo2MOhynvzchIYHma9ePlpGnvU1diKpqxcxfeOEF7Y3qrEtjOL1zN3dggCsI7CkA//zzz2n69OniYlmwYIE4+STAw8LCxGcFCxZU+IXcxUgFkrWSfuPGjaOvv/6a5DgCMhLgb775Jr3//vtGHqLpu3FDiYhYL8AtmyXAX3vtNVq7dq22qFucRxwzKnR17tyZFi9eLI7HHODyAP/2t7/R66+/Lq4pT25eDXCc6D/99KN2Am0QBYn9/f3piSeeoF69eom7qKw4r/cAeArAly9fTu+9954J4MWLFycZlTPA9R71nN2f5Tji2+XN2VMAnpSUJAKHP/74g/7v//6PunTpQsWKFcskFOAd/ccFGtSrPYUUDcpZEW18W0zsPfry601Uuuz/mSCOTVNSUujo0aO0efNm7e/J2u/pKnjiyc1rAX79+nVhEURGRmbRFyDHSd62bVu3QNzTAG5ul8gL/x//+AeNGTPGLb/fk09oXzk2OY7SLkGwIgGOJysEKUa3O3fu0Lx584S9g2gVUatlK1q0KC35+D2Pgbc8PkC83zszKTY2Nssxr1q1SoC8ceOnqVOnF42WOdvv90qA44SBL7hlyxZq3bo1vfrqq1SyZEm6e/eueOxcv349VapUiSZMmCD+Xe/mKQD/8ccfqW/fvqbHbNgl0lbxlChNb+1zy/7+9a9/0fjx40UgArvE3FaZOXMm9ejRw3Apbt++TXPnzqXAwEAaOHCgVbsBT8HbV88y/FitHUDLl0dQRkbWF9FhC61bt44B7s5RQwS+d+9eevHFFzNN5ty4cUNEnr///jtNmzaN6tWr59BhjBgxgho0aEAvv/yy3e09BeA///yzOF5zu0TaKtYALqM6awA4e/asiKLq1q1r1Tu/efMmffXVV7Rp0yY6f/48BQUFUfPmzalPnz7UsGFDyps3bxbd4uPjxQ11w4YNdOzYMYJuzzzzDA0ZMkRbF71alu3l78Hxde/eXfT59NNPaf/+/QR7CFFn//79Tb6+nOy7evWqeJS/du2aAMrOnTvFvnFzf+edd6hixYpZvgvnT0REBOEmiKe4e/fuUZUqVcTkL26K5jd+qU27du2ETQCwHjlyhPCUM3jwYNq4caPQLF++fDRlyhT6+9//nun7nNUBna2NY3bjZ/6FiB6///57KlGiBMHCAGDd0RwF+E+r7AM8Iz2DEpNTKDklVfPTUymf9hSdX9OzQIF8Dh16klbCMFmzQFK04M7PD339KSB/PsqTN4/N/q26McAdEjcnN4IvN2PGDAF3ZwAeHh5OpUuXFhcxsjpCQ0NtHranANxZXVUB/uuvv9KwYcPo9OnTWb4S3ieiRUsgY0Z/5MiRtH379ix9oN8nn3xCzz77bKbPJMCHDh0q9AcoMcFk3t5991166623xE1bAvz48eMEuK5Zs4YAZvMGD/PLL7+kRx991PTPAI+cELSmIW76c7QnvPIVKoiPJcBxo8JEHG5iaPjNuKH885//NH2vzBrBRBmaig7Ojqv59ua+NP4dx/Pcc8+5skubfR0H+Mxsvz8jPV0DbxrF3YsXENcYrN0M81BQoQAKLuLYzSfu7n26l5CoedcZ2lwYCXgHBxXWbgR+GsSzBhc4oFbd3uMI3C1nhgs7hac1duxYEYEjGgKMHWkffvih8PLwqNqyZUuqXbu2VU8P+8pNAE9LS6PJkyfTsmXLhAeLyBjpVZjwgcaIPhG1Vq5c2SQzPkMfgP3VV/vQ0KHDqEyZMlpRi3gRGQJ4AKolWCXA4ZtiHBDh4zsRQe/atYvwlITIGCmTgKt5uh2+HICdOHEi1axZky5evEijR4+mffv2iZuF+ZMVwIP5E+y/fv36hO/DozSeLHDuoA++Fzctc4CjH27wn2lPBd9rNh1svPz584snA9h4uPHgSUXe0FR1cOR8tbVNTgIcvxUeOJ7GsrNQfloxPduf9CApme5r8L1//wGFFC9FpUqXoahLv1HePKn0SDHHSg9evxNL6Rn+VL5iZboR/SfF3L6hPXkUpEDtJlCwQH6r39+q+6hsAQ529O7d25XhcHtfr/TAs1MFEAA8nnrqKXEBO5oGhLxaXMTpWjQQEBAgHofR31rLTQCXkIQviFxZRyypU6dOiQgXFwDsEBmNQktoDLsD8xMAeMeOHU0SS4DjH+DxIgKXubjyODDvgZsJUifNAd60aVMBajxFyZadnWTrHNqzZ4+4SQH4eGLBuSAj8AsXLojfg2OT+8bNArrgBgXo42lAAlxVB1ev+pywUO7fvy+yNWBzPfbYYzYnVeGB/7jcNsATErUqVYlJlJiYQoWDilKJko9oN9QQOnXqOCU/iBdRtCMN0Xv+goW1c66uNjEZQ7duXqf4e7Ha+OWjQgEFtP8CsuymdQ/rAEdgsmTJEsGC559/XmSigAee2HwK4Ii6cNHj5EIerSOwkYMC31w22AK4IPFYntsBDuAi0pR21Ntvv02AJSJPW2316tU0fPhw4Qtby5aQoLb06eW/Q3dE6ebgx3dJCwj7b9KkSSaAr1ixQhyXebP1PfYCAMt5BQlwvBSFmw+yLSTAYRMhUk/UQGQJcFUdPBEU8pjkBB/+v59fXqpQoSJ169Yty1jJ7QHwH5ZPtfmTom/FUHJSKuXxy0+1atfVAq6CGnjj6Nz5c3Qv7q5TUgQFF6GqVapqN4JgzXp7QKcij1NGWjLlL+BPpUuEZNnXcz3etxqBY8ODBw+KJAkECWgIDGw9ZTh1kDpv7DMAh/cJywSPwZhYwmO9M3ngmOlHFgcmfDD5hck82Ae5HeD4/bA+EHkiskTDEwjsB7wMgYlfy+gEcxCfffaZ3VPVFsAdzWE3j8Al1B0FOOwQpIv98MMPwtu39NrNj0ECXNg3GsAxoSoBLiNycz9eRuCqOtgVzsANzAGOievy5ctT165dhSbWmgD4N1NsHvHFqD+peKnSGiAfpYKa3eGnzTnCykzSJjNTtULhzjR//zxUQJu8RBpxmtb1gWbLREdfpds3oqlS+TJZAd4z3CbAT5w4IZ4wZJohA9yZkXBy2z///FPYJojAMalkmZniyO4QPeGRH7njiLQAczxCMcAfKoBI/MyZMwRQIjK5cuWK+PdmzZrRFE17OeGHf5ORsj3djQJ4dpOy8pj1ALiqDvZ084TPkfGDVDvYDbBQkI1kC+Bbv55kG+C/R2u2SWl6pPTftKc6P833ziPOteSUNErTMlOcaX5axkn+fNqkpbaPdOwjOY2uR1/T7BQN4OX+stbkPtv2GmsV4Mhvhy2GpyoEgrBjrWVZOXNs7trW6yPwqKgo8ah++fJlkdYFwVXExloOmFh7/PHHhda24I3PfNEDB5yRRgjbyd4r+NDmv//9r/CcEcH269dPrM0hbRXL6NTRk9daWmR2fVUicDkpiwsU2Rl48oJlJs8Za8egGoGr6uCoXkZvF6Vdc0u01FLMU8BesLbuDmC6dZltgEff1CwULdrWDBltHCpRYe0JGBPYCMbu3bvv1E8MCgoU73/gPIzXbNQLFy5q/dNESmHpklktlLa9rQMccwjffruG6tSpK+whT25eDfDffvtNTIbhcdjVNy+RliYnMe0NmLcCXL7kg3kCwFo281Q3R+0L9JXQx+MlrIWQkIcXCXKkkUuNp5lJkyZpubwF7EkqPs8JgMfExIgJVmSaWPPNke3Ss2fPTLn1qgBX1cEhsbLZKCcmMfH1Mo0Qf4dtac1GAcC3LJto82gfJCaLScwHD5IpQHvqLVq0mJbVEqjB94Lwn5EGiPzuPJRXROjJWpohWn4tTRARtpZ2IPLFkYaIp2bcjAH+2Ng7lKj1L1gwv5jELBiQdc6mXe9xuqQRYs4N66rACUD2Gt4VyKlJT68FOGb74T9ikHHyIPXPGc/blYvEWwGOF2oGDRokMjgQZeNkx00QQAe40CwBDuDBz4bnjZMTKXfQGb44AIj9wAtH+p6MwJErjTVakC+NSUwAs1y5cuKkxnhh9TrYMAClefphTgAcXjcmHvH4jyc2TLYiUwk3Mfwe3IjwUo8eFoqqDq6cmzmZRugowDcvnZDtT0pEGmF8IsVrnnVhLSUxRMtCuX49mlK0SBwv9PjlDyDkiqelJml/fxgMpCVrf/cvIHK805K1/G/NN8+nRd6PPFKaYrQslHhtDAtrnnpg4QAKsJFG+Hyfh5lnls3ZNzEtJ3Y7dw4TtktONK8EOF6Zx4s3mLDMruFNNESA1t7Ec0VcbwU48naRRSJhLTVAHi9ugnjpBpNS5haKvZdekEaHyL5GjRqZJLXnM1t7ASgnAI6DxOQl8r0tJy7xGW5uiKRwAUodVCNw7E9FB1fOTU8DOG74cycNpJAittMBAdFU8SJPAiVqb1SmaskDAHd6epr29wyqVvNx8d7B+TOnxd/Rzp4+SVWq1xRBAf7ur81+5s3rJ0Durz1NB2hvcAYHFdImNB964pYt5m48DR473+paKM4CHBzCG8fwzNFycg0VrwQ4Iht4l3jMYoA7d7lj8hHZEXiFHH4wImu82g7/Hz4m/jQHuPnkJQAL7xsNXjlyZOER2spAkJkeMl8Y/TDhhRRARO34u/l8RU4BHB4+jgnZIr/88ot4EQXZNHgZB8ck9dAD4PjNzurg3Ihm3dqTLBS8yv/nlfPUu2MjKhqcPcST/vcqfWpqugZm2CWpmr2STEVDSmgTmul0L/Y2BWt/R4uLuUVBRYuTnxaBx2p/L6RZJPnz+2ugT9Ogrdktmu9dAK/SW4F3bFw8LdtwgMqEVsm0GqFU0lmAox+e6NCPAe7q2ZsD/b01As8BafgrcpECjlgokMPT1wO3HDIVgCPtEBlaGRnpOboMrVdG4EZfIwxwo0eAv98TFECONF6lh3WApxdkgPhCW7/+e22Se79YlKxDhw7Z/iRYO6hFgCUicEPL6UIQDHCFM44BriAad/E5BWDBLVy4UKT84Zp45ZVXbK4f5A0/3rygA14mwu+RacXWjt988hKfIwsLNzK8xZ1TjQGuoDQDXEE07uKTCiCVFNk7cgIPP9Kba2LKQcJqmEi1zS4FFgBH7QEs+YA5FMztOJoyq9fJwABXUJIBriAad/FZBWAhYFXKP/+85hNFjbFMcKdOnbyiniwDXOGyYoAriMZdWAFWQHcFGOAKkjLAFUTjLqwAK6C7AgxwBUkZ4AqicRdWgBXQXQEGuIKkDHAF0bgLK8AK6K4AA1xBUga4gmjchRVgBXRXgAGuICkDXEE07sIKsAK6K8AAV5CUAa4gGndhBVgB3RVggCtIygBXEI27sAKsgO4KMMAVJGWAK4jGXVgBVkB3BRjgCpJ6CsBlzUXU8lyglQgrpa1Hgdqe3333nSgtN2vWLKtlrhR+ssd2MS+r1qJFC/riiy9EUVwUkcCrzgMGDBDl3lBxyRMalvPF69coIIG1N3Jy7Wi9fr9c7AlrcaMaE841vdfc1+tYfX0/DHCFEfYUgMsSaShCgEoyqCwjAe5MaTQFCTymC+onjhs3TiyoL38zCjVIgFsWTjbywC0X/sexWALcG5ZelQCXWgYEBIjKS1WqVDFS3lz53W4B+I0bN8TyiigagOo5KHaKArK4wGTdREu1Ub9ufUSEKMN1/fp1USgVJby6d+9OVatWtVsuDaW/UNZLFhyYNm2aKDrgjuYpAJdFcyXAUVhBRuW5BeAYX8vfjH+TNzJPAviyZcvo1KlTYuW+l19+mcqWLZvp9AS8o/+4QIN6tdfKigW549R1ep8xsffoy683Uemy/5el+MEff/wh1sDG9YqnwN69ezu9f+7gmgK6AhzVWw4fPixqVQLclg3VXlDKynLd4Fu3bgn4YmUzywaQ26t5ie9FBIb/ZMtNADe3SyTMUO9xzJgxdm98rp0+ntFb/mZplyAqlwBHVR1Eh0Y3rNb35ZdfEsra2VqmFOXHlnz8nsfAW2oGiPd7Z6bV8mOob7py5UpC+UJUdMJTILecU0BXgONODEBjYfN+/fqJqNtfq213+fJl+vjjj0UNy44dO4pistKThA+IormI1hExo5wVIhN4m1u3bqVFixaJkl2oPl+hQgWryuAk+vDDD0WRXrTIyEjKDQCHZqj+bh5tS1vFkyJPd5/OKI2GwszyN5vbKggmevTo4e5DsLt/2DrztXkKVDDProL79tWz7O7LiA1avjzCagFgWZUnMDCQAW7AwOgKcBz/wYMHRZ3D+vXrZ/o5qHcICAOyiJiwhi4a4ItIEVXLAeGSJUua+plH1qhg3qdPnywSIdJH9H7t2jVRJxO16fbu3ZsrAG6thqS0VawBHLqjGjyAh0gJE364CaAK+9NPPy0KHuMmallHEDfT//znP7R27Vo6fvw4YSIONgD6wGuG1SX7yCLIeNoaMWKEeBrbsWOHqGyCyUSMN27yd+7cEePVpUuXTN+HepV79uwRj+uHDh0SdTuxf0TXrVq1EkVsLZu13yyjcnsAR11VRJAIKNy5GL+jAP9plX2AZ6RnUOL/6kempWnV2LUgKb+mSwGtkK8jLUkrHJysBU4oAOznh77+FID6kXmzFv+V+2vVjQHuiLY5vY3uALf1A7BmMC5cgNsc4EuXLqVvvvlGgACRpHlDdXBE58eOHRNVwgF680c0AB4ZFwASgNVau8BnapkXKgAHbLAoO7xJe81TPHB7x2n5OXQHGLFQPdZvtiwKjYr0eMwHMM2bhKG170NBYGS7yNJTEuC4EcP+AhzRMG6IkuEDA+JoMnum/P+erPA0Nnv2bFGmy1rF+OHDh9Nbb71lFeLOaiG3l760PB53+biOA3xmtj8lQ7vBpYgK7vEC4hqDNT3yUFChAAouEuiQDHF379O9hEQtCyZDe0ImAe/goMLajUCr4K4FX9Zaq27vcQTukLo5u1GOARwQBoBr1qwpIm1c+LhgESEh3WvKlCnigkYDmBHpAQzwx9Hgm2Mb80nQs2fPiqgO+3zvvfdEFIWK6yoADw8PFylRmEnHcaAih63mzQBH1I2GJ6HJkyeLKiKALp6OEGEDkCNHjsz00wFVZBq0a9dORN6IgjFpPGfOHAFbmb6Hm7MEOOYzihUrJm7AsNCGDh0q/v+zzz4rbuQYS9x8MQmGY0Dbtm2bsNBQxgrj8cQTT4gIHOcOLDGAH9/Zpk0b3a6SnAQ4bo7x8fHZWig/rZie7W97kJRM9zX43r//gEKKl6JSpctQ1KXfKG+eVHqkWFGHdLl+J5bSM/ypfMXKdCP6T4q5fYMCAwtSoHYTKFggv3WAdx+VLcBhlcIahY/PLecUyBGA4yLEhYcME/NIG5kn0zXgnjt3jiZNmiRySQH1b7/9VkxIImrDYy0eweGvy20gD7xEXNSI7KU1k5SUpAxw3FSQPwz/tGXLliIKRYFSa83bAY4bHrzyGjVqmH4e7Bj46YA0Jv4KFixo9yzEhByiedhYSGOsXLmyCeC4KeNm8O6774obNJ5sAHDMaeBJR0b1EuAAG7bF/IW1pwBAHJNkzZs3F5ZZ/vzWQWP3oC02yAkLBeflrl27aPfuXdo59ajNUl2woX5cbhvgCdpEaEJikla+LIUKBxWlEiUf0YAZomW2HKfkB/EiinakIXrPX7CwFqjU1SYmY+jWzesUfy9Wu0nno0IBBbT/ArLspnUP6wDHb8OYwlaD/fb8889rNwPHngQcOVbeJnsF3A5wRNMA99y5c6l69eoiZ1dG0XFxccIHxZ+AM+7eiOh2795NKGsETxZeKqJqRHQS4NgnLABEk7BO8PiOk98VgCOSx37hwSLaRJQ5evRonwS4tcwMPM0AxnXr1nUY4DLaBshhY2HM5L/hgkbBW9wIpVePyUSMIeoGWgL8t99+Ezd33Fww3pbZDHK/GBDcLDCx7ekNmiIQQVCAeaFSpUqJDBRbRW9xDv+wfKrNnxV9K4aSk1Ipj19+qlW7rqZRQQ28cXTu/Dm6F5c16ys7fYKCi1DVKlW1G0GwZlc9oFORxykjLZnyF/Cn0iVCsnR9rsf7ViNwbAirE3UxcR7g+sHNFZk/OB+4uVcBtwIcQMREFICBuzI8UPMUQviCeIzHIzZObExAXr16VUSBgAk8VPNtJMARNQG4yA+HdSIvdlcADntHNtgLuMhwHL4YgVub2MsO4NB1586d4iKFjYGnIfMGvSwBbg51CXDziVVLgCNKh/9szfs2/y7znHf3Xhqu790S4LjpdOvWzaY9JwD+zRSbX3wx6k8qXqq0ZvU9SgU1u8NPm3PEU2NSSqr2Z4ZTB+zvn4cKaJOXsD7StK4PNFsmOvoq3b4RTZXKZ62q/lzPcJsAx811zZo1FBUVxQB3ahRc39htAAe8kbnw6aefCnjDV5Uetzxsc+Di3wBsvMwAcMo0Q3it8EPR4JsiesM+8cKOtE6s7c/ZNEI8CcA2wLG2bt1aRKKwfnI7wGFtwLOG1WGr6QFwCXl7p7Q3AVz+Fjxh4sU2PEUiMIAVZK16OQC+9etJtgH+e7Rmm5SmR0r/TYty/TTfO4+AanJKGqVpmSnOND8t4yR/Pm3SUttHOvaRnEbXo69pdooG8HKls+yqba+xNgGORIRff/1VWChIE3bEfnPmWHlb2wq4BeA4qbZv3y5sEwAR0TL8UWsNkRs8b1gliKbNfVlsL9MMkZaImwDSBQEUOblpb3CfeeYZ0c/aBWPeFy9+4AbTtm1b8eYoTkI8DuZ2gGMcBw0aJMCDGykmLKX/nJ2F4mwErmLh2Bt7T/o8NjZW2IOwU/B0aW1+RQB8mW2AR9/ULBQt2iby0yahK1Fh7drC/i5evKilgt536ucGBQWKp2GMZbw2n3ThwkWtf5pIKSxdMquF0ra3dYDL34VIHjcmXDvcck4B3QEO6MHzxsmKrA5rb16a/7wDB/ZrkfREkVNsCVprk58yHVFvgCMDAjcRZECg2YI3PvP2SUxnLBT40cgksfZmJxZkwkWLpyRXLRREqbBYsE+88GL5thZOpTsAACAASURBVK67LomcmMTEscs0QuS/2/KHAfAtyyba/KkPEpPFJOaDB8kUoAUYRYsW07K5AkU6KHL1kQaI/O48lFdE6MlamiFafi1NEBG2NsMj8sWRhogABU9OAH9s7B1CQkHBgvnFJGbBgKwTxO16j9MljRBJCsjbx9MIXszD+x086al+dusKcAB31apVYuIGg4OoFrnF2TWZTXL06FGxqhnWPkG2Av4dkTke3XExW77kY22frnjgsGzkJKY9OXMTwDGWGMfGjRuLrB9c9LBVMNGMt2vx6KyHhQLtkc2AcW7YsKGYwMZTF0CDix7rbmDiuly5UOrU6UV7Q+Tw5zmZRogbkz2Ab146IdtjT0QaYXwixWuedWEtFTdEy0K5fl1b2VCLxPFCj1/+AEKueFpqkvb3AmJfacna3/0LiBzvtGQt/1vzzfNpkfcjj5SmGC0LJV57kauw5qkHFg6gABtphM/3eTjJb9mcfRPTfF4A+2rWrJnNuSaHBzEXb6grwE+cOCGySmx5x1JnS1sDj4CY4LScHMP2WGMB1go8aXvNFYDb27f557kJ4Fj+AK9+nz59OotEsLuQsYM0QlcjcOzcEb/d3puVzowjtvUkgCMLa+6kgRRSxHY6ICCaKl7kSaBE7Y3KVC1oArjT09O0v2dQtZqPixve+TOnxd/Rzp4+SVWq1xSZVfi7vzb7mTevnwC5vxa4BGhvcAYHFdImNB964pYt5q6Wuz52vtW1UJwFOKw1ZCfBekGDtQpLiZuaAroCHLm6tlLvzA/Pmi+Nx3C82PHDDz+YVjB85pkmWv5wN5tpV5Y/mQGe/UmQ3evl2XnQgDiibWSi4LV7OVmFzCHMc8jX883TCJ31wOWRy4wXPGYjgwnfh5eqcAPv3Lkz/f3vf9d1ksyTLBRM4P955Tz17tiIigZnD/Gk/71Kn5qaroEZdkmqZq8kU9GQEtqEZjrdi71Nwdrf0eJiblFQ0eLkp0XgsdrfC2kWSf78/hro0zRoa3aL5nsXwKv0VuAdGxdPyzYcoDKhVbKsRoh9Owtw9EFyw5Ytm7VAL50BrsZtUy9dAe7isXhNd2+NwL1GYB88UEc8cPxsb1gP3Hx4VAAOOwxROHx7TIpj0TtuagowwBV0Y4AriJbLu+DJAi8g/fnnNe1JIkys7eMLTXrayHFHthIsNVsNiQF4zyNCW/f/999/Fy/uYZEy8wXsfEGTnPwNDHAFtRngCqJxF/Gyyy+//CJS7bC0gLdXsDEv6IB1a/CSkq1mOXmJyWkkLPDbmq5dGAxwBf0Y4AqicRfxyvmSJUvE0hGyeXNNTPkbAGOsWZRdXUwAHKuOIu8cyytgvSG8uMfNNQUY4Ar6McAVROMuQgFkWm3evEm8OOMrRY07deqU7eqdPPTuU4ABrqAtA1xBNO7CCrACuivAAFeQlAGuIBp3YQVYAd0VYIArSMoAVxCNu7ACrIDuCjDAFSRlgCuIxl1YAVZAdwUY4AqSMsAVROMurAAroLsCDHAFSRngCqJxF1aAFdBdAQa4gqQMcAXRuAsrwArorgADXEFSBriCaNyFFWAFdFeAAa4gKQNcQTTuwgqwArorwABXkJQBriAad2EFWAHdFWCAK0jqKQCX63ujlucCrdpLqUceEdVzsK46qhvNmjXLq2oUYnlRefxYZvSLL74QVdffeOMNQtV6rFyH+qqy4LXC0OnaBfVaUYrv9u1bYm3rl156iVB0mRsrkFMKMMAVlPYUgH/++ec0ffp0AQ0sVVqoUCETAMPCwsRn3lQhHAV6x40bJ0ryyePHOtoS4KiZiYpPntBwQ4mIWC/ALRsD3BNGJncdg9sBjio9EydOFOWyUDsRUWNwcHAWlVFUdb22TjAKImPBH6xUhlXLsORk1apVrVYLkTvBKm+oCoOlOqOiokTUhlJskyZNynaFNNWh9hSAo2oNys1JgGNNZhmVeyPAMR6Wx49/k1G5pwBcru2N5VRxTnfp0kXUceXGCuS0Am4FOGolAt6RkZHid9kCOCrMYztUqrZsADlqMmL5ScuST1jNDYWPEbEB2uYtNwHc3C6RALRWRT6nTy6V75PHL+0SROUS4HiiQEV3oxsKE8+bN0+cc6jn+Le//c3oQ+Lvz6UKuA3gKL4KsOK/1q1b05EjRygkJCRLBA4If/bZZ/Tjjz+KWotDhgyhsmXLinJLW7duFZXKEVlOmDBBVLqXDYWTly5dSitXrtSqaz8iFshv0qSJiO7zarX/3Nk8JQKHZn379jXZDbBLpK3iKdGqs+OA4sgocC2P39xW0bugsbPHJrdXKSOm+l3cjxXITgG3ARwTPB9++CHVqVNHPGJOmTJFwNXSQsF2Y8aMoXLlyontzcsrmd8EevbsSX369DH9FiwQjwmt0qVLC98UEXdONU8B+M8//yxuXOZ2ibRVbAEcmuKJCJ75/v37hV2FosEvvvgi9ejRQ4yDtYYixV999ZWwuFDkGH3atm0r/GnzCBT7x00XY9m0aVP65JNPxBjJhs9xjCNHjqRmzZrRp59+mmnMrR1/dsWYzY81pwoUM8Bz6krj77GngFsAfv/+fZo2bRpdunRJRM6IiMeOHWsV4IiiUakDIACIzBu8bUTn8NFRQxCgx0QdIIBIbePGjTR58mR6/PHH7f1OXT/3FIA7+6OgG55YcOPD5KBls+Wb42b51ltvEW62lq1mzZoi6q9Ro4bpI8x3YLxXr15Nw4cPF33z5csnPsfNA7UTYY1Z9nP291huv2zZMjp16pT4Z2Tm9O7d29VdWu3PAHeLrLxTBQV0BzgggTQ2ABZRYIcOHejy5ctWAQ77BI/FmNFHhI6LDg37OH78uEiDgz+OVqlSJbENbJh79+7RRx99RImJieLfUGNQte3atSvbrogSLZu3Ahw3RHjjACxurLgpAqywq2BxHT16VHi65pkrKP+FidKdO3eKuQhUTceTVExMjIjI586dS82bNxfjaD45/euvv9KwYcO0FLvbIgp/9tlnRSkxuS98/yuvvJLt5LSzY5pTAMfTCDzwoKAgGjhwoAgquLECRiigO8CltYHIDBcrTm5E4tYicGSeTJ8xg86dO2fKGDGfmERf1NrbsWOHeNSXWSVXrlyh8PBwqly5Mj33XBvatWu3ABAmTRHZ1a1bV0x2Afr2Go4LfrrlJKi/v7/IN8Z3+grAMTYANLJ6/vnPf1rNBrL8rdu3bxcRMywsPAHJSBrbYaxwI12/fr2A+ZNPPpmpO3KkMaeB8cCTFG7seDIbOnQovfvuu5n2ZW+cHPk8JywUPF1u3rxZPBU+9thjHjGp6og2vI1vKqArwPFYjkgMQEaEhawTNFsAR0SGvF78CVAWLVpURDa7d+8W1arffvttevTRR2mGBnlkqEiAy/3J6Nza0ADk2Hf9+vWzHTnYAtg3In7zBuhUr17dqj3jrRE4ombYGYBy165dBVwxRtlN+kJ7wHfFihXC07Zs0rO2NsEoJ6gRgSPVEeOGcbX0xb3h0sJT4rp168Sh+vnl1SbUK4oq7NZSYr3h9/Ax+oYCugEctgc8abw9J60TmfZnC+AAPjxsWCx4nMYFcvXqVWrXrp2IFAFh820sAR4bGyssGvyHiTREzEjxgqeOY4E3jsk0POraaoDX6dOn6fDhw+K70XDTAPjxFJGe/teLGnIf3gpwHD8mIJGWd/DgQfFz8BsxGdm5c2eR5WOeqgmLCjdBeNn2mq0MEdgNuBHDqipfvjx9+eWXIr/f25o5wHHO4LfgJogMKW6sgFEK6AbwixcvivQvRHTSOpE/yhbA8UIEIry9e/eKTQFseKwAuHxdGlEj7BI06YHL/SFCRjZDgQIFMukHKwXHYm67ZCcwLBT4wnjER8NkHo7F1ivb3gxw/D7ovmfPHlqzZo34E3MKsKv69+8vInTpgZu/2m7vBLUFcPju8ML37dsnvgPWzQsvvGBvdx77+bVr10Sg8fvvvwsLxTwzymMPmg/MZxXQDeCIeGfPnu2wUPBBETljshMv4yDqBfjNsxmwM5lmiIhYwvrGjRvCj8Xjq7UIW94YEFWbT47aOjhEVHjch/WDBo8YXq+16BufezvAzXUApGGp4EYqs36ef/550yYyhQ9ROPLsnWkyGwXnBm7MmMtA0zv7xJlj0mPbKO2JcYnm+eMmj0lMVybR9Tge3kfuVcBwgB84sF/zyyfS008/nSWaRmQ8Z84ckXtsnmYoAY2UNHjtltBH5I3ccEAZAC9TpoxDIyy9YFvgljvxJYDL34QXrmCtIALHjVK2DRs2iElM/Bsiacu3YW0Ja57vjSgVN1o84WA/sGswmQkA6tlyYhITxyvTCPF3ZOawjaLnKPK+nFFAN4Bn96W2LBT0kTnjSGHDK+FY+wTrSuDfEZkj8kM2ieVLPj/99JOYMK1SpYrIasCfgAuiyPnaynzwLPECESI/vVev81aAHzp0SETbePJBBg+sEoAWtgCAunbtWuFRd+zY0TScmBcAwDHRi2gTL/vgxRzc7DD5jMlfpBgC/EjxlA0T0cgBL1WqlJiYrlixoimNEDdkZKGgj55jk1NphAxwZxDD27pTAcMBjh8n/XNEzpYNb1jCWkFWiHnD5Cbe4gMorDXkOI8YMSITVPQS0lsBLt/ctKUD3urERLFlZCxhbG18sC/zxbTw/6XvDbhbet7yRR5MkMr8cL3GhQGul5K8H29RwCMADrEwWYlH7B9++EHkc8NXfOaZJtqr4t1sWiCwSJDdgH6I8hHNIVrv1KmTeE3bPGdZzwHxVoDLyUvoBbginx4ZOg0aNBCRNV7IsZwQlrph0g4pg1ifBpksmJBEBgtSC80zWMzfwoR1gslk830i4kemEiL+J554QkT8mP/Qo7GFooeKvA9vUiBHAO5NgjhyrN4KcEd+G29jXwG2UOxrxFvkjAIMcAWdGeAKovlQF7x/AF8fNhDeFHbkjV8f+vn8UzxIAQa4wmAwwBVE86EuyI5auHChmLvBuYCX0HhNcB8aYC/6KQxwhcFigCuI5mNdkJWD5QUQhcvGJdV8bJC94OcwwBUGiQGuIJoPdsHEOV5S+vPPa1zU2AfH1xt+EgNcYZQY4AqicRdWgBXQXQEGuIKkDHAF0bgLK8AK6K4AA1xBUga4gmjchRVgBXRXgAGuICkDXEE07sIKsAK6K8AAV5DUKIDjFXVHF+ZS+FnchRVgBbxMAQa4woAZBXCkrAUEBCgcMXdhBVgBX1SAAa4wqkYBHIWCLZfOVTh87sIKsAI+ogADXGEgjQI4WygKg8VdWAEfVoABrjC4RgGcLRSFweIurIAPK8AAVxhcowBulIVivo64LPggq9FjKVisC6JHoWLzGpwtWrQQy86mpqaKakwo0DFgwAD64IMPdC0C4czwr4pcRuHf9BFdhrSfTO80DacPt42kr7fPJD9/ojn9NlPryu2c2aXVbeMSY6nzwmZ0+coJKl4ilCIGHaSU9GTqOKce3YuLodrVmtPqvlspX978Ln8X78C7FWCAK4yfUQA3ykI5cuQI9e3bl+7cuSMqJKE2pgQ4ilijrmm1atUUlMzcJTk5WZTCQ3k3FJaePn06oXCHBPibb75J77//vsvfo7qDDb+upXeWhmm1UrUC2z2XUrfavU0Az6fV1V7Ufzc1Kd9UdfemfgkpCdR1SSs6c2E/VQitQ2sH7KK7SXEmgDeo1Z5W9N7o8vfwDrxfAbcD/NixYzRx4kRR9R0XO4rkohixZUvUiuuuj4gQ9S9R+QVVYRDVocQaigyb12LEPkePHm1XfVTzQYUZlPPSsxkFcKMslLNnz9Lrr79OKJggAS6j8uwAjjEHjFEa7/Tp02LlPtQ+BZAxttbqa8oiyhLgGDfU6kQRCqMB/nPUHuq/6FlKSfoL4DIqtwVwGaHbOv+CgkNow5BjFBpcPtMm3Zd1oEOnNpkAjg9lVM4A1/Nq9u59uRXgqKwDeKOMFpotgN+6dUtshxXeLBtAjsKxLVu2NF3wuRXgRlkoEuC4gUi7RAK8fv36IgIvWbJkpqGLjo4WNTH37NmTZUwB8rFjxxJW77OEuAS4tEsQlUuAIyLv1auXYVecBHh62l92iQR4YJFgWj/4KFUIqZTp+FwFuLRLEpITTAB/pdlwmtzuY8N04C/2HAXcBnCUzkL0hf9at25NeAxH0VvLCBxl0T777DP68ccfqV69ejRkyBAqW7YswQ9F+a5FixaJqt+oPl+hQgWHlDt58qQogoz9oQq6rTJhDu3MykZGReBGWSgoeoyoGTdkaZdIWwVPRwsWLMhUmR2l21BKbenSpfTcc8/RmDFjRNED2CFr1qwR5dRCQ0Np7ty5ohi1ecP+0VdG2+a2CopYo/SbUe3MrdPUdV4DSkmJN9kl0lYpHGQ9kpYA79XyPfqozQyHD314xBsU8fO/SEbb5raKs/ty+Et5Q69TwG0AlxCtU6eOqA4/ZcoUYZ1YAhzb4QIvV65clsrz5jeBnj17Emos2mvyhoDID34qIkS9m1EAN8pCQQkxAPzmzZsmgMuoHJG3JcAPHTpE/fv3p+rVq9Pnn3+e6e1R85qYiKyHDRuWaXikt25ul8io3B7A3V0T80pclPChExNjTACXUXlAgL4Al+A3t0ukrcIA1/uK9t79uQXg9+/fF1EW1ktG5Jw3b17xyGwN4IjSvvnmGwEI+J7mDREnonNYJqgyD9CjmG52Td4QAG53RN/4bqMAbpSF4uzpDWjD7pg0aSL16/dapu4opIynIxSvbt++Pc2aNUsUsNaj5VRVemeOVTUCd+Y7eNvcq4DuAEeEhQknPAojiurQoQNdvnzZKsARLSOqQooYIvRatWqJkcA+UDUdFzf8cTQ8gmMb2DC2Gvb3z3/+U/iuH3wwjho1etotI2sUwI2yUJwREU8JyBT56aef6KuvvqInn3zSNKb79u0TnyFSRrPlnzvzfebbMsBVleN+3qqA7gDHozVydWvWrEnvvfeeiJgRiVuLwJF5Mn3GDDp37pwpWwQQRtYCvHP0RdHYHTt2iMwUexklhw8fFpOhdevWFVkq9qJ11UEzCuBGWSjO6ASfG08+mLiWfjk88cWLF4unqaJFi9Jbb70lKtkgGtcrBRHH6G4LxRkd5Lb2JjE5o0RFVe4jFdAV4Lh4EVEDyLBOkHWCZgvgcXFxIiLDn4AzLm5U+969e7fIK3777bcJL4rM0CCPDJXsAA5IYLv9+/e7NfrG7zEK4N5goVj65cWKFRNPTjL9EOdF+fLlRWYJnrL0BLgnXtYMcE8cFd85Jt0ADtsDURXenpPWiUwRswVwAH/y5MnCYkFl73Xr1tHVq1epXbt2Iu8YKYTm22QH8JyKvo0EuDdYKMhUGTFihLjhDhw4kGBrYF4Ck5r4d/jd5tvkFoDzxKPvQNOTfoluAL948aJI/0LULa0T+UNtAVxGzXv37hWbAtivvfaaALifn5/4t5iYGAoPDxd/t+WBA/KYNP3ll1/cHn0bCXBvsFDMX4eXWuF8QCZSvnz5xDgimwU3aDRrOeSedIG4eiw8iemqgtw/OwV0Azii79mzZzus9tChQ8UEJy5geN6wSnChWy6X6khWyYED+zXLZqLIVHGn9y1/HFso2Q8zrCz43Y8//ri46T7xxBOZOsg0w+bNm4tslYIFCzp83njbhgxwbxsx7zpewwEu4YtXrC3T/tLS0mjOnDni9XpraYaQWqYsHj16NEeibyMjcG+wUKDP9u3badCgQeJJyhLQmKSGbYYbt7U0Q1cuH0+exMxJCwVvyW7ZskXcGF9++eUsL0u5ojH39SwFdAN4dj/LloViCWDkBWPtE0x8AcyIzDH5hRRC5A5bvq6N/jhZAYScir6NBLg3WCjQB5PSeJrauXOnePkKN188teDfkY2CNzCRKWT5ko+rlwanEZKYM5o/fz5hKQM0PNliLkLvt5FdHSvur48ChgMcP0P650gVtGxYkAowwAVv2cyjb7zkg1XycqKxhWJfZWTM4C1LLGJl2TBPgsgcT116NgY4EZ5akYIrdQ8MDBRrCWE5Cm6+p4BHAByyYrISLwDhDT1kKSBb4ZlnmmiPgN1sFvJFfjhe9oHHCu8bJ2tONKMA7i0WihwDTFbiZR6MK3K+sf5J27ZtxUQ1lk7Qu7GF8lBRnCd40sF1xADX+yzzrP3lCMA96ye7fjRGAdxbLBTXFeY9uKIA5hkwxxAVFSUWhoOFxRaKK4p6bl8GuMLYGAVwb3iRR0FO7qKjArGxsWLu4fDhQ2KvL7zQSVtSopGO38C78iQFGOAKo2EUwL3NQlGQlrsoKmA5eYkF5Bo3bkwdO3ZU3CN38wYFGOAKo2QUwNlCURisXNJFAhxzSZhfaNOmjVvmGXKJnF7zMxngCkNlFMDZQlEYLO7CCviwAgxwhcE1CuBsoSgMFndhBXxYAQa4wuAaBXCFQ+UurAAr4MMKMMAVBpcBriAad2EFWAHdFWCAK0jKAFcQjbuwAqyA7gowwBUkZYAriMZdWAFWQHcFGOAKkhoFcJ7EVBgs7sIK+LACDHCFwTUK4JwHrjBY3IUV8GEFGOAKg2sUwDkPXGGwuAsr4MMKMMAVBtcogLOFojBY3IUV8GEFGOAKg2sUwNlCURgs7sIK+LACDHCFwTUK4EZZKKh6hNJcaF9++aVYIGn58uWi0AYqvixcuJBq166toGTmLuYFkVu0aEFffPEFpaamiuVQDxw4QAMGDNDK5n1gKnjt8hc6uYNVkcso/Js+oteQ9pPpnabhJGte+vkTzem3mVpXbufkXrNuHpcYS50XNqPLV05Q8RKhFDHoIKWkJ1PHOfXoXlwM1a7WnFb33Ur58uZ3+bt4B96tAANcYfyMArhRFsqRI0eob9++dOfOHVHiDpWPJMBRXQdrT1erVk1BycxdkpOTady4caKiTFhYmKjag0WaJMDffPNNev/9913+HtUdbPh1Lb2zNIzS04mm9FxK3Wr3NgE8XwGiRf13U5PyTVV3b+qXkJJAXZe0ojMX9lOF0Dq0dsAuupsUZwJ4g1rtaUXvjS5/D+/A+xVwO8CPHTtGEydOpPj4eMLFPnXqVAoODs6iXOKDB7Q+IkIUMEZptcKFC4uoDjUyq1atSnny5MnSBzUWN27cKNY/RsUXNJRge/bZZ0WUWKZMGbeMkFEAN8pCOXv2LL3++uuEijcS4DIqtwfw33//nb755htas2aNGFfZ39bA4PxA5C0Bju1GjRolqvoYDfCfo/ZQ/0XPUkrSXwCXUbktgMsI3dbvDQoOoQ1DjlFocPlMm3Rf1oEOndpkAjg+lFE5A9wtl7VX7tStAEdJJ8A7MjJSiGML4Ldu3RLbnTlzJouIADlq+rVs2TITxLOroylBjkLIgL/ezSiAG2WhSIDjBiLtEgnw+vXriwjcvOA0KsIcOnSI/v3vf4ubK6Jo2RwFuLRLEJVLgCMi79Wrl97D6fD+JMDT0/6ySyTAA4sE0/rBR6lCSKVM+3MV4NIuSUhOMAH8lWbDaXK7jx0+bt7QdxVwG8AzMjLEozD+a926NeExPCQkJEsEjov9s88+ox9//JHq1atHQ4YMEWWg4Idu3bqVFi1aJAqyTpgwgSpUqCBGAn0++eQT2r59O3Xq1Elc1Kihie+8ceOGAAc+a9euHQ0dOlR3z9QogBtloVy7dk3YGLghS7tE2iq4QS5YsCBT0Vxzy6V9+/ZifD7++GOtSsxhuxE49j9+/HhTtG1uq8ycOZN69Ohh2NV45tZp6jqvgXb+xZvsEmmrFA6yHklLgPdq+R591GaGw8c+POINivj5XySjbXNbxdl9OfylvKHXKeA2gJ88eZIQAdepU4e6dOlCU6ZMEdaJpYWC7VBRHovQY3vzSM78JtCzZ0/q0+fhBBKsE3ihSUlJYr+WQD137pzYJyyYkSNH6l4P0CiAG2Wh3L59WwAcRYolwGVUjvGyBDjsMtxgmzVrJqrCoMiA9LHtReDSWze3S6StYg/g7i5qfCUuSvjQiYkxJoDLqDwgQF+AS/Cb2yXSVmGAex1n3XbAbgH4/fv3adq0aXTp0iUROaO809ixY60CfOnSpcIjxQUO39O8IeJEdA4f/amnnhJQLlSokAD3jBkzREQXHv4+NWzYyGSvAPrwxeGjmkNfTwWNArhRFoqr2skbADJJ7AHcle9atmwZnTp1SuyiVq1a1Lt3b1d2p0tf1Qhcly/nnfi8AroDHADFhBMiNURRHTp0oMuXL1sFOKwQRFW4sBFJ46JDwz6OHz9Os2bNIvjjaJUqVRLbwIZBk5OjiEqRcoZH64CAAFq/fj19++23VLlyZZHRgElNvZtRADfKQnFVPwb4TOKo2dWziPtbU0B3gOPRGrm6NWvWFHnCiJgRiVuLwJF5Ml2LpGF5TJo0iSpWrCj8bQAY3jn6vvrqq7Rjxw6RwSC3kT8Ek55z584lfKds/v7+9NJLL4nsFUyAuqMZBXCjLBRXNcwpgLvbQlHRwd4kJmeUqKjKfaQCugIc2QaIqAFkWCfIOkGzBXDpZeNPwLlo0aI0b9482r17t8grfvvtt8WLIrBLAGtLgMNbxYTltm3bKC1NSw34X0NmBCZDfS2NkC0U77twGeDeN2bedMS6Adzce5bWiczdtgVwAH/y5MnCYnnllVdo3bp1dPXqVZE9grxjRNDm25gDHGmE+P/YHlkueNHkt9/OaxH5PBGtI0pGNgOsF72bURE4Wyh6j6T798ceuPs1zs3foBvAZV42om5pnUhhbQFcTkbu3btXbApgv/baawLgfn5+4t8QZYeHh4u/Sw8cUMck6cGDB8Ur3oC33B7R/Keffkr79u3TJjcb0ujRo4UVo2czCuBsoeg5ijmzLwZ4zuicW79FN4Aj82P27NkO64j8bExwYrITnjesEoC/Ro0amfYh0wxhi8iUQJkmGBgYKKBuaZXAaoAPj0lNfB4aGurwcTmyoVEAZwvFkdHxrG0Y4J41Hr52NIYD/MCB/ZpfPpGeyn08aQAAIABJREFUfvrpLDnb8LXnzJkjXq83TzM8ceKEyAMvX758pswUy4gf6Yu+BHC2ULK//Dx5EjMns1DwluyWLVuoYMGC4gm1SpUqvsYt/j3/U0A3gGenqC0LBX1kzvjRo0cJb+0he6RYsWLi3xGZI28YPrb5Sz54oQQRdlRUlOiDk1SmC+JNTOQD481OtlA84zzPqSwUzgMnMWc0f/58io6OFoOPJ9uBAwfq/jKbZ5xZfBSGAxxDkN26JgAzrJW6deuaRgsTpnjNXi43am0YceIiddGXJjG9xUIxB3Z2l5jei1MxwElkYyEF9/Tp00J62IxYSwjLUXDzPQU8AuCQFZOVeAHohx9+EGtuYG2TZ55pokXX3aymAwLiAD8yV/BSD174wUQmgI3VCNu0aWN11UM9htAoD9xbLBSjAM4WysOzG+fJ4sWLxXXEANfjivfcfeQIwD3356sdmVEA99YsFDWVuZeqAngZDskBsBixMBzmjwoU0BYs5+ZzCjDAFYbUKIB7i4WiICl30UmB2NhYsYTv4cOHxB5feKETNWrUSKe98248TQEGuMKIGAVwb7FQFCTlLi4qYDl5iQwsrASJwibcfFcBBrjC2BoFcLZQFAYrl3SRAMdcEpZmxhwQ/uTm2wowwBXG1yiAs4WiMFjchRXwYQUY4AqDaxTA2UJRGCzuwgr4sAIMcIXBNQrgCofKXVgBVsCHFWCAKwwuA1xBNO7CCrACuivAAFeQlAGuIBp3YQVYAd0VYIArSGoUwNkDVxgs7sIK+LACDHCFwTUK4JxGqDBY3IUV8GEFGOAKg2sUwDmNUGGwuAsr4MMKMMAVBtcogLOFojBY3IUV8GEFGOAKg2sUwNlCURgs7sIK+LACDHCFwTUK4EZZKKjwgqIZaF9++aVYX2P58uVinXasu75w4UKqXbu2gpKZuzx48IBGjRollhVu0aKFab13rKZ34MABGjBggCjkIeufuvyFTu5gVeQyCv+mj+g1pP1keqdpOMmSaX7+RHP6babWlds5udesm8clxlLnhc3o8pUTVLxEKEUMOkgp6cnUcU49uhcXQ7WrNafVfbdSvrz5Xf4u3oF3K8AAVxg/owBulIVy5MgRUTj6zp07okJSkyZNTABHEWssXVqtWjUFJTN3SU5OpnHjxomCBGFhYTR9+nRRYUYCXO8CEM4e8IZf19I7S8MoPV0rsN1zKXWr3dsE8Hzaaq2L+u+mJuWbOrvbLNsnpCRQ1yWt6MyF/VQhtA6tHbCL7ibFmQDeoFZ7WtF7o8vfwzvwfgXcDnAUW5g4cSLFx8cTLvapU6daLbSQqEVf6yMiRP3L69eviwr1iOpQYq1q1aqUJ0+eLGrLPiifduXKFYf66DFkRgHcKAvl7Nmz9PrrrxMKJkiAy6g8O4Bfu3aNli5dSt9//70YHxSXBphxMyhZsqTVocD5gUpLEuDYSEblRgP856g91H/Rs5SS9BfAZVRuDeDdl3WgQ6c2UbHij9L3g/bTo0X+Kq5tHmWXKV2V1g/cS8UL/aWJ7CsBDh1kVM4A1+Mq9o19uBXgqAgCeEdGRgq1bAEc1XSw3ZkzZ7KoCpCjJFTLli0zQRzVeCZNmkRXr17N0geP2OiDepnWwO/q0BkFcKMsFAlw3ECkXSIBXr9+fRGBmwMZ1ZL27NkjwAtwW7bHH3+cPvvsM6tRuwS4tEsQlUuAIyLv1auXq8On3F8CPD3tL7tEAjywSDCtH3yUKoRUEvu/l3SXwhY3pwuXj5K2sivN6LWKXnrsoQ2FtvPijzRocRtKTSEKCg6hDUOOUWhwedPnEuDSLklITjAB/JVmw2lyu4+Vfwd39B0F3AZwXMR4FMZ/rVu3JjyGh4SEZInAUT0EFzOi6Hr16tGQIUNEFRH4oah7uWjRIlHPb8KECVShQgWhvHkhZHiznTt3FiXYsC+ABZXs8+fPLwBfsWJF3UfLKIAbZaEgkoaNgRuytEukrYKnowULFmSqufjHH3/QoEGDCP3effddMT6oCHP+/HlRp3Tfvn2i0O6YMWOy+NnY//jx40lG2+a2ysyZM6lHjx66j6ejOzxz6zR1nddAO8/iTXaJtFUKB2WGsIyw79y7Sqmp96lR9U60oOsKyqP9D23kxjdpy7FF5O8fSBkZaVkAPjziDYr4+V8ko21zWyUnK9w7qg1vZ4wCbgP4yZMnRSX5OnXqUJcuXWjKlCnCOrG0ULAdLmSsXWxeeR5ymN8EevbsSX36PJxAOnHiBL3//vvUtGlTAYh8+fJlUm/jxo00e/Zs6t+/v2nyTU95jQK4URaKrHF58+ZNE8BlVI7I2xLg0HrHjh0anPzFGJk33KhhoaBKjLV+cnLU3C6RUbk9gLu7JuaVuCjhQycmxpgALqPygADrAM/ISKdSwWXpQnSkyUa5nXCTOs1/hh4v14DO/XmSbsVdzhS9Qy85OWpul8ionAGu59Xs3ftyC8BlhHzp0iUROaM6CCIvawCHR/rNN9+ICA++p3lDxInoHD76U089JUBfqFAhkoCGTdKpU6csIwB7BdviUR2ZEpaAd3XIjAK4URaKq3qZ97cHfle+y5Oq0ktIF8hXkAY3G0XhK3vQR13/Ta/U6UOI2kevDqMFfXfTF3tm0LHzm3SbAHVFP+7rfQroDnBEzUgDw6MwoqgOHTrQ5cuXrQIclgeiKqSIIUKvVauWUBD7OH78OM2aNUtUm0dDtXlsAxsGNf+mTZtG7dq1o6FDh2Z5DI+LixMROm4c6AN7Rc9mFMCNslD01A4Wl4zAMVmJm7pezZMALqP14kXK0cKe39GrSztSaPHKtLTnOhr0bU/6484l+rbfDhqwqhsDXK8TIBfuR3eAI8JCrm7NmjVF9IuIGZG4tQgcWSTTZ8ygc+fOmfxqQP3bb78V3jn6vvrqq+JxHJkp0tOW+4NP3q9fPzHBiW3RFxOhyJSARwvP3FbWiytjbRTAjbJQXNHKvC/GZ/LkyeLmPmnSRG3sXtNr12I/7rZQnDlYCfBHS1SnNf1+ovE/jKRtkStprgbwt1Z1p+6NBos8ctgiHIE7oyxva66ArgBHzi4iagAZ1gmyTtBsAVxGyvgTcC5atCjNmzePdu/eLTIU3n77bfGiyAwN8gCzBLiM8hcvXkxpaVpKgI2WXdqiK6eBUQD3ZgsFY7Zy5Upxc2/QoAF9+umnNlMJXRkbT+krAV4jtLHI2YZXPmDxs9SoRhgdu7iDVr6xl6qXqCkAfui/m7QsleUUVqu7pxw+H4eXKKAbwHGBwpvGY7G0TmQKny2AA/iIyGCxvPLKK7Ru3TqRFghrBHnHSCE038Y8qyRde5vi8OHDIlo/ffq0NtOfSiVKlBCTY/XrP0Vz584TecfSN9dzPIwCuLdaKDg3YHuNGDFCZKt8/vnnVKNGDT2HxOP2JSc361V5+NJNfHI8dVnSgs5dPERP1GxDy3tvEG9SyolJ+WKQx/0QPiCPVkA3gGPiEOlfiHqldSJ/uS2AJyUlieh67969YlMA+7XXXhMAl69Lo8p2eHi4+Fx64PYUxRMAwI03Bq155Pb62/vcKIB7o4UCeCMdFOMBeGPu4sknn7Qnsdd/bglw/KAZuz6i+VvHU3jYHOpff7D4jTLbhAHu9UNuyA/QDeAyM8TRXwGwYoITfiiiaFglAL9lZCbTDPHCyMiRI0U+cXYNwMBkFjJbsL9WrVo5ekgOb2cUwL3NQsFY4KkKT06A98cffywyg3JDswZwa79bAnxU58/pjYZDc4M0/Bt1VMBwgB84sF/zyyfS008/nQXQ8LfxUg5er7eWZmipA4Bx6NAhsYYGIAsf3tYr265oaBTAvclCgcW1YsUK01OZrTcvXRkHy76eNIn53akVNPLrHtTgsezXLZEA1zO3G5k+W7ZsoYIFC4r3IKpUqaKnzLwvD1JAN4Bn95tsWSjoY/5WJV59x9onxYoVE/+OyBwZJUghtHzJx/z7YMXglW08BeBFEUTpSCNE1O6OZhTAvcVCQbYJnqw++eQTEXHjhpoTEPGkNEL5ir29dUv0BjjmjObPn0/R0dHi1MeTLd56tffk6o7rhPfpfgUMBzh+ovTPkSpo2TAxCSukbt26mT6yZdlg+2HDholMB3esg4KDMArg3mKhIK+/d+/eYgI6uyYXrEKkqEfzRIDbi6wlwPVa3wRPrUjBxcQ+WmBgoFgXCBYWN99TwCMADlkxWYkXgH744Qex5gZevnnmmSbaI2A3KlOmTBblzQEOaGPyFGtIN2rYkAJ0AoKt4TYK4N5ioZivH56TAPckC2XBwdk0fe0wsgfwj/dMoTmbxpjWPNEDMThPkGKL64gBroeinruPHAG45/58tSMzCuDeYqGoqcq99FJAWlhRUVFiYTjMH7GFope6nrUfBrjCeBgFcG+xUBQk5S46KRAbGyty7g8fPiT2+MILncS7Edx8UwEGuMK4GgVwb7FQFCTlLi4qYDl5iXWAGjduLMrfcfNdBRjgCmNrFMDZQlEYrFzSRQIcc0lYmrlNmzbiT26+rQADXGF8jQI4WygKg8VdWAEfVoABrjC4RgGcLRSFweIurIAPK8AAVxhcowCucKjchRVgBXxYAQa4wuAywBVE4y6sACuguwIMcAVJGeAKonEXVoAV0F0BBriCpAxwBdG4CyvACuiuAANcQVKjAM6TmAqDxV1YAR9WgAGuMLhGAZzzwBUGi7uwAj6sAANcYXCNAjjngSsMFndhBXxYAQa4wuAaBXC2UBQGi7uwAj6sAANcYXCNAjhbKAqDxV1YAR9WgAGuMLhGAdwoC8V8fe8vv/xSLJC0fPlyUWgDFV8WLlxItWvXVlAyc5cHDx7QqFGjxLrwWNv9iy++oNTUVLEcKopEDBgwgD744ANTwWuXv9DJHcgqO+g2pP1keqdpuKkosZ8/0Zx+m6l15XZO7jXr5nGJsdR5YTO6fOUEFS8RShGDDlJKejJ1nFOP7sXFUO1qzWl1362iqj233K0AA1xh/I0CuFEWypEjR6hv3750584dUeKuSZMmJoCjkAbKp1WrVk1BycxdkpOTady4caKijKzWg0WaJMDffPNNUSrPqLbh17X0ztIw0sp9kqwiLyvq5NNqbS/qv5ualG/q8uElpCRQ1yWt6MyF/VQhtA6tHbCL7ibFmQBur0ybywfAO/AaBdwO8GPHjtHEiRMpPj5eVM2ZOnUqBQcHWxUIgFq/fj1t27ZNbD9t2jSqV6+eTTFROPfw4cO0cuVKOnv2rNgO9TM7depEzZo1o3z58rllIIwCuFEWCrR9/fXXCRVvJMBlVG4L4HFxcbR27XdandJNFBkZKcqrYSyff/556tatm80SXzg/EHlLgGMAZVRuNMBlpfmUpL8ALqNyWwCXgLd1IgYFh9CGIccoNLh8pk26L+tAh05tMgEcH8qonAHulsvaK3fqVoCjpBPgjQsYzRrAUcMPn+Ox+ejRo4T/L1t2AMd2X331lQCKtfb88+006LxBhQoV0n1gjAK4URaKBDhuINIukQBH4WhE4CVLlsykswSxNfFR6BiQrly5cpaPZT9plyAqlwBHceRevXrpPp6O7lACPF07RaVdIgEeWCSY1g8+ShVCKmXanasAl3ZJQnKCCeB61c909Hfzdp6rgNsAnpGRIR6F8V/r1q0Jj+EhISFZIvBTp05ReHg4obI8YIDoGfX8UOg4O4Dv2LGDZs2aJfaJoq2y6gj299lnn4mq3EOHDqV27Vz3JC2HzyiAG2WhXLt2TdgYuCFLu0TaKlWrVqUFCxZkiajnzZtHRYsWpbZt24oxwtMSIngAGnVPAWUUn7Zs2P/48eNJRtvmtsrMmTOpR48ehl1NZ26dpq7zGlBKSrzJLpG2SuEg65G0atX54RFvUMTP/zLVyjS3VezV2TRMIP7iHFfAbQA/efIkffjhh1SnTh3q0qULTZkyRVgnlhYKHq0RSQPAqDx/79494XPiYrcFcIAEF/lvv/1GY8aMoYZaIWPzJr8bdgqOISgoSFdhjQK4URbK7du3BcBv3rxpAriMyhF5WwO4LcH37NlD3bt3NwHacjs5OWpul8io3B7A3V3U+EpclPChExNjTACXUXlAgL4Al+A3t0ukrcIA1/Vy9uqduQXg9+/fF/C9dOkSTZgwgVDeaezYsVYBbqkevFN7AJdRO4A/evToTDYJIrYVK1bQqlWrqHDhwjR58mRClKhnMwrgRlkoemq3ZcsWkU1iKwJ35buWLVtGODfQatWqRb1793Zld7r0VY3Adfly3onPK6A7wGGdwM/GozCiqA4dOtDly5d1BfjWrVvpk08+oZ49e1KfPn1Mg4QI8dNPP6VffvnF9G+TJk0S1oyezSiAG2Wh6KEdbqz79u0TN3ZYKhi/0qVL67Fr0z4Y4LrKyTvzAgV0BzgerZGrW7NmTZEnjElEROJ6RuDIVJk7d67wuHGDwE3j+PHjAgq3bt2iF198UUiPG4ncRs+xMArgRlkoqtqZZ6/IfSCb5a233hIQ17u520JROV57k5icUaKiKveRCugKcPjZ8CnPnTsnrBNknaDpDXC8TLJu3ToB5+eee442bNhAixYtEjcLAKJVq1a0efNmmj17tk8B3NssFGsAx/mA8Znw0UdUvkIFn78SGeA+P8SG/kDdAI4oeOPGjSI9TFonefLkcQvAkToIYMNC+eOPP2j37t3iZjFixAiRB44mt/GlCNybLZSUlBT6/fffxYQnMpOQpw+7yzL90NCrwQ1fzh64G0TlXZoU0A3gSPtDZghAKq0T+S16R+C4USC6lg1pioi85QtCuJkgjQ1Wiy954N5moVi7zpAuCjsN2SbytXxfvh4Z4L48usb/Nt0AbglVez/NVmTsSBbKiRMnRKYKInyAG2tz+Pn5mb5Sphlev35dALxixYr2Dsepz43ywL3NQrElKtJGkf5pLy3QqUHx0I0Z4B46MD5yWF4JcGSbYKIUoLYGaLwliPTBp556KkuaoR7jZhTAvdlCkbrLCByZRAD5k08+qceQiH148iRmTuZu4/xHumbBggXp5ZdfpipVquimMe/IsxTQDeDZ/Sy9LRTzVMXHHnuMBg4cKE5S/DtWrUOGCl4IsvaSjx7yGwVwb7ZQkEYID3zx4kW0Zs239MILL4ibLyCjV+M0QhJrzsyfP1+8iYyG1SJxfRQooK22xc3nFDAc4OaWSXbqvvTSSzRo0CDTJjhRMQmGCUzLBjsFa2Zg0SRza0Wv0TMK4N5iocg3N3EztdawXMJHWhaK3hOYDHASawlhkvj06dNC+sDAQLHURPHixfU6/Xk/HqSA1wIcGiKzYdeuXSLfG1G+v78/YaEkPDbiLU28AeqOZhTAvcVCsQZwPCHhharOnTuLpQ/cMTZsoTw823GeYD0hWIwMcHcQwHP2mSMA95yfq8+RGAVwb7ZQ9FGe9+KIAghs8CZ0VFQUlS1bVqxjwxaKI8p53zYMcIUxMwrg3mKhKEjKXXRSIDY2lnbu3Kmtk39I7PGFFzqZVurU6St4Nx6kAANcYTCMAri3WCgKknIXFxWwnLyERdW4cWORYsvNdxVggCuMrVEAZwtFYbBySRcJ8JiYGCpXrhy1adNG/MnNtxVggCuMr1EAZwtFYbC4CyvgwwowwBUG1yiAs4WiMFjchRXwYQUY4AqDaxTAFQ6Vu7ACrIAPK8AAVxhcBriCaNyFFWAFdFeAAa4gKQNcQTTuwgqwArorwABXkNQogLMHrjBY3IUV8GEFGOAKg2sUwDmNUGGwuAsr4MMKMMAVBtcogHMaocJgcRdWwIcVYIArDK5RAGcLRWGwuAsr4MMKMMAVBtcogLOFojBY3IUV8GEFGOAKg2sUwI2yUFDhBUv0osk6lqhpidqnKBiwcOFCql27toKSmbs8ePCARo0aJZYHbtGihSiQnZqaKlbTw9riAwYMEJWY3LHGuyMHvypyGYV/00dsOqT9ZHqnaTjJkml+/kRz+m2m1pXbObKrbLeJS4ylzgub0eUrJ6h4iVCKGHSQUtKTqeOcenQvLoZqV2tOq/tupXx587v8XbwD71aAAa4wfkYB3CgL5ciRI9S3b1+6c+cOrV69mpo0aSKKEgPgKGKNpUurVaumoGTmLqjaM27cOFGQICwsjKZPny4qzEiAv/nmm6IWqlFtw69r6Z2lYZSeTjSl51LqVru3CeD5tII3i/rvpiblm7p8eAkpCdR1SSs6c2E/VQitQ2sH7KK7SXEmgDeo1Z5W9N7o8vfwDrxfAbcD/NixYzRx4kSKj48XF/vUqVNN1eMt5QOgUEl+27ZtYvtp06ZRvXr1slU5UYvaftq+ndatW0d//PEHWVbucccQGQVwoyyUs2fPiuLRKJggAS6jckcBju1RyBqFphs1akQLFiywWiUG5wcibwlwjJ+Myo0G+M9Re6j/omcpJekvgMuo3BrAuy/rQIdObaJixR+l7wftp0eLhJpOR/Mou0zpqrR+4F4qXqik6XPZVwIcH8ionAHujqvaO/fpVoCjIgjgHRkZKdSxBnCUgMLneGw+evSoKAklmy2Ao/YlYB8REWGCvezjywA3ykKRAMcNRNolEuCosoMIPLvyaFgh76233qLt2o0WzRGAS7sEUbkEOCJylMozqkmAp2unqLRLJMADiwTT+sFHqUJIJXF495LuUtji5nTh8lGt+hDRjF6r6KXHHtpQaDsv/kiDFreh1BSioOAQ2jDkGIUGl88CcGmXJCQnmAD+SrPhNLndx0bJwN/rQQq4DeCALB6F8V/r1q0Jj+EhISFZIvBTp05ReHg4oVo5YIB6iSgHdfHiRZsROAoWo6biyZMnCdFw//79CZE+KnH7MsCNslCuXbsmbAzckKVdIm2VqlWr2oymcZ7jPEBEjZsx4Ltv3z4qVaqUzT7Y//jx40lG2+a2ysyZM6lHjx6GXT5nbp2mrvMaaKX84k12ibRVCgdlhrCMsO/cu6r5+PepUfVOtKDrCsqj/Q9t5MY3acuxRVoZwEBNo7QsAB8e8QZF/PwvktG2ua2SkxXuDRObv9ghBdwGcMD1ww8/pDp16lCXLl1oypQpwjqxtFDgcX711VciKkMdS8AZPice17OzUDZu3Ei4uJ9v144CtMrmmFyDjeLLADfKQpE1Lm/evGkCuIzKEXnbskNwBv7yyy8C/vDN4aMPHz5cROu2+khv3dwukbaKPYC7uybmlbgo4UMnJsaYAC6j8oAA6wDPyEinUsFl6UJ0pMlGuZ1wkzrNf4YeL9eAzv15km7FXc4UvUM3OTlqbpdIW4UB7hDbcsVGbgH4/fv3BXxRaHjChAmigO3YsWOtAtxSZfMq9Y544LJ/bgC4URaK6pWAscRE55kzZ2j+/PniPICXbg/6qt/nSVXpJaQL5CtIg5uNovCVPeijrv+mV+r0IUTto1eH0YK+u+mLPTPo2PlNuk2AqmrH/bxTAd0Bjkdm+Nl4FEYU1aFDB7p8+TIDXIfzwygLReXQcR4sWrRIPIXNmDFDWB/nzp3LNQCX0XrxIuVoYc/v6NWlHSm0eGVa2nMdDfq2J/1x5xJ9228HDVjVjQGucoJxH6GA7gDHozVydWvWrCmir0KFColInCNw1884oywUlSPHxPSgQYPoySefFE9jhQsXJkdtF5XvQx93WyjOHJcE+KMlqtOafj/R+B9G0rbIlTRXA/hbq7pT90aDRR45bBGOwJ1Rlrc1V0BXgMPPhk+JSAvWCbJO0Bjg+px03mKhIAV09OjRdOLECWGd1KhRQwjgboDro7I+e5EArxHaWORswysfsPhZalQjjI5d3EEr39hL1UvUFAA/9N9NWpbKcgqr1V2fL+e95BoFdAM4HpkxsYiMA2md5MnzcMadAa7P+eQNFgrOA0xEjhw50mSdyPMgNwFcTm7Wq/LwpZv45HjqsqQFnbt4iJ6o2YaW994g3qSUE5PyxSB9zhTeS25RQDeAI+0P6V+IuqV1IkVkgOtzOnmDhYKnhGHDhlH16tVN1on89bkZ4NBgxq6PaP7W8RQeNof61x8sZJHZJgxwfa6R3LYX3QCO6Hv27NkO64e38jDBadk4C8W2hN5gocg0QEdPBHupgY7ux9O2s4zAbR2fBPiozp/TGw2HetrP4OPxcAUY4AoDZNSr9N5goRgJcE+axPzu1Aoa+XUPavBY9uuWSIDrmduNt2TxUltB7f0ILEJWpUoVhbOcu3iDAroBPLsfyxaKPqeCN1go2f1Sd1sonpQHLl+xt7duid4ARyIBJo6jo6PFUGC1yIEDB1KBAtpqW9x8TgHDAW5umWSnruUblvLFnez62Fs8S3U0jYrAvcFCYYA/VEAC3F5kLQGu1/omWEsIy1ecPn1aHEdgYCANHjzY6sJhquc/9/McBRjgCmNhFMC9wUIxEuCeZKEsODibpq8dRvYA/vGeKTRn0xjTmicKp2OWLjhPsJ4Q1q5hgOuhqOfuI0cA7rk/X+3IjAK4t1soampzL2cVSElJEW9CR0VFUdmyZcVaNGyhOKuid2zPAFcYJ6MA7u0WioLU3MVJBWJjY2nnzp10+PAh0fOFFzqJheK4+aYCDHCFcTUK4N5uoShIzV0cVMBy8hILhzVu3Jg6duzo4B54M29UgAGuMGpGAZwtFIXByiVdJMBRPKNcuXLUpk0b8Sc331aAAa4wvkYBnC0UhcHiLqyADyvAAFcYXKMAzhaKwmBxF1bAhxVggCsMrlEAVzhU7sIKsAI+rAADXGFwGeAKonEXVoAV0F0BBriCpAxwBdG4CyvACuiuAANcQVIGuIJo3IUVYAV0V4ABriCpUQDnSUyFweIurIAPK8AAVxhcowDOeeAKg8VdWAEfVoABrjC4RgGc88AVBou7sAI+rAADXGFwjQI4WygKg8VdWAEfVoABrjC4RgGcLRSFweIurIAPK8AAVxhcowBulIWCEl0ozYWGQhpYIEmWTkPFl4ULF1Lt2rUVlMzc5cGDBzRq1Cj67rvvqEWLFvTFF19QamoBeeh3AAAgAElEQVSqWA71wIEDNGDAAPrggw/Iz8/P5e9S2YEs0oC+Q9pPpneahpuKEvv5E83pt5laV26nsutMfeISY6nzwmZ0+coJKl4ilCIGHaSU9GTqOKce3YuLodrVmtPqvltFVXtuuVsBBrjC+BsFcKMslCNHjlDfvn3pzp07tHr1amrSpIkJ4Kh6hLWnq1WrpqBk5i7Jyck0btw4UVEmLCyMpk+fTlikSQL8zTffpPfff9/l71HdwYZf19I7S8MoPZ1IVpGXFXXyaRXLFvXfTU3KN1XdvalfQkoCdV3Sis5c2E8VQuvQ2gG76G5SnAng9sq0uXwAvAOvUcDtAD927BhNnDiR4uPjyV6JMwBq/fr1tG3bNrH9tGnTqF69ejbFxAX/008/UkTEBkLdTX9/f3riiSeoV69eVLVqVcqTJ49bBsIogBtlochalqh4IwEuo3JbAJ86daqIoG01CWgU3jVvsp/8HJ/JqNxogMtK8ylJfwFcRuXWAN59WQc6dGoTFSv+KH0/aD89WiTU9FPNo+wypavS+oF7qXihkqbPZV8JcHwgo3IGuFsua6/cqVsBjpJOgHdkZKQQxxrAUcMPn+Ox+ejRo4T/L1t2AL9+/TrNmjXLtG9z9QFyXOxt27Z1C8SNArhRFooEOG4g0i6RAK9fv76IwEuW/As+GAtXAS7tEtykJcARkePmbFSTAE/XTlFpl0iABxYJpvWDj1KFkEri8O4l3aWwxc3pwuWjpC3NTTN6raKXHntoQ6HtvPgjDVrchlJTiIKCQ2jDkGMUGlw+C8ClXZKQnGACuF71M43Skb9XPwXcBvCMjAzxKIz/WrduTXgMDwkJERd2cHCw6RecOnWKwsPDKSkpiQCDTp06iXp+Fy9etBmBwxdFdLdlyxax71dffVUABDcMfB+i+EqVKtGECROygEUP6YwCuFEWyrVr14SNAX2lXSJtFTzpLFiwIEvRXAlwGbE7qjv2P378eHEDhl1ibqvMnDmTevTo4eiudN/uzK3T1HVeA0pJiTfZJdJWKRyUGcIywr5z76rm49+nRtU70YKuKyiP9j+0kRvfpC3HFmlPjYGUkZGWBeDDI96giJ//ZaqVaW6r2KuzqfsP5x16rAJuA/jJkyfpww8/pDp16lCXLl1oypQpAtyWAIfH+dVXX4myT3Xr1qV79+6JCxeP6/Yi8L1799KLL76YaVLrxo0bNGbMGPr999/tWjCqo2IUwI2yUG7fvi0AfvPmTRPAZVSOG6eeAJeTo+Z2ibwZ2AO4u4saX4mLEj50YmKMCeAyKg8IsA7wjIx0KhVcli5ER5pslNsJN6nT/Gfo8XIN6NyfJ+lW3OVM0TvOS+mtm9sl0lZhgKteub7Xzy0Av3//voAnfGlEwSjvNHbsWKsAt5Q0Li7OIYDbGgpE8jNmzCDA3Z6HrjqcRgHcKAtFRSfVCFzlu2SfZcuWEZ7o0GrVqkW9e/d2ZXcu9ZWQLpCvIA1uNorCV/agj7r+m16p04cQtY9eHUYL+u6mL/bMoGPnN+k2AerSQXNnr1NAd4DDOoGfjUdhRFEdOnSgy5cv5xjAUdQVNwtE4Ij6cSHr3YwCuFEWiop+uR3gMlovXqQcLez5Hb26tCOFFq9MS3uuo0Hf9qQ/7lyib/vtoAGrujHAVU4w7iMU0B3geLRGrm7NmjXpvffeo0KFColIPKcicEyuTZ48mZ566ikaPXq0+H69m1EAN8pCUdHPchIT41ClShVq2LChyCmvXr267hPM7rZQnNFBAvzREtVpTb+faPwPI2lb5EqaqwH8rVXdqXujwSKPHLYIR+DOKMvbmiugK8DhZ8OnPHfunLBOkHWCllMAx8QnJsBg4SCfOLsURFdOA6MA7o0WijWdAXPc5DEhadRLOa6MvyN9JcBrhDamFb03ErzyAYufpUY1wujYxR208o29VL1ETQHwQ//dpGWpLKewWt0d2TVvwwqYFNAN4LBONm7cKLJDpHUi87BzAuBIK4Rlcv78eRo8eDC1b99e9whPqmYUwL3JQrG8xlJSUoSttWjRQlqz5lsKCgoSk594UvLFJic361VpLwAenxxPXZa0oHMXD9ETNdvQ8t4bxJuUcmJSvhjki1rwb3KfAroBXEa/iLqldSIP290AB9hgm+AY+vfvnyUzRW/5jAK4N1kotjTHC1rvvvsubdiwQTytGZkWqPd5Yb4/S4Djsxm7PqL5W8dTeNgc6l9/sNhcZpswwN05Gr67b90Ajuh79uzZDis1dOhQMcFp2ZzNQomKihKvXGOi9B//+IeIvJH14s5mFMC9yUKxpT+e1HCznTdvXq4DuDVNJMBHdf6c3mg41J2nLe/bBxXwaoD/9ttvwmtHnrI737y0HHejAO7NForUEL9h2LBhdPz4cbEwVsuWLXW7rDxpEvO7Uyto5Nc9qMFjDy0UW00CXM/cbkzk4yU3LFOACWNMHnPzTQV0A3h28rjDQgEA8AiOFezgeQME7lr7xFMA7s0WCsbp8OHDYo5EvoY/adIkKly4sG5XliflgctX7O2tW6I3wJFIMH/+fIqOjha6YrXIgQMHUoEC2mpb3HxOAcMBbm6ZZKfuSy+9RIMGDRKb4JVuvH6PCcvsWokSJQiQqFixoq4DZ1QE7i0WivmysNaER1SILKFixYrpOi6eCHB7kbUEuF7rm2AtISwncfr0aaFtYGCgCHCKFy+uq9a8M89QwCsB7ij0fQ3g3mKhWAO4zAHHYlSPPfaYW+YpPMlCWXBwNk1fO4zsAfzjPVNozqYxpjVP9MACzhOsJ4RAhwGuh6Keu48cAbjn/ny1IzMqAvdmC0VNae6logBSNvEmNCb4y5YtK9axYQtFRUnP78MAVxgjowDuLRaKgqTcRScFsJTEzp07tfmGQ2KPL7zQSSwUx803FWCAK4yrUQD3FgtFQVLu4qIClpOXSKVt3LixKH/HzXcVYIArjK1RAGcLRWGwckkXCfCYmBgqV64ctWnTRvzJzbcVYIArjK9RAGcLRWGwuAsr4MMKMMAVBtcogLOFojBY3IUV8GEFGOAKg2sUwBUOlbuwAqyADyvAAFcYXAa4gmjchRVgBXRXgAGuICkDXEE07sIKsAK6K8AAV5DUKICzB64wWNyFFfBhBRjgCoNrFMA5jVBhsLgLK+DDCjDAFQbXKIBzGqHCYHEXVsCHFWCAKwyuUQBnC0VhsLgLK+DDCjDAFQbXKICzhaIwWNyFFfBhBRjgCoNrFMCNslBkAQZIhSo6WF9j+fLlovYpCgYsXLiQateuraBk5i7my9C2aNFCFH9ITU0Vq+kdOHCABgwYIKrZG1XJXhZpwFEPaT+Z3mkabqpp6edPNKffZmpduZ3LOsQlxlLnhc3o8pUTVLxEKEUMOkgp6cnUcU49uhcXQ7WrNafVfbeKosjccrcCDHCF8TcK4EZZKEeOHKG+ffvSnTt3aPXq1dSkSRMTwFHEGkuXVqtWTUHJzF2Sk5NFoQcUJAgLCxO1TrHGhwQ4yua9//77Ln+P6g42/LqW3lkaRunpRLIIsSzIkE8reLOo/25qUr6p6u5N/RJSEqjrklZ05sJ+qhBah9YO2EV3k+JMALdX5cflA+AdeI0Cbgf4sWPHaOLEiYRq5LjYp06dSsHBwVYFAqDWr19P27ZtE9tPmzaN6tWrZ3VbVB45evQoRURE0H//+1+xfZEiRahhw4aE6j2VKlVyW4k1owBulIVy9uxZev311wkFEyTAZVRuD+DpGu0OHjxIa9eupRMnToixQpOARt1G84bzA5G3/ByfjRo1ir777jtR99RIgMtK8ylJfwFcRuW2AC4Bb4sIQcEhtGHIMQoNLp9pk+7LOtChU5tMAMeHMipngHsNX91+oG4FOCqCAN6RkZHih1gDOECMz3GBAsj4/7JlB3DcGEaPHm1VIH9/f0LV+7Zt27pFQKMAbpSFIgGOG4i0SyTA69ev///tnQl4Tdfax1+3ghoSMfThatB+Ziq0RS+uxpD4lNtcQo1Rs4hqq4Mh5iklbmmLmmueq5qgerWKfoaKqYarihJypVpDRAgSl+/8l7tOT46Tk2SdfbLO2d51H4+rZ6+99/m/+/z2u/9r7fWKDLx06dKPaI0bMuKPm7J9yw7g0i5BVi4BjowcFX10NQnw+5ZLVNolEuBFff0oNvIQVfR/NtPpuQpwaZekpadZAW5U+TVdOvJxjVPAbQB/8OCBeBTGn+DgYMJjuL+//yMZ+PHjx0V9y7t37xJgEBoaKspBnT171mkGDujv2bOH2rRpQ3/+859FiS7cMJDpIUusUaMGjRkzhooVK2acWv/dky6A67JQkpKShI0BfaVdIm2VKlWq0Lx58x6puXj58mV6++23aceOHdSyZUvq1asX1alTR5T4ctaw/7Fjx1qzbVtbBUWsu3TpYng8c7rDk1dOUIfZ9Skj45bVLpG2SpFijjNp1aLFg+P6Udzu+dZSa7a2SnZl2nL6fXg771fAbQA/duyYAGhgYCC1b9+eoqOjhXVib6HA41y8eLGoGoIfeGpqqnhMxuO6sww8K+mxHjJuCKhQ78yucSV0ugCuy0K5evWqADigLAEus3Jk3vYAx8174cKFIv6DBw+mt956i3x8fHIkuRwctbVLpK2SHcDdXRMzMeW88KHv3Em2Alxm5YUKGQtwCX5bu0TaKgzwHF1Kj8VGbgH4zZs3BXzPnTtH48ePF9nxyJEjHQLcXmXbgsUqAP/tt98EwJHtmy0D12Wh5PaXcOXKFerfvz8VKlRI+NmIRV40T6pKL7+vagaeF3rxMbxfAcMBjuwLfjYyNWRRsDgSEhLcDnAMluFRH/bLjz/+KLJ4WDLuaLoycF0WSm41lPZKeHg4DRkyJLfdlbdngCtLxx29VAHDAY5Ha8zVhQeNecKFCxcWmbg7MnD45jExMbRr1y6r/JUqVRKP7fjbXU0XwHVZKLnVEWMQiAG8bMwM2rx5M8XHxwt7rHLlymKWEKYlZjUbKbfHk9u720JROa/sBjF5RomKqtxHKmAowOFnw6c8deqUsE4w6wQtLwGO45UoUYIGDhwo5ivDCze66QK4t1go0sd2pnuTJk1o+vTpVKZMGaPD41H7Y4B7VDhMdzKGARzWyaZNm4TnKa0TCU93Adw2Gjg+/PPvvvtOzHxBw0shWc0jdyWSugDuLRaKBHj16tWpd+/eosAubqqIEWYdYWohZhBheuCbb77pSig8vi974B4fIq8+QcMAjml/eGRG1i2tE6lMXgDcNgrffvuteBJo3ry5eJTP6QyInEZSF8C9xUKRAM9q1gjsFIC9adOm4m1L+5d5choHb9iOAe4NUfLeczQM4Mi+Z8yYkWMl8KINBjjtm6uzULC/M2fO0IgRI6hWrVpiEK1gQct7zgY2XQD3Fgvlm2++ER53Vhm2nIJYoUIF8cRmtBduYKhd3hUD3GUJeQdOFDAlwGUG3rVrV+revbvhF4AugHuLhSIBjZd8Pvzww0cAjaUSMEbRrl07YacUKGDMokyePIiZl3O38Zbsli1bxJPNa6+9JgaOuZlTAcMA7kyevLBQMI0Q2fv27dtp1apV4uLFQGrFihUNj5wugHuLhYLZQZh1BCsFa6gMGDCAoFlGRobwvidOnEiXLl2iWbNmEQYzjWo8jZDE4l9z584V+qJhtUjMyTf6KdSomPF+XFNAO8BtLRNnXwVTzyIiIqybYFnTDRs2OOwCWLz77rviLVB3NF0A9xYLBZrjXDFAeeLEiUdCgKmlGJsA3I0cn2CAk1hLCIP4UncsXRAZGfnIUgfu+F3wPvNeAdMAvEiRImIAFetINw0KokJ2q9wZKa0ugHuLhSK1xqv3WCYBL3YlJiaKLPwvf/mLeC0f64cbPcWTLZSHyuM6wQttWLuGAW7kL9/z9pUnAPe8r+3aGekCuLdYKK6py71dVQBWFd6EPn/+PD399NPihskWiquqemZ/BrhCXHQB3JssFAVZuYsBCly/fl2MA+3fHy/29uqroWKhOG7mVIABrhBXXQD3NgtFQVruoqiA/eAlFpBr2LChKH/HzbwKMMAVYqsL4GyhKATrMekiAY7llMuXLy/efsXf3MytAANcIb66AM4WikKwuAsrYGIFGOAKwdUFcLZQFILFXVgBEyvAAFcIri6AK5wqd2EFWAETK8AAVwguA1xBNO7CCrAChivAAFeQlAGuIBp3YQVYAcMVYIArSMoAVxCNu7ACrIDhCjDAFSTVBXAexFQIFndhBUysAANcIbi6AM7zwBWCxV1YARMrwABXCK4ugPM8cIVgcRdWwMQKMMAVgqsL4GyhKASLu7ACJlaAAa4QXF0AZwtFIVjchRUwsQIMcIXg6gK4LgsFJbpQmgsNhTSwQJIsXIyKLwsWLBDre7vabt++LepoYv1wrOuOepn37t0Ty6H+8MMP1KdPHxo9ejQ98cQTrh5Kqf+ao8soasXDEn0DW0+id5pEkax5+UR+olk9v6LgSq2U9m3bKeXOdWq3IIgSEo9QyVIBFBexjzLup9PfZtWl1JRkql21Ka3t8TX5/MmYUnQunzDvQJsCDHAF6XUBXJeFcvDgQVGk+Nq1a7R27Vpq1KiRFeAoooG1p6tWraqgZOYu6enpNGrUKFFRJiwsTFSsxyJNEuBvvPEGDR8+3OXjqO5g409f0DtLw8hSvY+iuy6ljrXDrQD3sdTNXth7JzWq4HqJuLSMNOqwqAWd/GUvVQwIpC/67KAbd1OsAK9fqzWtCt+k+jW4n4kUcDvADx8+LArX3rp1S1TM+eCDD7KsQg5AxcbGEoreYvvJkydT3bp1cyQ3VmHDcf71r3+J7XPTN0cHsNlIF8B1WSiySDEq3kiAy6zcEcARY2TP2TUJadQvlU32lZ/hv8usXDfAd5//nnovfJky7v4BcJmVOwJ452VtKP74ZipRshx9GbGXyvkGWL+nbZZdtkwViu2/i0oWLm39XPaVAMcHMitngGd3ZT0+n7sV4CjpBKgePXpUKOoI4Kjhh8/x2Hzo0CFR00+2nEL4wYMHImvDn9z2VQm1LoDrslAkwHEDkXaJBHi9evVEBl669B/wMQLg0i5BVi4Bjoy8W7duKiEzpI8E+H3LJSrtEgnwor5+FBt5iCr6PyuOlXr3BoV91pR+SThElqW5KabbGmpb86ENhbb97DcU8VkI3csgKubnTxsHHqYAvwqPAFzaJWnpaVaAdwoaTJNaTTPkO/FOvFsBtwHcFqrBwcGEx3B/f/9HMvDjx49TVFQUoZI5YBAaGirq+Z09ezbHWfSxY8dozJgx4gaBhhtCTuGvEj5dANdloSQlJQkbAzdkaZdIW6VKlSo0b968HBfNxXWB7BzxmTp1KnXp0iVTCLD/sWPHksy2bW0VR9urxE+1z8krJ6jD7PqUkXHLapdIW6VIscwQlhn2tdSLFh//Jr1ULZTmdVhF+Sz/Qxuy6Q3acngh5c9flB48+M8jAB8c14/ids8nmW3b2irdmr9P40JiVL8G9zORAm4DuIQqKsO3b9+eoqOjhXVib6HA40ThW5R9qlOnDqWmpgqfE4/rOYGwzPIBGfRDpfpdu3blqK9qHHUBXJeFcvXqVQFwFCmWAJdZOTLv3AD83LlzNGDAACpevDh9/PHHotCxbZODo7Z2iczoswO4u4saJ6acFz70nTvJVoDLrLxQIccAf/DgPj3l9zT9cumo1Ua5mnaZQuc2pufK16dTvx6jKykJmbJ36CEHR23tEmmrMMBVf7nm6+cWgN+8eVMAFD/W8ePHWx4h/0QjR450CHB7SVNSUnIMcGRzsF4AFfzgg1u0oKn/+IdpAa7LQjHqske8PvnkE4qJiXGYfbt6nGXLlhGe6NBq1apF4eHhru5Sub+EdEGfJykyaChFre5C4zosoU6B3QlZ+7C1YTSvx06a+X0MHT692bABUOUT5o5eqYDhALeHaps2bSghIcEtAEcWiGllNWrUoPfff19MLwMczJqB67JQjLqyYYv179+fihQpQrNnz6ayZcsatWuxH08CuMzWS/qWpwVd19PrS/9GASUr0dKuGyji867072vn6POe31GfNR0Z4IZeBY/XzgwHuD1UCxcuLDJxozNw+ywf/jd8dDMDXJeFYsRPAoPTH374obBNJk6cQD179jJit5n24W4LJTcnLAFerlQ1WtfzWxr7zyG09ehq+tQC8LfWdKbOL0WKeeSwRTgDz42yvK2tAoYCHH42fMpTp04J60QOKhoNcGT5mzZtEoNhsE6Q5efLl8/0APdmC0V65iVKlHBL9u1pP2sJ8OoBDcWcbXjlfT57mV6qHkaHz35Hq/vtomqlagiAx/9rs2WWykoKq9XZ074Gn4+HK2AYwLOCKr6/0QBHpgXrBDMgYJ0gy0czewburRZKXmTfnvY7k4ObdSs/fOnmVvotar+oGZ06G0/P1wihleEbxZuUcmBSvhjkad+Dz8ezFTAM4PA3Mf0LWbctVI0GOLL8jz76SLywY5vlPw4A91YLBQOLmMXy1FNPPRbZN65Fe4Djv8XsGEdzvx5LUWGzqHe9SEEGOduEAe7ZoPTUszMM4LA0ZsyYkePvOWjQIGF92LfsZqHIbP7KlSs5Olbjxo1pyJAhVLCg5V1ng5quaYTeaKEg+540aRLNnTvXbd63QWE1dDeOAO7oABLgQ9t9Qv0aDDL0HHhn5leAAa4QY10A90YLBS9VRURE5En27UmDmOuPr6Ihy7tQ/ZrO1y2RADdybjfekt2yZQthiQIsQla5cmWFq5y7eIMChgHc2Zc12gPP6lhm98C9zULJyMgQ2Tfm6btr5ontteBJ0wjlK/bZrVtiNMBhMeJp59KlS0IarBaJqZtGPoF6A9gel3PUDnBby8SZ6G3bthWZnLNmdoB7m4Uis++SJUuKZWgBE3c2TwR4dpm1BLhR65vAssKaQCdOnBBSFy1alCIjI3O81IE748P7Nl4BBriCpmyhZC8abqYY1F66dCmNGzeOevfuLaZ6urN5koUyb98MmvLFm5QdwKd9H02zNo+wrnlihD6w2rCeEJaZYIAboajn7iNPAO65X1/tzHQB3NssFDV1uZerCsC6gm11/vx5evrpp8UMILZQXFXVM/szwBXiogvg3mahKEjLXVxU4Pr167R9+3bavz9e7OnVV0PFQnHczKkAA1whrroA7o2zUBTk5S4KCtgPXmIBuYYNG4ryd9zMqwADXCG2ugDOFopCsB6TLhLgqExVvnx5CgkJEX9zM7cCDHCF+OoCOFsoCsHiLqyAiRVggCsEVxfA2UJRCBZ3YQVMrAADXCG4ugCucKrchRVgBUysAANcIbgMcAXRuAsrwAoYrgADXEFSBriCaNyFFWAFDFeAAa4gqS6AsweuECzuwgqYWAEGuEJwdQGcpxEqBIu7sAImVoABrhBcXQDnaYQKweIurICJFWCAKwRXF8DZQlEIFndhBUysAANcIbi6AM4WikKwuAsrYGIFGOAKwdUFcF0WCiq8oLILGtb1xvoaK1euFLVPscb3ggULqHbt2gpKZu5y+/ZtGjp0KK1fv56aNWtGM2fOpHv37onV9H744Qfq06ePKGb9xBNPuHwslR3IIg3oO7D1JHqnSZS1puUT+Ylm9fyKgiu1Utl1pj4pd65TuwVBlJB4hEqWCqC4iH2UcT+d/jarLqWmJFPtqk1pbY+vRVFkbo+3AgxwhfjrArguC+XgwYPUo0cPunbtGq1du5YaNWpkBTiKWGPp0qpVqyoomblLeno6jRo1ShQkCAsLoylTphDW+JAAf+ONN2j48OEuH0d1Bxt/+oLeWRpG9+8TySLEsiCDj6Xk6sLeO6lRhSaqu7f2S8tIow6LWtDJX/ZSxYBA+qLPDrpxN8UK8Oyq/Lh8ArwDr1HA7QA/fPgwTZgwgW7duiUq1n/wwQfk5+fnUCAAKjY2lrZu3Sq2nzx5MtWtW9fhttjvsGHDshS6VKlSljJeE+mZZ54xPBi6AK7LQvn555+pb9++hIIJEuAyK88K4A8ePKCTJ0/S4sWLaefOnZSYmEiFCxcWmXr79u0ty5y+SkWKFHkkNrg+kHlLgGMDmZXrBrgsVJxx9w+Ay6w8K4BLwGd1ERbz86eNAw9TgF+FTJt0XtaG4o9vtgIcH8qsnAFu+E/aa3foVoCjIgjgjdJaaI4AjhJQ+ByPzYcOHSL8WzYGeObrSpeFIgGOG4i0SyTA69WrJzLw0qVLW08W8F69erWwO5BBO2qhoaEOb+YS4NIuQVYuAY6MvFu3btp+bBLg9y2XqLRLJMCL+vpRbOQhquj/bKbzcxXg0i5JS0+zAtyo8mvahOQDG6aA2wCOHzEehfEnODiY8Bju7+//yI/2+PHjFBUVRSjBBRjgh41yUGfPns1RBp6TWpmGqfXfHenKwHVZKElJScLGwA1Z2iXSVqlSpQrNmzcvU83F8wkJ1M9SSPfy5cuinFrLli2pQIEChEox8okMN2tk57g2bBv2j1JsMtu2tVWmTp1KXbp0MTqcOd7fySsnqMPs+pbvcctql0hbpUgxx5m0atHiwXH9KG73fGupNVtbJbsybTn+Qryh1yvgNoAfO3aMxowZQ4GBgeKROTo6Wlgn9hYKMjT8kFE1pE6dOpSamip8Tjyu5yQDf5wArstCuXr1qgA4gCwBLrNyZN72AJfZec+ePcU14OPj4xDSjoAsB0dt7RKZlWcHcHfXxExMOS986Dt3kq0Al1l5oULGAlyC39YukbYKA9zruWvYF3ALwG/evCnge+7cORo/fjyhOsjIkSMdAtz+m9hWqWeAe4aFkturTcIdTyrTp08XdRllw9gGxi527NghbtwvvPBCbnef5faeVJVenqRqBm6YKLwjUytgOMBhncDPRqaGLKpNmzaUYHmkZoC7fh3pslBye+YYx/j444/pww8/pICAABowYICwxjCQOWPGDNq8eTMNHjyY3nrrrUey89wey3Z7Brgr6nFfb1TAcIAj+3fm0KgAACAASURBVMLgVY0aNcQ8Ycw8QCbuLoDbio6ZJxgo/d///V/hp9s/uhsVIF0euC4LRUU3+N24kX/00UcC3LJVr16d3n77bXrllVfEk5mRzd0Wisq5ZjeIyTNKVFTlPlIBQwEOPxs+5alTp4R1Apii5RXAbcPauHFjkeH5+voaHm1dANc1C0VFQDyJYcASNhg8cdmKFStGkZGRYlrik08+qbJrr+rDAPeqcHndyRoGcPxgN23aJObwSuskX758bgO4vdI4Pvzz7777jlatWiVmTGDKGf7I8zAqOroA7i0WCmKB+eIYwMQT2Lvvvisyblgcn376qRioxpudmKfvaC64UXHyhP2wB+4JUTDvORgGcEz7w/QvZN3SOpGyuSMDdxYSPLpjZgSy8CFDhlDBgpbX5AxsugDuLRYKpoZi1grOF4OYL7/8slV9TD/EIOaJEycsAJ9APXv2MjAynrcrBrjnxcRMZ2QYwJF9Y4Aqp23QoEFigNO+5XQWirPj7N+/X3juZgO4t1goci43nn7wIhfmgMuG7Bw3V1hsyMIxRbBQoUI5vWy8bjsGuNeFzKtO2HQAxwyIhQsXigE0LLqEGRBGL36kKwP3FgslJiZGzEKB9iNGjHjEwpJzvY0GuCcPYubl3G2MOWzZskWMMUDjypUrexWU+GRzroBhAHd2yLywUABuvDG4Zs0a4YNjRgosnWefzfxqc86lyXpLXQD3Fgtl27ZtFBERId7OhIWFNzHhdcs3MTGwuW/fPsMtFJ5GSGLpgrlz59KlS5fEBYzVIvtb3oo12kY04nfE+3BdAe0At7VMnH0d+zcunVk2uGjhw2PKmjuaLoB7i4WCl3Vw80SmnVXDK/HYxshBTAY4ibWEsHwFxhjQihYtKmb94GbKzXwKmAbgAAEGUGGb4LV8W9/V6LDpAri3WCjQG2vbbN++XcwIwrIKv/32G0E3zM/H0gpNmjQxPCtkC+XhlY7rBOsJYSYWA9zoX79n7S9PAO5ZX9n1s9EFcG+xUFxXmPfgigKwqjCQfP78ebGMAWYEsYXiiqKe25cBrhAbXQD3FgtFQVLuYpAC169fF08++/fHiz2++mqoeCLlZk4FGOAKcdUFcG+yUBRk5S4uKGA/eIllCho2bCgsRW7mVYABrhBbXQBnC0UhWI9JFwnw5ORkKl++PIWEhIi/uZlbAQa4Qnx1AZwtFIVgcRdWwMQKMMAVgqsL4GyhKASLu7ACJlaAAa4QXF0AVzhV7sIKsAImVoABrhBcBriCaNyFFWAFDFeAAa4gKQNcQTTuwgqwAoYrwABXkJQBriAad2EFWAHDFWCAK0iqC+A8iKkQLO7CCphYAQa4QnB1AZzngSsEi7uwAiZWgAGuEFxdAOd54ArB4i6sgIkVYIArBFcXwNlCUQgWd2EFTKwAA1whuLoAzhaKQrC4CytgYgUY4ArB1QVwXRYKSnShNBfanDlzxAJJsiwaimcsWLCAateuraBk5i63b9+moUOHinJ4zZo1o5kzZ9K9e/fEcqg//PAD9enTh0aPHm14ibycnviao8soakV3sfnA1pPonSZRJGtePpGfaFbPryi4Uquc7i7L7VLuXKd2C4IoIfEIlSwVQHER+yjjfjr9bVZdSk1JptpVm9LaHl+Tz5/+qDXq8kF5B16pAANcIWy6AK7LQkEl+R49etC1a9do7dq11KhRIyvAUUQDa09XrVpVQcnMXdLT02nUqFGiokxYWBhNmTJFlAiTAH/jjTdo+PDhLh9HdQcbf/qC3lkaRvfvE0V3XUoda4dbAe5TkGhh753UqEIT1d1b+6VlpFGHRS3o5C97qWJAIH3RZwfduJtiBXj9Wq1pVfgml4/DO/B+BdwO8MOHD4vK5CizhR87qpD7+fk5VA6Aio2Npa1bt4rtUTuxbt262aqMfijieuDAAbGIPbI21MScOHEiPfPMM9n2z+0GugCuy0L5+eefqW/fvoSKNxLgMit3BnDUQkXGvnPnTkpMTBTFdVu3bi1uBqVLl3YoO64PZN4S4NhIZuW6Ab77/PfUe+HLlHH3D4DLrNwRwDsva0PxxzdTiZLl6MuIvVTON8D6nW2z7LJlqlBs/11UsvAfmsi+EuDoKLNyBnhuf7Hm3d6tAEdJJ8D76NGjQkFHAEcNP3yOx+ZDhw6Jmn6yZQdwVB75/PPPRcYGaNs2MwJcl4UiAY4biLRLJMBRIg0ZuC2QHzx4IEA/ZswYSk1NfeTXU6NGDfrkk08c1iyVAJd2CbJyCXBk5N26ddP2a5QAv2+5RKVdIgFe1NePYiMPUUX/h0W0U+/eoLDPmtIvCYfIsjQ3xXRbQ21rPrSh0Laf/YYiPguhexlExfz8aePAwxTgV8H6uQS4tEvS0tOsAO8UNJgmtZqmTQc+sOco4DaA40cMsOJPcHAw4THc39//kQz8+PHjFBUVJWooAgahoaGint/Zs2edZuAA/dKlS2n16tWi1iI8WjzaI7vHYvbubLoycF0WSlJSkrAxcEOWdom0VapUqULz5s3LVDQXN2RUpc+fP7+ILfxs1CjFWtXIyBHfVq1aCYvkySefzBQq7B/FjmW2bWurTJ06lVAMWVc7eeUEdZhdnzIyblntEmmrFCmWGcIyw76WetGSXNykl6qF0rwOqyif5X9oQza9QVsOL7RoVJQePPjPIwAfHNeP4nbPJ5lt29oq3Zq/T+NCYnTJwMf1IAXcBnAUskUGFhgYKIrYRkdHC7jaWyjwOBcvXizKPtWpU0dkbPA58bjuLANHVogBrTJlygjfFBl3XjVdANdloVy9elUA/PLly1aAy6wcmbc9wGNiYujjjz+mGTNmULt27TKFRQ5UYlDS0eCnHBy1tUtkVp4dwN1d1Dgx5bzwoe/cSbYCXGblhQo5BviDB/fpKb+n6ZdLR602ytW0yxQ6tzE9V74+nfr1GF1JSciUvUMwOThqa5fIrJwBnle/dM8/jlsAfvPmTQFfeKDjx48XGfHIkSMdAtxeopSUlGwBjuwemdqmTZto0qRJ9Nxzz+Wp0roArstCyY24EtAY+0CMqlWr9kh3PJXBFpk+fbp1dktujpHVtsuWLSM80aHVqlWLwsPDjdit0j4kpAv6PEmRQUMpanUXGtdhCXUK7E7I2oetDaN5PXbSzO9j6PDpzYYNgCqdLHfyWgUMBzjgCj8bP15kUW3atKGEhARDAY4sfdy4cZZM6I7I7H19ffM0ALoArstCyY24tpYHnqxgn9k36Z+/9dZbNGTIkNzs3um2ngRwma2X9C1PC7qup9eX/o0CSlaipV03UMTnXenf187R5z2/oz5rOjLADbsCHr8dGQ5waW1goOr999+nwoULi0zcyAwcMxrgrVaqVIlatgyhHTt2Co8dHm2RIkWEFYPBrmeffTigZHTTBXBdFkpu9ZM2SIMGDWjYsGFiJpGPj4/wwHfs2CFu7keOHLH63Lndf1bbu9tCyc15SoCXK1WN1vX8lsb+cwhtPbqaPrUA/K01nanzS5FiHjlsEc7Ac6Msb2urgKEAh58Nn/LUqVPCOsGsEzSjAS73d+XKlSyjCZDDS8fAqNFNF8C9wUKB1tIGw5RQZ033tECjrwvb/UmAVw9oKOZswyvv89nL9FL1MDp89jta3W8XVStVQwA8/l+bLbNUVlJYrc7uPCXetwkVMAzgsE7gSWMOr7RO8uV7OOLuLoBfv35dWDT48+c//1m8oYeXTVasWCHOBd44BlKLFStmaOh0AdwbLBQpNObxw+veuHEjwQ/Hkxje1mzTprVl5oWPyMwx2wTzy83Y5OBm3coPX7q5lX6L2i9qRqfOxtPzNUJoZfhG8SalHJiULwaZUQv+Tu5TwDCAY9offpDIuqV1Ik/bXQDHABk81IIFLa/B2TRYKTiX3377zS0v8+gCuLdYKNldrnKqYFYeeXb9veFze4DjnGN2jKO5X4+lqLBZ1LtepPgacrYJA9wboup552gYwJHxYtpYTtugQYNE5mzfcjIL5ffff6cRI0aIWS2OMmzMKcdUtv3794tBTsxIMLLpAri3WCjOtIYPjic0xHDu3LluG6cwMt4q+3IEcEf7kQAf2u4T6tdgkMqhuM9jrIBXAlwCGi+MwGuvXr16phAi88bccLypCYCXLVvW0BDrArg3WSiOBEfcMD8cf/r37y9uwrC9jGqeNIi5/vgqGrK8C9Wv6XzdEglwI+d2Y5YPlpbAS1J4wQ1LGHAzpwKGAdyZPEZbKDjWt99+KwZMcXEim8ff8NwBOWR2eFEELxD16tXLUEjg2LoA7o0WCsZGMFaBZRLwBiZmoTRp0kTMAcdLWEY2T5pGKF+xz27dEqMBjokEuP4vXbokpMVqkbhZ2tuMRurO+9KngHaA21omzmRo27ateD1bNlyoH330kVgoyVF78cUX6b333hOv7xvddAHcWywU22Vh7bVv2bKlmMMfEPDHwk5GxccTAZ5dZi0BbtT6JlhiAoPHJ06cELIWLVqUIiMjMy11YJTevB/9CngtwCEdLBJkdHhxCFk+Hscx9xvrqQQFBYm5x+5ougDuLRaKLcAx+wRPR5gTjjEPzAl311o1nmShzNs3g6Z88SZlB/Bp30fTrM0jrGueGHG94jrB0w4G8xngRijqufvIE4B77tdXOzNdAPdGC0VNYe7ligJIbDDTB0srP/3002IdG7ZQXFHUc/sywBViowvg3mKhKEjKXQxSAOMN27dvt8zAihd7fPXVULFQHDdzKsAAV4irLoB7i4WiICl3cVEB+8FL2FQNGzYU5e+4mVcBBrhCbHUBnC0UhWA9Jl0kwDHPvnz58hQSEiL+5mZuBRjgCvHVBXC2UBSCxV1YARMrwABXCK4ugLOFohAs7sIKmFgBBrhCcHUBXOFUuQsrwAqYWAEGuEJwGeAKonEXVoAVMFwBBriCpAxwBdG4CyvAChiuAANcQVJdAGcPXCFY3IUVMLECDHCF4OoCOE8jVAgWd2EFTKwAA1whuLoAztMIFYLFXVgBEyvAAFcIri6As4WiECzuwgqYWAEGuEJwdQGcLRSFYHEXVsDECjDAFYKrC+C6LBRUeEFlF7Q5c+aI9TVWrlwpap+iYMCCBQtEwWIdzXbp2mbNmomi2vfu3RMr8KGoR58+fWj06NGGF/XI6XeVpdUy7hK1qNeZ5rZfSbLYA/ZhVCm1lDvXqd2CIEpIPEIlSwVQXMQ+yrifTn+bVZdSU5KpdtWmtLbH16KQMjfzKMAAV4ilLoDrslAOHjxIPXr0oGvXrtHatWupUaNGVoCjiDWWLq1ataqCkq53SU9PF+XzUMQgLCyMpkyZQlgXRAIc9TeHDx/u+oEU9/Djrwep67wX6U4aWdcGtwW4UcWM0zLSqMOiFnTyl71UMSCQvuizg27cTbECPLvKQIpfj7tpVsDtAD98+DBNmDCBbt26JSrWf/DBB6IYsaMGQMXGxtLWrVvF9pMnTxYFAOwb9jls2LBspStVqhRXpc9Wpew3+Pnnn6lv376EggkS4DIrzw7gFy5coBUrVtC6desItUpl/6yOev/+ffr+++9p3rx5oig1GrL7Ll26iIIQjta1xjWFzFsCXGS2Q4eKQh+6AZ6Yct4KUVncwTYrtwe4hLtlMUGK6baG2tZ8+OQjm6zg80R+olk9v6LgSq2sn3Ve1obij2+2AhwfyKycAZ79de6NW7gV4KgIAnij+DCaI4CjBBQ+x48NdRPxb9kY4JkvKV0WigQ4PHhpl0iA16tXT2TgpUuXtp4sCgrEx8fTkiVLxNrUyIhlcwZw9EPBY9TLdNRwE4FtU6RIkUwfS4BLuwRZuQQ4MvJu3bpp+23aAlzaJRLgOKn5vbbTXysGWc9v4rYRtGhrtPh3sxc70rwOqyif5X9oybevUei8xnQx6Sfxb3v4S4BLuyQtPc0KcKNKtmkTkg/sUAG3ARzFbPFYiz/BwcGEx3DUp7TPwI8fP05RUVGEiuWAAcqhoRzU2bNns8zAs4vlsWPHaMyYMSJ7HzJkiOHVSB43CyUpKUlYErghS7tE2ipVqlQR2XLJkiWtYbG1XFq3bi0AOm3aNJFROwN4XFwcvfvuu1S2bFkaOXIkNW3aVOwT+xs7dqx4Apg4cSJ17Ngx0yWAc8LnMtu2tVVQ+BrZu652Ne0yhc5tTL9eOmUFrrRVkKss7L2TGlVoYj09ZNhrdk0lP98KdP/+PfoyYi+V831YP3T72W8ockkIlfKvSkm//vwIwAfH9aO43fOt5dlsbZXsSrvp0oeP65oCbgO4hGhgYKCoDh8dHS2sE3uAIztbvHixqBpSp04dSk1NFZ4lfqxZZeDOvrLM4vAYDm8UNwWjmy6A65qFcvXqVQHwy5cvWwEus3Jk3vYAh/2FLBp1SVFUAGtUS086K4BjGwAYT2PIwjEgadsOHDgg9lGzZk1hl9jacHJA1dYukVl5dgB3dx1N28FFmTHLrPzOneQsAf73BoNow94ZNLnzHzYKAH3w3C6qW7EhbdqzkMZ1XEjdnu+VCf7Lt03NVF9TZuUMcKMp4Bn7cwvAb968KeCLQsPjx48XRWyRUTkCuL0MtlXqVQCOG8eIESMEuN2RfeN8dQFcl4Xi6qUqbwCYFZIVwGXWjgHSDz/8MJNNgpkmc+fOpVmzZomnOCNnvXhSJXvoDEhvOTCfYjp9TjH/jKIKpavS8m6x9FvqJXp1TgNqFdiJapR5jqJWdM+2YLKrceP+nq+A4QCHdQI/G4+1yIgw8JSQkJAnAEf2jR8/su/Ro0dZsvq/uCUCugCuaxaKqyLmBOAA++DBg4V3/eabb1oPie8MO2zz5s3W/7Zq1Spq0uQP28GV8/M0gCNjPnx6s8jMY4+tpa1HV1Ns5H46dHE/jf7idVrcayedufozA9yVoJuor+EAx6M15t3WqFFDDDgVLlxYZOJ5kYHDY8WgKawYzFLBsd3RdAFcl4XiqoY5ATjGSgBvaXkgEdi7d6+4llBdvXfv3uI0ZsyYYd3G1fNCf3dbKLk9RwD86NnNtKLfATFoOWBxCI1ut4i2n/6akpIv0Lqe39LGn9YzwHMrrEm3NxTg8LPxAzx16pSwTjDrBC0vAI5B0JiYmP/+6N2XfbOFkvtfQk4AbutZYzrg6tWrxXhJ8eLFRSLQtm1b8d/w/7PztXN/hp7TAwD/KXEPbRx4mHwL+olZJAV8CtKVlIvU9+Wh1M/ijcupho0CQ2lply895+T5TPJcAcMAjoxp06ZNYoBJWif58j2c/pQXAM+r7FsnwM1sociZJMjCcb3AUmnQoIEY/K5WrZq4juQ2ZgW4HPC8euOCAHiAXwWK2TGO5m4ZS0V9/Wht/71UtVR1K8B5bnee89LjDmgYwDHtD1O5kHVL60R+W3cDHJk/BjwxU8Gd3rf8Pmyh5O46zkkGLmeSyD2//np3eu+996lEiRLiPyFBmDRpEs2ePZuM9MBz903cu7UjgB+8GE/h8xtQzWdCaGX4RvEqvJxHXrdya1oVvsm9J8V792gFDAM4sm/4kzltgwYNEgOc9k1lFsoPP+y1WDYT6MUXX3Sr960b4GaehYIZKuHh4WLNEswi6tSpE/n4+FgvDznNMDExUeur+zm9vlW2cwRwR/uRAK9ekdc3UdHZTH28HuByyiLe4syL7JstlNxf/jnJwGEPDRgwQKy34mhtFSyvMHDgQGrevPkj0wxzf0Z/9PCkQcyLNxItr92/QPcf3LNaKM4AXu6ph2ue+BUq7ooEoi8mH+DJBksZILGqX7++y/vkHbhfAcMA7uxU3Wmh4JVuPFrnVfatE+BmnoUCi2ThwoViyiBeAIIXXqtWLbG0Al7HxxuYyMIdveTjys/Ek6YRyhd88H2kB55XAMdN88yZM+JwGDju37+/1b5yRV/u614FtAPc1jJx9lUxCyEiIiLTJrbZNx678RJIXjRdHri3WCi2GbezeNgvNIU3ODHdFAOY9g1TQjFPHOuh2ForrsbbEwFe0re808xaWihlS9eiDX2/p+KF/F2VgTZu3Eh79uwRGXiBAgXE8ge6Vph0+cs8RjvwaoB/99139I9//IOef/554X0XLVo0T0KnC+DeMgtFFeAIHqaDYjxl6dKlYlC6WLFi4nX8Xr16ib/xVq+RzZMslJNXTlCH2fXpKf9KTgEu11Lx8fF3mqnnRickQ1gSAStGMsBzo5zebfME4Hq/ovFH1wVwb7VQjI8A79EdCmAm0JEjR4SFgvEI/M3NsxVggCvERxfAvcVCUZCUu2hUANNwMQsIYw2oZoQnHVRd4ub5CjDAFWKkC+DeYqEoSMpdNClgO3gJewovTWH5XSPHGTR9tcfisAxwhTDrAjhbKArB4i5OFQDAsdZMmTJlxBTN6tWrs2JepAADXCFYugDOFopCsLgLK2BiBRjgCsHVBXC2UBSCxV1YARMrwABXCK4ugCucKndhBVgBEyvAAFcILgNcQTTuwgqwAoYrwABXkJQBriAad2EFWAHDFWCAK0jKAFcQjbuwAqyA4QowwBUk1QVwHsRUCBZ3YQVMrAADXCG4ugDO88AVgsVdWAETK8AAVwiuLoDzPHCFYHEXVsDECjDAFYKrC+BsoSgEi7uwAiZWgAGuEFxdAGcLRSFY3IUVMLECDHCF4OoCuC4LBVWPXnvtNaHUnDlzxEp1sghxuXLlaMGCBVS7dm0FJV3vcvv2bVG9Z/369dSsWTOaOXOmWFGvX79+YoW9Pn36WErtjRa1NnU0WXwh4y5Ri3qdaW77ldaq8jifoe0+oX4NBrl8arKeZkLiESpZKoDiIvZRxv10S4m2upSakky1q3L9TJdF9sAdMMAVgqIL4LoslIMHD1KPHj1EvUpUy0HlIwnw//mf/9FaZDg9PZ1GjRpFy5cvp7CwMJoyZQpheVQJcPuqPwrhdqmLLL5wJ42oW/P3aVxITCaAR3ddSh1rh7t0DHROy0ijDota0Mlf9lLFgIe1Mm/cTbECvH4trmDvssgeuAO3A/zw4cM0YcIEQrks/Ng/+OAD8vPzcygFABUbG0soYIvtJ0+eTHXr1s1SNpRjQ/UWrGOMauVopUqVopdffllkiWXLlnWL5LoArstCQcFblDJD9RoJcJmVZwfwCxcu0IoVK2jdunWi2ovs7ywwiH1cXByh3BkKDGQHYVxTyLwlwEVm+9+sPLu+brlAbHYq61wiC5YAt83KHQHc9vOszs9Rv87L2lD88c1WgKNvuwVBhKycAe7uSOvZv1sBfuPGDQHvo0ePim/nCOAoWovP8QiMyvL4t2zOAH727FkaO3asgIKjBpCjQG6VKlUMV1YXwHVZKBLguIFIu0QCvF69eiIDL126tFXnjIwMio+PpyVLloibKzJi2bICOIoaJyQk0OrVq62wl32yg7AEuLRLkJVLgCMjR31HXc0W4NIukYDGOc3vtZ3+WjEo0+m5CnBpl6Slp1kB3iloME1qNU2XDHxcNyngNoDjB4nHWvwJDg4mPIb7+/s/koEfP36coqKiRC1EwCA0NJQ+++wzAqCzAjgAMX36dNq2bZvYHj9QX19fwjF///13AQ581qpVKxo0aJDh/qcugOuyUJKSkoQlgRsyYI1it9JWwQ0StRRLlixpvURtLZfWrVuL+EybNo3279+fZQaOpymAGnVOsSb1O++8Q/v27RM3jOwAjnPCzVxuZ2urTJ06VRQo0NWupl2m0LmN6ddLp0hmzdJWQa6ysPdOalShiUOAl3vqoRXiVyhnpc0Gx/WjuN3zrdm2ra0is39dOvBx3aOA2wB+7NgxkQEHBgZS+/btKTo6Wlgn9hYKsrPFixfTSy+9RHXq1KHU1FQaPny4eFzPCuCykj2gj/3aA/XUqVOEKvUYWBsyZAgVLFjQUPV0AVyXhSKLFF++fNkKcJmVI/O2BzgsENxgg4KCRHmu5ORkqyftzEKBr46bM66XIkWKiGsF1kh2AJd+vO12sm92AHd3UWPbwUUJcJmV37mTbCjAx2wdQsu3Tc1kl0hbhQFuKAI8ZmduATgqXAO+586do/Hjx4tK4iNHjnQIcHslJJydARzgjomJERldVNRwatDgJcqXL5/YFbJw+OL44Xft2pW6d+9uuNi6AK7LQnFVQNsq9TnxwOXxcgpwV84PPjueAtFq1apF4eGuDyi6cj7oKy2U3Gbgrh6X+3ufAoYDHACFn43HWmREbdq0Ed6mkQCHzHJwFFkppo/hMblQoUJiEPTzzz+nSpUqidkJ8MKNbroArstCcVU/BnjuFGSA506vx3lrwwGOR2vMu61Rowa9//77VLhwYZGJGw1wBO3kyZP06aefEo4pW/78+alt27bUuXNn8RjujqYL4LosFFc19GSAu9tCUdEuu0HMYn7+tHHgYQrwq6Cye+5jIgUMBTj8bHiO8KBhnWDWCZq7AA5vFQOWmHZoO3sFg6EDBw403TRCtlBM9Mtz8lUY4I9HnI34loYB3NZ7ltaJ9KXdAXDMUpk4cSJdvHhRzHLBiyZnzpy2ZOSzxdRCZMmYmfDss88aoVOmfejKwNlCMTyUHrlDtlA8MiweeVKGAVzOy0bWLa0T+Y2NBjgyfQySYpoZXvEGvOWr0hgE/eijj2jPnj2Wwc0GNGzYMGHjGNl0AZwtFCOj6Ln7YoB7bmw87cwMAzhmfsyYMSPH3w/zszHAad9yMgtFThMsWrSomEZo/8YlrAb48BjUxOcBAQE5Pq+cbKgL4Gyh5CQ63r8NA9z7Y5hX38ArAY7XqzFXvEKFCgLQeEHItsmMH9MXzQRwtlCM/1l48iBmXk4jxESAVatW0f3790ViVb9+fePF5j0aroBhAHd2ZkZbKHihBBn2+fPnCW/6wUaR0wXxJibm9n7zzTdsoRh+uajt0JNnofA88IcxxbTfM2fOiP9fvHhx6t+/P5UoUUIt4NwrzxTQDnBby8TZt8bUwIiICLEJBky//vpr69KhjvphmVNMXTTTIKa3WCi2wHYWU/s3LOWLO8764I1d+zc/KMbtzQAAG/VJREFUXfm1MMAfqrdx40YxboQMvECBAmL5AyyZwM2zFfBKgEuIY+B0w4YN4qWeK1euiIFMABurEYaEhGS56qGrIdHlgXuLheJNAGcL5eGvAW9P48aIGVwMcFcJkXf98wTgefd18uZIugDurbNQ8iYqfBRXFcCaMhhfgoUyYMAA8Tc3z1aAAa4QH10A9xYLRUFS7qJRAUzLRfUiLP2LakZYgAzr6XPzfAUY4Aox0gVwb7FQFCTlLpoUsB28xKytatWqiXWFfHx8NJ0RHzY3CjDAc6PWf7fVBXC2UBSCxV2cKgCAYzZXmTJlqHnz5mItdm7eowADXCFWugDOFopCsLgLK2BiBRjgCsHVBXC2UBSCxV1YARMrwABXCK4ugCucKndhBVgBEyvAAFcILgNcQTTuwgqwAoYrwABXkJQBriAad2EFWAHDFWCAK0iqC+DsgSsEi7uwAiZWgAGuEFxdAOdphArB4i6sgIkVYIArBFcXwHkaoUKwuAsrYGIFGOAKwdUFcLZQFILFXVgBEyvAAFcIri6As4WiECzuwgqYWAEGuEJwdQFcl4Wye/duUTQDbc6cOWKhI6xch9qnWHd9wYIFVLt2bQUlXe9y+/ZtGjp0KK1fv56aNWtmXSO+X79+YoGmPn36iOIfsmaq60fM3R5sK8y3qNeZ5rZfSWuOLqOoFd3Fjoa2+4T6NRiUu5062DrlznVqtyCIEhKPUMlSARQXsY8y7qfT32bVpdSUZKpdtSmt7fE1+fypgMvH4h14jgIMcIVY6AK4Lgvl4MGDonD0tWvXaO3atdSoUSMrwFHEGutp6Fr8Pz09nUaNGkXLly+nsLAwmjJlCmF1PQlw+6IRCuF2qcuPvx6krvNepDtpRN2av0/jQmIyATy661LqWDvcpWOgc1pGGnVY1IJO/rKXKgYE0hd9dtCNuylWgNev1ZpWhW9y+Ti8A89SwO0AR7GFCRMm0K1btwg/dlRd8fPzc6gCABUbG0tbt24V26PyfN26dbNU7I4l+4qNixPl0xITE6lIkSIiE+zcuTNVqVKF8uXL5xa1dQFcl4WCeol9+/YlFD+QAJdZeXYAv3DhAq1YsYLWrVsnigXI/lkFBhk1rgHUZzxw4AAVK1aMmjZtKqoxIbaOYior+UiAi8z2v1m5boAnppy3QlQC3DYrtwe4zM4tCwNSTLc11Lbmwycf2cZsHULLt02lJ/ITzer5FQVXamX9rPOyNhR/fLMV4PhAZuUMcLegQPtO3QrwGzduCHgfPXpUfFFHAP/Pf/4jPscj8KFDhwj/ls0ZwFGNZ+LEiXTx4sVHRMTjcmRkpKiX6Q6I6wK4LgtFAhw3EGmXSIDXq1dPZOClS5e2xiEjI4Pi4+NpyZIlYo1pZMSyOQM4Yoli1du2bXskpgD5uHHjhJVjH1MJcGmXICuXAEdGjvJgupotwKVdIgGOc5rfazv9tWKQ9fQmbhtBi7ZGi383e7EjzeuwivJZ/oeWfPsahc5rTBeTfhL/toe/BLi0S9LS06wA7xQ0mCa1mqZLBj6umxRwG8BRtxKPtfgTHBxMeAxH9Xj7DPz48eMUFRVFd+/eJcAgNDSUPvvsMwKgswI4yj/hMwAfP+h27dqRr68vARwAy6xZs0RZKAD+mWeeMVw6XQDXZaEkJSUJSwI3ZGmXSFsFTzr2NSptLRfcRAHQadOm0f79+7PMwBE7xAs3iNdf706DBr1JZcuWpeTkZBHP2bNni+sDf+O/2zac09ixY0lm27a2ytSpU8X61rra1bTLFDq3Mf166ZQVuNJWQa6ysPdOalShifX0kGGv2TWV/HwrWOpT3qMvI/ZSOd8A8fn2s99Q5JIQKuVflZJ+/fkRgA+O60dxu+eTzLZtbRWZ/evSgY/rHgXcBvBjx47RmDFjKDAwkNq3b0/R0dHCOrEHOLKzxYsXE4rV1qlTh1JTU0UWhsf1rACOsk/YpkmTJvTuu+8+svj8pk2baMaMGdS7d2/r4JuR8ukCuC4LRda4vHz5shXgMitH5m0PcNhf06dPp6CgIFHdBRCWnnR2GfjWrf+0AD88U0zlDQR2nKP+ckDV1i6RWXl2AHd3TUzbwUWZMcus/M6d5CwB/nfLwOaGvTNocuc/bBQA+uC5XVS3YkPatGchjeu4kLo93ysT/GGv2NolMitngBtJAM/Zl1sALjPkc+fO0fjx4wmVPlAh3hHA7aWwrVKfFcAloGGTIGO3b8jeR4wYQc8995yYKWF0dRFdANdlobh6udoWOc7OA3d0LNuZJir9nZ2/p1WlB6S3HJhPMZ0+p5h/RlGF0lVpebdY+i31Er06pwG1CuxENco8J2axMJRdvTK9v7/hAId1Aj8bj7XIiNq0aUMJCQmGAhy+KuDeqlUry6P2oEemiMmbAG4cyPxhrxjZdAFcl4XiqnauAvzKlSvUv39/OnXqlHhae+GFF1w9JWt/TwM4MubDpzeLzDz22FraenQ1xUbup0MX99PoL16nxb120pmrPzPADbsCvHtHhgMcj9aYd1ujRg2R/RYuXJiQiRuZgcv9ITPr2bOnKAWF48BHPXnypHjMhg9bsWJFp7NeVEOnC+C6LBRVnWQ/VwGOWUkDBw4Ucf7www/FbCOjmrstlNyeJwB+9OxmWtHvgBi0HLA4hEa3W0TbT39NSckXaF3Pb2njT+sZ4LkV1qTbGwpw+NnwHJEpwTrBrBM0owEus3wMdtrOWrGPUXbTFlVjqgvgj6OFgu/85ptvEm4CGNfAHHQzNwD8p8Q9tHHgYfIt6CdmkRTwKUhXUi5S35eHipd+5FTDRoGhtLTLl2aWg79bNgoYBnBAFd70zJkzrdaJnO5lNMDxne7fvy9mNXz++ed04sQJunfvHpUqVUoMhtar9yJ9+ulsCggIEF44snMjmy6AP24WCqYVvvfee2I+OBKCTp06uWVaqJHXhiv7kgOeV29cEAAP8KtAMTvG0dwtY6morx+t7b+XqpaqbgU4z+12RW1z9DUM4Bg4xFQuZL3SOpESuQPgzuTHEwDAjWzNkUfuauh0AfxxslDOW8ZN3rNYcD/++KNlmunwR2amuBpDT+zvCOAHL8ZT+PwGVPOZEFoZvlG8Ci/nkdetzG9XemIc8/KcDAO4nBmS05MHWDHAad9yMgvF2THwJICBKbz9hxtJixYtcnpKOd5OF8AfFwvl9OnT4kUcTEVFUoA3azEgbfbmCOCOvrMEePWKvL6J2a+J7L6fqQAOeOMNQLx9B8jisdv2DcHsxMjp57oA/jhYKID2O++8I5ZGyOrNy5zGKSfbedIg5sUbiZbX7l+g+w/uWS0UZwAv99TDNU/8ChXPyVd1ug0mH2D5AliTSKzq16/v8j55B+5XwDCAOztVd1soeIsTP3g8BWBdlIIFC4oXffDmnjuaLoCb3ULZu3evyLzxHgFmLbVt29btnrcnTSOUL/jgmpUeeF4BHNN+z5w5Iw5XvHhxMW2zRIkS7vj58D4NVEA7wG0tE2ffCz9mLGgkW1aWDQYyMWsBGYQ71kHB8XUB3FssFNtpg85iavvmpHxbc8+ePU4v7+wWz8rtb8MTAV7St7zTzFpaKGVL16INfb+n4oX8c/u1H9l+48aNBO2RgWMZCix/oGuFSZe/zGO0A1MAHNDGDxvrQb/UoAEVevJJt4ZQF8C9xUJRAXhO+xgNcE+yUE5eOUEdZtenp/wrOQW4XEvFx8ffaaaemx8BnnqwJAJWjGSA50Y5vdvmCcD1fkXjj64L4N5qoRgfAd6jOxTAmjJYZwgWyoABA8Tf3DxbAQa4Qnx0AdxbLBQFSbmLRgXwAh6qF2GJCrxPgQXIUHWJm+crwABXiJEugHuLhaIgKXfRpIDt4CWmalarVk0sv2v0AnCavp7pD8sAVwixLoCzhaIQLO7iVAEA/Pz581SmTBmx1kz16tVZMS9SgAGuECxdAGcLRSFY3IUVMLECDHCF4OoCOFsoCsHiLqyAiRVggCsEVxfAFU6Vu7ACrICJFWCAKwSXAa4gGndhBVgBwxVggCtIygBXEI27sAKsgOEKMMAVJGWAK4jGXVgBVsBwBRjgCpLqAjgPYioEi7uwAiZWgAGuEFxdAOd54ArB4i6sgIkVYIArBFcXwHkeuEKwuAsrYGIFGOAKwdUFcLZQFILFXVgBEyvAAFcIri6As4WiECzuwgqYWAEGuEJwdQFcl4Wye/dueu2114RSc+bMESvVYelR1BwtV64cLViwgGrXrq2gpOtdbt++Lar4rF+/XqwHP3PmTLGiXr9+/cQKe3369KHRo0fTE0884frBFPYgiy9k3CVqUa8zzW2/0lpVHrsb2u4T6tdgkMKeM3eR9TQTEo9QyVIBFBexjzLup1tKtNWl1JRkql2V62e6LLIH7oABrhAUXQDXZaEcPHiQevToQdeuXaO1a9dSo0aNrAA3usBCbsORnp5Oo0aNouXLl1NYWJioh4rlUSXAbav+5HbfRmwviy/cSSPq1vx9GhcSkwng0V2XUsfa4S4fKi0jjTosakEnf9lLFQMe1sq8cTfFCvD6tbiCvcsie+AO3A7ww4cP04QJE+jWrVuias4HH3xAfn5+j0jx+++/05dffilqWt64cYN8fX2pZcuW4kfp7++4ZBTKP+3fv59Wr15NKMqK9uyzz1JoaCgFBQW5bUlMXQDXZaFA2759+xKq10iAy6w8O4BfuHCBVqxYQevWrRPVXmR/R7+FjIwMUdYL2T3iiu0DAgLo5ZdfFjcQLHXqqEwerilk3hLgIrP9b1auG+CyziWyYAlw26zcHuBrji6jqBXdybKyK8V0W0Ntaz588pFtzNYhtHzbVHoiP9Gsnl9RcKVW1s86L2tD8cc3WwGOD9otCCJk5QxwD6SvAafkVoADxID30aNHxak6AjgqyePHOnXqVAFu+4ZHdBS4BZht23/+8x9avHixAIKj9sorrSzQ6UeFCxc2QKbMu9AFcF0WigQ4biDSLpEAR+FoLElaunRpq0gAcXx8PC1ZskQUCUBGLJszgNtaNfZBK1asGE2cOJHat2//SDwlwKVdgqxcAhwZOeo76mq2AJd2iQQ4zml+r+3014pB1tObuG0ELdoaLf7d7MWONK/DKspn+R9a8u1rFDqvMV1M+kn82x7+EuDSLklLT7MCvFPQYJrUapouGfi4blLAbQAHmPFYiz/BwcGEx3Bk0vYZOLIsABo1EXv27Cmy7vz581NCQgJNmzaNTp8+LTxXlHiy9TG/++47+sc//iH2GRkZSS+99JKQ6Pjx4/Txxx/TpUuXaNCgQdSq1R8ZilEa6gK4LgslKSlJWBK4wQLWKHYrbZUqVaqIWoolS5a0ymtrubRu3VoAFLHEjdoZwAH9bdu2Cb/9mWeesWShfyIUO8aN+tNPPxUxRqZt/wSHcxo7dizJbNvWVkFigAIFutrVtMsUOrcx/XrplBW40lax5CC0sPdOalShifX0kGGv2TWV/HwrWAoM36MvI/ZSOd8A8fn2s99Q5JIQKuVflZJ+/fkRgA+O60dxu+dbs21bW0Vm/7p04OO6RwG3AfzYsWM0ZswYCgwMFFlTdHS0+OE5slD27dsnfqzI5mwbMrLx48c/krkDJPjBnjlzhkaMGEENLIWMbZs8NrJ2nAOyNyObLoDrslBkweHLly9bAS6zcmTe9gCHXTZ9+nRhY6E8l6w4j0FFZwDPKkY4Liwc3MDtj4U+ckDV1i6RWXl2AHd3UWPbwUWZMcus/M6d5CwB/nfLwOaGvTNocuc/bBQA+uC5XVS3YkPatGchjeu4kLo93ysT/GGv2NolMitngBtJAM/Zl1sAjgrXkydPpnPnzgkAA87IsrMCeFZyoL+jfsiyo6KiqE6dOjRs2LBMNgmyr1WrVtGaNWuoSJEiNGnSJEKWaGTTBXBdFoqr2tlWnFcB+L///W/xBIAs31EG7sr5LVu2TDy1odWqVYvCw10fUHTlfADpLQfmU0ynzynmn1FUoXRVWt4tln5LvUSvzmlArQI7UY0yzwmfnKHsitLm6Gs4wGGdYEoXHmuREbVp00bYISoAxwAoMuwaNWpkyqS//vprkeF17dqVunfvbo0EMrWPPvqIDhw4YP1v8E3tM3tXQ6cL4LosFFf1UgU4BqlxE4cltmvXLhFzDGga2TwN4MiYD5/eLDLz2GNraevR1RQbuZ8OXdxPo794nRb32klnrv7MADfyIvDifRkOcDxaY94toIt5whhEzCqTdqYbBilnzZpFmzdvFtkXZhjIFhsbKzxReNy4QeCm8eOPP4of+JUrV+jvf/+72BQ3ErmNkTHSBXBdFoqr2uUG4LbzuuVx//KXv4gb+HPPPefqqTzS390WSm5PGAA/enYzreh3QAxaDlgcQqPbLaLtp7+mpOQLtK7nt7Txp/UM8NwKa9LtDQU4ZhvAczx16pTVu4ZuuQU4gAxwA9KYOoZ5vrZTCfEyyYYNGwScMei5ceNGWrhwobhZwCtt0aIFffXVVzRjxgxTAfxxsFAcARzXEMYz8BQXEhLicCqhWX6fAPhPiXto48DD5FvQT8wiKeBTkK6kXKS+Lw8VL/3IqYaNAkNpaZcvzfLV+XsoKGAYwAHdTZs2CY9SWidyzm5uAI79YDYCpn8VLVpUDFbaTyGEjwpgw0KBP7pz504x0Pnee+9Zt5XbmCkDf9wsFFwLeHkIN+hPPvlEXN64KeNFIjM2OeB59cYFAfAAvwoUs2Mczd0ylor6+tHa/nupaqnqVoDz3G4zXgW5+06GAfzs2bMCtgCptE7kqeQU4PjB/t///Z/wsQHvIUOGiIEl+4YbBX7IsmGaIjJvOb0M+5k9ezbBajGTB/44WChZXb5ffPGFeJrClES8W1CgQIHcXelesLUjgB+8GE/h8xtQzWdCaGX4RvL5UwGS88jrVua3K70grG49RcMAbg/V7M7aPjMGdDEHGLYJ4A0fvVKlSg53c+TIERo+fLh4lAa4MU/cdo64nGaIOeYAOOYUG9l0eeCPg4WSVZwwUwRjIS+++KJ4OnvyySeNDKlH7MsRwB2dmAR49Yq8volHBE7jSXgEwDHbAJ43suYyZco4fPPSViPMNgHgAWpHgMb8cUwfxI/dfpqhEVrrAvjjZqHYxkpm4HjD8s033zQijGIfnjSIefFGomXtkhfo/oN7VgvFGcDLPfVwzRO/QsVd1gOTDzD9Fr9FTAyoX7++y/vkHbhfAcMA7uxUnVkomG2COdt4Y7NixYriFegKFSo4/ea2UxVr1qxJ/fv3p8qVK4vZKHhZBFl8amqqw5d8jJBUF8AfNwsFMMEMFgxI4+aOF7IQW8TaqOZJ0wjlCz74btIDzyuAY9ovXoxDK168uPhNlShRwiiZeT9uUkA7wKUdApA7a40bNxaeeMGCBcVmmPECrxwDmPYNdgq80o4dO7plGVFdAPcWC8V22qCzmNovNCXfnnTUp3r16uJpSy6ZYNTvwRMBXtK3vNPMWlooZUvXog19v6fihRwv9pYbjTBQjIXEcNPE+AJ+P1gygZtnK6Ad4HhZBzZHds0e4Ngeiybt2LFDzPdGlo81VDBXGGtp4C1NvAHqjqYL4N5ioRgFcOiMeL7yyivisR5v1hrdPMlCOXnlBHWYXZ+e8q/kFOByLRUfH3+nmXputMLb01imAONGDPDcKKd32zwBuN6vaPzRdQHcWy0U4yPAe3SHAlhTBk/EsFCweBz+5ubZCjDAFeKjC+DeYqEoSMpdNCoAOxJjR1j6F9WMsAAZZnZx83wFGOAKMdIFcG+xUBQk5S6aFLAdvITliDefsfyuj4+PpjPiw+ZGAQZ4btT677a6AM4WikKwuItTBQDw8+fPi+m7zZs3JwwWc/MeBRjgCrHSBXC2UBSCxV1YARMrwABXCK4ugLOFohAs7sIKmFgBBrhCcHUBXOFUuQsrwAqYWAEGuEJwGeAKonEXVoAVMFwBBriCpAxwBdG4CyvAChiuAANcQVJdAGcPXCFY3IUVMLECDHCF4OoCOE8jVAgWd2EFTKwAA1whuLoAztMIFYLFXVgBEyvAAFcIri6As4WiECzuwgqYWAEGuEJwdQGcLRSFYHEXVsDECjDAFYKrC+C6LBRUOMISvWhz5swRCx1h5TrUPi1XrhwtWLCAateuraCk611sq9g3a9ZMFNXGgkwov4YFmvr06SOqN9mW3HP9qDnfg1y7O+MuUYt6nWlu+5XWosTYy9B2n4hK8642WY4tIfEIlSwVQHER+yjjfrqlwk9dSk1JptpVufyaqxp7Yn8GuEJUdAFcl4Vy8OBB6tGjh6gQv3btWlEVXgIcRayxnoauxf/T09Np1KhRoqJTWFiYqJeJ1fUkwO2LRiiE26Uucu3uO2lE3Zq/T+NCYjIBPLrrUupYO9ylY6BzWkYadVjUgk7+spcqBjwstXbjbooV4FzB3mWJPXIHbgc4CjagivitW7dExXpUXZHV420V+f333+nLL7+kb775RtS69PX1pZYtW4ofpb9/1hVH7ty+Td9aiiFv2LCB/v3vf1Pbtm0pIiLCrWLrArguCwX1ElE8GsUPJMBlVp4dwC9cuEArVqygdevWiWIBsn9OAoTap2+//bYo2oGWVV9ZyUcCXGS2ltJ8KPShG+CyTBqyYAlw26zcHuBrji6jqBXdLcVIiGK6raG2NR8++cg2ZusQWr5tKj2Rn2hWz68ouFIr62edl7Wh+OObrQDHB+0WBBGycgZ4Tq4479vGrQAHiAHvo0ePCmUcARx1LPfv309Tp04V4LZveEQfOXIkPfvss9aP0AfZaFxcHG3dulXcHGQzM8B1WSgS4LiBSLtEArxevXoiAy9durQ1BqiUFB8fT0uWLBFrTCMjli2nAEeMYYdMnjw5274S4NIuQVYuAY6MHOXBdDVbgEu7RAIc5zS/13b6a8Ug6+lN3DaCFm2NFv9u9mJHmtdhFeWz/A8t+fY1Cp3XmC4m/ST+bQ9/CXBpl6Slp1kB3iloME1qNU2XDHxcNyngNoDjB4jHWvwJDg4mPIYjk7bPwJGVAdAow9WzZ0+RdaM0WkJCAk2bNo1Onz4tPFdUCJE+JgoWjxs3jo4dO0bIhnv37k3I9Lds2WLqDFyXhZKUlCQsCdxgpV0ibZUqVaqIUlwlS5a0XqK2lkvr1q0FQBFL3KhzCvADBw6IY6KkGq6lbZanrKz64pzGjh1rzbZtbRUkBljfWle7mnaZQuc2pl8vnbICV9oqKAO7sPdOalShifX0kGGv2TWV/HwrWOpT3qMvI/ZSOd8A8fn2s99Q5JIQKuVflZJ+/fkRgA+O60dxu+dbs21bW0Vm/7p04OO6RwG3ARxwHTNmDAUGBlL79u0pOjpaWCeOLJR9+/aJ+pXI5mwbsrzx48c7zNw3bdpE+KG+0qoVFXrySTG4BhvFzBm4LgtF1riEpSEBLrNyZN72AMcT0fTp0ykoKEhUd0lOTrZ60jkBOLZ/6623xE0c+0EmDzskq77Sj7e1S2RWnh3A3V0T03ZwUWbMMiu/cyc5S4D/3TKwuWHvDJrc+Q8bBYA+eG4X1a3YkDbtWUjjOi6kbs/3ygR/2Cu2donMyhng7gGo7r3+P85ZTasefvNkAAAAAElFTkSuQmCC"
    }
   },
   "cell_type": "markdown",
   "id": "ef935fc4",
   "metadata": {},
   "source": [
    "Возвращаемся к выгрузке про пользователей из социальной сети. Снова загрузите ее в датафрейм, оставьте только столбцы username, name, sex и сохраните в формате json (кодировка utf8). Сохранение выполните таким образом чтобы ключами были названия колонок, а значениями вложенные словари, которые будут хранить лейбл строки и само значение:\n",
    "![%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png](attachment:%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png)\n",
    "Когда функция to_json сохранит файл - загружайте на степик. Дополнительно форматировать результат для лучшей читаемости не следует. Чтобы тестовая система приняла результат - в файле .json должна быть всего одна строка."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "59d32913",
   "metadata": {},
   "outputs": [],
   "source": [
    "url = 'https://stepik.org/media/attachments/lesson/755302/users.csv'\n",
    "df = pd.read_csv(url, sep=';', usecols=['username', 'name', 'sex'])\n",
    "df.to_json('users.json')\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c3f98a25",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst = pd.read_html('https://cbr.ru/hd_base/bankpapers/')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "df500fc2",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f054a65",
   "metadata": {},
   "outputs": [],
   "source": [
    "lst.drop(0, inplace=True)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "368595e2",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = lst[0]"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "07d612a6",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "2a5bf57d",
   "metadata": {},
   "source": [
    "  Ваш друг Илья работает аналитиком в компании, которая занимается установкой и обслуживанием платных стоянок (стоек) для парковки велосипедов. Сегодня на работе ему поручили посчитать вместимость всех велосипедных стоянок в районе Тропарёво-Никулино. Говорит, что компания планирует устанавливать новые платные стоянки для велосипедов в этом районе. Проблема заключается в том, что данные лежат в формате HDF5 и Илья никогда раньше не работал с ним. Он попросил вашей помощи и сказал, что район записан в столбце District, а вместительность парковки в столбце Capacity\n",
    "\n",
    "#### Посчитайте суммарную вместительность велосипедных парковок в районе Тропарёво-Никулино.\n",
    "\n",
    "Источник данных: Портал открытых данных Правительства Москвы - Велосипедные парковки"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "98fa8503",
   "metadata": {},
   "outputs": [],
   "source": [
    "#s = pd.HDFStore('data_store2.h5')\n",
    "#s.keys()\n",
    "# >>> ['/parking_table', '/ser_district_value_counts']\n",
    "#s.close()\n",
    "\n",
    "f = pd.read_hdf('data_store2.h5', 'parking_table') \n",
    "f.loc[f['District'] == 'район Тропарёво-Никулино']['Capacity'].sum()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "6584ceef",
   "metadata": {},
   "source": [
    "### Скачайте выгрузку \"Общий прирост постоянного населения\" в формате html\n",
    "\n",
    "#### Загрузите данные в датафрейм и определите суммарный общий прирост постоянного населения за период с 2014 по 2020 (включительно) для субъекта Камчатский край\n",
    "\n",
    "Т.е. мы ходим понять, что произошло с приростом за этот период: был ли он положительным или отрицательным и в каком количестве.\n",
    "\n",
    "Источник данных: Росстат -  Общий прирост постоянного населения\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "cc2c8f0f",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('Общий_прирост_постоянного_населения.html', header=2, index_col='Unnamed: 0')[0]\n",
    "print(df.loc['Камчатский край'][2:9].sum())\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "25d84c1a",
   "metadata": {},
   "source": [
    "### Скачайте выгрузку \"Общий прирост постоянного населения\" в формате html\n",
    "Загрузите данные в датафрейм и определите в какой из областей произошел наибольший отрицательный прирост постоянного населения за 2020 год (сравниваем абсолютные значения)\n",
    "Источник данных: Росстат -  Общий прирост постоянного населения"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f7a6eb1",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_html('Общий_прирост_постоянного_населения.html', header=2, index_col ='Unnamed: 0')[0]\n",
    "# df.loc[['Свердловская область', 'Магаданская область','Сахалинская область', 'Калужская область','Ярославская область', 'Кировская область'], ['2020 г.']]\n",
    "df.loc[['Свердловская область', 'Магаданская область','Сахалинская область', 'Калужская область','Ярославская область', 'Кировская область'], ['2020 г.']].sort_values('2020 г.', ascending=True)[['2020 г.']].head(1)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ba1232a9",
   "metadata": {},
   "source": [
    "### Вы продолжаете работу в аналитическом отделе некоторой социальной сети, которая объединяет людей занимающихся благотворительностью. Коллеги аналитики для вас подготовили выгрузку пользователей в формате XML. Загрузите файл XML в датафрейм и посчитайте сколько пользователей женского пола с группой крови B+ в выгрузке. \n",
    "\n",
    "https://stepik.org/media/attachments/lesson/755303/users.xml"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "229ef3c5",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.read_xml('https://stepik.org/media/attachments/lesson/755303/users.xml')\n",
    "#df[(df['sex'] == 'F') & (df['blood_group'] == 'B+')]\n",
    "#df.query('sex == \"F\" & blood_group == \"B+\"').count()[0]\n",
    "\n",
    "df.query('sex == \"F\" & blood_group == \"B+\"').shape[0]\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c0fcfd49",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "markdown",
   "id": "dfae4e80",
   "metadata": {},
   "source": [
    "### Из серии (s1) вытяните слова, содержащие не менее 2 гласных.\n",
    "\n",
    "Требуемый финальный результат (наполнение):\n",
    "0     Apple\n",
    "1    Orange\n",
    "4     Money\n",
    "dtype: object\n",
    "\n",
    "Индексы строк:\n",
    "Int64Index([0, 1, 4], dtype='int64')\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.series.Series'>\n",
    "Int64Index: 3 entries, 0 to 4\n",
    "Series name: None\n",
    "Non-Null Count  Dtype \n",
    "--------------  ----- \n",
    "3 non-null      object\n",
    "dtypes: object(1)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a237f975",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = pd.Series(['Apple', 'Orange', 'Plan', 'Sky', 'Money'])\n",
    "\n",
    "# Вариант 1\n",
    "glas=(\"a|e|i|o|u|A|E|I|O|U\")\n",
    "s1[s1.str.count(glas) >= 2]\n",
    "\n",
    "# Вариант 2 - через RegEx (import re)\n",
    "# import re\n",
    "# s1[s1.str.count('[aoiuye]', re.IGNORECASE) >= 2]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "4041dc19",
   "metadata": {},
   "source": [
    "### Извлеките корректные почтовые адреса из серии (s1). Используйте pattern для этой задачи.\n",
    "\n",
    "<pre>\n",
    "Требуемый финальный результат (наполнение):\n",
    "1          help@stepik.com\n",
    "2                user@t.co\n",
    "3    lovepandas@google.com\n",
    "dtype: object\n",
    "\n",
    "Индексы строк:\n",
    "Int64Index([1, 2, 3], dtype='int64')\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.series.Series'>\n",
    "Int64Index: 3 entries, 1 to 3\n",
    "Series name: None\n",
    "Non-Null Count  Dtype \n",
    "--------------  ----- \n",
    "3 non-null      object\n",
    "dtypes: object(1)\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "66f5dfdc",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "#import re\n",
    "\n",
    "s1 = pd.Series(['teach pandas at stepik.com', 'help@stepik.com', 'user@t.co', 'lovepandas@google.com', 'alexas at stepik.com'])\n",
    "pattern ='[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\\\\.[A-Za-z]{2,4}'\n",
    "\n",
    "#s1[s1.str.count(pattern,re.IGNORECASE) == 1]\n",
    "\n",
    "s1[s1.str.match(pattern)]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c08df31b",
   "metadata": {},
   "source": [
    "### Вычислите среднее значение веса каждого фрукта.\n",
    "\n",
    "<pre>\n",
    "Требуемый финальный результат (наполнение):\n",
    "apple     6.0\n",
    "banana    4.0\n",
    "carrot    5.8\n",
    "dtype: float64\n",
    "\n",
    "Индексы строк:\n",
    "Index(['apple', 'banana', 'carrot'], dtype='object')\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.series.Series'>\n",
    "Index: 3 entries, apple to carrot\n",
    "Series name: None\n",
    "Non-Null Count  Dtype  \n",
    "--------------  -----  \n",
    "3 non-null      float64\n",
    "dtypes: float64(1)\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "695d64e4",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruit_list = ['banana', 'carrot', 'apple', 'carrot', 'carrot', 'apple', 'banana', 'carrot', 'apple', 'carrot']\n",
    "weights_list =  [1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 9.0, 10.0]\n",
    "\n",
    "fruits = pd.Series(fruit_list)\n",
    "weights = pd.Series(weights_list)\n",
    "\n",
    "print(weights.groupby(fruits).mean())"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8db93c59",
   "metadata": {},
   "source": [
    "### Вычислить евклидово расстояние между рядами (точками) X и Y"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e966312",
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "\n",
    "X = pd.Series([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])\n",
    "Y = pd.Series([10, 9, 8, 7, 6, 5, 4, 3, 2, 1])\n",
    "\n",
    "distance = np.linalg.norm(X-Y)\n",
    "\n",
    "#distance = np.sqrt(np.dot(X-Y, X-Y))\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "18463a3c",
   "metadata": {},
   "outputs": [],
   "source": [
    "distance"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "664ddb2f",
   "metadata": {},
   "source": [
    "### Отредактируйте название колонок датафрейма (df) следующим образом:\n",
    "<pre>\n",
    "1. user -> user_name\n",
    "\n",
    "2. все точки в названии колонок заменить нижним подчёркиванием\n",
    "\n",
    "Требуемый финальный результат (наполнение):\n",
    "  user_name  user_balance  user_age user_group\n",
    "0      Ivan           500        34          A\n",
    "1      Petr           200        25          B\n",
    "2      Alex             0        18          A\n",
    "\n",
    "Индексы строк:\n",
    "RangeIndex(start=0, stop=3, step=1)\n",
    "\n",
    "Индексы колонок:\n",
    "Index(['user_name', 'user_balance', 'user_age', 'user_group'], dtype='object')\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.frame.DataFrame'>\n",
    "RangeIndex: 3 entries, 0 to 2\n",
    "Data columns (total 4 columns):\n",
    " N   Column        Non-Null Count  Dtype \n",
    "---  ------        --------------  ----- \n",
    " 0   user_name     3 non-null      object\n",
    " 1   user_balance  3 non-null      int64 \n",
    " 2   user_age      3 non-null      int64 \n",
    " 3   user_group    3 non-null      object\n",
    "dtypes: int64(2), object(2)\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f13863b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data = {'user' : ['Ivan', 'Petr', 'Alex'], 'user.balance' : [500, 200, 0], 'user.age' : [34, 25, 18], 'user.group' : ['A', 'B', 'A']})\n",
    "\n",
    "#df.columns = ['user_name', 'user_balance', 'user_age', 'user_group']\n",
    "\n",
    "df.rename(columns = {'user':' user_name'}, inplace = True )\n",
    "df.columns = df.columns.str.replace('.', '_', regex = False)\n",
    "\n",
    "#df.columns = df.columns.map(lambda x: x.replace(\".\", \"_\"))\n",
    "\n",
    "df\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "de0d9f66",
   "metadata": {},
   "source": [
    "### Проверьте, имеются ли пропущенные значения в датафрейме (df). Если в строке датафрейма есть хотя-бы одно пропущенное значение - верните True иначе False.\n",
    "\n",
    " \n",
    "<pre>\n",
    "Рекомендация:\n",
    "<b>\n",
    "pandas.isnull\n",
    "pandas.DataFrame.any\n",
    "</b>\n",
    "Требуемый финальный результат (наполнение):\n",
    "0    False\n",
    "1     True\n",
    "2    False\n",
    "dtype: bool\n",
    "\n",
    "Индексы строк:\n",
    "RangeIndex(start=0, stop=3, step=1)\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.series.Series'>\n",
    "RangeIndex: 3 entries, 0 to 2\n",
    "Series name: None\n",
    "Non-Null Count  Dtype\n",
    "--------------  -----\n",
    "3 non-null      bool \n",
    "dtypes: bool(1)\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c439e02a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data = {'user' : ['Ivan', 'Petr', 'Alex'], 'user.balance' : [500, None, 0], 'user.age' : [34, 25, 18], 'user.group' : ['A', 'B', 'A']})\n",
    "\n",
    "# Проверка на хотя бы одно значение NaN \n",
    "# df.isnull().values.any()\n",
    "\n",
    "df.isnull().any(axis=1)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1ccc2313",
   "metadata": {},
   "source": [
    "## Графики\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "01692ae5",
   "metadata": {},
   "outputs": [],
   "source": [
    "plt.plot([1,5],[1,5],'r')\n",
    "plt.grid()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ff6a313",
   "metadata": {},
   "outputs": [],
   "source": [
    "x = np.linspace(0, 10, 50)\n",
    "y1 = x\n",
    "y2 = [i ** 2 for i in x]\n",
    "\n",
    "\n",
    "y4 = np.sin(x)\n",
    "y5 = np.cos(x)\n",
    "y6 = np.tan(x)\n",
    "y7 = np.exp2(x)\n",
    "\n",
    "# Построение графика\n",
    "plt.title('Зависимости: y1 = x, y2 = x^2') # заголовок\n",
    "plt.xlabel('x') # ось абсцисс\n",
    "plt.ylabel('y1, y2') # ось ординат\n",
    "plt.grid() # включение отображения сетки\n",
    "plt.plot(x, y1, 'r', x, y2,'b') # построение графика\n",
    "\n",
    "#plt.plot(x,y4,'orange')\n",
    "#plt.plot(x,y5,'b') \n",
    "#plt.plot(x,y6,'g')\n",
    "#plt.plot(x,y7,'r')"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "84eca097",
   "metadata": {},
   "outputs": [],
   "source": [
    "fruits = ['Яблоки', 'Персики', 'Апельсины', 'Банана', 'Арбузы','Дыня']\n",
    "counts = [34, 25, 43, 31, 20, 17]\n",
    "plt.bar(fruits, counts)\n",
    "plt.title('Фрукты !')\n",
    "plt.xlabel('фрукт')\n",
    "plt.ylabel('количество')\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "328465a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Линейная зависимость\n",
    "x = np.linspace(0, 10, 50)\n",
    "y1 = x\n",
    "\n",
    "# Квадратичная зависимость\n",
    "y2 = [i**2 for i in x]\n",
    "\n",
    "# Построение графиков\n",
    "plt.figure(figsize=(9, 9))\n",
    "plt.subplot(2, 1, 1)\n",
    "plt.plot(x, y1) # построение графика\n",
    "plt.title('Зависимости: y1 = x, y2 = x^2') # заголовок\n",
    "plt.ylabel('y1', fontsize=14) # ось ординат\n",
    "plt.grid(True) # включение отображение сетки\n",
    "plt.subplot(2, 1, 2)\n",
    "plt.plot(x, y2) # построение графика\n",
    "plt.xlabel('x', fontsize=14) # ось абсцисс\n",
    "plt.ylabel('y2', fontsize=14) # ось ординат\n",
    "plt.grid(True) # включение отображение сетки"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "46f500a1",
   "metadata": {},
   "source": [
    "### Классическая круговая диаграмма\n",
    "Круговые диаграммы - это наглядный способ показать доли компонент в\n",
    "наборе. Они идеально подходят для отчетов, презентаций и т.п. Для\n",
    "построения круговых диаграмм в Matplotlib используется функция pie()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ff994c2",
   "metadata": {},
   "outputs": [],
   "source": [
    "vals = [24, 17, 53, 21, 35, 12, 2]\n",
    "labels = ['Ford', 'Toyota', 'BMV', 'AUDI', 'Jaguar', 'Лада', 'Москвичъ']\n",
    "fig, ax = plt.subplots()\n",
    "explode = (0, 0, 0.15, 0, 0, 0, 0)\n",
    "ax.pie(vals, labels=labels, explode=explode, autopct='%1.1f%%')\n",
    "ax.axis('equal')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "60978a04",
   "metadata": {},
   "source": [
    "### Измените даты лежащие в серии (s1) таким образом чтобы они начинались с 10-го числа соответствующего месяца.\n",
    "\n",
    "<pre>\n",
    "Требуемый финальный результат (наполнение):\n",
    "0   2022-01-10\n",
    "1   2022-02-10\n",
    "2   2022-03-10\n",
    "dtype: datetime64[ns]\n",
    "\n",
    "Индексы строк:\n",
    "RangeIndex(start=0, stop=3, step=1)\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.series.Series'>\n",
    "RangeIndex: 3 entries, 0 to 2\n",
    "Series name: None\n",
    "Non-Null Count  Dtype         \n",
    "--------------  -----         \n",
    "3 non-null      datetime64[ns]\n",
    "dtypes: datetime64[ns](1)\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1fb1ebf6",
   "metadata": {},
   "outputs": [],
   "source": [
    "N = 8\n",
    "y = np.zeros(N)\n",
    "x1 = np.linspace(0, 1000, N, endpoint=True)\n",
    "x2 = np.linspace(0, 1000, N, endpoint=False)\n",
    "plt.plot(x1, y, 'o')\n",
    "plt.plot(x2, y + 0.5, 'o')\n",
    "plt.ylim([-0.5, 1])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ba9d44b8",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = pd.Series(['Jan 2022', 'Feb 2022', 'Mar 2022'])\n",
    "s1 = s1.astype(\"datetime64[ns]\") + pd.DateOffset(days=9) \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "c96b5b37",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "08decb1a",
   "metadata": {},
   "source": [
    "### В серии (s1) находятся даты с 1 по 8 января 2022 года. Однако некоторые даты и значения к датам пропущены. Сделайте так, чтобы все отсутствующие даты отображались и заполнялись значением из предыдущей даты.\n",
    "<pre>\n",
    "Требуемый финальный результат (наполнение):\n",
    "2022-01-01     1.0\n",
    "2022-01-02     1.0\n",
    "2022-01-03    10.0\n",
    "2022-01-04    10.0\n",
    "2022-01-05    10.0\n",
    "2022-01-06     3.0\n",
    "2022-01-07     3.0\n",
    "2022-01-08     3.0\n",
    "Freq: D, dtype: float64\n",
    "\n",
    "Индексы строк:\n",
    "DatetimeIndex(['2022-01-01', '2022-01-02', '2022-01-03', '2022-01-04',\n",
    "               '2022-01-05', '2022-01-06', '2022-01-07', '2022-01-08'],\n",
    "              dtype='datetime64[ns]', freq='D')\n",
    "\n",
    "Info:\n",
    "<class 'pandas.core.series.Series'>\n",
    "DatetimeIndex: 8 entries, 2022-01-01 to 2022-01-08\n",
    "Freq: D\n",
    "Series name: None\n",
    "Non-Null Count  Dtype  \n",
    "--------------  -----  \n",
    "8 non-null      float64\n",
    "dtypes: float64(1)\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c5e71c65",
   "metadata": {},
   "source": [
    "По условию задания нам нужно расширить (вставить пропущенные) Series с шагом в 1 день, т.к. у нас есть пропуски по датам. После расширения дат мы получим Series со значениями NaN напротив каждой вновь добавленной даты, почле чего нам нужно транслировать для этих новых дат значения от предыдущих дат (которые изначально были известны).\n",
    "\n",
    "Шаг 1. Расширить по датам можно с помощью pandas.Series.asfreq, где нужно задать аргумент freq (значние частоты) равный 1 дню.\n",
    "\n",
    "<code>\n",
    "pandas.Series = pandas.Series.asfreq(freq='D')\n",
    "</code>    \n",
    "результат:\n",
    "<pre>\n",
    "2022-01-01     1.0\n",
    "2022-01-02     NaN\n",
    "2022-01-03    10.0\n",
    "2022-01-04     NaN\n",
    "2022-01-05     NaN\n",
    "2022-01-06     3.0\n",
    "2022-01-07     NaN\n",
    "2022-01-08     NaN\n",
    "Freq: D, dtype: float64\n",
    "</pre>\n",
    "\n",
    "Шаг 2. Заполним NaN значениями с предыдущей строки серии, для чего совместно с методом заполнения pandas.Series.fillna будем использовать аргумент method (метод заполнения), равный ffill (распространение последнего действительного наблюдения вперед к следующему действительному).\n",
    "\n",
    "<code>\n",
    "pandas.Series = pandas.Series.fillna(method=\"ffill\")\n",
    "</code>    \n",
    "\n",
    "результат:\n",
    "<pre>\n",
    "2022-01-01     1.0\n",
    "2022-01-02     1.0\n",
    "2022-01-03    10.0\n",
    "2022-01-04    10.0\n",
    "2022-01-05    10.0\n",
    "2022-01-06     3.0\n",
    "2022-01-07     3.0\n",
    "2022-01-08     3.0\n",
    "Freq: D, dtype: float64\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "85a75c2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "s1 = pd.Series([1,10,3,np.nan], index=pd.to_datetime(['2022-01-01', '2022-01-03', '2022-01-06', '2022-01-08']))\n",
    "#s1 = s1.asfreq(freq='D').fillna(method=\"ffill\")\n",
    "s1 = s1.asfreq('D').ffill()\n",
    "s1"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "81c1ffb9",
   "metadata": {},
   "source": [
    "### Для столбца А найдите индекс строки в которой находится второе наибольшее значение.\n",
    " \n",
    "Пояснение:\n",
    "\n",
    "eсли все значения колонки отсортировать от минимума до максимума, то получится числовой ряд: n1 < n2 < n3 < n4 < n5 < n6 < n7 < n8 < n9 < n10. Найдите индекс строки в которой находится n9."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "655d901a",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame([[16,24,29],[1,10,16],[26,21,10],[3,3,8],[6,17,17],[2,25,14],[9,13,21],[27,24,17],[19,29,1],[20,24,6]], columns=list('abc'))\n",
    "\n",
    "# Сортировка\n",
    "#df['a'].sort_values(ascending=False).index[1]\n",
    "\n",
    "# Без сортировки !\n",
    "df[\"a\"].nlargest(2).index[1]\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "729331c1",
   "metadata": {},
   "source": [
    "### Выведите последние две строки датафрейма, сумма ячеек которых больше 100.\n",
    "\n",
    "<pre>\n",
    "Sample Output:\n",
    "\n",
    "    0   1   2   3\n",
    "5  35  13  36  21\n",
    "6  32  32  25  17\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ccf4f87c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame([[23,33,16,35],\n",
    "                   [24,20,13,10],\n",
    "                   [32,33,30,28],\n",
    "                   [13,32,36,18],\n",
    "                   [25,27,31,10],\n",
    "                   [35,13,36,21],\n",
    "                   [32,32,25,17],\n",
    "                   [34,24,23,19]])\n",
    "\n",
    "df[df.sum(axis=1) > 100][-2:]\n"
   ]
  },
  {
   "attachments": {
    "%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "55bce8ee",
   "metadata": {},
   "source": [
    "### Создайте составной индекс на основе колонок user и user.number для датафрейма\n",
    "\n",
    "![%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png](attachment:%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png)\n",
    "\n",
    "<pre>\n",
    "<b>Sample Output:</b>\n",
    "                  user user.number  user.speed  user.bag_weight\n",
    "Ivan_222-333      Ivan     222-333        40.0              8.0\n",
    "Petr_missing      Petr     missing         NaN              NaN\n",
    "Alex_222-555      Alex     222-555        42.0              2.0\n",
    "Den_222-666        Den     222-666        35.0              4.0\n",
    "Viktor_222-777  Viktor     222-777        60.0             19.0\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3e26322c",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame(data = {'user' : ['Ivan', 'Petr', 'Alex', 'Den', 'Viktor'], 'user.number' : ['222-333', None, '222-555', '222-666', '222-777'], 'user.speed' : [40, None, 42, 35, 60], 'user.bag_weight' : [8, None, 2, 4, 19]})\n",
    "df\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3dde320d",
   "metadata": {},
   "outputs": [],
   "source": [
    "df['user.number'].fillna('missing', inplace=True)\n",
    "df.index = df['user'] + '_' + df['user.number'] \n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d67061f6",
   "metadata": {},
   "source": [
    "### Выведите на экран сводку основной информации о датафрейме. \n",
    "\n",
    "<pre>\n",
    "Для получения ответа не используйте функцию print!\n",
    "\n",
    "Sample Output:\n",
    "\n",
    "<class 'pandas.core.frame.DataFrame'>\n",
    "Index: 10 entries, a to j\n",
    "Data columns (total 4 columns):\n",
    " N   Column    Non-Null Count  Dtype  \n",
    "---  ------    --------------  -----  \n",
    " 0   animal    10 non-null     object \n",
    " 1   age       8 non-null      float64\n",
    " 2   visits    10 non-null     int64  \n",
    " 3   priority  10 non-null     object \n",
    "dtypes: float64(1), int64(1), object(2)\n",
    "memory usage: 400.0+ bytes\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "310fc190",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],\n",
    "        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],\n",
    "        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\n",
    "        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "df = pd.DataFrame(data, index=labels)\n",
    "\n",
    "#### YOUR ANSWER BELOW THIS LINE ######\n",
    "\n",
    "df.info()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "10e20a34",
   "metadata": {},
   "source": [
    "### Выведите на экран данные, которые хранятся в строках [3, 4, 8] и колонках ['animal', 'age'].\n",
    "\n",
    "<pre>\n",
    "Sample Output:\n",
    "\n",
    "  animal  age\n",
    "d    dog  NaN\n",
    "e    dog  5.0\n",
    "i    dog  7.0\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0995e007",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],\n",
    "        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],\n",
    "        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\n",
    "        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "df = pd.DataFrame(data, index=labels)\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "911b6f05",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.iloc[[3, 4, 8], :2]"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "1005e637",
   "metadata": {},
   "source": [
    "### Выберите только те строки, в которых количество посещений (visits) больше 2.\n",
    "\n",
    "<pre>\n",
    "Sample Output:\n",
    "\n",
    "  animal  age  visits priority\n",
    "b    cat  3.0       3      yes\n",
    "d    dog  NaN       3      yes\n",
    "f    cat  2.0       3       no\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "eb03d2b1",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],\n",
    "        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],\n",
    "        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\n",
    "        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "df = pd.DataFrame(data, index=labels)\n",
    "\n",
    "#### YOUR ANSWER BELOW THIS LINE ######\n",
    "\n",
    "#print(df[df['visits'] > 2])\n",
    "\n",
    "print(df.query('visits > 2'))\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "602b4221",
   "metadata": {},
   "source": [
    "### Выберите строки датафрейма  в которых animal = cat, а age < 3.\n",
    "<pre>\n",
    "\n",
    "Sample Output:\n",
    "  animal  age  visits priority\n",
    "a    cat  2.5       1      yes\n",
    "f    cat  2.0       3       no\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "165b0c3e",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],\n",
    "        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],\n",
    "        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\n",
    "        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "df = pd.DataFrame(data, index=labels)\n",
    "\n",
    "df.query(\"animal == 'cat' and age < 3\")\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7121dfb5",
   "metadata": {},
   "source": [
    "### В строке f замените значение в колонке age на 1.5\n",
    "<pre>\n",
    "Sample Output:\n",
    "\n",
    "  animal  age  visits priority\n",
    "a    cat  2.5       1      yes\n",
    "b    cat  3.0       3      yes\n",
    "c  snake  0.5       2       no\n",
    "d    dog  NaN       3      yes\n",
    "e    dog  5.0       2       no\n",
    "f    cat  1.5       3       no\n",
    "g  snake  4.5       1       no\n",
    "h    cat  NaN       1      yes\n",
    "i    dog  7.0       2       no\n",
    "j    dog  3.0       1       no\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "61d8cf30",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],\n",
    "        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],\n",
    "        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\n",
    "        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "df = pd.DataFrame(data, index=labels)\n",
    "\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ca0b1479",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.at['f', 'age'] = 1.5"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0ae40520",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ebc0d329",
   "metadata": {},
   "source": [
    "### Посчитайте средний возраст каждого вида животного (animal)\n",
    "<pre>\n",
    "Sample Output:\n",
    "\n",
    "animal\n",
    "cat      2.5\n",
    "dog      5.0\n",
    "snake    2.5\n",
    "Name: age, dtype: float64\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a09f1636",
   "metadata": {},
   "outputs": [],
   "source": []
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "db00a02b",
   "metadata": {},
   "outputs": [],
   "source": [
    "data = {'animal': ['cat', 'cat', 'snake', 'dog', 'dog', 'cat', 'snake', 'cat', 'dog', 'dog'],\n",
    "        'age': [2.5, 3, 0.5, np.nan, 5, 2, 4.5, np.nan, 7, 3],\n",
    "        'visits': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],\n",
    "        'priority': ['yes', 'yes', 'no', 'yes', 'no', 'no', 'no', 'yes', 'no', 'no']}\n",
    "\n",
    "labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']\n",
    "\n",
    "\n",
    "df = pd.DataFrame(data, index=labels)\n",
    "\n",
    "df.groupby('animal')['age'].mean()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "57d8876d",
   "metadata": {},
   "source": [
    "### Отсортируйте датафрейм по столбцу age в порядке убывания, а затем по столбцу visits в порядке возрастания. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "e1443691",
   "metadata": {},
   "outputs": [],
   "source": [
    "print(df)\n",
    "print()\n",
    "print(df.sort_values(['age','visits'], ascending=[False, True]))"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "8871c5d6",
   "metadata": {},
   "source": [
    "### Столбец priority содержит строковые значения yes и no. Замените их на булевы True и False\n",
    "\n",
    "<pre>\n",
    "Sample Output:\n",
    "\n",
    "  animal  age  visits  priority\n",
    "a    cat  2.5       1      True\n",
    "b    cat  3.0       3      True\n",
    "c  snake  0.5       2     False\n",
    "d    dog  NaN       3      True\n",
    "e    dog  5.0       2     False\n",
    "f    cat  2.0       3     False\n",
    "g  snake  4.5       1     False\n",
    "h    cat  NaN       1      True\n",
    "i    dog  7.0       2     False\n",
    "j    dog  3.0       1     False\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7ec6d1c1",
   "metadata": {},
   "outputs": [],
   "source": [
    "#df.loc[df['priority'] == 'no', 'priority'] = False\n",
    "#df.loc[df['priority'] == 'yes', 'priority'] = True\n",
    "#df['priority'] = np.where((df['priority'] == 'yes'), True, False)\n",
    "\n",
    "df['priority'] = (df['priority'] == 'yes')\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ab1e6d42",
   "metadata": {},
   "source": [
    "### Определите средний возраст для каждого типа животного и количества посещений.\n",
    "\n",
    "<pre>\n",
    "Другими словами, постройте сводную таблицу, где каждая строка — это тип животного, каждый столбец — количество посещений, а значения — средний возраст.\n",
    "\n",
    "Sample Output:\n",
    "\n",
    "visits    1    2    3\n",
    "animal               \n",
    "cat     2.5  NaN  2.5\n",
    "dog     3.0  6.0  NaN\n",
    "snake   4.5  0.5  NaN\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9e4115a8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.pivot_table(values='age', columns = ['visits'], index = ['animal'], aggfunc = np.mean)\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c1224121",
   "metadata": {},
   "source": [
    "### Вычтите среднее значение строки из каждого элемента в строке.\n",
    "\n",
    "<pre>\n",
    "Sample Output:\n",
    "          0         1         2\n",
    "0 -0.469429 -0.032952  0.502381\n",
    "1  0.280649  0.092736 -0.373386\n",
    "2 -0.103336  0.085149  0.018186\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "f0850fb8",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame([[0.020448, 0.456925, 0.992258], [0.743399, 0.555486, 0.089364], [0.094699, 0.283184, 0.216221]])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1601ccd4",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.sub(df.mean(axis=1), axis='rows')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "a2881bb8",
   "metadata": {},
   "source": [
    "### В каком столбце чисел сумма наименьшая? Выведите на экран название этого столбца.\n",
    "\n",
    "Sample Output:\n",
    "a\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "25d7bbcd",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame([[0.020448, 0.456925, 0.992258], [0.743399, 0.555486, 0.089364], [0.094699, 0.283184, 0.216221]], columns=list('abc'))\n",
    "df\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d1f4afd3",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.sum().idxmin()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "3ada2ba9",
   "metadata": {},
   "source": [
    "### Как подсчитать, сколько уникальных строк имеет датафрейм (т. е. игнорировать все повторяющиеся строки)?\n",
    "\n",
    "Sample Output:\n",
    "2\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "39393b65",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame([[0.020448, 0.456925, 0.992258], [0.743399, 0.555486, 0.089364], [0.020448, 0.456925, 0.992258], [0.094699, 0.283184, 0.216221]], columns=list('abc'))\n",
    "df\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b58b4be9",
   "metadata": {},
   "outputs": [],
   "source": [
    "(df.value_counts(ascending = True)==1).sum()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "7a8d15ee",
   "metadata": {},
   "source": [
    "### Имеется датафрейм состоящий из 10 столбцов чисел с плавающей запятой. Ровно 5 записей в каждой строке являются значениями NaN. Для каждой строки датафрейма найдите столбец, содержащий третье значение NaN.\n",
    "<pre>\n",
    "Sample Output:\n",
    "0    e\n",
    "1    c\n",
    "2    d\n",
    "3    h\n",
    "4    d\n",
    "dtype: object\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7c5dcd2f",
   "metadata": {},
   "outputs": [],
   "source": [
    "nan = np.nan\n",
    "\n",
    "data = [[0.04,  nan,  nan, 0.25,  nan, 0.43, 0.71, 0.51,  nan,  nan],\n",
    "        [ nan,  nan,  nan, 0.04, 0.76,  nan,  nan, 0.67, 0.76, 0.16],\n",
    "        [ nan,  nan, 0.5 ,  nan, 0.31, 0.4 ,  nan,  nan, 0.24, 0.01],\n",
    "        [0.49,  nan,  nan, 0.62, 0.73, 0.26, 0.85,  nan,  nan,  nan],\n",
    "        [ nan,  nan, 0.41,  nan, 0.05,  nan, 0.61,  nan, 0.48, 0.68]]\n",
    "\n",
    "columns = list('abcdefghij')\n",
    "\n",
    "df = pd.DataFrame(data, columns=columns)\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "65fbd692",
   "metadata": {},
   "source": [
    "#### Транспонируем фрейм. Проверяем на null. Тут вступает интересная функция cumsum(). Для каждой строки накапливает сумму. Теперь отметим ячейки равные 3. И выберем индекс с макс значение в каждом столбце(т.к там было по одной тройке и по одному true)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "8f59f1a3",
   "metadata": {},
   "outputs": [],
   "source": [
    "(df.T.isna().cumsum() == 3).idxmax()\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "78f53c45",
   "metadata": {},
   "source": [
    "### Датафрейм содержит колонку grps (название некоторой группы) и колонку целочисленных значений vals.  Для каждой группы найдите сумму трех наибольших значений.\n",
    "<pre>\n",
    "Sample Output:\n",
    "grps\n",
    "a    409\n",
    "b    156\n",
    "c    345\n",
    "Name: vals, dtype: int64\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "c2f91ed9",
   "metadata": {},
   "source": [
    "<pre>\n",
    "1) Cортируем df по возрастанию 'grps' и убыванию 'vals' (такая задача у нас недавно была - сортировка сразу по двум значениям)\n",
    "2) Применяем группировку по ('grps').head(3), в которой будут три наибольших числа для а, b, c\n",
    "3) Выводим обычную группировку с суммой по 'vals'\n",
    "</pre>"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "21e0da60",
   "metadata": {},
   "outputs": [],
   "source": [
    "df = pd.DataFrame({'grps': list('aaabbcaabcccbbc'), \n",
    "                   'vals': [12,345,3,1,45,14,4,52,54,23,235,21,57,3,87]})\n",
    "\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "2a4eb361",
   "metadata": {},
   "outputs": [],
   "source": [
    "\n",
    "df.groupby('grps')['vals'].nlargest(3).groupby('grps').sum()\n",
    "\n",
    "# df.sort_values(['grps','vals'], ascending=[True, False], inplace=True)\n",
    "# df.groupby('grps').head(3).groupby('grps').sum().squeeze()"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "154d3abe",
   "metadata": {},
   "source": [
    "### Датафрейм df имеет два целочисленных столбца «A» и «B». Значения в «A» находятся в диапазоне от 1 до 100 (включительно).\n",
    "\n",
    "<pre>\n",
    "Для каждой группы из 10 последовательных целых чисел в столбце А (т. е. (0, 10], (10, 20], ...) вычислите сумму соответствующих значений в столбце B.\n",
    "\n",
    "Sample Input:\n",
    "\n",
    "Sample Output:\n",
    "\n",
    "A\n",
    "(0, 10]      635\n",
    "(10, 20]     360\n",
    "(20, 30]     315\n",
    "(30, 40]     306\n",
    "(40, 50]     750\n",
    "(50, 60]     284\n",
    "(60, 70]     424\n",
    "(70, 80]     526\n",
    "(80, 90]     835\n",
    "(90, 100]    852\n",
    "Name: B, dtype: int64\n",
    "</pre>\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a873b4bc",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df = pd.DataFrame(np.random.RandomState(8765).randint(1, 101, size=(100, 2)), columns = [\"A\", \"B\"])\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "d592ad8a",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df.head(11)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "339d0ca3",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "pd.cut(df['A'], 1, precision=0)"
   ]
  },
  {
   "attachments": {
    "%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png": {
     "image/png": "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AkygCglEsX54bazCnqnhKnkE3q3h1heaVksMWE+seXHlBjIBJlA9BGrWWFM9iCdOTUzxAlLdpZ84TeeaMgEmwASYABNgAkyACTgIsJ7I4sEEmAATqCwBNtZUljeXxgSYABNgAkyACTABJsAEmAATYAJMgAkwAScBNtawgDABJsAEmAATYAJMgAkwASbABJgAE2ACTKCKCLCxpoo6g6vCBJgAE2ACTIAJMAEmwASYABNgAkyACTABNtawDDABJsAEmAATYAJMgAkwASbABJgAE2ACTKCKCLCxpoo6g6vCBJgAE2ACTIAJMAEmwASYABNgAkyACTABNtawDDABJsAEmAATYAJMgAkwASbABJgAE2ACTKCKCCQaaz64fAr27RuC3zsq/acLVkDL/I9l3qzp06dnnidnyASYABNgAvkTGB0Zgd6eVdC566WosGkNDbB50054+KufcRY+MnIYDvU8Do/unwLff+UUfMf9eZTXmcPLob15HxRKArir/Qj09S2EGTk18/2z3bBgTmdU3jcHr8ATTYaCrhyEFfUtsNfw09SPtsPgW31wX07142yZQMUJXDkLXQ1z4NedlvFQ8QqNFRiN188ehbZX/eaTcawqF80EmAATYAI2ArFeNc2md9UouURjzZUrF+DYEy/CJ5Ytg3nXlVM4ufdv4J9m5GesUZXipD6o/1CDt3KflBf/zgSYABOoFQKne26FWztOR825e+tr8Ny6maD+m/rvWbRZztsfVowm0qAyLS5fL+dg722wbeBWWLRoETSvfw8erd8GC84lb67eFYaaz22bB7tPrisaZw603g4/nPIovCAMNnn8dc2vgx/fcgS+fqbJvjmNlAq/NpDr6DAI6XlajUrkwjnhZCQwKoypbW29sGd4uKz5d7Vtgb7+9bkZSUm8YyMSjtfXc5oPSPXiRBOawIHWOli6a6wJcn7F9WiqODiQf9PFGshyN6G7mitfZQRQd23snQeviAOvvA7kqqzJkGiscVU48rrZ/0u42WLISdtY1bMGO+f+813GSQ8nzSfnFjYg/McEmAATYALlBKQB5VcLtsJJadhQDArfHi14i/wiA6M3zslrp5QrqajIXtM+NdmrxNPQgW26o/EidL9d7qWCBpU8TvmlooCeMUOuMjzbkImsWspyrZuZlMuZTC4CsXHwuJhDXuhbB7NmVX/zcc75yLJLfJBX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"
    }
   },
   "cell_type": "markdown",
   "id": "79a789a5",
   "metadata": {},
   "source": [
    "### В базе данных sqlite3 создана таблица stations, которая содержит информацию о местоположении станций велопроката, количестве мест на станции и слотов для парковки велосипедов. \n",
    "\n",
    "<pre>\n",
    "Выполните действия:\n",
    "\n",
    "1) Выгрузите имя станции (столбец Name),  количество мест на станции (столбец StationCapacity), адресный ориентир (столбец Location). \n",
    "\n",
    "2) Выполните сортировку датафрейма по правилам:\n",
    "\n",
    "    сначала идут станции с наибольшим количеством мест\n",
    "    если у нескольких станций одинаковое количество мест, то отсортируйте их в алфавитном порядке\n",
    "\n",
    "3) Сохраните датафрейм в формате csv: без индекса, разделитель точка с запятой, кодировка utf8\n",
    "\n",
    "Первые несколько записей результирующего файла:\n",
    "</pre>\n",
    "![%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png](attachment:%D0%B8%D0%B7%D0%BE%D0%B1%D1%80%D0%B0%D0%B6%D0%B5%D0%BD%D0%B8%D0%B5.png)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "942521c5",
   "metadata": {
    "scrolled": false
   },
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import sqlalchemy as sql\n",
    "\n",
    "c = sql.create_engine('sqlite:///local_db.db')\n",
    "sql = 'SELECT Name,StationCapacity,Location FROM stations ORDER BY Name'\n",
    "\n",
    "df = pd.read_sql(sql, c)\n",
    "df = df.astype({'StationCapacity': 'int32'})\n",
    "df.sort_values(by=['StationCapacity', 'Name'], ascending=[False, True], inplace=True)\n",
    "df.to_csv('local_db.csv', sep=';', index=False)\n",
    "\n",
    "df.head(10)"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "15098b72",
   "metadata": {},
   "source": [
    "### Ваш старый друг Андрей купил электрокар Tesla Model X, а теперь подумывает о покупке квартиры в другом районе Москвы. Андрей устал, что в его районе почти всегда заняты зарядные станции и подзарядка машины превратилась в проблему, поэтому ему важно, чтобы на районе было много зарядных станций. \n",
    "\n",
    "Порекомендуйте Андрею ТОП-3 района по количеству зарядных станций. Андрей уже подготовил для вас выгрузку в Excel - данные на двух листах. "
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a214be58",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_0 = pd.read_excel(\"Зарядные_станции_для_электромобилей.xlsx\", sheet_name=\"0\", header=0, skiprows=[1])\n",
    "df_1 = pd.read_excel(\"Зарядные_станции_для_электромобилей.xlsx\", sheet_name=\"1\", header=9, skiprows=[10])\n",
    "\n",
    "df = pd.concat([df_0,df_1], ignore_index=True)\n",
    "df['District'].value_counts().head(3)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "d09c0898",
   "metadata": {},
   "source": [
    "## 5.1 Учимся обрабатывать пропуски"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "ce02032b",
   "metadata": {},
   "outputs": [],
   "source": [
    "f = pd.read_csv('image.csv', index_col=[0])\n",
    "df = pd.DataFrame(f)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "0f78f728",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "f1276497",
   "metadata": {},
   "source": [
    "### 5.1.1 При помощи функции dropna удалите колонки в которых полностью отсутствуют значения (везде NaN)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a4f23058",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df.dropna(axis=1, how='all')"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "ae9ef49a",
   "metadata": {},
   "source": [
    "### 5.1.3 При помощи функции dropna удалите строчки, где в ячейках А, С, D, G меньше трех значений (т.е. строки с двумя и более пропущенными значениями в ячейках А, С, D, G должны быть удалены; c одним пропуском - ок)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "44f9098b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df.dropna(subset=['A','C','D','G'],thresh=3)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "399ba215",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df=df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9cd722d0",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df"
   ]
  },
  {
   "cell_type": "markdown",
   "id": "41082668",
   "metadata": {},
   "source": [
    "### 5.1.5 Не пользуясь функцией dropna, отфильтруйте датафрейм так чтобы остались строчки, где в ячейках C и G нет пропусков."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5ce54c66",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df[_df[['C', 'G']].notnull().all(1)]\n"
   ]
  },
  {
   "attachments": {
    "image-2.png": {
     "image/png": "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"
    },
    "image-3.png": {
     "image/png": "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"
    },
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "a32ed5d8",
   "metadata": {},
   "source": [
    "### 5.2.2 На вход функции подается датафрейм, который содержит информацию о предпочитаемом классе в самолете для некоторых клиентов:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "#### В функцию также передается словарь, в котором лежит расшифровка каждого класса:\n",
    "\n",
    "![image-2.png](attachment:image-2.png)\n",
    "\n",
    "#### Примените функцию map для создания дополнительного столбца class-info, который расшифровывает букву класса:\n",
    "\n",
    "![image-3.png](attachment:image-3.png)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "7e9dc697",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_class = pd.DataFrame(['Sergey','Viktor','Pavel','Andrey','Petr'], columns=['client'])\n",
    "df_class['class'] =['A','B','A','C','D']\n",
    "\n",
    "data = {'a':'buisness',\n",
    "        'b':'comfort',\n",
    "        'c':'econom',\n",
    "        'd':'promo'}"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "b7bb6b81",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_class\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "3f567cea",
   "metadata": {},
   "outputs": [],
   "source": [
    "data\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "a9f2d58b",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_class['class-info'] = df_class['class'].str.lower().map(data)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5c416689",
   "metadata": {},
   "outputs": [],
   "source": [
    "df_class"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "iVBORw0KGgoAAAANSUhEUgAAAZgAAAE+CAYAAACwfgamAAAgAElEQVR4nO29QWsbSfe+fevlWY0+gB3sIbYZsgkBk4UdeXgwETzLQZ42FoxMCCLLEExCMAFbMbIUMCYkhCHLIEKQAjLWRMwyoGCGsWIvjGHIJgRLITaWP0DPtt9Fd0vVrarulrpKdn7/c4FhrC5Xna77VJ2qU6VJxDAMAwRBEAQhmf/vvA0gCIIg/m9CAYYgCIJQAgUYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglACBRiCIAhCCRRgCIIgCCVQgCEIgiCUQAGGIAiCUAIFGIIgCEIJFGAIgiAIJVCAIQiCIJTwnQaYFkrJCCKRCCLJElrnbY5F6+28aVPXzxPUz9u4Nkzf2T+5C2DdcQnzvL5TaJtYrwiefFTWbHBEfRKZR+n4vI0D6rkB2WX3g8sXzPYvRl90U8eTCzE/8exg5gDFY//7DDDHNWxvWf+9tY3aBXOwfN2AYVg/34rQsIqZc3c0wHS2S1hEEaesfY9nLsBAsFjfdfbdAGxz6GX9rNxQ2GCvsH1iGDCMbaRGz9Mgc9KaeZzHLmPX7noFiz9ekOBMCKnnLmFxC6ZfZWJK2/ouA0zrr21UAOTX8wAq2P7rQkyNfEbjmF8AsNVA45xNqedmsIo8dsspDNsfjqawbRgw2M8uCqMpvCxpwNYiXtGkdWEw/UhD8dsK2OkplrmAwZlw0Ho7j5nHABaKOFUcXIDvMsC0UPujAiCPeCaOPIDKH7WLsfrmYe+21uNQL6cXddQeA1gYx/i52tEbw/+dhwbgoHFhFf5/DNuP5hE/110U0SuNt/O4lKqYwWVAC8rvL8A4JuwY4uu4cGmy1RiTl/5xERXksTuA1YInxw0cAMC18Yu3UwlA5Yu6/Z9Drwt3ZnbBOE8/ejzj0Gnm8aAN+I7ZWsRMqmL99+Dmy+8uwLTTY/8zJ+zY/y5emsyZ099FHquYubCHkUT3GczKOe82Xbgm1gtxKYOh67KEKvtcZ1G762qa+b9LHrt1c75cfDCYM9fvLMAw6TE7zzs6Dg0XOU0Ww52SBqCCxnkGmNFxXAeAfxoXtJ+80X76nhJ7knEf8p/nbpjjR8O/bTMXWggHFyZjkMeusYLYjTsoLmBg55rfV4Bp3x5bxYwjBYULlya7eNjpxPO/bNAL9o71+vjFGKaEtWCi8eZEcJX6wtA+ex1G6kEeALAaU58K/q4CjD3ZaKVTx4ru1NohXKQ0WQfOruuciGWsdB177dceGBflmrKDOl5Zh5J36GbShWH4t4fIo4LFH9kJqo4n9mLv/0XcO7uPNayik8q/UNi7GKzi6VvFo974bjg1igswAM0ofnM9+lY0NMDAQtE4PRfbTE5LmgGA88Ox+dyw+5H5Wd89b6M6Grp/FNom1guGVjpPT7Kw++Qi6MNhd31Aegn6wWz/Ao0tlw9fCB8ydo08b25s25o3VHpXxDAMQ20IIwiCIP5f5LtKkREEQRDfDxRgCIIgCCVQgCEIgiCUQAGGIAiCUAIFGIIgCEIJFGAIgiAIJVCAIQiCIJRAAYYgCIJQQgTmt04JgiAIwkHY7+H/R9d1SaYQBEEQRAdKkREEQRBKoABDEARBKIECDEEQBKEECjAEQRCEEijAEARBEEqgAEMQBEEogQIMQRAEoQQKMARBEIQSPAPMWTmFaDRq/mzsDcSgvY1ou83NfXllfTkpIxWNIlU+c7eCzWgK5RP/Ksz+4pTd30T0VhnumnvBfNdNuFU4K6cCayOjjr7Z3+z4km9/7mGzXbbbXpXsbQzC189QvhVl+sO7TXYcdvunevu82xygVg4fCtZ3MnDMgz7jWLZW4cespU9XWVPj0POmD+IAs7+JiXQVax906J8LSOTi6p17fxPx3Bpqug79wxqyNz0ctpeyPVBNvw5ZTxXpN6ocPosXoTWQUUePnJSRunmIwmcduq7jqACkr4j12tuII5upQdd11DJZxAe0uDF9ahANNdGsJNr9oes69EfT/KInZdxPwyz7uQCk7wda7IRhb2MCaRRwpOvQ9Rom0xPCiWigWk0td/pLt+YlJFC4Jeg7GexvYiI9ac4z+hEKSGNC9I7KtJIwZnMvlPsND2GA2atlAaxhdgrAyCzmNKD6506oVbgfe7UskJnFNABM3UZBy2JH5Ng9lA1OAgkt5CDREkjk4mpWBloivNPKqKNXRpIo6SUkR8xfh36eQwKH+Mq1YQ87OWAtbk4a07cKSOR2BrCLOUP590MkNOUNASdfcYhJXB7xL3r29ztUtTnMjgAYSWIpU8W7v5WOQuzkEihsJDEEAJjGsq5jeUpU9jy0AoAzlB+lgcLztl8paaV5CGhjGAMADGH2lwTw6St3HlSmlYQxm9CA9KNwWZR+EASYM3z9BEfHXr4KoNJEU5kpZpuJiTHHp4dNrpQ9lO2NuXsFnwDhTm+4V+JzWCokpO2oHFxdwlKm6u0orjRC164zSB2KcQxENydfcYgExhzPRMFIok3l+3j3y3MsXVXbDgDgpIlqe2x50zyqAlcvW5O9SfVI3SjE/g6yAYPfeWkFANh/jXRlDUvJIf+yIRgam2TmvTPs/FlF4pdZ8FpVppWEcT95bwlrlTTuDzh7IQgwTTQrvM/VO8/kmC2PFdQklQ3MSBLPCwlkf+eLeVa+j/TVmrVNP0JB696+jiWfcz+XwfSjGtYqabzmBsA9bDKpKP3DGjfl512HQqxzrol0FWv3ktxBasJMcCOXMancsD28Tk8qn6xszpqHQCWNiYBnF+xCamwiod5AbQwIfJYwaK0Ac7eZRaJwGwqTYyZTy9A/j+FFNIpodALNezpKHn6iSqvw434ay4L5QCV0i4zDUPI5CuBH+6FkicmXiwLxEJIbqvLlpqPwd0jTWGZSUWfNwz7qUMhIEiUrd354U/0BY1D2NuLAh2X1k5VF86gKaPYZh3V2EfISiFQqabzA8/Y5BzzOYM6Fkx28qyQw97P6BcFZOYXolSaWLK1ma4O78OREwrifWh7smSaEAWYMY9xcdMCtcwg6aS4rTSepbG8MIXlvDVVegHBsRV/gUJSzt3KwSlJR1plTt6M403f3/+ynjgEwksRSBsjWRG0zO+WTrxCFSSmclPHiUwG3uWcMaph+pEN/09nBTd8qIFF5hx3BYoRNszSPquoNBJN6ukha2Zw0xSlWqVgpMWanZJ4ziQ/MlWolYdyb9is6I+YgCDDuMxf3mYwK+GmuThqs37J9MrWMWqaK9Jsd5kN7a35kpcieY86jiva2tibPLBNzh5TIvcDrI+ZjKy9ds1ZbpXteCQtBHQOBf4YGQJBmUbewOfv7HapMuiqeA5CLh75W3jv8d+SlWbj9JouRMfASOxdBK5u9WrbrrOMioF4rCeO+fQTwWuF5egdhimw6vgbAupl1soN3FQgPt2QxHWdyhFanzQpWlr2U7dueRzWs5bLIuj5vr1L2XyPNTZG1azC3tTl3DRIYSeJ5Acjm3Kske0VpBsP+6pDMSRkp9rsv+6+RFqY4pjGb6Vz13nuTRtW+LaiAoWTJcfW1lgGQqTl2GHIxV5udcw3zNpToHYd+nuusmE/KeJFTnBoamcUce37o2eZgtTIxFyf2zTW1mLfG2HOLvTdp4e5pIFpJGPfmEUAWWc+5Sw7iM5ipZRwVEsjejCJ6JY1qpuZ5uCUFO0cYjSJ6M4s1Ni/u/rKiV1lpTON2gV2VmKkz5OLmdrQ2i1rG56bI1G0UFF19HUouYa2rrSrSV6KIRu8D9woe14EFdahgJInSh0nLLlsvJmfs+tKYGdjj1o5iDTXRd0S+S4aQfHOEuT8nrJSG9Z2T9ju6vthrTSjpK+Y4VH0tt8u+K2lMMlq5x+HgtRKde6phKFnqzDPRKOKfCjhqLz5cX1YckFbhx701jw2AiK7r4f7RZYIgCOL/JD/88EOov6dbZARBEIQSKMAQBEEQSqAAQxAEQSiBAgxBEAShBAowBEEQhBIowBAEQRBKoABDEARBKIECDEEQBKEECjAEQRCEEiKGYdA3+QmCIAjp0A6GIAiCUAIFGIIgCEIJFGAIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglBAgwdTyJRBDJ1UM2JaqnhVIygicfB1VHcOq5CObftroffHyCSLIEzpMOxyXMRyKIRCL+ZQPaEok8Qdebv50PrI2MOgLB65+PT8y+iEQQicyjdOxpqalzhG9vGISaMs+l9gXXN83POv3h3Wbr7Xy7nJftfcH1Zad93m2q06rLNocPBeu73uDPI2z/+41l2VqFH7ODnTPdeAeYj08QicxgVWaLj5/6TC4DqsOHei6CmcecBx+fIBLz65EWSg8WgdIpDOMURSzirpSJYRVPQ9cjow4PeP1zXMJ87ADFbwYMw8BpCVj8UTwZ1XMzWF3fhWEY2F1fxYykCUSoKWO75/OeaaGUvITFLffnDTS2tHZ/GIYBIxPjV3Fcwt0UzLLfikDqrjzfF/hyPXcJiyji1DBgGLu4nroknIhUacW17cZKp78Msz80aCimBX3XEwKtPj7BpdR17BpGeyxfEr2jMq0kjNkBzJk8hAGm9XbeFHhBgyaxQW0BWHwQbkUvow4xZsSf+SeP/ILrSS6CSOwA+XWfHjmuYXtLw/x/hwEMI/Ugj8oftfD2LmjhnVZGHQKE/TOawraxjdSo+evwf+eh4QANrg111B4D+f+Zk0YsXYT2uBZyZSzWtEMLpWcH0ITPe+S4hPnIJSxeyyPf9ayBA1zH+Kh/Na2/tlFZmEd8FMBoCg/XK9j+S9LKmOvLddQeayg+S2EYABDDimFg5Qa3FgVaBR1n9iLuZduv+sZDq1bjAFgYxzgAYBjxXzXgnwZ3LKvSSsaYVTtnivHcwWilUxjP5qU2eP3BQ+S3fFb0rq2we6sZqI4QxOsGjPIdy6kY/rcLw9jGnZ98KjhuoOKeQLYaaIQ17NpDPFyveDuKT98FqqNfAvaPYyC6OW7gAJpr8hUFo+AINbVtensX27++xMNr4drpMI6H3wwYmXj3o+MGKu1Jy5vGlwpwbdya7E0qX0J7klirjzWsBgx+qrQK5EcfX2FxK4+Hvw17FAqKWKvh8evM2G2h9kcF2q9x8FpVppWEca96zhQhDDDDv21jW4p4bmJYqedRSb0SrHTqeMKkUwxuWb86wtkX467WgNiNHrbi7AQyOi5tFxjL7CK/tYhX3JRFkL7zqyOEbX79Y51LXUpVkH+Q4g5SE2aCGx3H9fCWCTU1qeNV6rqkycpiNIaYYJJuNQ6ArUVcCnh2of3UCUXjP8nxJE+tFsaBwGcJsrUKMs5aKD1bhVa6AxnJMS+tcGMFxrdxPI1EEIlcQuOB4TkvqtAKkDHuVc6ZYs7nFtmNFY98bQwrTDql1Tjoo47/y5iOshrjTUoB+86zDoWMprBt5c4PYuoPGINSz80A9RU5k1UAGl8qwIJ9xmGdXUi4CCKNrUU8xcv2OQc8zmDOBUcKWi2tt/OI/NjAQ0ur+HvZl0CCImHcn8OceW7XlM187QzHcZ03WO7+0U8dFwA2JXbcQEVm3TfuoLjAc5TgfSeuYwCMpvBwHVh9L2qbSbMcNyAKk1I4LuHpP0Xc8dzhyCWWMWCUOzu4WLoIbWsbNUFqiU2zNL5I9SQBTOrpImllc9wQp1ilYqXEmJ2SOeeID8yVaiVh3A96zjy/78GMpvCypGH12Svn2YSVW921VgzbDzw23aI6zhteSixgzj0Yw0g9Mx391Rfm4176TlTHQGih8Y8zndCGm2YJeCbQjyV/baPCpKtmHgN4PCPlanlv8N+Rl2bh9pssBOnci6CVTf39atdZx0VAvVYSxv2A58xz/aLl8G8vUcQqVruucdqrIjPX2l8d58hoHPML9tVCK18sOBjsv40UXpaA1cfuVVLwvhPXIZnjEubZ7758fIVFYYojhvh6BYsFc5VWLyyish5Xlr4a/m3bcfV1dx3A+q5jhyEXc7XZOdcwb0OJ3nH4v/OdFfNxCU8fK04NOXzXr83BamViLk7sm2tqMW+NsecW9cKicPc0EK0kjPtBzpnn/E1+8wqvgxt3UFyoYPHHCCKRu8CDoseVVkEdA8f9pSVzpYHUJUQi5ncKXiq4MDH820Pntcqe+45ThwpGU9iuX7fsiiASW0W+zuSMXV8ai2V2kX88Y+0o8tgVfUfku2QYqfIp5v+4ZKU0rO+ctN+xjidsMLYmlMUfI4j8KOlabi/2/biI64xW7i8/Dl6rBhoDXEwO/7ZtnlvYO9x/ijhtLz5c435AWoUf94ObM+lftCQIgiCUQP8vMoIgCEIJFGAIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglACBRiCIAhCCf/5999/z9sGgiAI4gLyww8/hPp72sEQBEEQSqAAQxAEQSiBAgxBEAShBAowBEEQhBIowBAEQRBKoABDEARBKIECDEEQBKEEcYA5KSMVjSJq/9wq4yxUU3vYjEYR3dhzfX6G8q0oNvcHVYcA631TZfdb7mEzmkL5xL+Ks3IKUV7Z/U0J/WfX39HE+b5W3wTUi62r+537Y2+Dad/dD/ub4mfdNTHvsgm32n1YFrhv9jZ4/tUH7vHjqNP016jwuZOBa+Wyz7tN2Vp52ObwoWB9FwhPrVzjbsDjyuyL7n49K6cCvrfCOTMAggBzhvKjNKpYQ03XoetHKCCNCQmTJHIvAk3WyusQUE2/DjlIqki/kTHMXOxvYiI9aemhQ/+whuxNe/CdoXwrjsPCkfnM1kvkgCdl3E8Dhc869M8FIH0/dH+elVOIfyrgyLLvqACkr1gD46SM1M1Dsz33Mw57G3FkMzXouo5aJot4qAmkh77Z30Q8F6KpNnvYvJLG5AdLK72GtVycmXCaaFYS7f7QdR36o2l+VYPWCsDexgTSsJ/XMJmeEE5EcrXysW1qudNfutkfCSRQuCXou0D4aOUYd4MfVyZZvAgbrBTOmV4IAswQkm906Poypq3fL18FUHmHnZBGJjQg/ShcoJJRh6BmJLSQg0RLIJGLy18ZTC0zegCYmsUaqmieALZepeSQ9XAIs78kgE9fuX109vc7VLU5zI4AGEliKVPFu7/D9eZQsgT9TRJtC36eQwKH+HpitlHSS0iOcJ51sYedHLAWN990+lYBidxOiKAftG/OUP79EAmt74YYprGs61ie6vw+mwGqR03z15OvOMQkLo/41zRwrbCHnVwChQ37uftdWGRr5Wcbi7kIRuF526/6w1urs+YhoI1hzLRm4OMKAKAlQgcrdXOmNwHPYExHksHkvSWsVdK47xWRXVth91YzUB19Mnev4BMg3OkN90p8DkuFBLI35aQLVNA8qgJXL7cHMcBMfgPAMRDdnHzFIRIYczwTBSOJNpXv490vz7F0VW07AICTJqrtScubgWu1v4NswOB3XloBAPZfI11Zw1JyyL9sCIbGJoFKE1a4wc6fVSR+mQWvVWVaXV3CUqbqHSDOcc70IlCA2duIIwsAokmhJ6ax/GHNIxW1h00mnaJzy/rVEYKRJJ4XEsj+zhfzrHwf6au1TrpF696+jiWfcz+XyVn5BbJYw6xgZfk6LR4IAJCY6ExvYxMJ6fbtvUl3BxEr1z2RrmLtXlJoG9gJbuQyJuVaxumbPbxOT6qbrE7KeMGs9M+ah0AljYmAZxcD10obAwKfJajUSuBHOEP59ywShdsIkxzj4tIKU8vQP4/hRTSKaHQCzXvsbrgbVVpNP6phrZLGa+7C95znTA98A8zeRrSdl/aeFHpgatkjXzuNZSadctY87KOOcAwln6MAfrQfSpaYfHkTzQq3BiQ3ZOZgXexvmpP0h2XOADPPHLJaAc8Vr+5EnJVTiDvSLBYjSZSs3PnhTfUHjBzLuH2ztxEHuH0pAzPHX83U2mmY5lEV0DrnDLVMFnEZ55t9wNWqksYLPG+fc8DjDGbgtgHAyQ7eVRKY+1m2f3drdVZOIXqliSVLq9mapEsgPWMGCH5m5PznTBGeAcYU2PqF6XQZmPlaXirKmYK6/2c/dYRlCMl7a6jyAoRjK/oCh6KcvZWDlZ733N9E9GYWax94efEzlG9ZB7RvvBcD7Na9eVSVZt5ZOYWJNFD4XBLnxkeSWMoA2ZrI0Zk0y8lXCIZLr5bx++akjBefCrgt0bc77GEzah2CM4f40490xznD9K0CEh7nm4PXikk9nYtWPn500hSnWPuGp5WVEmN2SuacIz4wV6UVAGDqNgrcM+KLMGfyEQcYa5UMAHANECm0U1Gv4chSWrlV+7ZU6Z7HpltUhwymllHLVJF+s8N8aG/N7RtJzzHnUUV7W1uTZNP+JqLWVlgYXK7WHJMXD97Wnd3a94s5KUyipnsEF7Mkvn4StMlNswQ8E/BoT9Q3Z3+/Q5VJV8VzAHJxSdfyrdtrgcYO/x0HrtXIGHiJncFp5e9He7Vs11lHOHrVio8qrTqYmZFE7gVeHzEfX5Q5k4P4mvLvWfM/tQKOZAcXCzMVlUW2K81kr4oYO3quIzzTj2pYy2XhtqC9Stl/jbRnu9a2Nuf9DoE4KSN1M4u1D4JBZ18tDaDV0M9znVXYSRkvchLSDfub1oqTk2o6KSPl+D7Da6SFKY5pzGY6V7333qRRzcyGSl959c1QsuS4+lrLwFxQ+QRpb6xUXKbGydebq83OuYb1lQDBOw5cq5FZzLHnh55tytfK0zYA9uKkfUYSGi+tzFtj7LkF/0zIKq1CKzcjSTwvANmce3d0MeZMN/wAc7KDd3bjjsPIYF84DI6ZinIwdRsFrYr0lSii0fvAvYLHlVZBHdKYxu0Cuyqx2srFzf6ozaKW8bkpMnUbBQlXX8/+focqgOzNKOe2iHXLz6EVe3js+rKo5aTpK1FEr8i46mmtKmHr5voy6EgSpQ+TnWeuQOn+0pgZ2OPWjmINtVALHL++UYA9fmw/cXxJbwjJN0eY+3PC+twd/M5ZK7d9V9KYZBc1ri8Ny9XKzzZAfO7ZJ55amQuQWiaLuL3D/cSmWF1fVlSgFY+h5BIcM96FmjOdRHRdNwbSEkEQBPFdQf+iJUEQBHEhoQBDEARBKIECDEEQBKEECjAEQRCEEijAEARBEEqgAEMQBEEogQIMQRAEoQQKMARBEIQSKMAQBEEQSogYhkHf5CcIgiCkQzsYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglACBRiCIAhCCRRgCIIgCCVQgCEIgiCUQAGGIAiCUIJHgKnjSSSCiP2Tq0tpsPV2vlNn5AnctdZznTaffPSuq5eyAa1DKRngnT8+QSRZQsurquMS5u16/MoG5eMTpu/mUTpmH7r08mmT1WH+rRTrvLX1tN0N+y7dPtKHZcF0heVTIX3d7AfOOwbxG9YOzru33s5LGYve49DZX97+IVsrD9scPiRzbnKOHff7OuwZ8LgK7wfWu3WVNTWWM296YAjYXYcBaEbxm2EY9bwBwNBKp6LiwajnDSBv7LJtLBSNU95zV1nPuvzKBmR3HQbW29YZed47W33hsLuLU6O4YP8t+98h+FY0NFsPwzBOSxrzzu42zN877+JRl6vevvHS1tP2blgdnJr0RyBd2+8Qvj3z/Tj11PM+fuOymWPnaUkLbZ/fOHT+bvZXvu5hp0StfOcIFim+6xo734qGxr6vw57Bj6vwfmDqhy5bzHcR6SoLYYBxYHV6aOdxw3OmdhveHdBL2X5xDxg76ObXNe+Jwu1cPUwsgfFx4NOS2Eb3s911CQHQjVfQ97TdNaF9KxqahMWDowXuRHhqFBc0Q/OaQAJi9q/mnKgMo/cAs6B19ZOUAOPGodWukQ88MarXSuxHkhZuPvW6x8qgx1V4P7AWVAtuuwcTYIKdwRw3UAGQ/19M6u6p/n4VWI/DrLWFxj+A9tO4o8xBg7fN7KVs39ah9tj1zv/bhWFs485PPn963EAF1zE+yny21UBDonWtv7ZRWZhHfNS/rJvGlwpwbRzDzGeVLzKtc2vrxNP24wYOoDn7DgdoeKbUerKsW1cArbd3sf3rSzy8JqudeTwsaViNeaSN2DQqL41x7SEerlew+EBSilWAQ6uPNay6fVeEcq08/OjjKyxu5fHwt2Hen/XPcQ3bWxrm/2vWOzx+nRm7LdT+qED7NQ5eq8rGVRA/cKUP3em56w8eIr+1iLuS0uFB8Q0wrbfziMRWka8bWLkhqVWrM2Yeayimna5zfdyWZxjjPoO9l7K9YOY9Z7C6UMQd5p1jN3oIsAvjaIe/0XFosoyzJqVLqQryD1JcRwfqeJUSDwTAGZzHf5Jmnae2wWwHwE5wo+O4Lsk0ka5mf12XPlmN//YSxYVVPOUO6hZKDxZxvW7AMAwY34rQHj/tOreJZXaR31rEKxW5cpFWC+NA4LMENVp5+hFaKD1bhVa6w13A9Id17vTjIirrD5Gy3+nGCoxv43gaiSASuYTGAwPbHn6ialx5+0EdT2IHKH6zfKmeRyX1yrWwiWGF+7lafAPM8G/bMIxdICbxsPrGitUR17H4o9+B7+CJZUyhdq8t4pKsd5bFaArb1oR0EOMd0rVQSpqT6EvZq7sgeGnra7taRLrWczNAfUXiZGUzjNSzIpC6y/HxYaTKzKLNyhJwrMZKPe+9E+oXkVZbi3iKl+3Ah9SlgWvl6UeuXYYcTD0M4xTFf2bau8nW23lEfmzgoXmcgPh7eReeesPLD2JYMbbbQbHVOOBXcWMFu+urmBmg/QGvKccQXwewtY2azGBw4w6KCxVs/9WZwjtpLjMN5kUvZfshli5C6/ed2ZSYcPIIwWgKD9eB1fess7RQSl7CIoo4LXvtEJxb98YX6dZxtW3DtZ2FSbMcNyAYLn3j0PW4hKf/uHc0EhlNCdMb7C3IyLMD8S73xh0UFxRODF1aMamnc9aK60fHjb7Tw/4MI/UgDzyuoW6nxJidUizN32naKB1XQj9w3vq7+zomloIAACAASURBVIe4CtP+mYEtGHr8HkzA3GxgGmhs2akufpqrkwZj6aVsCHhnKUHgpcTYlJkU3OdQVnC5tgvDJ7jwtu7u86zwsNq64Z+hARCkWST7HaNr669tVLYWcckanDOPATyekbdbB5PeeM/aUMLTx1onrfFs3qMGcyekPX6KV18kGeWA0UqQzj03rTh+VH+/2nXWIZNW46Cv8ap+XAn8wDqP2rV2WdsPPBKVoym8LGlYffZK6pmwEP7Zv3Udz769IesWmetGSNd11Qt1TVl8JdHrJgn7tyqvKZvv3Pnd8zqnV12Krik7tPWx3Y3aa8reV01ltMf1D/f1dtd1WMfXAgR2CK8/94rnOORd2x2cVr5zhPTbT+7x6bzG7m4/8LVpmdeU/fzAMZ5cczf3mrld5lyvKdv3pyHHqS3ancO9m92599318pwrnsKy/VvX7njHZMB7B78rf3ZQ9v3OTA/Yk1TXO7u0av+Ir56yOsi66umprdB23pVL9n1kXHsNpqthKAwwtg3u75u0+8M5EfDtsPpFwlj0HofO/vIeh7K18rPN+3s5/eE917E6+Y172eMqmB+wemlGsc4GN0F/WeNRdYChfzKZIAiCUAL9v8gIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglACBRiCIAhCCf/5999/z9sGgiAI4gLyww8/hPp72sEQBEEQSqAAQxAEQSiBAgxBEAShBAowBEEQhBIowBAEQRBKoABDEARBKIECDEEQBKEECjAEQRCEEgIFmL2NKKLRKDb3ZTZ9hvKtKFLlM25bQdrrpWzPnJSRiqZQPuE8299E9FYZZ5xHzr+37PMrGwDzXTex5/r8rJxCdMP9qbo6gsHRdn+zrVVU1K8dS7HZLtttbyi8dIXVR1L7Ata7s+9h9k+nP7zbPCun2uXc4yU8vHHotM+7TYVauW1z+FCwvuuZLq2c/e83lmVrFX7MWvp0lTX7Vvq86cI/wJyU8SInv+Gz8n2kK64P9zcRz62hpuvQP6whe9PDYXsp27t1KD9KoypoN3ozG+jvUTiCrh+hgDTuS5kYsngRuh4ZdXjTpe1JGambhyh81qHrOo4KQPqKWK+9jTiymRp0XUctk0Vc2gTioStg+ZSkptrsYbPLX5poVhLt/tB1Hfqjaf6fn5RxPw2z7OcCkL7vE5x7gzcO9zYmkEYBR7oOXa9hMj0hnIjUacWxbWq501+62R8JJFC4Jei7nuFotb+JifSkOc9YY3lC9I7KtJIwZnMvpPpNUHwDzN4bjwHZN3t4nQYSmuvTWhbIzGIaAKZuo6BlsSNy7B7K9sz+a6SRQMLd5kYU0ZuHWMu4n7g42cG7SgJzPw8BGELy3hqqf+6E3sVAS4R3Whl1eMLRdiSJkl5CcsT8dejnOSRwiK9cG/awkwPW4uakMX2rgERuR87iQaCryRnKvx92+WRYzsovcKi5Wjz5ikNM4vJIgL//+x2q2hxmRwCMJLGUqeLd37IWCLxxuIedXAKFjSSGAADTWNZ1LE/x/16ZVoI5ooO9iHve9quw8LQ6ax4C2hjGAABDmP0lAXz6yh3LyrSSMGYTGpB+FD6T0iveAcZa0SXcAyQkextx4MNzzDk+PcPXT0BiYszx6WGTK2UPZXu2Dps3gdrGXPejeA26XsLtCZ8qTpqouieQShPNsKZdXcJSpurtKK40Qtc2PUgdIeBr68QxEN2cfMUhEhhzPBMFo54sE+sKc7X87pfnWLoath2GkzLu/zmH5/cmXZ83UW1PWt40j6rA1cvWZG9SPQrtSQAEWu3vIBsw+KnTKoAf7b9GurKGpeSQqERvCLQaGptkxu4Zdv6sIvHLLHitKtNKwrifvLeEtYqsTEpwPALMGcq/Z4FMDc9/kdjiSRkvPhVwm7siAibHbHmGcNlnsPdSNihn5Rc4LNwGb9M9PdXDVpydQEbGBKvm3pl+VMNaJY3X3N3aHjaZVJT+YQ3V9OuuFaV3HSHw0dY+l5pIV7F2L8kdpCbMBDdyGZPCcsHx0tVcLU/Km6zsWt+kMcl5z7PmIVBJYyLg2QW7kBqbkORJXlppY0DgswT5Wvn6kTU3JYR69o5IK0wtQ/88hhfRKKLRCTTv6Sh5+IkSrSBj3E9jWTAfqEQcYPZfI12Rmd8EzG3tO8xteE0u54i9ipE80cjFdBT+mdM0lplU1FnzsI86+iWAtiNJlKzc+eFN9QeMbXx0NVfLy9ImKwDm7h81bmqpeVQFNPuMwzq7kHARJDg+WlXSeIHn7XMOeJzBDNw2wJWCloCHVmflFKJXmliytJqtKbgEEggJ435qWfo5mR+CAGMddmWWpOU3AZhB66p3nZ00l5kG86KXskEQrmL6gU2JnTTlnmNZZ07djuK8/XP/z37q6JMA2rYZSWIpA2RroraZNMvJV4jCZFA8dfVdLfeDeZ4jWpxNP9Khv+nYM32rgETlHXYEqSU2zdI8kuBJvloxqacBaxXIj06a4hRrz3hpZaXEmJ2Sec4kPjCXrhWLhHFv2h8f2ILhP9xP93eQBYBcHFHmVk32ZhSHhSPPLaIXe7UskIOjTlQmED2qQX80zU1zddJgLPyUGL9sYOuwkwOyuSjYeyTVK1E0P4gOOQWMjCHhPnEJmHMPxhCSGwW8u/ICrzPMx1ZeuqZbq/H9TUTdN/X86ugTP22dWGdov3B6hJtmCXgmwLfMU9fbzXeoVqqoVtLM0ziinwo4etPnYuNkB+8qVVQrUThqjR6i8LkkmDz57zg2kQCOnJ+5zx57xVOrWxzfFbUpXatgfrRXywJXa3IWgp5aPe+pKhVaOZEw7keSeF54h4nfX2NNomUi+DsY13XAo4KZS1z74J1/9GP6EXPFUD9CQQMShaO240zHmRyh1Wmzgom9l7IBrcMy7wrk5x6DCwCMzGJOs68WWvliwcFg34wk8bwAZHPuVZK9orTO0Pqqo3c8tXV/98RKv/JTHNOYzVSRfmOu0vbepFG1bwv2Z5mnrkPJksPXaxkAmZpjh9EzdipQ7+TEgTXU9BKSI+7vnVhXpwXvOPTzXGfFfFLGi1z41JCnVg7f9WtTtlb+c4S9OLFvroXGUyvz1hh7brH3Ji3cPanQimdv2HE/lHyOArLIChef8rhY3+S3c4TRKKI3s1hj8+LuLzd6lR047i8tmSsNpCcQjZrfKVBxrjOUXHKuQqZuo6BVkb4SRTR6H7hX8LgOLKhDBSNJlD5MWnbZejE5Y9eXxqYf1bCWiyMajZrfdRJ9R+S7ZAjJN0eY+3PCSmlY3zlpv+MeNtlgbE0o6StRRK/IvZYbyL4raUwyWrnH4eC1aqI5gInRZihZ6swz0Sjijp2ta9wPSKvw49786sQgiOi6bgykJYIgCOK7gv7JZIIgCOJCQgGGIAiCUAIFGIIgCEIJFGAIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglRAzDoC9aEgRBENKhHQxBEAShBAowBEEQhBIowBAEQRBKoABDEARBKIECDEEQBKEECjAEQRCEEijAEARBEEqgAEMQBEEowSPAtFBKRhCJMD/JElohG2y9nXfWGXmCOvO8nus8e/LRu65eyga0rvudc/XuYh+f+PfFcQnzEvut3a6j7+ZROrYf1vGkB61YHebfhrXOarurr8z+DKSN1V/dttTxxPGe/RBQV1g+JXjWGy49HO8W3B7gAmolpQ4xwjmiy//9+y4YXlq57BnouLLnOOcc2W4n0Hur1coPjwDTQGMLwPouDMMwf8opDIdssPGlAq102qnTWEHMfvjxCWYe57FrGDDqeazGujsW/ZQNbh0aWxqK34yOfZmYs8jHJ4jEVn3qaaH0YBEoncIwTlHEIu5KcLZW48Cph7GN1KjVXnIGB+1+Ndu8JHLA4xLupmC+57cikLobcgK3ePw0dD2V1CsJOroJoCtg+ZSkJo8bOIDln9bP9m/26AloD3ChtZJSBwfhHHFjhfnM7A8NGoppQd8FxUurj09wKXXdenZO4wqreBp2/lCklR/iAPOxhlUA2k/jEptrofEPcH2cH6bq71eB9bjlTHdQXFhFTRBheykbmOMGDnAd46OCNnMRRGIHyK9rPvXUsL2lYf6/wwCGkXqQR+WPWuhdTONLRaDHMFJldgIbRvxXDfinwW2z9dc2KgvziI8CGE3h4XoF23+FD4DaArD4IMxuTYO2sIoZKTsIBh9dTVooPTuAtiCvzcrCOLijJ5A9llUXVis5dXTjPUew5cxF3EtrkRUCD61ajQOg/ex8xhUWtNDBSo1W/ggDTKtxAACopC5xU1n9Ya7c+APLdCz3BHrQ4ErZQ9ke8JoUAOB/uzCMbdz5KUA97glkq4FGKOOCDjx/Gl8qwLVxx2608iWcdQBw/cFD5Le8d2tsWjPCSX3NPyhCezwjd+vupyuA1tu72P71JR5ek9Nkq3HQ1ce92GNzkbUKUkfveM0RDB9fYXErj4e/hR8PXloNj19nxm4LtT8q0H6Nc8uq0grXHuLhesU7QLjSh+70nBqt/BEGmMaXCgB7G7+LPFYxE/Ys4biBA1Sw+KP47KQzgQ5j3Gew91I2CK3GAbC1iEuC86HYjR624uwEMjoOnz1PAMyU5WpM7EQd6niVEg8EwBmcx38Kb51JDCv1vDjN9fEJZv4p4tRKQ+yuV7BYcJUcTeFlScPqM3mrLT9dzf66LmWysml8qQCPZ7i5e397nFxYrfzq6IcAc4S521yFVrqDkMkxAN5a4cYKjG/jeBqJIBK5hMYDNlPQjRqtgFhmF/mtRbziLrzqeBI76KRcuZoo0CoAwgATy7A5/hji6wC2tlELk8c7bqACzdERq7GwB7jyaHypAAvsoJIQVGVx3MABgHy9k39G6hJ/8CVnsLpQxEuJE2ZgbqyY/cZLc91YYc7xzB0Zj+HfXko7twL8da3nZoD6ipTJysR6t/Z5mTN3f2H8TIJWnnX0Q5A5wpGCDou3Vq2384j82MBDS6v4e1mXQHrFDBD8s+YYVtpzdSf71IVsrQIQ+JqylGh8Y4UJWrDOTpx5yk6ay8Op+ygbhFjGeZEhli5C6zeosimx4wYqYY0bTWHbMLByo/P7w3Vg9T3rLC2UkpewiCJOfS5ksFt3c7cqj1hakOZib9ZF7mJbWIN1biXpkNRT1+MSnv5TxJ0bXjX0inkm1jm4N98Hj2uo+9nD4WJr5VFHPwSYI8wUo3XWERovrayUGLNTMt9VfGCuUiv7rLk7QDhvJd79Q1yFVK0CEDjASO8sBjPVxU9z8c8ceikblmCHsQ54KbGAOfde6WzJreBybdf3th9vsSD1Mkc7zfXKce5ULyyi0l4pbnufd9xYsdIyNXl2OTB1bf21jQqTrpp5DDNdomJH4ekDfD/7LrQS1CETdmzX36+Kz7dk0cd4Va4VhpF6Zga4V1+Yj63zKPsW3PaD6+IqBqCVA4PLqVFcgAHkjV3DMAxj18gDBtZ3+cUDclrSDCwUjVP293YbhmHU853f2f/m0UvZYNYZxQUYWunU8Tvvnd3v4V2Xu94+cb9jPW8AmlH8Zv66uw4fmxi+FQ3N/lv2v/vG9I98nf3M9qHO5w4bvxUNjfUprh2W34WyL7iubRtD+nl3f5i/8/3B254LqVXAOvrBd46w2gnThhMvrbrb9xxn0rXi+6NpE/O5Yy7gz90qtAqCIMB0DIP9E3Ty8qHdOYKJY3e906bj5ev5LhuEZfu3rt3xXu/cHWA4Tm8PSol9ZzoS751dWrV/WCdz9jWrQ+jgx3Xijr3tz119ssv2o2BAmnaGHajBdDUMWQHGMLo0cdTpZc93oFXQOvrEe44QtB0KL62c84zfuJerlcgf3Qt+1p80o1hnx5JarfygfzKZIAiCUAL9v8gIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglACBRiCIAhCCRRgCIIgCCX8599//z1vGwiCIIgLyA8//BDq72kHQxAEQSiBAgxBEAShBAowBEEQhBIowBAEQRBKoABDEARBKIECDEEQBKEECjAEQRCEErwDzP4motGo9ZNC+URGk3vYbNcZxea+6+mG+FlXTT2UDYzjnTexJypzq4wzr3pOykjZ9fiVDcwZyrc675wqs7U6+9WvzbNySlBPGDy07cmX2HoEGvRKEF1h+dRGuBbNvuW8YxC/Ye3g2HlWToW2z2rBYxx6+ZlXPZK0Etnm0JD5CdEfMrSSUYeI8H5g9WVXWVNjafOmAHGAOSkjdTOLtQ86dL2GNVSRfhR2ojxD+VYc2UwNuq5D/1zA4U1GmP1NxHNrqOk69A9ryN70cNheygbF8c46jgqHiLsdZH8T0ZtZ//d8lAYKR9D1IxSQxn0Jk/jexgTSKOBINzWZTE9YDmL262HhyOxXq80JkQOelHE/DRQ+mxogfV/C4sFD25MyUjcPzfZ0HUcFIH3Fa5Lv1FPLZBEPO6EG0RWwfCpcUx2qSL8J65FZvJAW/Fm8x6HYz7qRrpWXbVPLln/r7WcJJFC4NR2yTRlayahDhAQ/yL2QtEHoDWGA2XuTRhVrmJ0CgGks6zr0N0kMhWntZAfvKmuoPbIcYiSJkl5CcsRqs5YFMrOYBoCp2yhoWeyIHLuHskE5+/sdqpkalqfM34eSJcc7721EEb15iLVMwruikx28qyQw9/MQgCEk762h+udOyOC8h51cAoUN2x5TE9PWISTf6CglbUuHMPtLAvj0ldvm2d/vUNXmMDsCYCSJpUwV7/4O6cBe2rp0Hvp5Dgkc4ivX4fewkwPW4mY907cKSOR2Qi0e/HS1SqH8+yESWoiGWLQEErl4uBWilpAU/F14jkMvP3MjXyu/OaKDvYh7znnWI5K0Cl2HR91h/SChQcIGoXcEAeYMXz8B0MYwJrExc2IT1Wm2mZhwPj1scqfIHsoGtg47f1a76nQQr0HXS7g94VPVSRNVTOIy6/iVJpohrMP+DrLuOvukeVQFrl52TLDVo1DW+WjLK2sFODcnX3GIBMYcz0TBKJBl/roCOCvfx7tfnmPpar/tuJnDUiHhvbNm06i8NMbVJSxlZGQOnHhq1YufSdeqBz/af410ZQ1LyVBLXgsJWgWpo1+C+IErfehOa07eW8JaRU4mpRcEAaaJZgXA1SZey86vXr2MpsfZyeRYZxV+2Wew91I2KJNjTWFOeXqqh604O0hGxuCz5wlcJwKdnezhdbqKxC+zwh0nO+GOTUixzldbe5BOpKtYu+e1G2YmuJHLmJRgmpeuZn9NSpqsOowln6OgidIb5gp88gOT7uGkMaYf1bBWSeO17JWxl1aB/QxQoZWvH+EM5d+zSBRuI2xyzEaGVt51hMPbD/awyaSg9Q9rqKZfu3x8Gsvcz9XifcifO8TYZ/sMJsvPW/dKLo6deKcjsjdlXR6QQ/bmDmatHG8tI+mdZVFJ4wWet50c3Ny4lcPWCnguecL0xU/bkSRK7by6+gNGFi9d9zbiwIdlaZNVhyEkN0RnXGZas516Ommiyq3DnBikr4y9tArkZwrx8yNHCloWMrTyqiMsXn4wjWUmjXjWPORXMbUs6ZwsOIIAM4YxDUA7jTGN2QyAyjvshO04rYDbtlBTt1HQnPn/TprLStN50EvZoLCroulbBST6fWc2JSZ0yF5hUgIjSSxlgGyNdZYzlG9ZB7Q+52VsSqx5JMc6P23bcG1nYdIsJ18hGC49IdT1pIwXnxi7ZWOdcfHSG+wtyOjvh+JdrnXGKHVi8NTKz89Y5Gvl60cnTXGKNQwytPKoIzRCP3De+rv/p7gK85xM0VkRB0GAsVJOYc8N3LWO8TfQZqqLn+bqpME49gUqG9g6QZqtj3MPXkos7HmWIM3WSXVZweVqzfcyBi8l5ndG4Ye3tm74Z2gABGmWMGdP3rqe/f0O1UoaE9bgjOcA5OISr5Yz6Y0a8+FJGS9yiU5aY2PO8x2SG2Za5vVReHs8tfL1MwbpWgXzo71atusMURbhtRLUIQWBH1jnUTVrh16655GoHEnieSGB7O+vpc7tIoQpsun4GgD7ZpZ5WwRhVw1Ts848otUxs1OdNts5Qtcznn1BywbFUSesm3T2TbVeGJnFXDsXa+WLPc5Deq8Tbae30wTtq6WP/K0d+nmuk0N21dM3XtqelJFivyew/xppYYpjGrOZzpXPvjVga/TQdShZclx9rWUAZPyDdI8WmOmNnPt6exVN+2rwm7T3LnckiecFIJuTsNv00srHz5zI18pvjrAXJ/bNNflI0EpYhwSEfmDvJM35xouh5HMUkEW2It88N+IzmKllK/8ZRTRq5vT90i7+TGNZrwE3re3czUMUPjO5bztHGI0iejOLNTYv7v7SklfZfplahv4BZp3RKOKfgk3Y3V9asnOxE4hGzYk//HnIEJJvjjD354TZd1fSmPzAXi0FwKzEnYfZe9hkJ3jLSdNXzHqkXPX00nYkidKHSbO9tl5Mztj1pbHpRzWs5eLWjoK5stovfesqkanbKLBXoO3Uk9VfO3Hzu2ZNj3TsUHIJa1KM8RqHXn6GrnEoXSu/OcK+gKQSCVp11SGRLj+w0ojm+LoP3Ct4fA0AsL86MQgiuq4bA2mJIAiC+K6gf9GSIAiCuJBQgCEIgiCUQAGGIAiCUAIFGIIgCEIJFGAIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglRAzDoG/yEwRBENKhHQxBEAShBAowBEEQhBIowBAEQRBKoABDEARBKIECDEEQBKEECjAEQRCEEijAEARBEEoQBJg6nkQiiHT9zKN03G9TVp25uuvzFkrJCJ58HFQdIsw6Ar3zxyeIJEtoeVV3XMK8XYdf2SB8fMKxje0Ll2Y+bbbezrfLzr8NbZ2jPvanXbfDfj8/Yt/lCdxq92hZcF0B1HM8/+oV0fix34Vjk0ebA9fKZZ93mzK18rHNdwz0g59WLpsGPK7qOX6/tt7OB3xvlXNmAIwg1PMGAAPru4GK89k18oABaEbxG/v5qVFcgJGvD6qO4Oyuc97Z7ouFonEq/EvTHq106vpviXwrGlq7H9xtmL8L9WL/1lGPROp5A8gbu122GsZpSes848D2O1eDkAjrlOLnPNz67Br5oH0+aK0Mq3/a/m2OOdHYUq2V2zYHSvrDpZWj/cGPq911GED3/HFa0gL29WDnTDcBAozVqR4TQjDMF9UWNNfk3HuACVdHQDiObYqtGfl1d/su3M5Vz/sEpF7xD1qnJbGN7me767IDoPek5D34XH/7rWhooX2PQThhnRrFBc3QvCaQPunSood3GrxWPQQ/1Vp5+pGahZu7v/1+9/pbGVqZwV7rGi+9BpiBzJkc/M9gPr7C4hagle4gJmHHdP3BQ+S3FnHXa/vo2gq7t5qB6ghFC6Vnq93v/L9dGMY27vzk8+fHDVRwHeOjzGdbDTRkmffxFRa38nj423Bff974UgGujYP968oXadah9fYpVheKuHND8PyvbVQW5hEf5Tw8buAAmrPvcIBG36lZR8t8XQG03t7F9q8v8fCajHZY6niVqiD/INXp7+MGKgvjGA/w1wPX6mMNq27fFaFUKx8/CjkG+HRrNTx+nRm7LdT+qED7NQ5eq8q0uvYQD9crWHzgkZ479zmTj2+Aqb9fBaBh/r+yhIxhpZ5HJfVKkK+t40nsAMVvBgzDgMEt61dHSATOG7vRQ4hlJ5DRcWjSjBNPkh3MgSIaCACg/dSZ3sZ/kmcdd0K1sc6lLomet2EmuNFxXJdlmnBSquNV6rrkycqEN0m2GgfA1iIuBTy7GLhWC+NA4LMERVp5+VGgMdA73IB2YwXGt3E8jUQQiVxC44GBbQ8/UaVVLLOL/NYiXnHPTC7AnCnAJ8DUUXsMQLTa7JcbK9hdX8UM95AqhhVjGymrvVbjoI86wlF/vwqsx6U6rzSOa9je8gr4LZSSM1hdKOKlggnTl481rCKPOG/VOZrCtmHA+FbEQWwAB4wuRLrWczNAfUWB3vwVb+NLBVgo4tRMUZt+LOMiSK+ItNpaxFO8NCerb0UgdWngWnn6ke8Y6Ae+Vq2384j82MBDS6v4exmXQPrBDBCrMd5i5PznTBHeAeZjDauA50q4X2LpIrTHMxzHdd5guftHP3WEoYXGP0D+fyGnGzYldtxAJaxZbF3CgN9CKXkJiyjitOy1Q3Bu3RtfpFlnOrdfcB5N4eE6sPpe5OhMmuW4AcFw6dUyvq7HJTz9R5zOC0cDDc5EGMsYMBh9YukitK1t1ASppcFrxezyzkUrHz/yHAP9wtPKCjrMTsmcc54Kb0Gq0goAcOMOigu8AHHec6YYzwBjR8Lr4wpWwqMpvCxpWH32ynk2YaUxdq0Vw/YDj023qI4wWKujQDlooV2clFjAnLsf9ferXXleEyu4XNt1TF48eFt3dmvfP9aA9K3LnOy55bhploBnAl4IdG39tY0Kk66aeQzg8Yykq+U9nGcIyg1cK0E6d6Ba+fiReAyEoCet+KjTymYYqWdmgHv1hfn4vOdML7xuANi3puRcA+TdCLFvqDGf1/NMm+4bbAHrCEOAG19eN0lYm+RfUxbf/HBeLfVB2dVXwQ0k3q06jzaVXH0NeJNP5lVb/k2fi3KlXHRbzGWfT5tqril73WRTc/tJdCvLfaXec5ypuqbsssu0ifn8vOdMDzwCjKzryTaCK4fWdw86n3deHtCMYp0VKmgd/eMfPHhlOE7/rWhoQIDvzPSC6Nqmfdfd/cM6GeeaI/h37PvGa1DZ3zFBt2N3D272feT4XxBdDUNugBHXxfq42z8ugFYu+xz+1hWo5WvV0zV2SXjpbn8XpVur7nEvWyu+XVaftz8/3znTC/oXLQmCIAgl0P+LjCAIglACBRiCIAhCCRRgCIIgCCVQgCEIgiCUQAGGIAiCUAIFGIIgCEIJFGAIgrmN0AAAD+tJREFUgiAIJVCAIQiCIJRAAYYgCIJQwn/+/fff87aBIAiCuID88MMPof6edjAEQRCEEijAEARBEEqgAEMQBEEogQIMQRAEoQQKMARBEIQSKMAQBEEQSqAAQxAEQSiBAgxBEAShBI8Ac4byrSiiUftnE3syWjwpI9WuM4XyifPx3kanzc1976p6KRuUs3Kq8863yjjjFdrfFD+zYd/Tr2xg9rAZFb2z85lfm+x7pspyrPPUdn+T8aVu3Z2w7yLH7wLpCsunNqR4usM/nXW6x5Z3m3K1svq2qz3TpmDjSEYdHoj8yOFDwfouKGKtgvuOu6yMcWXa1T0GzsqpgO+tWCsfhAHmrHwf6Qqw9kGH/rmABLKIhxZyD5tX0pj8oEPXdRwVgPQVpvP2NxHPraGm69A/rCF702Ny6aVsUPY3MZGeNOvUj1BAGhPud97fRPRm1qeiM5QfpYHCUbue+6Gd7QzlW3EcFo6gt9/ZHnyuZyLbbU7KuJ8GCp9NbZG+7zPhB8FD25MyUjcPzfZ4urtr2ogjm6lB13XUMhL8LoiuVrl4LlxTNmflFOKfCjjSdeh6DWu5ODPhNNGsJNr9oes69EfT/IqUaAUg9yJ8PTLq6MLDj6aWO/2l2/NSAoVbgr4LiKdWQX0HUKcVsngRdv5QopU/wgDTPKoCWMPsFICRWcxpAHI74Sbxk684RAJjI+avQz/PIYFDfLVefK+WBTKzmAaAqdsoaFnsCCJsL2WDctY8BLQxjJnWYfaXBPDpa3vFsrcRRfTmIdYyCZ/33MG7SgJzPw8BGELy3hqqf+6E3MU00awAk2ND5q9Ts1hDFc0T09bkGx2lpPWMY7vjPf9+h6o2h9kRACNJLGWqePd3SAf20nYkiZJeQlKgu5M97OSAtbg5aUzfKiAR0u/8dLVKofz7IRJaiIYYmkdV4OplmIpMYzYDVI+a5sOTrzjEJC6PBLBdhVYAEhqQfhRuZy2jji585ogO9iLueduv+sVLq2C+Y1mkSCtoidDBSolWARAGmLGJBABr0j7ZwbsKOhN6v4xcxmR7UnQJgjN8/QQkJsYcf3LY5ErZQ9ngDI1NApUmLNfCzp9VJH6ZhT1tI16Drpdwe8KnopMmqu4JpF1vv4xhTGPecX8HWXsB0CPOAWXSnvz6xVNbJ17P3BOMiSgYBcNXV5g79ne/PMfS1f7bYRmbYCciZ9DESRPV9qTljRKtAEzeW8JaxXtn7UgbcdKaQeromaB+tP8a6coalpJDXVX0ipdWQXzHRpVWuLqEpUzVO0C40ofu9JwSrQIgDDBDyZKVhokieiWNaqYm3sYHZhrL+hHGfjc7YeJoCfqbpEOQ9godQ7jsM9h7KRuIqWXon8fwIhpFNDqB5j12VwBMT/Xw/uwEMjIGnz1PAMxdytLRhOlEv4/hSF8WBPw9vE6LBwLgDM7mYiIs/traufWJdBVr95JC28AG55HLmAxrmo+uZn9NSpmsbIaSJej3mpiIRhGNvsDYZx3L1mLgrHkIVNLWM/9zJvlaAcA0lj+soZp+zW97f5NJG+moZapIv3GX9KmjX7v8/AhnKP+eRaJwO9yC18JLK3/fcaJGK2D6UQ1rlTRec7M0e9hkUtA6VxMVWvnjcQaTQrRttJmXDH1YfVJGyhJJ13Xo8R15lwckcFZOIXqliSVrUM3W5B34hsc8rHsxYZ2zbAD3uYfl5nlMVivgucQJ05cg2o4kUbJy54c31R8w2vjpurcRBz6IgnV/7G3YiwAduv4ceNRZVTaPqoDGTt5ZxKVdBOmBqWXxGdfUMjOxmxmDnuvohyB+5EhBh8dLq4szJ5gBgn/WPI1lJgV91jzkVyFbqwAIAoy5FUR7a2rmJVF5h50QqQpzu1vA7fbqwDw7YQ+wOmkuD6fuo2wA68ztL7MqMvP/fR6OsSmxkyaqYc2zUmLtVbaV43WuKs9QvjWBNAo46lr1OWG37uZ5WziCaNtmJImlDJCtiRydSYmdfIVguAS1zFvXkzJefGLsloKVZmnv0qxzOGv1OP1Id6zKp28VkPAYW7K1YjH7It4d7B03ue7jXT919EEgPzppilOsPeOlVe9zgkqt7L7oDhDOW4n3/xRXIVOrIFyg78Hw01ydNFi/Zc8BXkosYM69f6zgcrXGSSk44W3d3edZauGfoQEQpMSCHYj3Zcnf71Bl0lXxHAAZu/We4b+jcq1GknheSCD7+2vHGeHeGystruvQ9ZL32ZSgDlXs1bJdZx0XAfXjagjJDTPAvT5iPrbOo2rWLqt0zyOpPGCtBAHGmsDbOT8zyiPkqmHo5zkk2Dzi/mukma3udJzJEVqdJjrE7qVsQOsw+0vCkaPce5Pub6U0Mou59qrLyhd7nIcEYmoWa+x1xZMyXjCHkXsb1s4lwDnZ0M9zzhV8Lny6wVPbkzJSju8zOHV3Mo1ZZmdmTnRhLpd46zqULDmuvtYyADL+Qdobc8ef/d0OUqYPmJdkzNVm5xDWvA0lekcVWnW1kXyOArLIVlwP7INvy9f6qqNXW3zmCHtx0r4wERovrXqbEwahlRkggGzOvTuyd/2W/R7I0ioQuq4bop9aBgZg/WgF48ijbOCfD2udOpEwCp/Fba59cP2dywZh2RA/Qd75qJBwPTsyCprLhs8FIyG779g6He9cM9aYzzs/a0at/dzZ10eFRLtconAkpe88tXU8c/bVUSFhIFNj6mLfx34H9bq2yzls6ffH9Il2m446Xc8c9qjWyuzbrvFi6dP+3OW/NYfPB6xDhR+J2lamlZfvdI972eOK74/W+Gh/ztqfMAofCkai3W/htApLRNd1Q0XgIgiCIL5v6J9MJgiCIC4kFGAIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglBCxDAM+qIlQRAEIR3awRAEQRBKoABDEARBKIECDEEQBKEECjAEQRCEEijAEARBEEqgAEMQBEEogQIMQRAEoQQKMARBEIQSPAJMC6VkBJGI+TP/tiWnxY9P2nVGIk9Qdz2u5zptPvnoXVUvZYPC1hnJua2z+PgEkWQJnj1yXMK8XY9f2aCwdUbmUTp2WI4nEcZ2nzZbb+cHq63jmdt2N+y7dPtIPwTS1S7n8Tw4XuPH+czPpoFr1dPYl6+V0DbH58H6Lhje78v2/6DHlem33f3aejsf8L0tfbrKmu8sa94UIvq3lHfXYQB5Y9cwDONb0dAAQyudhvsHmq168nXr93rewELRaNdaz3faZP+bRy9lA3Ja0hz17K5z3rmeN//ta9bu7pqM4oL9t+x/h2HXyLMafCsaWttWdxvm71gX9Mi3oqFBM4rfXP8dBi9tXW24+7nrTdc7trP/3S+BdLVtRvj27DY6PmLq0e4bY9fIB+3zQWvVZbvpdx3bncjWyneO6Cobvj88tXLMLYMfV+Y83O2vpyUtYF+b+qHLFrdPqkEQYCyjhE7XH6clzVXHqVFc6Ly400G9O6CXsgGt6w4E34qG5u4DaEZ+3f0eLtzO5TVIgsIJorvr4nfu7mvxM+GE2wN+2jrwHHyuCc0RSPuyzFdX1l7NawIJDGdSruc79fbwToPXqofgJ12rXvxI7sJNpJXbnkGPK3Pe1brGS68BRlvg9av6ANPbGcxWAw3pe6gKGscA0ELjH0D7adzx9KDB22b2UjYk7Dv/bxeGsY07P/n8zXEDFVzH+KigHon0886NLxXg2jiGmc8qX1RYZ2vrpPXXNioL84iPdj/DcQMH0Jx9hwNuPaFw6dF6exfbv77Ew2uS22H5p2GmV44bqCyMY9yvPM5Bq481rLp9V8SgtOL50cdXWNzK4+Fvw9y/CI2l1fD4dcZXWqj9UYH2axy8VpVpde0hHq5XsPjAIz3nSh+603PXHzxEfmsRd2WlWAMiCDAxxNcBbG2jdgwAddQeA2GdxxRrEa/svN/HV1jcck6S18dteYYx7jPYeykbwDqMXwMqqVftfGe9sIgK886xG7Hg1bETyOg4tLDmjY5Dwyqe2g5yXMLTxyIHruNVSjwQAGdwHv8ptHWBtLXPkC6lKsg/SAltAzvBjY7jejjLfHU1++u6xMlqHOMLwOoze0JoofRstT1RtRoHwNYiLgU8uxi4VgvjQOCzBJlaBfQjqz+10h30MCIFeGuFGyswvo3jaSSCSOQSGg8MbHv4iWytbGKZXeTZfnFQx5PYAYrfDBiGAaOed/i7VQNWuJ+rRbiDiWVOUVyoYPHHCCKRp8C6hM66sYLTkobVmDWw3o+juBC+WlmY77yKGWtg1X4qhg8MshhNYbueRyV1yey7B8D8Oq9gC6XkDFYXinipanXHI4i2oylsGwaMb0UcxAZwwGjhp2s9NwPUVyRMVjbDSJXNCcEMIneBX/Ptp40vFWChiFMzRY3d9VXMyLoIEgQ/rbYW8RQvzcnqWxFIXRqYVoH86LiG7S0N8/+V4d/eWrXeziPyYwMPLa3i72VdAukVM0CsxniLkRhWjG2krEDfahzwq7ixYvraAO33SJENI1W2IqKxjTgqQNCtswfDv21bdRowMuNobLE7EXalYqbBvOilbEDrmHc2sDLOSXUFhU3BHDdQkWHejZVO35XjQFeasIVS8hIWUcRp2WuH4Nz5NL5Isc5X2zajKTxcB1bfixyd2V0cNyAYLr1YJtb1uISn/xRx50boRlzEsGKw4+egvauNZQwYjD6xdBFaO1vQzeC1YlJPA9cqgB8dN8Qp1r4QaWWlxJidUixdhPb4qfAWpAqt2ty4Yy6UBDfC7B3n3T/EVZj2zwxswRDwDMaawAPmjQPjyOHy01zcCaqnsv3Tahz09868lJjsvkPDNfCs4HJt1zF58eBt3d3nWaHh5udt+GdoAARplvALG0frjK6tv7ZRYdJVM48BPJ6Rd7Xcgpefd8J/x4FrJUjnnpdWPD+qv1/16ctw+GvFR71Ww0g9MwPcqy/Mx9Z51K4VJLcfeCQqR1N4WdKw+uyVkjPhLvhn/9Z1PNc15dA3DjhXax03IS7CNWXHTR/+O3vdJLFKKLqm7Lpx1+8tP2VXXwXa8m7VebSp5JpyAF1ltWfX09bc8b4X5Uq5aBy67PNpU801Za9rwfJvP4m14l9xD3RtWuY1ZVefmjYxn3P8q2Mz75q5Xebcril3DAP497D7pd05gu+S2Pe+u16ec9VXWLZ/69od7/XO/KuULhusiUz0nn1hf08DcAVUp1bdZbqvnrI6DERbh+3Ovuq+csm+T/iFQ1BdDUNegHFrIhrg3X11AbRy2ec9DmVr5Web9/dy+sNLK+c84zfuZWvF90fLXteiAPb3XepscBP0lzUeVQcY+ieTCYIgCCXQ/4uMIAiCUAIFGIIgCEIJFGAIgiAIJVCAIQiCIJRAAYYgCIJQAgUYgiAIQgkUYAiCIAglUIAhCIIglEABhiAIglACBRiCIAhCCf8/T3kV6+5HPisAAAAASUVORK5CYII="
    }
   },
   "cell_type": "markdown",
   "id": "593558dd",
   "metadata": {},
   "source": [
    "### 5.2.4 На вход функции подается датафрейм:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "Заполните пропуски по следующим правилам:<br>\n",
    "Столбец А: 0<br> \n",
    "Столбец B: среднее значение из столбца Е<br>\n",
    "Столбец С: максимальное значение из столбца H<br>\n",
    "Стобец F: по методу ffill<br>\n",
    "Столбец G: по методу bfill<br>\n",
    "\n",
    "Дополнительно:<br>\n",
    "\n",
    "Удалите столбец в котором все значения пропущены. Функцию drop не использовать!<br>\n",
    "Удалите строки, в которых хотя бы одно значение пропущено<br>\n",
    "\n",
    "---"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "afc8a8db",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df = pd.DataFrame([[0, np.nan, np.nan, 3, 4, 5, 6, 7, 8, np.nan],\n",
    "                    [np.nan, 11, np.nan, 13, 14, 15, 16, 17, 18, np.nan],\n",
    "                    [np.nan, np.nan, 22, 23, 24, 25, 26, 27, 28, np.nan],\n",
    "                    [30, 31, 32, 33, 34, np.nan, 36, 37, 38, np.nan],\n",
    "                    [40, 41, np.nan, 43, 44, 45, 46, 47, 48, np.nan],\n",
    "                    [50, 51, 52, np.nan, 54, 55, np.nan, 57, 58, np.nan],\n",
    "                    [60, 61, 62, 63, 64, np.nan, 66, 67, np.nan, np.nan],\n",
    "                    [np.nan, 71, 72, 73, 74, 75, 76, 77, 78, np.nan],\n",
    "                    [80, 81, 82, 83, 84, 85, np.nan, 87, 88, np.nan],\n",
    "                    [90, 91, 92, 93, 94, 95, 96, 97, 98, np.nan]],\n",
    "                   columns=[\"A\", \"B\", \"C\", \"D\", \"E\", \"F\", \"G\", \"H\", \"J\", \"K\"])\n",
    "df"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "1bd6bf2d",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Столбец А: 0\n",
    "df['A'].fillna(0,inplace=True)\n",
    "\n",
    "# Столбец B: среднее значение из столбца Е\n",
    "df['B'].fillna(df['E'].mean(),inplace=True)\n",
    "\n",
    "# Столбец С: максимальное значение из столбца H\n",
    "df['C'].fillna(df['H'].max(),inplace=True)\n",
    "\n",
    "# Столбец F: по методу ffill\n",
    "df['F'].ffill(inplace=True)\n",
    "\n",
    "# Столбец G: по методу bfill\n",
    "df['G'].bfill(inplace=True)\n",
    "\n",
    "# Удалите столбец в котором все значения пропущены. Функцию drop не использовать!\n",
    "df.dropna(axis=1, how='all', inplace=True)\n",
    "\n",
    "# Удалите строки, в которых хотя бы одно значение пропущено\n",
    "df.dropna(inplace=True)\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "37589627",
   "metadata": {},
   "outputs": [],
   "source": [
    "df"
   ]
  },
  {
   "attachments": {
    "image.png": {
     "image/png": "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"
    }
   },
   "cell_type": "markdown",
   "id": "1d528c56",
   "metadata": {},
   "source": [
    "### 5.2.6 На вход функции подается уже знакомый датафрейм с клиентами авиакомпании:\n",
    "\n",
    "![image.png](attachment:image.png)\n",
    "\n",
    "\n",
    "Оператор call-центра не проверил присутствие некоторых клиентов в списке и повторно внес информацию.<br> \n",
    "Найдите все повторяющиеся записи в датафрейме.<br>\n",
    "\n",
    "Функция должна вернуть новый датафрейм в котором будут оригинал записи + его дубликаты.<br>\n",
    "Записи, которые не имеют дубликатов не должны попасть в новый датафрейм.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "bed72ada",
   "metadata": {
    "scrolled": true
   },
   "outputs": [],
   "source": [
    "df_class = pd.DataFrame(['Sergey','Viktor','Pavel','Andrey','Petr','Sergey'], columns=['client'])\n",
    "df_class['class'] =['A','B','A','C','D','A']\n",
    "df_class"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "5b34f7ff",
   "metadata": {},
   "outputs": [],
   "source": [
    "#df_class[df_class.client == df_class[df_class.duplicated()].client.values[0]]\n",
    "#df_class[df_class.duplicated(subset=['class'], keep=False)]\n",
    "\n",
    "df_class[df_class.duplicated(keep=False)]\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 114,
   "id": "c3737969",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ext\n",
       "csv        92\n",
       "exe      8342\n",
       "jpeg    11703\n",
       "json       94\n",
       "mkv      1282\n",
       "mp3       109\n",
       "mp4      4260\n",
       "py        213\n",
       "xml      2271\n",
       "zip      1852\n",
       "Name: size, dtype: int64"
      ]
     },
     "execution_count": 114,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "from math import floor, log\n",
    "\n",
    "def get_unit_name(size: int) -> str:\n",
    "    \"\"\"Принимает число в байтах и возвращает число в B, KB, MB, GB\"\"\"\n",
    "    unit_names = ('B', 'KB', 'MB', 'GB', 'TB')\n",
    "    pwr = floor(log(size, 1024))\n",
    "    return f'{size / 1024 ** pwr:.0f} {unit_names[pwr]}'\n",
    "\n",
    "\n",
    "f = pd.read_csv('files.txt', sep=',', header=0)\n",
    "df = pd.DataFrame(f)\n",
    "\n",
    "df['name_'] = df['name'].str.split('.').str[0]\n",
    "df['ext'] = df['name'].str.split('.').str[1]\n",
    "df['size_bytes'] = 'NaN'\n",
    "#df['size_bytes'] = df['size'].astype(str) + \" \" + df['bytes'] \n",
    "mask = df['bytes'] == 'GB'\n",
    "df.groupby('ext')['size'].sum() \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 80,
   "id": "60198d70",
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "ext\n",
       "csv        92\n",
       "exe      8342\n",
       "jpeg    11703\n",
       "json       94\n",
       "mkv      1282\n",
       "mp3       109\n",
       "mp4      4260\n",
       "py        213\n",
       "xml      2271\n",
       "zip      1852\n",
       "Name: size, dtype: int64"
      ]
     },
     "execution_count": 80,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# df['size_bytes'] = df['size'] * 1024\n",
    "df.groupby('ext')['size'].sum()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "88c5cdbf",
   "metadata": {},
   "outputs": [],
   "source": [
    "_df = df.copy()\n",
    "_df['size_bytes'][_df['bytes'].str.startswith('MB')] = _df['size'] * 1024 \n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "75af289a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
