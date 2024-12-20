{
 "cells": [
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "# Introduction to Statistics in Python\n",
    "\n",
    "> Statistics is the study of how to collect, analyze, and draw conclusions from data. It’s a highly valuable tool that you can use to bring the future into focus and infer the answer to tons of questions.\n",
    "\n",
    "- toc: true\n",
    "- branch: master\n",
    "- badges: true\n",
    "- comments: true\n",
    "- author: Datacamp\n",
    "- categories: [Python, Data Visualization, EDA, Time Series, Machine Learning, scikit-learn, Regression, classification, Tempogram, Spectrogram, Cross-valiation, Stationarity]\n",
    "- image: images/stats_intro.png\n",
    "- hide: false\n",
    "- search_exclude: true\n",
    "- metadata_key1: metadata_value1\n",
    "- metadata_key2: metadata_value2\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "[**Download Datasets and Presentation slides for this post HERE**](https://github.com/anhhaibkhn/Data-Science-selfstudy-notes-Blog/tree/master/_notebooks/Introduction%20to%20Statistics%20in%20Python)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> Statistics is the study of how to collect, analyze, and draw conclusions from data. It’s a hugely valuable tool that you can use to bring the future into focus and infer the answer to tons of questions. For example, what is the likelihood of someone purchasing your product, how many calls will your support team receive, and how many jeans sizes should you manufacture to fit 95% of the population? In this course, you'll discover how to answer questions like these as you grow your statistical skills and learn how to calculate averages, use scatterplots to show the relationship between numeric values, and calculate correlation. You'll also tackle probability, the backbone of statistical reasoning, and learn how to use Python to conduct a well-designed study to draw your own conclusions from data."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 2,
   "metadata": {},
   "outputs": [],
   "source": [
    "import pandas as pd\n",
    "import numpy as np\n",
    "import warnings\n",
    "import matplotlib.pyplot as plt\n",
    "import matplotlib as mpl \n",
    "\n",
    "\n",
    "plt.rcParams['figure.figsize'] = [7, 5]\n",
    "\n",
    "pd.set_option('display.expand_frame_repr', False)\n",
    "\n",
    "warnings.filterwarnings(\"ignore\")"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 7,
   "metadata": {},
   "outputs": [],
   "source": [
    "mpl.rcParams['axes.grid'] = True\n",
    "plt.style.use('seaborn')"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Summary Statistics\n",
    "\n",
    "> Summary statistics gives you the tools you need to boil down massive datasets to reveal the highlights. In this chapter, you'll explore summary statistics including mean, median, and standard deviation, and learn how to accurately interpret them. You'll also develop your critical thinking skills, allowing you to choose the best summary statistics for your data."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What is statistics?"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Descriptive and inferential statistics**\n",
    "\n",
    "Statistics can be used to answer lots of different types of questions, but being able to identify which type of statistics is needed is essential to drawing accurate conclusions. In this exercise, you'll sharpen your skills by identifying which type is needed to answer each question.\n",
    "\n",
    "Identify which questions can be answered with descriptive statistics and which questions can be answered with inferential statistics.\n",
    "\n",
    "![](./images/infer_desc.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Data type classification**\n",
    "\n",
    "In the video, you learned about two main types of data: numeric and categorical. Numeric variables can be classified as either discrete or continuous, and categorical variables can be classified as either nominal or ordinal. These characteristics of a variable determine which ways of summarizing your data will work best.\n",
    "\n",
    "Map each variable to its data type by dragging each item and dropping it into the correct data type.\n",
    "\n",
    "![](./images/infer_desc2.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Measures of center"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Mean and median**\n",
    "\n",
    "In this chapter, you'll be working with the 2018 Food Carbon Footprint Index from nu3. The food_consumption dataset contains information about the kilograms of food consumed per person per year in each country in each food category (consumption) as well as information about the carbon footprint of that food category (co2_emissions) measured in kilograms of carbon dioxide, or CO2, per person per year in each country.\n",
    "\n",
    "In this exercise, you'll compute measures of center to compare food consumption in the US and Belgium using your pandas and numpy skills.\n",
    "\n",
    "pandas is imported as pd for you and food_consumption is pre-loaded.\n",
    "\n",
    "Instruction: <br>\n",
    "\n",
    "- Import numpy with the alias np.\n",
    "- Create two DataFrames: one that holds the rows of food_consumption for 'Belgium' and another that holds rows for 'USA'. Call these be_consumption and usa_consumption.\n",
    "- Calculate the mean and median of kilograms of food consumed per person per year for both countries.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>country</th>\n",
       "      <th>food_category</th>\n",
       "      <th>consumption</th>\n",
       "      <th>co2_emission</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Argentina</td>\n",
       "      <td>pork</td>\n",
       "      <td>10.51</td>\n",
       "      <td>37.20</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Argentina</td>\n",
       "      <td>poultry</td>\n",
       "      <td>38.66</td>\n",
       "      <td>41.53</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Argentina</td>\n",
       "      <td>beef</td>\n",
       "      <td>55.48</td>\n",
       "      <td>1712.00</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Argentina</td>\n",
       "      <td>lamb_goat</td>\n",
       "      <td>1.56</td>\n",
       "      <td>54.63</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Argentina</td>\n",
       "      <td>fish</td>\n",
       "      <td>4.36</td>\n",
       "      <td>6.96</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     country food_category  consumption  co2_emission\n",
       "1  Argentina          pork        10.51         37.20\n",
       "2  Argentina       poultry        38.66         41.53\n",
       "3  Argentina          beef        55.48       1712.00\n",
       "4  Argentina     lamb_goat         1.56         54.63\n",
       "5  Argentina          fish         4.36          6.96"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "food_consumption = pd.read_csv('./datasets/food_consumption.csv', index_col=0)\n",
    "display(food_consumption.head())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 4,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "42.13272727272727\n",
      "12.59\n",
      "44.650000000000006\n",
      "14.58\n"
     ]
    }
   ],
   "source": [
    "# Import numpy with alias np\n",
    "import numpy as np\n",
    "\n",
    "# Filter for Belgium\n",
    "be_consumption =food_consumption[food_consumption['country'] == 'Belgium'] \n",
    "\n",
    "# Filter for USA\n",
    "usa_consumption = food_consumption[food_consumption['country'] == 'USA'] \n",
    "\n",
    "# Calculate mean and median consumption in Belgium\n",
    "print(np.mean(be_consumption['consumption']))\n",
    "print(np.median(be_consumption['consumption']))\n",
    "\n",
    "# Calculate m)an and median consumption in USA\n",
    "print(np.mean(usa_consumption['consumption']))\n",
    "print(np.median(usa_consumption['consumption']))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Subset food_consumption for rows with data about Belgium and the USA.\n",
    "- Group the subsetted data by country and select only the consumption column.\n",
    "- Calculate the mean and median of the kilograms of food consumed per person per year in each country using .agg()."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 5,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "              mean  median\n",
      "country                   \n",
      "Belgium  42.132727   12.59\n",
      "USA      44.650000   14.58\n"
     ]
    }
   ],
   "source": [
    "# Import numpy as np\n",
    "import numpy as np\n",
    "\n",
    "# Subset for Belgium and USA only\n",
    "be_and_usa = food_consumption[(food_consumption['country'] == 'Belgium') | (food_consumption['country'] == 'USA')]\n",
    "\n",
    "# Group by country, select consumption column, and compute mean and median\n",
    "print(be_and_usa.groupby('country')['consumption'].agg([np.mean, np.median]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "When you want to compare summary statistics between groups, it's much easier to use .groupby() and .agg() instead of subsetting and calling the same functions multiple times."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Mean vs. median**\n",
    "\n",
    "In the video, you learned that the mean is the sum of all the data points divided by the total number of data points, and the median is the middle value of the dataset where 50% of the data is less than the median, and 50% of the data is greater than the median. In this exercise, you'll compare these two measures of center.\n",
    "\n",
    "pandas is loaded as pd, numpy is loaded as np, and food_consumption is available.\n",
    "\n",
    "Instructions: <br>\n",
    "\n",
    "- Import matplotlib.pyplot with the alias plt.\n",
    "- Subset food_consumption to get the rows where food_category is 'rice'.\n",
    "- Create a histogram of co2_emission for rice and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 8,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Import matplotlib.pyplot with alias plt\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Subset for food_category equals rice\n",
    "rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']\n",
    "\n",
    "# Histogram of co2_emission for rice and show plot\n",
    "rice_consumption.co2_emission.hist()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Use .agg() to calculate the mean and median of co2_emission for rice."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 9,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "        consumption  co2_emission\n",
      "mean      29.375154     37.591615\n",
      "median    11.875000     15.200000\n"
     ]
    }
   ],
   "source": [
    "# Subset for food_category equals rice\n",
    "rice_consumption = food_consumption[food_consumption['food_category'] == 'rice']\n",
    "\n",
    "# Calculate mean and median of co2_emission with .agg()\n",
    "print(rice_consumption.agg([np.mean, np.median]))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Given the skew of this data, what measure of central tendency best summarizes the kilograms of CO2 emissions per person per year for rice?\n",
    "\n",
    "> Answer: Median"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Measures of spread\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Quartiles, quantiles, and quintiles**\n",
    "\n",
    "Quantiles are a great way of summarizing numerical data since they can be used to measure center and spread, as well as to get a sense of where a data point stands in relation to the rest of the data set. For example, you might want to give a discount to the 10% most active users on a website.\n",
    "\n",
    "In this exercise, you'll calculate quartiles, quintiles, and deciles, which split up a dataset into 4, 5, and 10 pieces, respectively."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   0.        5.21     16.53     62.5975 1712.    ]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the quartiles of co2_emission\n",
    "print(np.quantile(food_consumption['co2_emission'],np.linspace(0, 1, 5)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[   0.       3.54    11.026   25.59    99.978 1712.   ]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the quintiles of co2_emission\n",
    "print(np.quantile(food_consumption['co2_emission'],np.linspace(0, 1, 6)))"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[0.00000000e+00 9.05555556e-01 4.19111111e+00 8.05333333e+00\n",
      " 1.32000000e+01 2.10944444e+01 3.58666667e+01 7.90622222e+01\n",
      " 1.86115556e+02 1.71200000e+03]\n"
     ]
    }
   ],
   "source": [
    "# Calculate the deciles of co2_emission\n",
    "print(np.quantile(food_consumption['co2_emission'],np.linspace(0, 1, 10)))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Those are some high-quality quantiles! While calculating more quantiles gives you a more detailed look at the data, it also produces more numbers, making the summary more difficult to quickly understand."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Variance and standard deviation**\n",
    "\n",
    "Variance and standard deviation are two of the most common ways to measure the spread of a variable, and you'll practice calculating these in this exercise. Spread is important since it can help inform expectations. For example, if a salesperson sells a mean of 20 products a day, but has a standard deviation of 10 products, there will probably be days where they sell 40 products, but also days where they only sell one or two. Information like this is important, especially when making predictions.\n",
    "\n",
    "Both pandas as pd and numpy as np are loaded, and food_consumption is available."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 24,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "                        var         std\n",
      "food_category                          \n",
      "beef           88748.408132  297.906710\n",
      "dairy          17671.891985  132.935669\n",
      "eggs              21.371819    4.622966\n",
      "fish             921.637349   30.358481\n",
      "lamb_goat      16475.518363  128.356996\n",
      "nuts              35.639652    5.969895\n",
      "pork            3094.963537   55.632396\n",
      "poultry          245.026801   15.653332\n",
      "rice            2281.376243   47.763754\n",
      "soybeans           0.879882    0.938020\n",
      "wheat             71.023937    8.427570\n"
     ]
    },
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAlYAAAHiCAYAAAAqFoLhAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjUuMywgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/NK7nSAAAACXBIWXMAAAsTAAALEwEAmpwYAAAgZUlEQVR4nO3dfZRkd10m8OdLEkUZIInAnBiQQQVWNCuYWURRd0YUgSDBdVUQNVHc6Flf1/gyLK4H11XjesSXg7suqywRkBFdkSxRgRMZFY8KCQIBAwY0QEJMBJPARFSC3/2j7mBlmO6u7v5Vd03y+ZxTp6tu3ar7VHX1r5/70reruwMAwPbdY7cDAADcVShWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVqy8qnpGVb16t3MAwEYUK1ZKVe2rqq6qU49N6+6XdPfjdzMXwKK2uzJYVV9cVe8YmYmdU04Qyiqpqn1J/jrJad19xy7HAU4yVfWwJD+d5AuTnJLkDUm+u7sVFXaELVYnsap6UFX9VlX9bVV9oKqeV1X3qKofrqp3V9XNVfWrVXXfaf5jW4MuqKr3VNX7q+rZc8/36Kq6sqo+WFU3VdVzp+kHqur645Z9XVV92XT9OVX1G1X14qr6UFVdXVUPq6pnTRneW1WPn3vskar6yap6fVXdVlWvqKozp7v/cPp6a1UdraovqKoLq+p1c4//wqp6w/TYN1TVFx733D9WVX88ZXl1Vd1v9HsPrKzTk1yW5OFJ9iZ5fZJX7GYg7l4Uq5NUVZ2S5JVJ3p1kX5KzkxxOcuF0OZjk05PsSfK84x7+RZkNOo9L8iNV9VnT9J9P8vPdfZ8kn5HkZZuI9JVJXpTkjCR/nuRVmX2+zk7yX5P8r+Pm/6Yk35LkU5PckeQXpulfMn09vbv3dPefHPe6z0xy+TT/pyR5bpLLq+pT5mb7+iTfnOQBST4hyfdv4nUAK2SzK5Dd/fru/pXu/rvu/kiSn03y8OPGiBMt5x5Vdaiq3jUt52XHVvjmVkq/eVpRvKWqvr2q/k1VvaWqbq2q580918dWBmvmZ6ect03zf85035Oq6i+mlcAbqur7p+l3Wpmtqs+aVhpvraq3VdVT5u57YVX9YlVdPj3Pn1XVZ4z7DrBZitXJ69GZlZIf6O7bu/sfuvt1SZ6R5Lnd/VfdfTTJs5I8reaOWUryo9394e5+c5I3J/ncafpHknxmVd2vu492959uIs8fdferpt13v5Hk/kkumQa2w0n2VdXpc/O/qLvf2t23J/kvSb52KosbOS/Jtd39ou6+o7tfmuTtmRW7Y/5Pd/9ld384s3L4yE28DmBFbHMF8pgvSfI33f2BDRb33UmemuTfZja23pLkF4+b5/OTPDTJ1yX5uSTPTvJlST47szHs357geR8/ZXhYZlvTvi7JsSy/kuTbuvveST4nye8f/+CqOi3J/0vy6sxWFr8ryUuq6uFzsz09yY9mtmL7ziQ/vsFrZYkUq5PXg5K8+wTHIX1qZoPQMe9Ocmpmm8SP+Zu563+f2aCUJM/M7If/7dMutidvIs9Nc9c/nOT93f3RuduZW06SvPe4jKclWWSX3fGv79jjz567vdbrA04u21mBTFU9MLNy9H0LLOvbkjy7u6/v7n9M8pwk//645/yxKcOrk9ye5KXdfXN335Dkj5I86gTP+5Ek907yrzI7rvma7r5x7r5HVNV9uvuW7n7jCR7/mMzGsEu6+5+6+/czK5tPn5vnt6YtdXckeUmsTO4qxerk9d4kn3b8QJLkfUkePHf70zLb1XZTNtDd13b30zNbK/qpJL9ZVffKbAD55GPzTWuR999e/DzouIwfSfL+JBv9NcXxr+/Y42/YZh5g9Wx5BbKq7p/ZVp7/MW3Z3siDk7x82t12a5Jrknw0d14pPX4F8vjbH7cSNxWh52VW8G6qqudX1X2mu786yZOSvLuq/qCqvuAEuT41yXu7+5+Pe71WJleUYnXyen2SG5NcUlX3qqp7VtVjk7w0yX+qqodU1Z4kP5Hk1xf5C7uq+oaquv/0A3zrNPmjSf4yyT2r6rxps/QPJ/nEbeb/hqp6RFV9cmbHYP3mtIXrb5P8c2ab90/kd5I8rKq+vqpOraqvS/KIzNbggLuWLa1AVtUZmZWqy7p70d1i703yxO4+fe5yz2lr1LZ09y9097mZ7TJ8WJIfmKa/obvPz2xl9rdz4uNa35fkQVU1//vayuQKU6xOUlMJ+cokn5nkPUmuz2zf/QsyO4j8DzM7bcE/ZLZPfhFPSPK2qjqa2YHsT5s2e9+W5D8m+eXMfphvn5a3HS9K8sLM1rTumdnxDenuv8/s+IA/ntYcHzP/oOk4iScnuTiz4xR+MMmTu/v928wDrJ5Nr0BOW4NeleSPu/vQJpb1S0l+vKoenMy2eFXV+dt9AdMB7p8/rZTentmY/NGq+oSane/qvtOxqB/MbEX2eH82Pe4Hq+q0qjqQ2dh/eLvZWJLudnHZ0UuSI0m+dbdzuLi4rP4ls60zv53ZitT7M/uL4Hsk+ZHMtjL9bZIXJzljmv+CzA4puD3J0bnLp22wnHtkdizWO5J8KMm7kvzEdN++6TlPnZv/+iQH5m6/OMkPT9cvTPK66frjkrxlyvD+zI6B2pPZXyz/XmYHyX8ws/NtfdH0mANJrp977s9O8gdJbkvyF0m+au6+Fyb5b3O37/RYl52/OEEoO66qjiR5cXf/8m5nAYCR7AoEABjEFisA7haq6neTfPEJ7vqJ7v6Jnc7DXZNiBQAwiF2BAACDHH9ukKW63/3u1/v27Vvz/ttvvz33ute9di7QJsm3faueUb7FXHXVVe/v7u2eJPYu62QY62TY/eXLsBrLXy/Dlsa6nfwTxHPPPbfX89rXvnbd+3ebfNu36hnlW0ySK3sF/qx5VS8nw1gnw+4vX4bVWP56GbYy1tkVCAAwiGIFADCIYgUAMIhiBQAwiGIFADCIYgUAMIhiBQAwiGIFADCIYgUAMIhiBQAwiGIFADCIYgUAMIhiBQAwiGIFADCIYgUAMMipi8xUVdcl+VCSjya5o7v3V9WZSX49yb4k1yX52u6+ZTkxAZbPWAds12a2WB3s7kd29/7p9qEkV3T3Q5NcMd0GONkZ64At286uwPOTXDpdvzTJU7edBmD1GOuAhS1arDrJq6vqqqq6aJq2t7tvTJLp6wOWERBgBxnrgG2p7t54pqpP7e73VdUDkrwmyXcluay7T5+b55buPuMEj70oyUVJsnfv3nMPHz685nKOHj2aPXv2JEmuvuG2zb2SBZ1z9n23/Nj5fKto1fMlq59RvsUcPHjwqrldZXcZd6exbhU+S7udYbeXL8NqLH+9DFsZ6xYqVnd6QNVzkhxN8h+SHOjuG6vqrCRHuvvh6z12//79feWVV655/5EjR3LgwIEkyb5Dl28q16Kuu+S8LT92Pt8qWvV8yepnlG8xVXWXLFbz7upj3Sp8lnY7w24vX4bVWP56GbYy1m24K7Cq7lVV9z52Pcnjk7w1yWVJLphmuyDJKzazYIBVYqwDRljkdAt7k7y8qo7N/2vd/XtV9YYkL6uqZyZ5T5KvWV5MgKUz1gHbtmGx6u6/SvK5J5j+gSSPW0YogJ1mrANGcOZ1AIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEWLlZVdUpV/XlVvXK6fWZVvaaqrp2+nrG8mAA7w1gHbMdmtlh9T5Jr5m4fSnJFdz80yRXTbYCTnbEO2LKFilVVPTDJeUl+eW7y+Ukuna5fmuSpQ5MB7DBjHbBd1d0bz1T1m0l+Msm9k3x/dz+5qm7t7tPn5rmluz9uE3lVXZTkoiTZu3fvuYcPH15zOUePHs2ePXuSJFffcNvmXsmCzjn7vlt+7Hy+VbTq+ZLVzyjfYg4ePHhVd+/f7Ryj3Z3GulX4LO12ht1evgyrsfz1MmxlrDt1oxmq6slJbu7uq6rqwGaePEm6+/lJnp8k+/fv7wMH1n6KI0eO5Nj9Fx66fLOLWsh1z1h7+RuZz7eKVj1fsvoZ5bv7uruNdavwWdrtDLu9fBlWY/mjM2xYrJI8NslTqupJSe6Z5D5V9eIkN1XVWd19Y1WdleTmIYkAdoexDti2DY+x6u5ndfcDu3tfkqcl+f3u/oYklyW5YJrtgiSvWFpKgCUz1gEjbOc8Vpck+fKqujbJl0+3Ae5qjHXAwhbZFfgx3X0kyZHp+geSPG58JIDdZawDtsqZ1wEABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAGUawAAAZRrAAABlGsAAAG2bBYVdU9q+r1VfXmqnpbVf3oNP3MqnpNVV07fT1j+XEBlsNYB4ywyBarf0zypd39uUkemeQJVfWYJIeSXNHdD01yxXQb4GRlrAO2bcNi1TNHp5unTZdOcn6SS6fplyZ56jICAuwEYx0wQnX3xjNVnZLkqiSfmeQXu/uHqurW7j59bp5buvvjNpFX1UVJLkqSvXv3nnv48OE1l3P06NHs2bMnSXL1Dbdt7pUs6Jyz77vlx87nW0Wrni9Z/YzyLebgwYNXdff+3c4x2t1prFuFz9JuZ9jt5cuwGstfL8NWxrqFitXHZq46PcnLk3xXktctMtjM279/f1955ZVr3n/kyJEcOHAgSbLv0OUL59qM6y45b8uPnc+3ilY9X7L6GeVbTFXdJYvVMXeHsW4VPku7nWG3ly/Daix/vQxbGes29VeB3X1rkiNJnpDkpqo6a1rwWUlu3sxzAawqYx2wVYv8VeD9p7W3VNUnJfmyJG9PclmSC6bZLkjyiiVlBFg6Yx0wwqkLzHNWkkunYw/ukeRl3f3KqvqTJC+rqmcmeU+Sr1liToBlM9YB27ZhserutyR51AmmfyDJ45YRCmCnGeuAEZx5HQBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYBDFCgBgEMUKAGAQxQoAYJBTdzvATtt36PItP/bic+7IhWs8/rpLztvy8wKMttFYt954th5jHazPFisAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQU7d7QB3FfsOXb6U573ukvOW8rwAWzFyrLv4nDty4dzzGe+4K7DFCgBgEMUKAGAQxQoAYJANi1VVPaiqXltV11TV26rqe6bpZ1bVa6rq2unrGcuPC7AcxjpghEW2WN2R5OLu/qwkj0nyHVX1iCSHklzR3Q9NcsV0G+BkZawDtm3DYtXdN3b3G6frH0pyTZKzk5yf5NJptkuTPHVJGQGWzlgHjLCpY6yqal+SRyX5syR7u/vGZDYgJXnA8HQAu8BYB2xVdfdiM1btSfIHSX68u3+rqm7t7tPn7r+luz/u2IOquijJRUmyd+/ecw8fPrzmMo4ePZo9e/YkSa6+4bZNvIydsfeTkps+vLPLPOfs+y487/z7t6pWPaN8izl48OBV3b1/t3Msw91lrNuN8WyjDJsZ70ZYhZ8nGXZ/+etl2MpYt1CxqqrTkrwyyau6+7nTtHckOdDdN1bVWUmOdPfD13ue/fv395VXXrnm/UeOHMmBAweSLO+Em9tx8Tl35Geu3tlzqm7mhHnz79+qWvWM8i2mqu6SxeruNNbtxni2UYadPkHoKvw8ybD7y18vw1bGukX+KrCS/EqSa44NNJPLklwwXb8gySs2s2CAVWKsA0ZYZHXlsUm+McnVVfWmadp/TnJJkpdV1TOTvCfJ1ywlIcDOMNYB27Zhseru1yWpNe5+3Ng4ALvDWAeM4MzrAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIOcutsBWN++Q5cvPO/F59yRCxec/7pLzttqJICl2Mx4txnGO3aSLVYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAg2xYrKrqBVV1c1W9dW7amVX1mqq6dvp6xnJjAiyf8Q7YrkW2WL0wyROOm3YoyRXd/dAkV0y3AU52L4zxDtiGDYtVd/9hkr87bvL5SS6drl+a5KljYwHsPOMdsF1bPcZqb3ffmCTT1weMiwSwUox3wMKquzeeqWpfkld29+dMt2/t7tPn7r+lu0943EFVXZTkoiTZu3fvuYcPH15zOUePHs2ePXuSJFffcNvCL2Kn7P2k5KYP73aKtW0m3zln33e5YdYw/z1eRfIt5uDBg1d19/7dzrEMWx3vTraxbhXGs53KsNZ4two/TzLs/vLXy7CVse7ULWa4qarO6u4bq+qsJDevNWN3Pz/J85Nk//79feDAgTWf9MiRIzl2/4WHLt9itOW5+Jw78jNXb/UtW77N5LvuGQeWG2YN89/jVSQfJ7DQeHeyjXWrMJ7tVIa1xrtV+HmSYfeXPzrDVncFXpbkgun6BUleMSQNwOox3gELW+R0Cy9N8idJHl5V11fVM5NckuTLq+raJF8+3QY4qRnvgO3acBtsdz99jbseNzgLwK4y3gHb5czrAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIOcutsBuGvZd+jyde+/+Jw7cuEG85zIdZect9VIAEux0Xi3iBONica7k5stVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgziP1d3UiPOvAJwM1hrvtnpePViPLVYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAgyhWAACDKFYAAIMoVgAAg5y62wFgEfsOXb6U573ukvOW8rwAW2W8O7nZYgUAMIhiBQAwiGIFADCIYgUAMIhiBQAwiGIFADCIYgUAMIhiBQAwiBOEcrd2/In4Lj7njlw44OR8yzoR39U33DYk34k4eSDcta114tHtjnvLGjtO1hOl2mIFADCIYgUAMIhiBQAwyLaKVVU9oareUVXvrKpDo0IBrBrjHbCILRerqjolyS8meWKSRyR5elU9YlQwgFVhvAMWtZ0tVo9O8s7u/qvu/qckh5OcPyYWwEox3gEL2U6xOjvJe+duXz9NA7irMd4BC6nu3toDq74myVd097dOt78xyaO7+7uOm++iJBdNNx+e5B3rPO39krx/S4F2hnzbt+oZ5VvMg7v7/rsdYqcsMt6dhGOdDLu/fBlWY/nrZdj0WLedE4Ren+RBc7cfmOR9x8/U3c9P8vxFnrCqruzu/dvItFTybd+qZ5SPNWw43p1sY50Mu798GVZj+aMzbGdX4BuSPLSqHlJVn5DkaUkuGxEKYMUY74CFbHmLVXffUVXfmeRVSU5J8oLuftuwZAArwngHLGpb/yuwu38nye8MypIsuBl9F8m3faueUT5OaPB4twrfRxl2f/mJDKuw/GRghi0fvA4AwJ35lzYAAIOsRLFaxX8VUVUvqKqbq+qtc9POrKrXVNW109czdjHfg6rqtVV1TVW9raq+Z5UyVtU9q+r1VfXmKd+PrlK+uZynVNWfV9UrVzTfdVV1dVW9qaquXMWMbM5OjHfrjA/Pqaobps/Tm6rqSXOPedaU6R1V9RWDcmzq8zsyQ1U9fO51vqmqPlhV37vs92CzvzvWWmZVnTu9d++sql+oqtpmhp+uqrdX1Vuq6uVVdfo0fV9VfXju/filJWbY9Hu/1QxrLP/X55Z9XVW9aSnvQXfv6iWzA0HfleTTk3xCkjcnecQK5PqSJJ+X5K1z0/57kkPT9UNJfmoX852V5POm6/dO8peZ/auNlciYpJLsma6fluTPkjxmVfLN5fy+JL+W5JWr9j2eMlyX5H7HTVupjC6b+n7uyHi3zvjwnCTff4L5HzFl+cQkD5kynjIgx8Kf32VlmHvf/ybJg5f9Hmzmd8d6y0zy+iRfMI2lv5vkidvM8Pgkp07Xf2ouw775+Y57ntEZNv3ebzXDiZZ/3P0/k+RHlvEerMIWq5X8VxHd/YdJ/u64yecnuXS6fmmSp+5kpnndfWN3v3G6/qEk12R2JuiVyNgzR6ebp02XzorkS5KqemCS85L88tzklcm3jpMhIye2I+PdOuPDWs5Pcri7/7G7/zrJO6esy7DW53eZGR6X5F3d/e4Ncm17+Zv83XHCZVbVWUnu091/0rPf7r+aTfycnyhDd7+6u++Ybv5pZudiW9MyMqxj+Puw3vKnrU5fm+Sl6z3HVpe/CsXqZPpXEXu7+8ZkNnAlecAu50ky24yZ5FGZbRVamYw12832piQ3J3lNd69UviQ/l+QHk/zz3LRVypfMyuirq+qqmp3ZO1m9jCxux8e748aHJPnOaXfQC+Z2SS0r12Y+v8t8b56WO/8S3cn3INn8az57ur6MLEnyLZltfTnmITU7JOIPquqL57ItI8Nm3vtlZfjiJDd197Vz04a9B6tQrE60v9KfKi6oqvYk+b9Jvre7P7jbeeZ190e7+5GZrRk9uqo+Z5cjfUxVPTnJzd191W5n2cBju/vzkjwxyXdU1ZfsdiC2ZUfHuxOMD/8zyWckeWSSGzPbHbLMXJv5/C4lQ81O6PqUJL8xTdrp92DdeGssc2lZqurZSe5I8pJp0o1JPq27H5Xp0Iiqus+SMmz2vV/W+/D03LloD30PVqFYLfSvcVbETdOmwWObCG/ezTBVdVpmg+ZLuvu3pskrlTFJuvvWJEeSPCGrk++xSZ5SVddltjvmS6vqxSuUL0nS3e+bvt6c5OWZ7ZpYqYxsyo6NdycaH7r7pmmF55+T/O/8y66upeTa5Od3We/NE5O8sbtvmrLs6Hsw2exrvj533lU3JEtVXZDkyUmeMe3ayrT77QPT9asyO77pYcvIsIX3fniGqjo1yb9L8utzuYa+B6tQrE6mfxVxWZILpusXJHnFbgWZ9hH/SpJruvu5c3etRMaquv/cX518UpIvS/L2VcnX3c/q7gd2977MPnO/393fsCr5kqSq7lVV9z52PbODT9+aFcrIpu3IeLfW+HDsl/vkqzL7PGXK8LSq+sSqekiSh2Z20O52Mmz28zs8w+ROWyd28j2Ys6nXPO0u/FBVPWb6Xn5TtvlzXlVPSPJDSZ7S3X8/N/3+VXXKdP3Tpwx/taQMm3rvl5Eh0++i7v7YLr7h78FGR7fvxCXJkzL7q5V3JXn2bueZMr00s82DH8mstT4zyackuSLJtdPXM3cx3xdltknyLUneNF2etCoZk/zrJH8+5Xtr/uWvL1Yi33FZD+Rf/ipwZfJl9pdjb54ubzv2s7FKGV229H1d+ni3zvjwoiRXT9MvS3LW3GOePWV6Rzbx11/rZNj053cJGT45yQeS3Hdu2lLfg83+7lhrmUn2T2Pnu5I8L9MJvbeR4Z2ZHcd07PPwS9O8Xz19f96c5I1JvnKJGTb93m81w4mWP01/YZJvP27eoe+BM68DAAyyCrsCAQDuEhQrAIBBFCsAgEEUKwCAQRQrAIBBFCsAgEEUKwCAQRQrAIBB/j96sN9trBN3oAAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 720x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    },
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x576 with 2 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Print variance and sd of co2_emission for each food_category\n",
    "print(food_consumption.groupby('food_category')['co2_emission'].agg([np.var, np.std]))\n",
    "\n",
    "# Import matplotlib.pyplot with alias plt\n",
    "import matplotlib.pyplot as plt\n",
    "\n",
    "# Create histogram of co2_emission for food_category 'beef'\n",
    "food_consumption[food_consumption['food_category']=='beef'].hist()\n",
    "# Show plot\n",
    "plt.show()\n",
    "\n",
    "# Create histogram of co2_emission for food_category 'eggs'\n",
    "food_consumption[food_consumption['food_category']=='eggs'].hist()\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Beef has the largest amount of variation in its CO2 emissions, while eggs have a relatively small amount of variation."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Finding outliers using IQR**\n",
    "\n",
    "Outliers can have big effects on statistics like mean, as well as statistics that rely on the mean, such as variance and standard deviation. Interquartile range, or IQR, is another way of measuring spread that's less influenced by outliers. IQR is also often used to find outliers. If a value is less than $Q1−1.5×IQR$ or greater than $Q3+1.5×IQR$, it's considered an outlier. <br>\n",
    "\n",
    "![iqr](images/iqr.png)\n",
    "\n",
    "<br>\n",
    "\n",
    "In this exercise, you'll calculate IQR and use it to find some outliers."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 28,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "country\n",
      "Albania      1777.85\n",
      "Algeria       707.88\n",
      "Angola        412.99\n",
      "Argentina    2172.40\n",
      "Armenia      1109.93\n",
      "              ...   \n",
      "Uruguay      1634.91\n",
      "Venezuela    1104.10\n",
      "Vietnam       641.51\n",
      "Zambia        225.30\n",
      "Zimbabwe      350.33\n",
      "Name: co2_emission, Length: 130, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate total co2_emission per country: emissions_by_country\n",
    "emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()\n",
    "\n",
    "print(emissions_by_country)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/plain": [
       "country\n",
       "Mozambique      141.40\n",
       "Rwanda          181.63\n",
       "Togo            188.09\n",
       "Liberia         203.38\n",
       "Malawi          207.94\n",
       "                ...   \n",
       "Iceland        1731.36\n",
       "New Zealand    1750.95\n",
       "Albania        1777.85\n",
       "Australia      1938.66\n",
       "Argentina      2172.40\n",
       "Name: co2_emission, Length: 130, dtype: float64"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "display(emissions_by_country.sort_values())"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "country\n",
      "Argentina    2172.4\n",
      "Name: co2_emission, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Calculate total co2_emission per country: emissions_by_country\n",
    "emissions_by_country = food_consumption.groupby('country')['co2_emission'].sum()\n",
    "\n",
    "# Compute the first and third quantiles and IQR of emissions_by_country\n",
    "q1 = np.quantile(emissions_by_country, 0.25)\n",
    "q3 = np.quantile(emissions_by_country, 0.75)\n",
    "iqr = q3 - q1\n",
    "\n",
    "# Calculate the lower and upper cutoffs for outliers\n",
    "lower = q1 - 1.5 * iqr\n",
    "upper = q3 + 1.5 * iqr\n",
    "\n",
    "# Subset emissions_by_country to find outliers\n",
    "outliers = emissions_by_country[(emissions_by_country > upper) | (emissions_by_country < lower)]\n",
    "print(outliers)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Outstanding outlier detection! It looks like Argentina has a substantially higher amount of CO2 emissions per person than other countries in the world."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Random Numbers and Probability\n",
    "\n",
    "> In this chapter, you'll learn how to generate random samples and measure chance using probability. You'll work with real-world sales data to calculate the probability of a salesperson being successful. Finally, you’ll use the binomial distribution to model events with binary outcomes."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### What are the chances?\n",
    "\n",
    "- Measuring chance\n",
    "\n",
    "What's the probability of an event?\n",
    "$$ P(\\text{event}) = \\frac{\\text{\\# ways event can happen}}{\\text{total \\# of possible outcomes}} $$"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **With or without replacement?**\n",
    "\n",
    "For each scenario, decide whether it's sampling with replacement or sampling without replacement.\n",
    "\n",
    "![](./images/with_without_replacement.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Correctly identifying the type of sampling that needs to be used is key to calculating accurate probabilities. With replacement, everyone always has a 5% chance of working on the weekend. Without replacement, the second pick has a 4/19 chance, and the third pick has a 3/18 chance of working on the weekend."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Calculating probabilities**\n",
    "\n",
    "You're in charge of the sales team, and it's time for performance reviews, starting with Amir. As part of the review, you want to randomly select a few of the deals that he's worked on over the past year so that you can look at them more deeply. Before you start selecting deals, you'll first figure out what the chances are of selecting certain deals.\n",
    "\n",
    "Recall that the probability of an event can be calculated by\n",
    "\n",
    "$$ P(\\text{event}) = \\frac{\\text{\\# ways event can happen}}{\\text{total \\# of possible outcomes}} $$"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>product</th>\n",
       "      <th>client</th>\n",
       "      <th>status</th>\n",
       "      <th>amount</th>\n",
       "      <th>num_users</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>Product F</td>\n",
       "      <td>Current</td>\n",
       "      <td>Won</td>\n",
       "      <td>7389.52</td>\n",
       "      <td>19</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>Product C</td>\n",
       "      <td>New</td>\n",
       "      <td>Won</td>\n",
       "      <td>4493.01</td>\n",
       "      <td>43</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>Product B</td>\n",
       "      <td>New</td>\n",
       "      <td>Won</td>\n",
       "      <td>5738.09</td>\n",
       "      <td>87</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>Product I</td>\n",
       "      <td>Current</td>\n",
       "      <td>Won</td>\n",
       "      <td>2591.24</td>\n",
       "      <td>83</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>5</th>\n",
       "      <td>Product E</td>\n",
       "      <td>Current</td>\n",
       "      <td>Won</td>\n",
       "      <td>6622.97</td>\n",
       "      <td>17</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "     product   client status   amount  num_users\n",
       "1  Product F  Current    Won  7389.52         19\n",
       "2  Product C      New    Won  4493.01         43\n",
       "3  Product B      New    Won  5738.09         87\n",
       "4  Product I  Current    Won  2591.24         83\n",
       "5  Product E  Current    Won  6622.97         17"
      ]
     },
     "execution_count": 37,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "amir_deals = pd.read_csv('./datasets/amir_deals.csv', index_col=0)\n",
    "amir_deals.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 40,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product B    62\n",
      "Product D    40\n",
      "Product A    23\n",
      "Product C    15\n",
      "Product F    11\n",
      "Product H     8\n",
      "Product I     7\n",
      "Product E     5\n",
      "Product N     3\n",
      "Product G     2\n",
      "Product J     2\n",
      "Name: product, dtype: int64\n"
     ]
    }
   ],
   "source": [
    "# Count the deals for each product\n",
    "counts = amir_deals['product'].value_counts()\n",
    "print(counts)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 41,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Product B    0.348315\n",
      "Product D    0.224719\n",
      "Product A    0.129213\n",
      "Product C    0.084270\n",
      "Product F    0.061798\n",
      "Product H    0.044944\n",
      "Product I    0.039326\n",
      "Product E    0.028090\n",
      "Product N    0.016854\n",
      "Product G    0.011236\n",
      "Product J    0.011236\n",
      "Name: product, dtype: float64\n"
     ]
    }
   ],
   "source": [
    "# Count the deals for each product\n",
    "counts = amir_deals['product'].value_counts()\n",
    "\n",
    "# Calculate probability of picking a deal with each product\n",
    "probs = counts / len(amir_deals['product'])\n",
    "print(probs)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "If you randomly select one of Amir's deals, what's the probability that the deal will involve Product C?\n",
    "\n",
    "> Ans: 8.43%"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Sampling deals**\n",
    "\n",
    "In the previous exercise, you counted the deals Amir worked on. Now it's time to randomly pick five deals so that you can reach out to each customer and ask if they were satisfied with the service they received. You'll try doing this both with and without replacement.\n",
    "\n",
    "Additionally, you want to make sure this is done randomly and that it can be reproduced in case you get asked how you chose the deals, so you'll need to set the random seed before sampling from the deals.\n",
    "\n",
    "Instructions: <br>\n",
    "\n",
    "- Set the random seed to 24.\n",
    "- Take a sample of 5 deals without replacement and store them as sample_without_replacement."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 38,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       product   client status   amount  num_users\n",
      "128  Product B  Current    Won  2070.25          7\n",
      "149  Product D  Current    Won  3485.48         52\n",
      "78   Product B  Current    Won  6252.30         27\n",
      "105  Product D  Current    Won  4110.98         39\n",
      "167  Product C      New   Lost  3779.86         11\n"
     ]
    }
   ],
   "source": [
    "# Set random seed\n",
    "np.random.seed(24)\n",
    "\n",
    "# Sample 5 deals without replacement\n",
    "sample_without_replacement = amir_deals.sample(5, replace=False)\n",
    "print(sample_without_replacement)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Take a sample of 5 deals with replacement and save as sample_with_replacement."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "       product   client status   amount  num_users\n",
      "163  Product D  Current    Won  6755.66         59\n",
      "132  Product B  Current    Won  6872.29         25\n",
      "88   Product C  Current    Won  3579.63          3\n",
      "146  Product A  Current    Won  4682.94         63\n",
      "146  Product A  Current    Won  4682.94         63\n"
     ]
    }
   ],
   "source": [
    "# Set random seed\n",
    "np.random.seed(24)\n",
    "\n",
    "# Sample 5 deals with replacement\n",
    "sample_with_replacement = amir_deals.sample(5, replace=True)\n",
    "print(sample_with_replacement)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "What type of sampling is better to use for this situation?\n",
    "\n",
    "> Answers: Without replacement"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "It's important to consider how you'll take a sample since there's no one-size-fits-all way to sample, and this can have an effect on your results."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Discrete distributions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Creating a probability distribution**\n",
    "\n",
    "A new restaurant opened a few months ago, and the restaurant's management wants to optimize its seating space based on the size of the groups that come most often. On one night, there are 10 groups of people waiting to be seated at the restaurant, but instead of being called in the order they arrived, they will be called randomly. In this exercise, you'll investigate the probability of groups of different sizes getting picked first. Data on each of the ten groups is contained in the restaurant_groups DataFrame.\n",
    "\n",
    "Remember that expected value can be calculated by multiplying each possible outcome with its corresponding probability and taking the sum. The restaurant_groups data is available. pandas is loaded as pd, numpy is loaded as np, and matplotlib.pyplot is loaded as plt.\n",
    "\n",
    "Instructions: <br>\n",
    "\n",
    "- Create a histogram of the group_size column of restaurant_groups, setting bins to [2, 3, 4, 5, 6]. Remember to show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "text/html": [
       "<div>\n",
       "<style scoped>\n",
       "    .dataframe tbody tr th:only-of-type {\n",
       "        vertical-align: middle;\n",
       "    }\n",
       "\n",
       "    .dataframe tbody tr th {\n",
       "        vertical-align: top;\n",
       "    }\n",
       "\n",
       "    .dataframe thead th {\n",
       "        text-align: right;\n",
       "    }\n",
       "</style>\n",
       "<table border=\"1\" class=\"dataframe\">\n",
       "  <thead>\n",
       "    <tr style=\"text-align: right;\">\n",
       "      <th></th>\n",
       "      <th>group_id</th>\n",
       "      <th>group_size</th>\n",
       "    </tr>\n",
       "  </thead>\n",
       "  <tbody>\n",
       "    <tr>\n",
       "      <th>0</th>\n",
       "      <td>A</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>1</th>\n",
       "      <td>B</td>\n",
       "      <td>4</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>2</th>\n",
       "      <td>C</td>\n",
       "      <td>6</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>3</th>\n",
       "      <td>D</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "    <tr>\n",
       "      <th>4</th>\n",
       "      <td>E</td>\n",
       "      <td>2</td>\n",
       "    </tr>\n",
       "  </tbody>\n",
       "</table>\n",
       "</div>"
      ],
      "text/plain": [
       "  group_id  group_size\n",
       "0        A           2\n",
       "1        B           4\n",
       "2        C           6\n",
       "3        D           2\n",
       "4        E           2"
      ]
     },
     "execution_count": 43,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "restaurant_groups = pd.read_csv('./datasets/restaurant_groups.csv')\n",
    "restaurant_groups.head()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 44,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 720x576 with 1 Axes>"
      ]
     },
     "metadata": {
      "needs_background": "light"
     },
     "output_type": "display_data"
    }
   ],
   "source": [
    "restaurant_groups['group_size'].hist(bins=[2, 3, 4, 5, 6])\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Count the number of each group_size in restaurant_groups, then divide by the number of rows in restaurant_groups to calculate the probability of randomly selecting a group of each size. Save as size_dist.\n",
    "- Reset the index of size_dist.\n",
    "- Rename the columns of size_dist to group_size and prob.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "   group_size  prob\n",
      "0           0   0.2\n",
      "1           1   0.4\n",
      "2           2   0.6\n",
      "3           3   0.2\n",
      "4           4   0.2\n",
      "5           5   0.2\n",
      "6           6   0.3\n",
      "7           7   0.2\n",
      "8           8   0.4\n",
      "9           9   0.2\n"
     ]
    }
   ],
   "source": [
    "size_dist = restaurant_groups['group_size'] / restaurant_groups.shape[0]\n",
    "\n",
    "# Reset index and rename columns\n",
    "size_dist = size_dist.reset_index()\n",
    "size_dist.columns = ['group_size', 'prob']\n",
    "\n",
    "print(size_dist)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "- Calculate the expected value of the size_distribution, which represents the expected group size, by multiplying the group_size by the prob and taking the sum.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "12.200000000000001\n"
     ]
    }
   ],
   "source": [
    "# Calculate expected value\n",
    "expected_value = (size_dist['group_size'] * size_dist['prob']).sum()\n",
    "print(expected_value)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "\n",
    "- Calculate the probability of randomly picking a group of 4 or more people by subsetting for groups of size 4 or more and summing the probabilities of selecting those groups."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.30000000000000004\n"
     ]
    }
   ],
   "source": [
    "# Create probability distribution\n",
    "size_dist = restaurant_groups['group_size'].value_counts() / restaurant_groups.shape[0]\n",
    "# Reset index and rename columns\n",
    "size_dist = size_dist.reset_index()\n",
    "size_dist.columns = ['group_size', 'prob']\n",
    "\n",
    "# Expected value\n",
    "expected_value = np.sum(size_dist['group_size'] * size_dist['prob'])\n",
    "\n",
    "# Subset groups of size 4 or more\n",
    "groups_4_or_more = size_dist[size_dist['group_size'] >= 4]\n",
    "\n",
    "# Sum the probabilities of groups_4_or_more\n",
    "prob_4_or_more = groups_4_or_more['prob'].sum()\n",
    "print(prob_4_or_more)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Identifying distributions**\n",
    "\n",
    "\n",
    "Which sample is most likely to have been taken from a uniform distribution?\n",
    "\n",
    "![](./images/distributions.png)\n",
    "\n",
    "<br>\n",
    "- A: bell-shaped distribution, \n",
    "- B: relatively flat distribution, \n",
    "- C: lots of lower values, fewer high values\n",
    "\n",
    "**Ans: B** <br>\n",
    "\n",
    "\n",
    "Since the histogram depicts a sample and not the actual probability distribution, each outcome won't happen the exact same number of times due to randomness, but they're similar in number.\n",
    "\n",
    "\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Expected value vs. sample mean**\n",
    "\n",
    "The app to the right will take a sample from a discrete uniform distribution, which includes the numbers 1 through 9, and calculate the sample's mean. You can adjust the size of the sample using the slider. Note that the expected value of this distribution is 5.\n",
    "\n",
    "A sample is taken, and you win twenty dollars if the sample's mean is less than 4. There's a catch: you get to pick the sample's size.\n",
    "\n",
    "Which sample size is most likely to win you the twenty dollars?\n",
    "\n",
    "- **10**\n",
    "- 100\n",
    "- 1000\n",
    "- 5000\n",
    "- 10000\n",
    "\n",
    "Ans: **10**. Since the sample mean will likely be closer to 5 (the expected value) with larger sample sizes, you have a better chance of getting a sample mean further away from 5 with a smaller sample."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Continuous distributions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Which distribution?**\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Data back-ups**\n",
    "\n",
    "The sales software used at your company is set to automatically back itself up, but no one knows exactly what time the back-ups happen. It is known, however, that back-ups happen exactly every 30 minutes. Amir comes back from sales meetings at random times to update the data on the client he just met with. He wants to know how long he'll have to wait for his newly-entered data to get backed up. Use your new knowledge of continuous uniform distributions to model this situation and answer Amir's questions.\n",
    "\n",
    "Instructions: <br>\n",
    "\n",
    "1. To model how long Amir will wait for a back-up using a continuous uniform distribution, save his lowest possible wait time as min_time and his longest possible wait time as max_time. Remember that back-ups happen every 30 minutes.\n",
    "2. Import uniform from scipy.stats and calculate the probability that Amir has to wait less than 5 minutes, and store in a variable called prob_less_than_5.\n",
    "3. Calculate the probability that Amir has to wait more than 5 minutes, and store in a variable called prob_greater_than_5.\n",
    "4. Calculate the probability that Amir has to wait between 10 and 20 minutes, and store in a variable called prob_between_10_and_20.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 1,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.16666666666666666\n",
      "0.8333333333333334\n",
      "0.3333333333333333\n"
     ]
    }
   ],
   "source": [
    "# Min and max wait times for back-up that happens every 30 min\n",
    "min_time = 0\n",
    "max_time = 30\n",
    "\n",
    "# Import uniform from scipy.stats\n",
    "from scipy.stats import uniform\n",
    "\n",
    "# Calculate probability of waiting less than 5 mins\n",
    "prob_less_than_5 = uniform.cdf(5, 0, 30)\n",
    "print(prob_less_than_5)\n",
    "\n",
    "# Calculate probability of waiting more than 5 mins\n",
    "prob_greater_than_5 = 1 - uniform.cdf(5, 0, 30)\n",
    "print(prob_greater_than_5)\n",
    "\n",
    "# Calculate probability of waiting 10-20 mins\n",
    "prob_between_10_and_20 = uniform.cdf(20, 0, 30) - uniform.cdf(10, 0, 30)\n",
    "print(prob_between_10_and_20)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Simulating wait times**\n",
    "\n",
    "To give Amir a better idea of how long he'll have to wait, you'll simulate Amir waiting 1000 times and create a histogram to show him what he should expect. Recall from the last exercise that his minimum wait time is 0 minutes and his maximum wait time is 30 minutes."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAu8AAAGqCAYAAAC7/qoTAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/av/WaAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAtx0lEQVR4nO3de3RU5b3/8U+GIWQIhCSaqq32qORi5SIhQAi3SjTECgHKRVxFCljBAp4KR0DUoC4xJBaUiyxQLjEHQbFEkEaQiyJqlWBQDyinESKnQKVFQkjMlVxmfn+wmB8jIBncMPNM3q+1XHGe2bOf7/Own+QzOzt7glwul0sAAAAA/J7N1wUAAAAAaBzCOwAAAGAIwjsAAABgCMI7AAAAYAjCOwAAAGAIwjsAAABgCMI7AAAAYAjCOwAAAGAIu68L8Mbx4+WW7s9mC1JkZKhKSirldPJZVT8Fc2kt5tM6zKV1mEvrMJfWuZxzGRXV2tL9AVZo0mfebbYgBQUFyWYL8nUpxmMurcV8Woe5tA5zaR3m0jrMJZqaJh3eAQAAAJMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAENccngvKSlRSkqKdu3a5W7bsmWLBg0apM6dOys5OVmLFi2S0+l0P79+/XqlpKSoU6dOGjJkiL744oufVj0AAADQhFxSeP/ss880YsQIHT582N321Vdfafr06Zo8ebJ2796tZcuWad26dcrJyZEk7dq1S7NmzVJWVpYKCgo0cOBATZgwQdXV1ZYMBAAAAAh0dm9fsH79ei1cuFDTpk3TlClT3O3ffvut7r33XvXt21eS1LZtW6WkpKigoED333+/1q5dq/79+yshIUGSNGbMGL3xxhvatGmThg4d2qi+bTZrP0GtWTObx1dcOubSWsyndZhL6zCX1mEurcNcoqnxOrz36tVLaWlpstvtHuE9NTVVqamp7sc1NTXasWOH0tLSJElFRUXnhPTo6GgVFhY2uu/IyFAFBVn/8cdhYQ7L99lUMZfWYj6tw1xah7m0DnNpHeYSTYXX4T0qKuqi21RUVOjhhx9WSEiIxowZI0mqrKyUw+G5sEJCQlRVVdXovktKKi0/8x4W5tD331erocF58RfggphLazGf1mEurcNcWoe5tM7lnMuIiFBL9wdYwevwfjEHDx7Un/70J1111VVauXKlWrVqJUlyOByqqanx2LampkYRERGN3rfT6ZLT6bK0XklqaHCqvp5vnlZgLq3FfFqHubQOc2kd5tI6zCWaCksvEPvggw80fPhw9e7dWytWrFCbNm3cz8XExOjAgQMe2xcVFSkmJsbKEgAAAICAZVl4/5//+R9NmjRJjz32mB599FHZ7Z4n9YcNG6a8vDzl5+errq5OOTk5OnHihFJSUqwqAQAAAAholl0289JLL6m+vl4ZGRnKyMhwtyckJGj58uVKSkrSU089paefflrHjh1TdHS0li1bpvDwcKtKAAAAAAJakMvlsv4i8svk+PFyS/dnt9sUERGqkycruU7uJ2IurcV8Woe5tA5zaR3m0jqXcy6jolpbuj/ACpb/wSp87/6s7b4uwWvZM5J9XQIAAIDf4xMNAAAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABDEN4BAAAAQxDeAQAAAEMQ3gEAAABD2H1dAHAh92dt93UJXsuekezrEgAAQADjzDsAAABgCMI7AAAAYAjCOwAAAGAIwjsAAABgCMI7AAAAYAjCOwAAAGAIwjsAAAAsl5mZqVGjRv3oNhUVFerbt69mzJhx0f2VlJQoPT1dvXv3VpcuXTRmzBj97//+7wW3/+qrr9SuXTv985//9Lr2xvjnP/+puLg4rVu37rLs/0II7wAAALDU0qVLlZOTc9HtMjMzdfTo0Ytu53K59NBDD+ndd9/Vww8/rBdeeEENDQ267777dOTIkXO2Lyws1IMPPqj6+vpLKb9Rfvazn+mNN97Q7bffftn6OB/COwAAACxx5MgRTZo0SfPnz1fr1q1/dNsPPvhA77zzzkW3k6R//OMf+uyzz/TII49o2LBh6tOnjxYvXqza2lpt2LDBvV1tba2ys7M1YsSIyxrcJSk4OFidOnVSZGTkZe3nhwjvAAAAXqqpqdHzzz+vfv36qX379urcubPGjh2rv//975KkvLw8xcXFqbCw0ON1H3zwgeLi4rR3715JUmlpqZ588kn16NFDHTp00D333KOdO3d6vCYuLk6LFi3S0KFDlZCQoMWLF0uSCgoK9Ic//EFdu3ZV+/btlZycrBdffFFOp9P92u+++05TpkxRt27d1LVrVz355JOaN2+ekpM9PxF87dq16t+/v9q3b6/bb79dL774okf43bVrV6MuEcnMzNThw4f13//93/rVr351we3KysqUnp6uadOmKSws7Ef3KZ0O5ZLUqlUrd1toaKhatGih0tJSd9uHH36oRYsW6Y9//KOmTp160f1K///yly1btmjixInq1KmTevToocWLF6uiokKPP/64EhIS1KNHD82ZM0cul8vjdWfmZN26dbr11lu1Z88ejRgxQh06dNDtt9+uZcuWefS3adMmDRw4UB07dlT37t01depUfffdd42qVSK8AwAAeG369OnKzc3V+PHjlZ2drRkzZmj//v2aMmWKXC6XUlJSFBoaqo0bN3q87u2339ZNN92kjh076tSpUxo9erTee+89TZkyRYsWLdK1116rBx544JwAv2TJEqWmpuqFF17QHXfcocLCQo0ZM0bh4eGaN2+elixZos6dO2vRokXuPmtrazV69Gh9/vnnevzxx5WZmanCwkJlZ2d77Pvll1/WzJkzlZSUpJdeekkjR47UsmXL9OSTT7q3adeuXaMuEZk8ebL++te/qmvXrj+63axZs9S2bVvde++9F5tqSaffwJwJ1Pv371dpaamysrJUU1Oju+++271dhw4dtH37dk2YMEHNmjVr1L7PeOKJJxQbG6slS5aoe/fuWrBggYYNG6aQkBAtWLBAycnJWr58uTZv3nzBfTidTk2ePFl33323li5dqoSEBM2dO1cfffSRJOmzzz7T1KlT1a9fPy1btkyPPfaY8vPz9cgjjzS6TrtXowIAAGjiamtrVVlZqZkzZ7qDY7du3VRZWamsrCwdP35cP/vZz5SamqpNmza5g1lNTY3ee+89jRs3TpK0YcMGFRYW6i9/+Ytuu+02SVKfPn00atQozZ07V2+++aa7z44dO2r8+PHux2+99Zb7TLDNdvpcbM+ePbVjxw4VFBQoLS1Nf/3rX3Xw4EG9+eabat++vSSpe/fuuvPOO937KS8v15IlSzRixAilp6dLknr16qXw8HClp6dr7NixiomJUatWrdSpU6eLzk1sbOxFt9m2bZvee+895eXlKSgo6KLbnzFz5kyNGzdOaWlpkqSgoCBlZmaqc+fO7m2uueaaRu/vh3r37q3JkydLkqKjo7Vx40ZdddVV7jcxPXv21DvvvKPPP/9cv/nNb867D5fLpYkTJ2r48OGSpISEBG3btk07duxQ79699dlnn6lFixYaN26cWrRoIUkKDw/Xl19+KZfL1aj5ILwDAAB4ITg4WCtWrJB0+rKUQ4cO6eDBg3r//fclSXV1dZKkgQMHat26ddqzZ49uu+02bd++XVVVVe7wuXPnTkVFRaldu3Yel6j07dtXf/7zn1VWVqY2bdpIOjcUDx48WIMHD9apU6d0+PBhHTp0SPv27VNDQ4O7//z8fN1www3u4C6dvuykb9++2rVrlyTpiy++UHV1tZKTkz1qOHNZzccff6yYmBjL5q6kpERPPfWUpk+fruuvv77Rr/vmm29077336vrrr9fChQvVunVrbdy4Uenp6QoJCblgmPZGfHy8+/+joqIkyf2mSjr9ZqFNmzYqLy9v9H6Cg4MVGRmpqqoqSVLXrl01b948paWl6Te/+Y369OmjXr166de//nWj6yS8AwAAeOmjjz7S7NmzdfDgQYWGhiouLk6hoaGS5L4munv37rruuuu0ceNG3XbbbXr77bfVpUsXd2gtLS3V8ePH1a5du/P2cfz4cXd4v/rqqz2eq6mp0axZs7RhwwbV19fr+uuvV3x8vOx2u7v/kydP6qqrrjpnv2fv68z14mef1T+bN9diN8bTTz+ttm3batiwYR5vFlwul+rr69WsWbPznn3OycmR0+lUdna2IiIiJEk9evRQeXm5nnnmGaWmprp/A3Gpzr6e/gyHw+H1fkJCQjwe22w2979JfHy8+048K1as0EsvvaSoqCiNGzdOo0ePbtT+Ce8AAABeOHz4sCZNmqQ77rhDL7/8sn75y19KklavXu2+tlk6faY2LS1NGzZs0KRJk/Thhx/qqaeecj/funVr3XjjjZo7d+55+/mxM9MZGRnasmWL5s+frx49eqhly5aSpKSkJPc211xzjQ4dOnTOa0+cOOH+/zN/LDp37lzdeOON52z7wzcNP9WWLVskyeO3AZL07bff6q233tLKlSuVmJh4zuuOHj2qm2++2R3cz+jWrZu2bNmikpISy2u9XHr37q3evXururpa+fn5WrlypWbPnq1OnTp5nOm/EMI7gCbl/qztvi7Ba9kzks9pM20c5xsDYKqvvvpKp06d0oMPPugO7pLcwf3MWVZJGjRokJYuXaoXX3xRQUFBuuuuu9zPdevWTTt27NBVV12ln//85+72pUuXat++fRcM9dLpP3xMTEz0uH79q6++UklJiftuM926ddObb76pv//97+47v5w6dUoffvihgoODJZ2+LKR58+Y6duyY+3Ie6fR90rOysjRp0iRdd911lzRP55Obm3tO24QJE9S+fXtNmjRJN91003lfd9NNN+nNN99UaWmpwsPD3e2ff/65WrVq5f4Nhb977rnnVFBQoLVr18rhcKhv37667rrrNGjQIP3rX/8ivAMAAFitXbt2stvtmjNnju6//37V1tZq3bp12rFjhyS5r2+WTv/hY7t27fTaa68pJSXF457mQ4YM0apVqzR27Fj98Y9/1HXXXadPPvlEy5Yt03333afmzZtfsIaOHTvqnXfe0euvv662bduqsLBQS5YsUVBQkKqrqyVJAwYM0NKlSzVp0iQ9/PDDCgsLU3Z2tk6cOOF+sxAREaEHHnhACxYsUEVFhRITE3Xs2DEtWLBAQUFBuuWWWySd/iTUoqIi/fKXv/xJ9zXv0KHDOW3BwcEKDw/3eO7f//63/v3vf+vWW29VcHCwxo4dq7y8PI0ZM0YPPvigWrdura1bt2rjxo2aMWPGj86VP0lKStIrr7yiGTNmaODAgaqrq9Py5csVHh6u7t27N2ofhHcAAAAv/Md//Ieef/55LVq0SBMmTFCbNm3UqVMnvfrqqxo1apR2796tuLg49/aDBg3Svn37NHDgQI/9tGzZUqtXr9bzzz+vOXPmqLy8XL/4xS/0yCOP6P777//RGmbMmKG6ujrNnz9ftbW1uv766zVhwgQVFRVp+/btamhokN1u14oVK5SRkaGnn35adrtdAwcOVEREhP7v//7Pva/JkycrKipKr732mpYvX642bdooKSlJ//Vf/+V+s7Fv3z79/ve/V2ZmpoYMGWLhbJ7f2rVrtWjRIr333nu6/vrr9Ytf/EKvv/66XnjhBc2cOVNOp1PR0dF68cUX1a9fv8tej1X69OmjuXPnKjs7Ww899JCCgoKUkJCglStXevxG4ccEuc7+3Y6fO378x/+611t2u00REaE6ebJS9fXOi7/AEKb9Ol0KjMsCJOsuDQjUY9MXfjiXgXJcmTYOLpvxxBq3zuWcy6ioi3/ypz87cOCADh48qH79+nn8EejQoUN13XXXadGiRT6sDpeKM+8AAAABqKqqSg8/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qIyMDNXX11/JEgAAAABjXdHwPnnyZLVs2VIfffSRcnNztXPnTuXk5FzJEgAAAABj2a9UR4cOHdKnn36qDz/8UA6HQzfccIMmTpyoOXPm6IEHHmjUPmy2INlsQZbV1KyZzeOriex2c2s/G+PwL4E0Dta5fwiEMUiMw98EyhoHvBHkcrlcV6Kjd999V0888YR27drlbvv66681cOBAFRQUKCws7EqUAQAAABjrir1NrayslMPh8Gg787iqqupKlQEAAAAY64qF95YtW6q6utqj7czj0NDQK1UGAAAAYKwrFt5jYmJUWlqq4uJid9s333yja6+9Vq1bt75SZQAAAADGumLh/cYbb1RCQoJmz56tiooKHTlyRIsXL9awYcOuVAkAAACA0a7YH6xKUnFxsZ555hnt2rVLNptNgwcP1tSpU9WsWbMrVQIAAABgrCsa3gEAAABcOm6KCgAAABiC8A4AAAAYgvAOAAAAGILwDgAAABiiyYb3EydOaOLEierSpYsSExOVkZGh+vp6X5dlpE2bNunWW29VfHy8+79p06b5uiyjlJSUKCUlRbt27XK37dmzR8OHD1d8fLySk5O1du1aH1ZolvPN51NPPaX27dt7HKdvvPGGD6v0b4WFhRo7dqy6deumnj17avr06SopKZHEsemtH5tLjkvv7Ny5U8OHD1fnzp3Vs2dPzZo1SzU1NZI4LtGEuJqo++67z/XII4+4qqqqXIcPH3b179/ftWzZMl+XZaSsrCzXjBkzfF2GsXbv3u268847XbGxsa78/HyXy+VylZaWurp16+ZatWqVq66uzvXJJ5+44uPjXXv27PFxtf7vfPPpcrlcv/3tb13r1q3zYWXmqK6udvXs2dO1YMEC16lTp1wlJSWucePGuR588EGOTS/92Fy6XByX3jhx4oSrQ4cOrjfffNPV0NDgOnbsmGvAgAGuBQsWcFyiSWmSZ94PHTqkTz/9VNOmTZPD4dANN9ygiRMnavXq1b4uzUhffvml2rdv7+syjLR+/XpNnTpVU6ZM8WjfunWrwsPDNXLkSNntdiUlJSktLY1j9CIuNJ+1tbXav38/x2kjHT16VLfccosmTZqk4OBgRUREaMSIESooKODY9NKPzSXHpXciIyP1ySefaMiQIQoKClJpaalOnTqlyMhIjks0KU0yvB84cEDh4eG65ppr3G1t27bV0aNH9f333/uwMvM4nU7t27dPO3bsUN++fdWnTx/NnDlTZWVlvi7NCL169dK2bdt09913e7QfOHBAsbGxHm3R0dEqLCy8kuUZ50LzWVhYqPr6ei1cuFA9evRQamqqli5dKqfT6aNK/dvNN9+s5cuXe3yA3pYtW9SuXTuOTS/92FxyXHqvVatWkqRf//rXSktLU1RUlIYMGcJxiSalSYb3yspKORwOj7Yzj6uqqnxRkrFKSkp06623KjU1VZs2bdKaNWv0j3/8g2veGykqKkp2u/2c9vMdoyEhIRyfF3Gh+SwvL1e3bt00atQoffDBB5ozZ45effVVZWdn+6BKs7hcLs2bN0/vv/++nnjiCY7Nn+CHc8lxeem2bt2qDz/8UDabTX/60584LtGknPtTrglo2bKlqqurPdrOPA4NDfVFSca6+uqrPX4t6XA4NG3aNN1zzz2qqKhwnyWBdxwOh8rLyz3aampqOD4vUc+ePdWzZ0/3444dO2r06NHatGmTHnjgAR9W5t8qKir02GOPad++fVq1apXi4uI4Ni/R+eYyLi6O4/IShYSEKCQkRNOmTdPw4cM1atQojks0GU3yzHtMTIxKS0tVXFzsbvvmm2907bXXqnXr1j6szDyFhYWaO3euXC6Xu622tlY2m03BwcE+rMxssbGxOnDggEdbUVGRYmJifFSR2d59912tWbPGo622tlYhISE+qsj/HT58WEOHDlVFRYVyc3MVFxcniWPzUlxoLjkuvfP555/rrrvuUm1trbuttrZWzZs3V3R0NMclmowmGd5vvPFGJSQkaPbs2aqoqNCRI0e0ePFiDRs2zNelGSc8PFyrV6/W8uXLVV9fr6NHj2rOnDn67W9/S3j/CVJSUlRcXKycnBzV1dUpPz9feXl5Gjp0qK9LM5LL5VJmZqZ27twpl8ulL774QitXrtSIESN8XZpfKisr0+jRo9W5c2etWLFCkZGR7uc4Nr3zY3PJcemduLg41dTU6Pnnn1dtba2+/fZbPffccxo2bJhSU1M5LtFkBLnOPmXahBQXF+uZZ57Rrl27ZLPZNHjwYE2dOtXjj4rQOJ9++qleeOEF7d+/Xy1atFD//v01bdo0tWjRwtelGSUuLk4rV65UYmKipNN38cnIyND+/fsVGRmpiRMnasiQIT6u0hw/nM81a9bolVde0bFjx3T11Vdr7NixGjlypI+r9E+vvPKKsrKy5HA4FBQU5PHcF198wbHphYvNJceld4qKijR79mx9+eWXat26tdLS0tx38uG4RFPRZMM7AAAAYJomedkMAAAAYCLCOwAAAGAIwjsAAABgCMI7AAAAYAjCOwAAAGAIwjsAAABgCMI7AAAAYAjCOwAAAGAIwjsAAABgCMI7AAAAYAjCOwAAAGCI/wdoe5hpcJ+X5AAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set random seed to 334\n",
    "np.random.seed(334)\n",
    "\n",
    "# Import uniform\n",
    "from cProfile import label\n",
    "from scipy.stats import uniform\n",
    "\n",
    "# Generate 1000 wait times between 0 and 30 mins\n",
    "wait_times = uniform.rvs(0, 30, size=1000)\n",
    "\n",
    "# Create a histogram of simulated times and show plot\n",
    "plt.hist(wait_times, rwidth=0.9)\n",
    "plt.text(1.01, 0.85, f'average: {np.mean(wait_times):.2f} mins', \n",
    "         fontsize=12, transform=plt.gca().transAxes)\n",
    "\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The binomial distribution\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Simulating sales deals**\n",
    "\n",
    "Assume that Amir usually works on 3 deals per week, and overall, he wins 30% of deals he works on. Each deal has a binary outcome: it's either lost, or won, so you can model his sales deals with a binomial distribution. In this exercise, you'll help Amir simulate a year's worth of his deals so he can better understand his performance.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 49,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "[1]\n",
      "[1]\n",
      "0.8269230769230769\n"
     ]
    }
   ],
   "source": [
    "# Import binom from scipy.stats\n",
    "from scipy.stats import binom\n",
    "\n",
    "# Set random seed to 10\n",
    "np.random.seed(10)\n",
    "\n",
    "# Simulate a single deal\n",
    "print(binom.rvs(1, 0.3, size=1))\n",
    "\n",
    "np.random.seed(10)\n",
    "# Simulate 1 week of 3 deals\n",
    "print(binom.rvs(3, 0.3, size=1))\n",
    "\n",
    "np.random.seed(10)\n",
    "# Simulate 52 weeks of 3 deals\n",
    "deals = binom.rvs(3, 0.3, size=52)\n",
    "\n",
    "# Print mean deals won per week\n",
    "print(np.mean(deals))"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Calculating binomial probabilities**\n",
    "\n",
    "ust as in the last exercise, assume that Amir wins 30% of deals. He wants to get an idea of how likely he is to close a certain number of deals each week. In this exercise, you'll calculate what the chances are of him closing different numbers of deals using the binomial distribution.\n",
    "\n",
    "binom is imported from scipy.stats.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.026999999999999996\n",
      "0.784\n",
      "0.21599999999999997\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'Amir has about a 22% chance of closing more than one deal in a week.'"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Probability of closing 3 out of 3 deals\n",
    "prob_3 = binom.pmf(3,3,0.3)\n",
    "\n",
    "print(prob_3)\n",
    "\n",
    "# Probability of closing <= 1 deal out of 3 deals\n",
    "prob_less_than_or_equal_1 = binom.cdf(1,3,0.3)\n",
    "\n",
    "print(prob_less_than_or_equal_1)\n",
    "\n",
    "# Probability of closing > 1 deal out of 3 deals\n",
    "prob_greater_than_1 = 1 - binom.cdf(1, 3, 0.3)\n",
    "\n",
    "print(prob_greater_than_1)\n",
    "\n",
    "\"\"\"Amir has about a 22% chance of closing more than one deal in a week.\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **How many sales will be won?**\n",
    "\n",
    "Now Amir wants to know how many deals he can expect to close each week if his win rate changes. Luckily, you can use your binomial distribution knowledge to help him calculate the expected value in different situations. Recall from the video that the expected value of a binomial distribution can be calculated by $n \\times p$.\n",
    "\n",
    "Instructions:<br>\n",
    "\n",
    "- Calculate the expected number of sales out of the 3 he works on that Amir will win each week if he maintains his 30% win rate.\n",
    "- Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate drops to 25%.\n",
    "- Calculate the expected number of sales out of the 3 he works on that he'll win if his win rate rises to 35%."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 52,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8999999999999999\n",
      "0.75\n",
      "1.0499999999999998\n"
     ]
    }
   ],
   "source": [
    "# Expected number won with 30% win rate\n",
    "won_30pct = 0.3 * 3\n",
    "print(won_30pct)\n",
    "\n",
    "# Expected number won with 25% win rate\n",
    "won_25pct = 0.25 * 3\n",
    "print(won_25pct)\n",
    "\n",
    "# Expected number won with 35% win rate\n",
    "won_35pct = 0.35 * 3\n",
    "print(won_35pct)\n",
    "\n",
    "\"\"\"Excellent expectation experimentation! If Amir's win rate goes up by 5%, he can expect to close more than 1 deal on average each week.\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## More Distributions and the Central Limit Theorem\n",
    "\n",
    "> It’s time to explore one of the most important probability distributions in statistics, normal distribution. You’ll create histograms to plot normal distributions and gain an understanding of the central limit theorem, before expanding your knowledge of statistical functions by adding the Poisson, exponential, and t-distributions to your repertoire."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The normal distribution"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Distribution of Amir's sales**\n",
    "\n",
    "Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals As part of Amir's performance review, you want to be able to estimate the probability of him selling different amounts, but before you can do this, you'll need to determine what kind of distribution the amount variable follows."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "metadata": {},
   "outputs": [],
   "source": [
    "amir_deals = pd.read_csv('./datasets/amir_deals.csv', index_col=0)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 14,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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fPhwug+xR5g3b54CgYCmTZuWGKPv6bN//3796Ec/0nnnnae8vDx97Wtf05YtWxLr6X3qHT9+XL/85S9VWVmp3NxcXXTRRfq///s/tbe3J+bQ99RYt26dxo4dq7KyMgUCAT3zzDNJ6zPZ571792rs2LHq27evioqKdM899+jYsWO2AzrztwDGp1m2bJkLBoPusccec2+++aa79957Xd++fd2ePXv8Lq1HuP76693SpUvdjh073LZt29yYMWPcBRdc4D766KPEnPnz57v8/Hz31FNPue3bt7sf/OAHrrS01EWj0cScu+66y51//vkuEom4rVu3ulGjRrnLL7/cHT9+PDHnhhtucFVVVW79+vVu/fr1rqqqyn3729/O6PF2R6+99pq78MIL3WWXXebuvffexDh9T48PP/zQVVRUuEmTJrlXX33VNTQ0uBdeeMG9++67iTn0PvUeeeQRd95557m///3vrqGhwf3lL39x/fr1c4sWLUrMoe+psXLlSjdz5kz31FNPOUnu6aefTlqfqT4fP37cVVVVuVGjRrmtW7e6SCTiysrK3JQpU0zHQ3hKg6uuusrdddddSWOXXHKJmzFjhk8V9WwHDhxwklx9fb1zzrn29nYXCoXc/PnzE3M+/vhjV1hY6H73u98555w7fPiwCwaDbtmyZYk5+/fvd1lZWW7VqlXOOefefPNNJ8lt3LgxMWfDhg1OknvrrbcycWjdUmtrqxs4cKCLRCJuxIgRifBE39Pn/vvvd9dee+2nrqf36TFmzBj34x//OGls3Lhx7kc/+pFzjr6nyyfDUyb7vHLlSpeVleX279+fmPPnP//ZeZ7nWlpaunwMvGyXYseOHdOWLVtUU1OTNF5TU6P169f7VFXP1tLSIknq37+/JKmhoUFNTU1JPfY8TyNGjEj0eMuWLYrH40lzysrKVFVVlZizYcMGFRYWasiQIYk5V199tQoLC3v112ry5MkaM2aMvvWtbyWN0/f0efbZZzV48GB9//vfV3Fxsa644go99thjifX0Pj2uvfZa/eMf/9A777wjSfrnP/+pV155RTfeeKMk+p4pmezzhg0bVFVVpbKyssSc66+/XrFYLOll8tNJy9uz9GYHDx7UiRMnOrwJcklJSYc3S8bpOedUW1ura6+9VlVVVZKU6GNnPd6zZ09iTp8+ffS5z32uw5yTn9/U1KTi4uIO+ywuLu61X6tly5Zp69at2rRpU4d19D19/v3vf2vJkiWqra3Vgw8+qNdee0333HOPPM/T7bffTu/T5P7771dLS4suueQSZWdn68SJE5ozZ45uvfVWSTznMyWTfW5qauqwn8997nPq06eP6WtBeEqTQCCQtOyc6zCG05syZYreeOMNvfLKKx3WnUmPPzmns/m99Wu1b98+3XvvvVqzZo3OOeecT51H31Ovvb1dgwcP1ty5cyVJV1xxhXbu3KklS5bo9ttvT8yj96m1fPlyPfnkk6qrq9NXv/pVbdu2TdOmTVNZWZkmTpyYmEffMyNTfU7F14KX7VKsqKhI2dnZHRLsgQMHOqRdnNrUqVP17LPP6qWXXtKAAQMS46FQSJJO2eNQKKRjx46pubn5lHM++OCDDvv9z3/+0yu/Vlu2bNGBAwc0aNAg5eTkKCcnR/X19frNb36jnJycRE/oe+qVlpbqK1/5StLYl7/8Ze3du1cSz/l0+cUvfqEZM2bohz/8oS699FJNmDBBP//5zzVv3jxJ9D1TMtnnUCjUYT/Nzc2Kx+OmrwXhKcX69OmjQYMGKRKJJI1HIhENGzbMp6p6FuecpkyZohUrVujFF19UZWVl0vrKykqFQqGkHh87dkz19fWJHg8aNEjBYDBpTmNjo3bs2JGYM3ToULW0tOi1115LzHn11VfV0tLSK79W3/zmN7V9+3Zt27Yt8Rg8eLBuu+02bdu2TRdddBF9T5Nrrrmmw+043nnnHVVUVEjiOZ8ubW1tyspK/jGYnZ2duFUBfc+MTPZ56NCh2rFjhxobGxNz1qxZI8/zNGjQoK4X3eVfLUeXnbxVweOPP+7efPNNN23aNNe3b1+3e/duv0vrEX72s5+5wsJCt3btWtfY2Jh4tLW1JebMnz/fFRYWuhUrVrjt27e7W2+9tdM/ax0wYIB74YUX3NatW911113X6Z+1XnbZZW7Dhg1uw4YN7tJLL+1Vfz58Ov/713bO0fd0ee2111xOTo6bM2eO27Vrl/vTn/7k8vLy3JNPPpmYQ+9Tb+LEie78889P3KpgxYoVrqioyE2fPj0xh76nRmtrq3v99dfd66+/7iS5hQsXutdffz1xC59M9fnkrQq++c1vuq1bt7oXXnjBDRgwgFsVdBe//e1vXUVFhevTp4/7+te/nvgze5yepE4fS5cuTcxpb293Dz30kAuFQs7zPDd8+HC3ffv2pO0cPXrUTZkyxfXv39/l5ua6b3/7227v3r1Jcw4dOuRuu+02l5+f7/Lz891tt93mmpubM3CUPcMnwxN9T5+//e1vrqqqynme5y655BL3+9//Pmk9vU+9aDTq7r33XnfBBRe4c845x1100UVu5syZLhaLJebQ99R46aWXOj2vT5w40TmX2T7v2bPHjRkzxuXm5rr+/fu7KVOmuI8//th0PAHnnOv6dSoAAIDejd95AgAAMCA8AQAAGBCeAAAADAhPAAAABoQnAAAAA8ITAACAAeEJAADAgPAEAABgQHgCAAAwIDwBAAAYEJ4AAAAM/h+3NG1gbdjwNQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "' the sales amounts most closely follows the Normal probability distribution '"
      ]
     },
     "execution_count": 14,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Histogram of amount with 10 bins and show plot\n",
    "amir_deals['amount'].hist( bins=10)\n",
    "plt.show()\n",
    "\"\"\" the sales amounts most closely follows the Normal probability distribution \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Probabilities from the normal distribution**\n",
    "\n",
    "Since each deal Amir worked on (both won and lost) was different, each was worth a different amount of money. These values are stored in the amount column of amir_deals and follow a normal distribution with a mean of 5000 dollars and a standard deviation of 2000 dollars. As part of his performance metrics, you want to calculate the probability of Amir closing a deal worth various amounts.\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 18,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8943502263331446\n",
      "0.9772498680518208\n",
      "0.6826894921370859\n",
      "3651.0204996078364\n"
     ]
    }
   ],
   "source": [
    "from scipy.stats import norm\n",
    "# Probability of deal < 7500\n",
    "prob_less_7500 = norm.cdf(7500, 5000,2000)\n",
    "\n",
    "print(prob_less_7500)\n",
    "\n",
    "# Probability of deal > 1000\n",
    "prob_over_1000 = 1 - norm.cdf(1000, 5000, 2000)\n",
    "\n",
    "print(prob_over_1000)\n",
    "\n",
    "# Probability of deal between 3000 and 7000\n",
    "prob_3000_to_7000 = norm.cdf(7000, 5000,2000) - norm.cdf(3000,5000,2000)\n",
    "\n",
    "print(prob_3000_to_7000)\n",
    "\n",
    "# Calculate amount that 25% of deals will be less than\n",
    "pct_25 = norm.ppf(0.25,5000,2000)\n",
    "\n",
    "print(pct_25)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Simulating sales under new market conditions**\n",
    "\n",
    "The company's financial analyst is predicting that next quarter, the worth of each sale will increase by 20% and the volatility, or standard deviation, of each sale's worth will increase by 30%. To see what Amir's sales might look like next quarter under these new market conditions, you'll simulate new sales amounts using the normal distribution and store these in the new_sales DataFrame, which has already been created for you.\n",
    "\n",
    "In addition, norm from scipy.stats, pandas as pd, and matplotlib.pyplot as plt are loaded.\n",
    "\n",
    "Instructions:<br>\n",
    "\n",
    "- Currently, Amir's average sale amount is $5000. Calculate what his new average amount will be if it increases by 20% and store this in new_mean.\n",
    "- Amir's current standard deviation is $2000. Calculate what his new standard deviation will be if it increases by 30% and store this in new_sd.\n",
    "- Create a variable called new_sales, which contains 36 simulated amounts from a normal distribution with a mean of new_mean and a standard deviation of new_sd.\n",
    "- Plot the distribution of the new_sales amounts using a histogram and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 25,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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SUQRAEASUQQAkEQUAQAkEUUAAElEEQBAElEEAJBEFAEAJBFFAABJRBEAQBJRBACQRBQBACQRRQAASUQRAEASUQQAkEQUAQAkqTKKWlpactZZZ6V3797p379/PvOZz+Spp56q1dwAAOqmqihavnx5pkyZkpUrV2bp0qV58803c+mll+bVV1+t1fwAAOqiZzWDH3zwwU6358+fn/79+2ft2rU5//zzD+vEAADqqaooequ2trYkSd++fQ84plwup1wuV263t7cfyikBAGqiy2+0Looi06dPz3nnnZfm5uYDjmtpaUljY2NlGzx4cFdPCQBQM12OoqlTp+bJJ5/Mvffee9BxM2fOTFtbW2VrbW3t6ikBAGqmSy+fXXfddbn//vvz6KOPZtCgQQcdWyqVUiqVujQ5AIB6qSqKiqLIddddlyVLluSRRx7J8OHDazUvAIC6qiqKpkyZknvuuSf/9m//lt69e2fHjh1JksbGxvTq1asmEwQAqIeq3lM0b968tLW15cILL8zAgQMr26JFi2o1PwCAuqj65TMAgKOR7z4DAIgoAgBIIooAAJKIIgCAJKIIACCJKAIASCKKAACSiCIAgCSiCAAgiSgCAEgiigAAkogiAIAkoggAIIkoAgBIIooAAJKIIgCAJKIIACCJKAIASCKKAACSiCIAgCSiCAAgiSgCAEgiigAAkogiAIAkoggAIIkoAgBIIooAAJKIIgCAJKIIACCJKAIASCKKAACSiCIAgCSiCAAgiSgCAEgiigAAknQhih599NFMmDAhTU1NaWhoyH333VeDaQEA1FfVUfTqq6/mjDPOyDe/+c1azAcAoFv0rPaAcePGZdy4ce94fLlcTrlcrtxub2+v9pQAADVXdRRVq6WlJbNmzar1aQCos2E3PdDdU+iyn88Z391TOKz8WRweNX+j9cyZM9PW1lbZWltba31KAICq1fxKUalUSqlUqvVpAAAOiY/kAwBEFAEAJOnCy2evvPJKnn322crtLVu2ZMOGDenbt2+GDBlyWCcHAFAvVUfRmjVrctFFF1VuT58+PUkyefLk/Mu//MthmxgAQD1VHUUXXnhhiqKoxVwAALqN9xQBAEQUAQAkEUUAAElEEQBAElEEAJBEFAEAJBFFAABJRBEAQBJRBACQRBQBACQRRQAASUQRAEASUQQAkEQUAQAkEUUAAElEEQBAElEEAJBEFAEAJBFFAABJRBEAQBJRBACQRBQBACQRRQAASUQRAEASUQQAkEQUAQAkEUUAAElEEQBAElEEAJBEFAEAJBFFAABJRBEAQBJRBACQRBQBACQRRQAASboYRXfccUeGDx+e4447LqNHj86Pf/zjwz0vAIC6qjqKFi1alBtuuCE333xz1q9fn9/7vd/LuHHjsm3btlrMDwCgLnpWe8Dtt9+eP/uzP8uf//mfJ0nmzp2bhx56KPPmzUtLS8s+48vlcsrlcuV2W1tbkqS9vb2rc35bHeXXavaz6+HXa3MkP46j4TEkR8fjOBoeQ3J0PI6j4TEkR8fjqOXvoO7gz+Ltf35RFG8/uKhCuVwuevToUSxevLjT/uuvv744//zz93vMLbfcUiSx2Ww2m81m67attbX1bTunqitFv/jFL7J3796cfPLJnfaffPLJ2bFjx36PmTlzZqZPn1653dHRkV/+8pfp169fGhoaqjl9zbW3t2fw4MFpbW1Nnz59uns6RxRr1zXWreusXddZu66xbl3XnWtXFEV2796dpqamtx1b9ctnSfaJmaIoDhg4pVIppVKp074PfOADXTlt3fTp08cTvousXddYt66zdl1n7brGunVdd61dY2PjOxpX1RutTzrppPTo0WOfq0I7d+7c5+oRAMCRpKooOvbYYzN69OgsXbq00/6lS5fmnHPOOawTAwCop6pfPps+fXomTZqUMWPGZOzYsbnzzjuzbdu2XHvttbWYX12VSqXccsst+7zcx9uzdl1j3brO2nWdtesa69Z1R8raNRTv6DNqnd1xxx35+7//+2zfvj3Nzc35+te/nvPPP78W8wMAqIsuRREAwNHGd58BAEQUAQAkEUUAAElEEQBAkqMsilpaWnLWWWeld+/e6d+/fz7zmc/kqaee6jSmKIp85StfSVNTU3r16pULL7wwmzdv7jSmXC7nuuuuy0knnZQTTjghn/rUp/L88893GrNr165MmjQpjY2NaWxszKRJk/Lyyy/X+iHWTUtLSxoaGnLDDTdU9lm7A3vhhRdy1VVXpV+/fjn++OPzkY98JGvXrq3cb+329eabb+bLX/5yhg8fnl69euXUU0/NV7/61XR0dFTGWLdfefTRRzNhwoQ0NTWloaEh9913X6f767lO27Zty4QJE3LCCSfkpJNOyvXXX5833nijFg/7sDjY2u3ZsyczZszIyJEjc8IJJ6SpqSlXX311XnzxxU4/4724dm/3nPtNn//859PQ0JC5c+d22n9Erls1Xwj7bveJT3yimD9/frFp06Ziw4YNxfjx44shQ4YUr7zySmXMnDlzit69exff+973io0bNxZ/8id/UgwcOLBob2+vjLn22muLU045pVi6dGmxbt264qKLLirOOOOM4s0336yM+f3f//2iubm5ePzxx4vHH3+8aG5uLi677LK6Pt5aWbVqVTFs2LBi1KhRxbRp0yr7rd3+/fKXvyyGDh1afPazny2eeOKJYsuWLcWyZcuKZ599tjLG2u3ra1/7WtGvX7/iP/7jP4otW7YU3/3ud4v3v//9xdy5cytjrNuvfP/73y9uvvnm4nvf+16RpFiyZEmn++u1Tm+++WbR3NxcXHTRRcW6deuKpUuXFk1NTcXUqVNrvgZddbC1e/nll4tLLrmkWLRoUfGzn/2sWLFiRXH22WcXo0eP7vQz3otr93bPuV9bsmRJccYZZxRNTU3F17/+9U73HYnrdlRF0Vvt3LmzSFIsX768KIqi6OjoKAYMGFDMmTOnMub1118vGhsbi29961tFUfzqL8n73ve+YuHChZUxL7zwQnHMMccUDz74YFEURfHTn/60SFKsXLmyMmbFihVFkuJnP/tZPR5azezevbv40Ic+VCxdurS44IILKlFk7Q5sxowZxXnnnXfA+63d/o0fP7645pprOu37gz/4g+Kqq64qisK6Hchbf0HVc52+//3vF8ccc0zxwgsvVMbce++9RalUKtra2mryeA+ng/1y/7VVq1YVSYqtW7cWRWHtiuLA6/b8888Xp5xySrFp06Zi6NChnaLoSF23o+rls7dqa2tLkvTt2zdJsmXLluzYsSOXXnppZUypVMoFF1yQxx9/PEmydu3a7Nmzp9OYpqamNDc3V8asWLEijY2NOfvssytjPvrRj6axsbEy5kg1ZcqUjB8/Ppdcckmn/dbuwO6///6MGTMml19+efr3758zzzwzd911V+V+a7d/5513Xn70ox/l6aefTpL85Cc/yWOPPZZPfvKTSazbO1XPdVqxYkWam5s7fdv4Jz7xiZTL5U4vFx/J2tra0tDQUPnicmu3fx0dHZk0aVJuvPHGjBgxYp/7j9R1q/prPo4URVFk+vTpOe+889Lc3JwklS+yfeuX15588snZunVrZcyxxx6bE088cZ8xvz5+x44d6d+//z7n7N+//z5flnskWbhwYdatW5fVq1fvc5+1O7Dnnnsu8+bNy/Tp0/OlL30pq1atyvXXX59SqZSrr77a2h3AjBkz0tbWltNOOy09evTI3r17M3v27Fx55ZVJPOfeqXqu044dO/Y5z4knnphjjz32qFjL119/PTfddFP+9E//tPJN7tZu/2677bb07Nkz119//X7vP1LX7aiNoqlTp+bJJ5/MY489ts99DQ0NnW4XRbHPvrd665j9jX8nP+fdqrW1NdOmTcsPf/jDHHfccQccZ+321dHRkTFjxuTWW29Nkpx55pnZvHlz5s2bl6uvvroyztp1tmjRoixYsCD33HNPRowYkQ0bNuSGG25IU1NTJk+eXBln3d6Zeq3T0bqWe/bsyRVXXJGOjo7ccccdbzv+vbx2a9euzTe+8Y2sW7eu6rm/29ftqHz57Lrrrsv999+fhx9+OIMGDarsHzBgQJLsU5c7d+6slOiAAQPyxhtvZNeuXQcd89JLL+1z3v/5n//Zp2iPFGvXrs3OnTszevTo9OzZMz179szy5cvzj//4j+nZs2flcVm7fQ0cODCnn356p30f/vCHs23btiSedwdy44035qabbsoVV1yRkSNHZtKkSfniF7+YlpaWJNbtnarnOg0YMGCf8+zatSt79uw5otdyz549+eM//uNs2bIlS5curVwlSqzd/vz4xz/Ozp07M2TIkMrvi61bt+Yv//IvM2zYsCRH7rodVVFUFEWmTp2axYsX5z//8z8zfPjwTvcPHz48AwYMyNKlSyv73njjjSxfvjznnHNOkmT06NF53/ve12nM9u3bs2nTpsqYsWPHpq2tLatWraqMeeKJJ9LW1lYZc6S5+OKLs3HjxmzYsKGyjRkzJhMnTsyGDRty6qmnWrsDOPfcc/f5rx+efvrpDB06NInn3YG89tprOeaYzv8E9ejRo/KRfOv2ztRzncaOHZtNmzZl+/btlTE//OEPUyqVMnr06Jo+zlr5dRA988wzWbZsWfr169fpfmu3r0mTJuXJJ5/s9PuiqakpN954Yx566KEkR/C6Hfa3bnejL3zhC0VjY2PxyCOPFNu3b69sr732WmXMnDlzisbGxmLx4sXFxo0biyuvvHK/H10dNGhQsWzZsmLdunXFxz72sf1+jHDUqFHFihUrihUrVhQjR448oj7i+0785qfPisLaHciqVauKnj17FrNnzy6eeeaZ4l//9V+L448/vliwYEFljLXb1+TJk4tTTjml8pH8xYsXFyeddFLx13/915Ux1u1Xdu/eXaxfv75Yv359kaS4/fbbi/Xr11c+IVWvdfr1x6MvvvjiYt26dcWyZcuKQYMGvWs/Vl4UB1+7PXv2FJ/61KeKQYMGFRs2bOj0e6NcLld+xntx7d7uOfdWb/30WVEcmet2VEVRkv1u8+fPr4zp6OgobrnllmLAgAFFqVQqzj///GLjxo2dfs7//d//FVOnTi369u1b9OrVq7jsssuKbdu2dRrzv//7v8XEiROL3r17F7179y4mTpxY7Nq1qw6Psn7eGkXW7sD+/d//vWhubi5KpVJx2mmnFXfeeWen+63dvtrb24tp06YVQ4YMKY477rji1FNPLW6++eZOv4ys2688/PDD+/23bfLkyUVR1Hedtm7dWowfP77o1atX0bdv32Lq1KnF66+/XsuHf0gOtnZbtmw54O+Nhx9+uPIz3otr93bPubfaXxQdievWUBRFcfivPwEAHFmOqvcUAQB0lSgCAIgoAgBIIooAAJKIIgCAJKIIACCJKAIASCKKAACSiCIAgCSiCAAgiSgCAEiS/D9SSiSoY4rDjQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "data": {
      "text/plain": [
       "\" Although the average sale amount went up, the variation also increased, so it's not straightforward to decide whether these sales are better than his current ones. In the next exercise, you'll explore the effects of higher variation.\""
      ]
     },
     "execution_count": 25,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Calculate new average amount\n",
    "new_mean = 5000 * 1.2\n",
    "\n",
    "# Calculate new standard deviation\n",
    "new_sd = 2000 * 1.3\n",
    "\n",
    "# Simulate 36 new sales\n",
    "new_sales = norm.rvs(new_mean, new_sd, size=36)\n",
    "\n",
    "# Create histogram and show\n",
    "plt.hist(new_sales, rwidth=0.96)\n",
    "plt.show()\n",
    "\n",
    "\"\"\" Although the average sale amount went up, the variation also increased, so it's not straightforward to decide whether these sales are better than his current ones. In the next exercise, you'll explore the effects of higher variation.\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Which market is better?**\n",
    "\n",
    "The key metric that the company uses to evaluate salespeople is the percent of sales they make over $1000 since the time put into each sale is usually worth a bit more than that, so the higher this metric, the better the salesperson is performing.\n",
    "\n",
    "Recall that Amir's current sales amounts have a mean of $5000 and a standard deviation of $2000, and Amir's predicted amounts in next quarter's market have a mean of $6000 and a standard deviation of $2600.\n",
    "\n",
    "Based only on the metric of percent of sales over $1000, does Amir perform better in the current market or the predicted market?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 26,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.9772498680518208\n",
      "0.9727648049862613\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\" In the current market, Amir makes sales over $1000 about 97.7% of the time, and about 97.3% of the time in the predicted market, so there's not much of a difference. However, his average sale amount is higher in the predicted market, so your company may want to consider other metrics as well.\""
      ]
     },
     "execution_count": 26,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "\n",
    "cur_market_sales_over_1000 = 1 - norm.cdf(1000,5000,2000)\n",
    "print(cur_market_sales_over_1000)\n",
    "\n",
    "predicted_market_sales_over_1000 = 1 - norm.cdf(1000,6000,2600)\n",
    "print(predicted_market_sales_over_1000)\n",
    "\n",
    "\"\"\" In the current market, Amir makes sales over $1000 about 97.7% of the time, and about 97.3% of the time in the predicted market, so there's not much of a difference. However, his average sale amount is higher in the predicted market, so your company may want to consider other metrics as well.\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The central limit theorem\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Visualizing sampling distributions**\n",
    "\n",
    "try creating sampling distributions of different summary statistics from samples of different distributions. Which distribution does the central limit theorem not apply to?\n",
    "\n",
    "\n",
    "- Discrete uniform distribution\n",
    "\n",
    "- Continuous uniform distribution\n",
    "\n",
    "- Binomial distribution\n",
    "\n",
    "- All of the above\n",
    "\n",
    "- **None of the above**\n",
    "\n",
    "*Regardless of the shape of the distribution you're taking sample means from, the central limit theorem will apply if the sampling distribution contains enough sample means.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **The CLT in action**\n",
    "\n",
    "The central limit theorem states that a sampling distribution of a sample statistic approaches the normal distribution as you take more samples, no matter the original distribution being sampled from.\n",
    "\n",
    "In this exercise, you'll focus on the sample mean and see the central limit theorem in action while examining the num_users column of amir_deals more closely, which contains the number of people who intend to use the product Amir is selling.\n",
    "\n",
    "pandas as pd, numpy as np, and matplotlib.pyplot as plt are loaded and amir_deals is available.\n",
    "\n",
    "Instructions:<br>\n",
    "\n",
    "- Create a histogram of the num_users column of amir_deals and show the plot."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 27,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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rW99K/vxj3+cXX/99dnxxx+fvfHGG9Xe2jHv85//fLZu3brs5ZdfzrZt25ZdfPHF2cknn5y999575XPuuOOOrKGhIXvggQey7du3Z1/60pey5ubmrLu7u4o7P/Y9//zz2Sc/+cns9NNPz66//vrycfMYXe+88042Y8aMbOnSpdkPf/jDrKOjI3vyySez1157rXyOmYyub3zjG9lJJ52U/fu//3vW0dGRffe7381OOOGE7O677y6fYyYj67HHHstWrlyZPfDAA1lEZA899FCf21M+/1dffXX2iU98Imtvb89efPHF7MILL8zOOOOM7ODBg8Pe3zEdTZ/97Gezq6++us+x0047LbvpppuqtKOPr927d2cRkW3atCnLsizr7e3NmpqasjvuuKN8zi9+8Yts4sSJ2T/90z9Va5vHvH379mWzZs3K2tvbs3nz5pWjyTxG34033pidf/75A95uJqPv4osvzv78z/+8z7FFixZlX/7yl7MsM5PR9sFoSvn8v/vuu1ldXV22fv368jlvvfVWNmbMmOzxxx8f9p6O2ZfnDhw4EFu3bo3W1tY+x1tbW2Pz5s1V2tXHV1dXV0RETJo0KSIiOjo6orOzs8988vl8zJs3z3xG0LJly+Liiy+O3//93+9z3DxG3yOPPBJz586NP/mTP4kpU6bEZz7zmfjWt75Vvt1MRt/5558f//Ef/xE/+clPIiLiv/7rv+LZZ5+Niy66KCLMpNpSPv9bt26NUqnU55yWlpaYPXt2RWY0Im+jUgv27NkThw4d6vcmwVOnTu33ZsKMrCzLYsWKFXH++efH7NmzIyLKMzjSfN54441R3+PHwfr16+PFF1+MF154od9t5jH6/vd//zfWrl0bK1asiFtuuSWef/75+OpXvxr5fD6+8pWvmEkV3HjjjdHV1RWnnXZajB07Ng4dOhS33357XH755RHh+6TaUj7/nZ2dMX78+PiVX/mVfudU4rH/mI2mw3K5XJ/rWZb1O8bIuvbaa+NHP/pRPPvss/1uM5/RsXPnzrj++uvjiSeeiOOOO27A88xj9PT29sbcuXNj9erVERHxmc98Jnbs2BFr166Nr3zlK+XzzGT0bNiwIe6///5oa2uLT33qU7Ft27ZYvnx5tLS0xJIlS8rnmUl1DeXzX6kZHbMvz02ePDnGjh3bryx3797dr1IZOdddd1088sgj8YMf/CCmTZtWPt7U1BQRYT6jZOvWrbF79+6YM2dOjBs3LsaNGxebNm2Kf/iHf4hx48aVP+fmMXqam5vjt37rt/oc+83f/M148803I8L3SDX8zd/8Tdx0003xp3/6p/HpT386rrjiivjrv/7rWLNmTUSYSbWlfP6bmpriwIEDsXfv3gHPGY5jNprGjx8fc+bMifb29j7H29vb49xzz63Srj4+siyLa6+9Nh588MH4/ve/HzNnzuxz+8yZM6OpqanPfA4cOBCbNm0ynxHwe7/3e7F9+/bYtm1b+TJ37tz4sz/7s9i2bVuccsop5jHKzjvvvH5/huMnP/lJzJgxIyJ8j1RDT09PjBnT92Fx7Nix5T85YCbVlfL5nzNnTtTV1fU5Z9euXfHyyy9XZkbD/qfkNezwnxz49re/nf34xz/Oli9fnh1//PHZ66+/Xu2tHfP+6q/+Kps4cWL21FNPZbt27Spfenp6yufccccd2cSJE7MHH3ww2759e3b55Zf71d1R9Mu/PZdl5jHann/++WzcuHHZ7bffnr366qvZv/zLv2T19fXZ/fffXz7HTEbXkiVLsk984hPlPznw4IMPZpMnT85uuOGG8jlmMrL27duXvfTSS9lLL72URUR21113ZS+99FL5TwWlfP6vvvrqbNq0admTTz6Zvfjii9nnPvc5f3Ig1T/+4z9mM2bMyMaPH5/9zu/8TvlX3hlZEXHEy7p168rn9Pb2ZrfddlvW1NSU5fP57IILLsi2b99evU1/zHwwmsxj9P3bv/1bNnv27Cyfz2ennXZa9s1vfrPP7WYyurq7u7Prr78+O/nkk7PjjjsuO+WUU7KVK1dmxWKxfI6ZjKwf/OAHR3zsWLJkSZZlaZ//999/P7v22muzSZMmZRMmTMj+4A/+IHvzzTcrsr9clmXZ8J+vAgA4th2z/6YJAKCSRBMAQALRBACQQDQBACQQTQAACUQTAEAC0QQAkEA0AQAkEE0AAAlEEwBAAtEEAJDg/wOwVyi0aV7HLQAAAABJRU5ErkJggg==",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a histogram of num_users and show\n",
    "amir_deals['num_users'].hist()\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 29,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "iVBORw0KGgoAAAANSUhEUgAAAk0AAAGsCAYAAADACpPiAAAAOXRFWHRTb2Z0d2FyZQBNYXRwbG90bGliIHZlcnNpb24zLjYuMSwgaHR0cHM6Ly9tYXRwbG90bGliLm9yZy/av/WaAAAACXBIWXMAAA9hAAAPYQGoP6dpAAAbSklEQVR4nO3df2zV1f348dcF6h1oi0OEthMZOvxjomYRp+CmqAMlzsDYlk2WBbM53fyxGVyMP2K4ZA4IyZz7hMhiljj9g+gfQ2cyHXRR0I24gI7IiDMYqzAFCeoogl4rnO8f+9JRWnpP8ba32McjuZH7vu/2Hl493D69tz8KKaUUAAD0aEitFwAAcCwQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBAhmG1XsDhDhw4EG+99VbU19dHoVCo9XIAgE+5lFLs2bMnmpubY8iQIz+fNOCi6a233opx48bVehkAwCCzbdu2OOWUU454+4CLpvr6+oj478IbGhpqto729vZYvXp1zJgxI+rq6mq2joHMjCozo56ZT2VmVJkZVWZGPWtra4tx48Z1NMiRDLhoOviSXENDQ82jacSIEdHQ0GCDHYEZVWZGPTOfysyoMjOqzIzyVPqyIF8IDgCQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAECGYbVeAHz+9j/Vegmf2OtLrqz1EgDoY55pAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAy9iqbFixfHeeedF/X19TFmzJiYPXt2vPLKK53OSSlFqVSK5ubmGD58eEybNi02b95c1UUDAPS3XkXT2rVr48Ybb4znn38+Wlpa4uOPP44ZM2bE3r17O85ZunRp3HvvvbFs2bJYv359NDY2xvTp02PPnj1VXzwAQH8Z1puT//znP3e6/uCDD8aYMWPihRdeiIsuuihSSnHffffFXXfdFXPmzImIiIceeijGjh0bK1asiOuvv77L+yyXy1Eulzuut7W1RUREe3t7tLe39/ovVC0H77uWaxjoqjWj4tBUjeXU1JFmYB/1zHwqM6PKzKgyM+pZ7lwKKaWj/oz16quvxsSJE2PTpk0xadKkeO211+L000+PF198Mb70pS91nDdr1qw48cQT46GHHuryPkqlUixcuLDL8RUrVsSIESOOdmkAAFn27dsXc+fOjd27d0dDQ8MRzzvqaEopxaxZs+K9996L5557LiIi1q1bFxdeeGG8+eab0dzc3HHuddddF2+88UasWrWqy/vp7pmmcePGxa5du3pceF9rb2+PlpaWmD59etTV1dVsHQNZtWY0qdR1Xxxr/lm6vNvjx9I+qsXHoTgkxS8mH4i7NwyJ8oFCVd7nkT4Wx6pjaQ/VihlVZkY9a2tri9GjR1eMpl69PHeom266KV566aX461//2uW2QqHzg19Kqcuxg4rFYhSLxS7H6+rqBsQHdqCsYyD7pDMq76/OJ8taqvT3Pxb2US0/DuUDhard/0Cf89E6FvZQrZlRZWbUvdyZHNWPHLj55pvjiSeeiGeeeSZOOeWUjuONjY0REbFjx45O5+/cuTPGjh17NHcFADAg9CqaUkpx0003xcqVK+Ppp5+OCRMmdLp9woQJ0djYGC0tLR3HPvroo1i7dm1MnTq1OisGAKiBXr08d+ONN8aKFSvij3/8Y9TX13c8ozRy5MgYPnx4FAqFuOWWW2LRokUxceLEmDhxYixatChGjBgRc+fO7ZO/AABAf+hVNC1fvjwiIqZNm9bp+IMPPhjXXHNNRETcdttt8cEHH8QNN9wQ7733Xpx//vmxevXqqK+vr8qCAQBqoVfRlPONdoVCIUqlUpRKpaNdEwDAgON3zwEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQYVitFwCfBp+//U/dHi8OTbH0yxGTSquivL/Qz6sanI70sTiWvL7kylovAeiGZ5oAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACBDr6Pp2Wefjauuuiqam5ujUCjE448/3un2a665JgqFQqfLBRdcUK31AgDURK+jae/evXHOOefEsmXLjnjOFVdcEdu3b++4PPnkk59okQAAtTast28wc+bMmDlzZo/nFIvFaGxsPOpFAQAMNL2Ophxr1qyJMWPGxIknnhgXX3xx/PKXv4wxY8Z0e265XI5yudxxva2tLSIi2tvbo729vS+Wl+XgfddyDQNdtWZUHJqqsZwBqTgkdfovnZlP9w79N+WxqDIzqsyMepY7l0JK6agfrQqFQjz22GMxe/bsjmOPPvponHDCCTF+/PhobW2Nu+++Oz7++ON44YUXolgsdnkfpVIpFi5c2OX4ihUrYsSIEUe7NACALPv27Yu5c+fG7t27o6Gh4YjnVT2aDrd9+/YYP358PPLIIzFnzpwut3f3TNO4ceNi165dPS68r7W3t0dLS0tMnz496urqaraOgaxaM5pUWlXFVQ0sxSEpfjH5QNy9YUiUDxRqvZwBx3y698/S5R1/9lhUmRlVZkY9a2tri9GjR1eMpj55ee5QTU1NMX78+NiyZUu3txeLxW6fgaqrqxsQH9iBso6B7JPOqLz/0//JsnygMCj+nkfLfDrr7t+Tx6LKzKgyM+pe7kz6/Oc0vfPOO7Ft27Zoamrq67sCAOgzvX6m6f33349XX32143pra2ts3LgxRo0aFaNGjYpSqRTf/OY3o6mpKV5//fW48847Y/To0fGNb3yjqgsHAOhPvY6mDRs2xCWXXNJxff78+RERMW/evFi+fHls2rQpHn744fjPf/4TTU1Ncckll8Sjjz4a9fX11Vs1AEA/63U0TZs2LXr62vFVqz69X9QLAAxefvccAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQIZeR9Ozzz4bV111VTQ3N0ehUIjHH3+80+0ppSiVStHc3BzDhw+PadOmxebNm6u1XgCAmuh1NO3duzfOOeecWLZsWbe3L126NO69995YtmxZrF+/PhobG2P69OmxZ8+eT7xYAIBaGdbbN5g5c2bMnDmz29tSSnHffffFXXfdFXPmzImIiIceeijGjh0bK1asiOuvv/6TrRYAoEZ6HU09aW1tjR07dsSMGTM6jhWLxbj44otj3bp13UZTuVyOcrnccb2trS0iItrb26O9vb2ay+uVg/ddyzUMdNWaUXFoqsZyBqTikNTpv3RmPt079N+Ux6LKzKgyM+pZ7lwKKaWjfrQqFArx2GOPxezZsyMiYt26dXHhhRfGm2++Gc3NzR3nXXfddfHGG2/EqlWruryPUqkUCxcu7HJ8xYoVMWLEiKNdGgBAln379sXcuXNj9+7d0dDQcMTzqvpM00GFQqHT9ZRSl2MH3XHHHTF//vyO621tbTFu3LiYMWNGjwvva+3t7dHS0hLTp0+Purq6mq2jJ5NKXSO0PxWHpPjF5ANx94YhUT7Q/cd3sDOjnplP9/5Zurzjz8fCY1GtmVFlZtSzg69yVVLVaGpsbIyIiB07dkRTU1PH8Z07d8bYsWO7fZtisRjFYrHL8bq6ugHxgR0o6+hOef/A+CRTPlAYMGsZqMyoZ+bTWXePOQP5sWigMKPKzKh7uTOp6s9pmjBhQjQ2NkZLS0vHsY8++ijWrl0bU6dOreZdAQD0q14/0/T+++/Hq6++2nG9tbU1Nm7cGKNGjYpTTz01brnllli0aFFMnDgxJk6cGIsWLYoRI0bE3Llzq7pwAID+1Oto2rBhQ1xyySUd1w9+PdK8efPi97//fdx2223xwQcfxA033BDvvfdenH/++bF69eqor6+v3qoBAPpZr6Np2rRp0dM33BUKhSiVSlEqlT7JugAABhS/ew4AIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAyiCQAgw7BaLwCAzj5/+586/lwcmmLplyMmlVZFeX+hhqvqndeXXFnrJUDVeaYJACCDaAIAyCCaAAAyiCYAgAyiCQAgg2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADJUPZpKpVIUCoVOl8bGxmrfDQBAv+qTX9h75plnxl/+8peO60OHDu2LuwEA6Dd9Ek3Dhg3z7BIA8KnSJ9G0ZcuWaG5ujmKxGOeff34sWrQoTjvttG7PLZfLUS6XO663tbVFRER7e3u0t7f3xfKyHLzvWq6hkuLQVNv7H5I6/ZeuzKhn5lPZsTqj/nzsPBYer2vNjHqWO5dCSqmq/xKfeuqp2LdvX5xxxhnx9ttvxz333BP/+te/YvPmzXHSSSd1Ob9UKsXChQu7HF+xYkWMGDGimksDAOhi3759MXfu3Ni9e3c0NDQc8byqR9Ph9u7dG6effnrcdtttMX/+/C63d/dM07hx42LXrl09Lryvtbe3R0tLS0yfPj3q6upqto6eTCqtqun9F4ek+MXkA3H3hiFRPlCo6VoGKjPqmflUZkaV9eWM/lm6vKrvr1aOhc9ptdTW1hajR4+uGE198vLcoY4//vg466yzYsuWLd3eXiwWo1gsdjleV1c3ID6wA2Ud3SnvHxgPoOUDhQGzloHKjHpmPpWZUWV9MaOB+vh/tAby57Rayp1Jn/+cpnK5HC+//HI0NTX19V0BAPSZqkfTz3/+81i7dm20trbG3//+9/jWt74VbW1tMW/evGrfFQBAv6n6y3P//ve/4+qrr45du3bFySefHBdccEE8//zzMX78+GrfFQBAv6l6ND3yyCPVfpcAADXnd88BAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZBBNAAAZRBMAQAbRBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBhWK0XUCufv/1PPd5eHJpi6ZcjJpVWRXl/oZ9WBQDV9fnb/3TMf057fcmVtV5CRHimCQAgi2gCAMggmgAAMogmAIAMogkAIINoAgDIIJoAADKIJgCADKIJACCDaAIAyCCaAAAyiCYAgAx9Fk33339/TJgwIT7zmc/EueeeG88991xf3RUAQJ/rk2h69NFH45Zbbom77ror/vGPf8RXv/rVmDlzZmzdurUv7g4AoM8N64t3eu+998YPf/jDuPbaayMi4r777otVq1bF8uXLY/HixZ3OLZfLUS6XO67v3r07IiLefffdaG9v74vlRUTEsI/39nz7gRT79h2IYe1DYv+BQp+t41hmRpWZUc/MpzIzqqwvZ/TOO+9U9f3VwrCP9x7z+6ivPw579uyJiIiUUs8npiorl8tp6NChaeXKlZ2O//SnP00XXXRRl/MXLFiQIsLFxcXFxcXFpaaXbdu29dg4VX+madeuXbF///4YO3Zsp+Njx46NHTt2dDn/jjvuiPnz53dcP3DgQLz77rtx0kknRaFQuxpua2uLcePGxbZt26KhoaFm6xjIzKgyM+qZ+VRmRpWZUWVm1LOUUuzZsyeam5t7PK9PXp6LiC7Bk1LqNoKKxWIUi8VOx0488cS+WlavNTQ02GAVmFFlZtQz86nMjCozo8rM6MhGjhxZ8ZyqfyH46NGjY+jQoV2eVdq5c2eXZ58AAI4VVY+m4447Ls4999xoaWnpdLylpSWmTp1a7bsDAOgXffLy3Pz58+P73/9+TJ48OaZMmRIPPPBAbN26NX784x/3xd31iWKxGAsWLOjy0iH/Y0aVmVHPzKcyM6rMjCozo+oopFTp++uOzv333x9Lly6N7du3x6RJk+LXv/51XHTRRX1xVwAAfa7PogkA4NPE754DAMggmgAAMogmAIAMogkAIMOgjqbFixfHeeedF/X19TFmzJiYPXt2vPLKK53Oueaaa6JQKHS6XHDBBTVacf9bvnx5nH322R0/RXbKlCnx1FNPddyeUopSqRTNzc0xfPjwmDZtWmzevLmGK+5/lWY02PfQ4RYvXhyFQiFuueWWjmP2UWfdzWiw76NSqdTl79/Y2Nhxuz1UeUaDfQ9Vw6COprVr18aNN94Yzz//fLS0tMTHH38cM2bMiL1793Y674orrojt27d3XJ588skarbj/nXLKKbFkyZLYsGFDbNiwIS699NKYNWtWx4PR0qVL4957741ly5bF+vXro7GxMaZPn97xG6MHg0ozihjce+hQ69evjwceeCDOPvvsTsfto/850owi7KMzzzyz099/06ZNHbfZQ//V04wi7KFPrMdf5zvI7Ny5M0VEWrt2bcexefPmpVmzZtVuUQPQZz/72fS73/0uHThwIDU2NqYlS5Z03Pbhhx+mkSNHpt/+9rc1XGHtHZxRSvbQQXv27EkTJ05MLS0t6eKLL04/+9nPUkrJPjrEkWaUkn20YMGCdM4553R7mz30Xz3NKCV7qBoG9TNNh9u9e3dERIwaNarT8TVr1sSYMWPijDPOiB/96Eexc+fOWiyv5vbv3x+PPPJI7N27N6ZMmRKtra2xY8eOmDFjRsc5xWIxLr744li3bl0NV1o7h8/oIHso4sYbb4wrr7wyvva1r3U6bh/9z5FmdNBg30dbtmyJ5ubmmDBhQnz3u9+N1157LSLsoUMdaUYHDfY99En1ya9RORallGL+/Pnxla98JSZNmtRxfObMmfHtb387xo8fH62trXH33XfHpZdeGi+88MKg+XH0mzZtiilTpsSHH34YJ5xwQjz22GPxxS9+sePB6PBfxDx27Nh44403arHUmjnSjCLsoYiIRx55JF588cVYv359l9sO/nLvwb6PeppRhH10/vnnx8MPPxxnnHFGvP3223HPPffE1KlTY/PmzfbQ/9fTjE466aRBv4eqotZPdQ0UN9xwQxo/fnzatm1bj+e99dZbqa6uLv3hD3/op5XVXrlcTlu2bEnr169Pt99+exo9enTavHlz+tvf/pYiIr311ludzr/22mvT5ZdfXqPV1saRZtSdwbaHtm7dmsaMGZM2btzYcezQl57so8oz6s5g20eHe//999PYsWPTr371K3voCA6dUXcG+x46Gl6ei4ibb745nnjiiXjmmWfilFNO6fHcpqamGD9+fGzZsqWfVld7xx13XHzhC1+IyZMnx+LFi+Occ86J3/zmNx3flXHw//IO2rlzZ5f/4/u0O9KMujPY9tALL7wQO3fujHPPPTeGDRsWw4YNi7Vr18b//d//xbBhwzr2ymDeR5VmtH///i5vM9j20eGOP/74OOuss2LLli0ei47g0Bl1Z7DvoaMxqKMppRQ33XRTrFy5Mp5++umYMGFCxbd55513Ytu2bdHU1NQPKxyYUkpRLpdjwoQJ0djYGC0tLR23ffTRR7F27dqYOnVqDVdYewdn1J3Btocuu+yy2LRpU2zcuLHjMnny5Pje974XGzdujNNOO23Q76NKMxo6dGiXtxls++hw5XI5Xn755WhqavJYdASHzqg7g30PHZUaP9NVUz/5yU/SyJEj05o1a9L27ds7Lvv27Usp/fc7WW699da0bt261Nramp555pk0ZcqU9LnPfS61tbXVePX944477kjPPvtsam1tTS+99FK6884705AhQ9Lq1atTSiktWbIkjRw5Mq1cuTJt2rQpXX311ampqWnQzCelnmdkD3Xv8Jee7KOuDp2RfZTSrbfemtasWZNee+219Pzzz6evf/3rqb6+Pr3++uspJXsopZ5nZA9Vx6COpojo9vLggw+mlFLat29fmjFjRjr55JNTXV1dOvXUU9O8efPS1q1ba7vwfvSDH/wgjR8/Ph133HHp5JNPTpdddllHMKX032/1XbBgQWpsbEzFYjFddNFFadOmTTVccf/raUb2UPcOjyb7qKtDZ2QfpfSd73wnNTU1pbq6utTc3JzmzJnT6esG7aGeZ2QPVUchpZRq+UwXAMCxYFB/TRMAQC7RBACQQTQBAGQQTQAAGUQTAEAG0QQAkEE0AQBkEE0AABlEEwBABtEEAJBBNAEAZPh/O7S4O09TuY0AAAAASUVORK5CYII=",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Set seed to 104\n",
    "np.random.seed(104)\n",
    "\n",
    "sample_means = []\n",
    "# Loop 100 times\n",
    "for i in range(100):\n",
    "  # Take sample of 20 num_users\n",
    "  samp_20 = amir_deals['num_users'].sample(20, replace=True)\n",
    "  # Calculate mean of samp_20\n",
    "  samp_20_mean = np.mean(samp_20)\n",
    "  # Append samp_20_mean to sample_means\n",
    "  sample_means.append(samp_20_mean)\n",
    "  \n",
    "# Convert to Series and plot histogram\n",
    "sample_means_series = pd.Series(sample_means)\n",
    "sample_means_series.hist()\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **The mean of means**\n",
    "\n",
    "You want to know what the average number of users (num_users) is per deal, but you want to know this number for the entire company so that you can see if Amir's deals have more or fewer users than the company's average deal. The problem is that over the past year, the company has worked on more than ten thousand deals, so it's not realistic to compile all the data. Instead, you'll estimate the mean by taking several random samples of deals, since this is much easier than collecting data from everyone in the company."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 30,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 10548 entries, 0 to 10547\n",
      "Data columns (total 3 columns):\n",
      " #   Column      Non-Null Count  Dtype\n",
      "---  ------      --------------  -----\n",
      " 0   Unnamed: 0  10548 non-null  int64\n",
      " 1   product     10548 non-null  int64\n",
      " 2   num_users   10548 non-null  int64\n",
      "dtypes: int64(3)\n",
      "memory usage: 329.6 KB\n"
     ]
    }
   ],
   "source": [
    "all_deals = pd.read_csv('./datasets/all_deals.csv', index_col=0)\n",
    "all_deals.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 32,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "38.31333333333332\n",
      "37.651685393258425\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\" Amir's average number of users is very close to the overall average, so it looks like he's meeting expectations. Make sure to note this in his performance review! \""
      ]
     },
     "execution_count": 32,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Set seed to 321\n",
    "np.random.seed(321)\n",
    "\n",
    "sample_means = []\n",
    "# Loop 30 times to take 30 means\n",
    "for i in range(30):\n",
    "  # Take sample of size 20 from num_users col of all_deals with replacement\n",
    "  cur_sample = all_deals['num_users'].sample(20, replace=True)\n",
    "  # Take mean of cur_sample\n",
    "  cur_mean = np.mean(cur_sample)\n",
    "  # Append cur_mean to sample_means\n",
    "  sample_means.append(cur_mean)\n",
    "\n",
    "# Print mean of sample_means\n",
    "print(np.mean(sample_means))\n",
    "\n",
    "# Print mean of num_users in amir_deals\n",
    "print(np.mean(amir_deals['num_users']))\n",
    "\"\"\" Amir's average number of users is very close to the overall average, so it looks like he's meeting expectations. Make sure to note this in his performance review! \"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### The Poisson distribution\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Identifying lambda**\n",
    "Now that you've learned about the Poisson distribution, you know that its shape is described by a value called lambda. In this exercise, you'll match histograms to lambda values.\n",
    "\n",
    "Instructions:<br>\n",
    "\n",
    "Match each Poisson distribution to its lambda value.\n",
    "\n",
    "Ans: <br>\n",
    "\n",
    "![](./images/identify_lambda.png)\n",
    "\n",
    " The Poisson distribution is a family of distributions, just like the uniform, binomial, or normal distributions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Tracking lead responses**\n",
    "\n",
    "Your company uses sales software to keep track of new sales leads. It organizes them into a queue so that anyone can follow up on one when they have a bit of free time. Since the number of lead responses is a countable outcome over a period of time, this scenario corresponds to a Poisson distribution. On average, Amir responds to 4 leads each day. In this exercise, you'll calculate probabilities of Amir responding to different numbers of leads.\n",
    "\n",
    "Instructions: <br>\n",
    "\n",
    "- Import poisson from scipy.stats and calculate the probability that Amir responds to 5 leads in a day, given that he responds to an average of 4.\n",
    "- Amir's coworker responds to an average of 5.5 leads per day. What is the probability that she answers 5 leads in a day?\n",
    "- What's the probability that Amir responds to 2 or fewer leads in a day?\n",
    "- What's the probability that Amir responds to more than 10 leads in a day?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 34,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.1562934518505317\n"
     ]
    }
   ],
   "source": [
    "# Import poisson from scipy.stats\n",
    "from scipy.stats import poisson\n",
    "\n",
    "# Probability of 5 responses\n",
    "prob_5 = poisson.pmf(5,4)\n",
    "\n",
    "print(prob_5)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 35,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.17140068409793663\n"
     ]
    }
   ],
   "source": [
    "# Probability of 5 responses\n",
    "prob_coworker =poisson.pmf(5,5.5)\n",
    "\n",
    "print(prob_coworker)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 36,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.23810330555354436\n"
     ]
    }
   ],
   "source": [
    "# Probability of 2 or fewer responses\n",
    "prob_2_or_less = poisson.cdf(2,4)\n",
    "\n",
    "\n",
    "print(prob_2_or_less)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 37,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.0028397661205137315\n"
     ]
    }
   ],
   "source": [
    "# Probability of > 10 responses\n",
    "prob_over_10 = 1 - poisson.cdf(10,4)\n",
    "\n",
    "print(prob_over_10)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Note that if you provide poisson.pmf() or poisson.cdf() with a non-integer, it throws an error since the Poisson distribution only applies to integers."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### More probability distributions\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Distribution dragging and dropping**\n",
    "\n",
    "By this point, you've learned about so many different probability distributions that it can be difficult to remember which is which. In this exercise, you'll practice distinguishing between distributions and identifying the distribution that best matches different scenarios.\n",
    "\n",
    "![](./images/distributions2.png)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Modeling time between leads**\n",
    "\n",
    "To further evaluate Amir's performance, you want to know how much time it takes him to respond to a lead after he opens it. On average, it takes 2.5 hours for him to respond. In this exercise, you'll calculate probabilities of different amounts of time passing between Amir receiving a lead and sending a response.\n",
    "\n",
    "Instructions:<br>\n",
    "\n",
    "- Import expon from scipy.stats. What's the probability it takes Amir less than an hour to respond to a lead?\n",
    "- What's the probability it takes Amir more than 4 hours to respond to a lead?\n",
    "- What's the probability it takes Amir 3-4 hours to respond to a lead?"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 39,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.3296799539643607\n",
      "0.20189651799465536\n",
      "0.09929769391754684\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "\"There's only about a 20% chance it will take Amir more than 4 hours to respond, so he's pretty speedy in his responses.\""
      ]
     },
     "execution_count": 39,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Import expon from scipy.stats\n",
    "from scipy.stats import expon\n",
    "\n",
    "# Print probability response takes < 1 hour\n",
    "print(expon.cdf(1, scale=2.5))\n",
    "\n",
    "# Print probability response takes > 4 hours\n",
    "print(1 - expon.cdf(4,scale=2.5))\n",
    "\n",
    "# Print probability response takes 3-4 hours\n",
    "print(expon.cdf(4,scale=2.5) - expon.cdf(3,scale=2.5))\n",
    "\n",
    "\"\"\"There's only about a 20% chance it will take Amir more than 4 hours to respond, so he's pretty speedy in his responses.\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **The t-distribution**\n",
    "\n",
    "Which statement is not true regarding the t-distribution?\n",
    "\n",
    "\n",
    "Possible Answers\n",
    "\n",
    "- The t-distribution has thicker tails than the normal distribution.\n",
    "- A t-distribution with high degrees of freedom resembles the normal distribution.\n",
    "- The number of degrees of freedom affects the distribution's variance.\n",
    "- **The t-distribution is skewed.**"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "## Correlation and Experimental Design\n",
    "\n",
    "> In this chapter, you'll learn how to quantify the strength of a linear relationship between two variables, and explore how confounding variables can affect the relationship between two other variables. You'll also see how a study’s design can influence its results, change how the data should be analyzed, and potentially affect the reliability of your conclusions."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correlation\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Guess the correlation**\n",
    "\n",
    "On the right, use the scatterplot to estimate what the correlation is between the variables x and y. Once you've guessed it correctly, use the New Plot button to try out a few more scatterplots. When you're ready, answer the question below to continue to the next exercise.\n",
    "\n",
    "Which of the following statements is NOT true about correlation?\n",
    "\n",
    "Instructions: <br>\n",
    "\n",
    "- If the correlation between x and y has a high magnitude, the data points will be clustered closely around a line.\n",
    "- Correlation can be written as r.\n",
    "- If x and y are negatively correlated, values of y decrease as values of x increase.\n",
    "- **Correlation cannot be 0.**\n",
    "\n",
    "*When correlation is 0, that means there is no relationship between two variables and the points appear to be randomly scattered.*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Relationships between variables**\n",
    "\n",
    "In this chapter, you'll be working with a dataset world_happiness containing results from the 2019 [World Happiness Report](https://worldhappiness.report/ed/2019/). The report scores various countries based on how happy people in that country are. It also ranks each country on various societal aspects such as social support, freedom, corruption, and others. The dataset also includes the GDP per capita and life expectancy for each country.\n",
    "\n",
    "In this exercise, you'll examine the relationship between a country's life expectancy (life_exp) and happiness score (happiness_score) both visually and quantitatively. seaborn as sns, matplotlib.pyplot as plt, and pandas as pd are loaded and world_happiness is available."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 42,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 143 entries, 1 to 143\n",
      "Data columns (total 8 columns):\n",
      " #   Column           Non-Null Count  Dtype  \n",
      "---  ------           --------------  -----  \n",
      " 0   country          143 non-null    object \n",
      " 1   social_support   142 non-null    float64\n",
      " 2   freedom          142 non-null    float64\n",
      " 3   corruption       135 non-null    float64\n",
      " 4   generosity       142 non-null    float64\n",
      " 5   gdp_per_cap      143 non-null    int64  \n",
      " 6   life_exp         143 non-null    float64\n",
      " 7   happiness_score  143 non-null    int64  \n",
      "dtypes: float64(5), int64(2), object(1)\n",
      "memory usage: 10.1+ KB\n"
     ]
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "world_happiness = pd.read_csv('./datasets/world_happiness.csv', index_col=0)\n",
    "world_happiness.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 43,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    }
   ],
   "source": [
    "# Create a scatterplot of happiness_score vs. life_exp and show\n",
    "sns.scatterplot(x='life_exp', y='happiness_score', data=world_happiness)\n",
    "\n",
    "# Show plot\n",
    "plt.show()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 45,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 500x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7802249053272062\n"
     ]
    }
   ],
   "source": [
    "# Create scatterplot of happiness_score vs life_exp with trendline\n",
    "sns.lmplot(x='life_exp', y='happiness_score', data=world_happiness, ci=None)\n",
    "\n",
    "# Show plot\n",
    "plt.show()\n",
    "\n",
    "# Correlation between life_exp and happiness_score\n",
    "cor = world_happiness['life_exp'].corr(world_happiness['happiness_score'])\n",
    "\n",
    "print(cor)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "Based on the scatterplot, which is most likely the correlation between life_exp and happiness_score? <br>\n",
    "\n",
    "*Ans: 0.8*"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Correlation caveats\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **What can't correlation measure?**\n",
    "\n",
    "While the correlation coefficient is a convenient way to quantify the strength of a relationship between two variables, it's far from perfect. In this exercise, you'll explore one of the caveats of the correlation coefficient by examining the relationship between a country's GDP per capita (gdp_per_cap) and happiness score."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 46,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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o5GUlITHH38clZWVxvNDhw7FtGnTUFhYCKVSieHDh9t975qaGjz99NNISkpCREQEsrKy8MknnwAAqqqqkJ+fjy5dukAul6Nv374oKioyeb3hPadNm4a4uDgkJCTg+eefB3egI/I/DGFE5HWFhYXYu3cvtmzZgm3btmH37t04evSo8fyECRNw4cIFfPXVV/jnP/+JN998ExUVFWb3mTdvHsaOHYvvvvsOjz32GPLz83Hq1CmH2/Hss8/ij3/8I9RqNQYNGoQHH3wQVVVVAIArV64gLy8P/fv3x+HDh/Gf//wHV69exa9//WuTe6xduxZhYWHYu3cv/v73v9t8v9bWVowcORL79u3D+vXr8f3332Pp0qUIDQ0FADQ0NOCWW27BJ598ghMnTuDpp5/G448/joMHD1p8z4MHD2LFihV49dVX8b//+78Of24i8hEibyBOREFGq9UK4eHhwocffmg8VlNTI8jlcmHmzJnC6dOnBQDCgQMHjOdPnTolABBeffVV4zEAwuTJk03uPXDgQOH3v/+93TaUlJQIAISlS5cajzU1NQldunQRli1bJgiCIMybN08YMWKEyevKysoEAMLp06cFQRCEvLw8oX///g5/9i+++EIICQkxvt4R9913n/DHP/7R+H1eXp7Qu3dvobW11Xhs9uzZQu/evR2+JxH5BvaEEZFXnT9/Hk1NTbjtttuMxxQKBX71q18BAE6dOoWwsDAMGDDAeL5Xr16Ii4szu9cdd9xh9n1HesLavt7wnobXHzlyBF9//TWio6ONX7169QIAnDt3zvi6tu2059tvv0WXLl3Qs2dPi+dbWlqwaNEi9OvXDwkJCYiOjsbWrVtRWlpqct3tt98OiURi8jmKi4vR0tLicFuISHxhYjeAiIKL8N+5S21DRNvj1s47ytnXtX99a2srRo0ahWXLlpldk5KSYvzvqKgoh+8dGRlp8/wrr7yCV199Fa+99hr69u2LqKgozJo1ixP+iQIUe8KIyKt69OiB8PBwfPPNN8ZjWq0WxcXFAIDevXujubkZhw8fNp4/ffo0ampqzO514MABs+8NvVWOaPv65uZmHDlyxPj6m2++GSdPnkS3bt2QkZFh8tWR4NVWv3798OOPP+LMmTMWz+/evRsPPfQQHnvsMdx0003o3r278blYa7fh+8zMTOPcMiLyDwxhRORVMTExGD9+PJ599ll8/fXXOHnyJAoKChASEgKJRIJf/epXuPfeezFx4kQcPHgQR44cwe9+9zuLvUgffvghVq9ejTNnzuDFF1/EN998g2nTpjncljfeeAObN2/GDz/8gKlTp6K6uhoFBQUAgKlTp+Lnn39Gfn4+vvnmG5w/fx5bt25FQUGB08N+eXl5GDJkCMaOHYtt27ahpKQEn3/+Of7zn/8AADIyMrBt2zbs27cPp06dwqRJk1BeXm52n7KyMhQWFuL06dMoKirCypUrMXPmTKfaRETiYQgjIq9bvnw57rjjDjzwwAO4++67kZOTg969eyMiIgIAsGbNGqSlpSEvLw9jxozB008/jcTERLP7LFiwABs2bEC/fv2wdu1avP/++7jxxhsdbsfSpUuxbNky3HTTTdi9ezf+9a9/QalUAgBSU1Oxd+9etLS04J577kFWVhZmzpwJhUKBkBDn/+rctGkTbr31VuTn5+PGG2/Ec889Zwx18+bNw80334x77rkHQ4cORXJyMh5++GGzezzxxBOor6/HbbfdhqlTp2L69Ol4+umnnW4TEYlDIggsLkNE4rp27Ro6d+6MV155BU899ZRDr5FIJNi8ebPFkGLPhQsXoFKpoFar0b9//w6/XkxDhw5F//79uYUTUQDgxHwi8jq1Wo0ffvgBt912GzQaDRYuXAgAeOihh0RuGRGR93A4kohE8fLLL+Omm27C3XffjWvXrmH37t3GoUBXLV682KS0RNuvkSNHuuU9LHn//fetvm+fPn089r5E5J84HElEAefnn3/Gzz//bPFcZGQkOnfu7JH3ra2txdWrVy2eCw8PR3p6ukfel4j8E0MYERERkQg4HElEREQkAoYwIiIiIhEwhBERERGJgCGMiIiISAQMYUREREQiYAgjIiIiEgFDGBEREZEIGMKIiIiIRPD/AQNOBRMAtjY5AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.7019547642148012\n"
     ]
    }
   ],
   "source": [
    "# Scatterplot of gdp_per_cap and life_exp\n",
    "sns.scatterplot(x='gdp_per_cap', y='life_exp', data=world_happiness)\n",
    "\n",
    "# Show plot\n",
    "plt.show()\n",
    "  \n",
    "# Correlation between gdp_per_cap and life_exp\n",
    "cor = world_happiness['gdp_per_cap'].corr(world_happiness['life_exp'])\n",
    "\n",
    "print(cor)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "The correlation between GDP per capita and life expectancy is 0.7. Why is correlation not the best way to measure the relationship between these two variables?\n",
    "\n",
    "Possible Answers: <br>\n",
    "\n",
    "- Correlation measures how one variable affects another.\n",
    "\n",
    "- **Correlation only measures linear relationships.**\n",
    "\n",
    "- Correlation cannot properly measure relationships between numeric variables."
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Transforming variables**\n",
    "\n",
    "When variables have skewed distributions, they often require a transformation in order to form a linear relationship with another variable so that correlation can be computed. In this exercise, you'll perform a transformation yourself.\n",
    "\n",
    "pandas as pd, numpy as np, matplotlib.pyplot as plt, and seaborn as sns are imported, and world_happiness is loaded.\n",
    "\n",
    "Instructions:<br>\n",
    "\n",
    "- Create a scatterplot of happiness_score versus gdp_per_cap and calculate the correlation between them.\n",
    "- Add a new column to world_happiness called log_gdp_per_cap that contains the log of gdp_per_cap.\n",
    "- Create a seaborn scatterplot of log_gdp_per_cap and happiness_score and calculate the correlation between them."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 47,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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L7wAnhhI5HoYqBGRLKWlpSE7Oxsff/wxMjMzceDAAeTl5Yn3H3vsMfz000/Yt28f/v3vf2Pt2rUoLS1t8jmLFi3Cfffdh++++w6PPPIIJk6ciFOnTlk8j7lz52LOnDnIz89HQkICxo8fjytXrgAALl26hKSkJPTt2xdHjhzBF198gV9++QUPPPCA0Wds2rQJ3t7eyM7Oxttvv93s99XX12P06NHIycnB5s2bcfLkSSxfvhxeXl4AgOvXr6N///749NNPUVBQgKeeegqTJ0/Gt99+a/I7v/32W7z++ut47bXX8I9//MPi35uIZMLJh8ITETWh0+kEHx8f4cMPPxSvlZeXC2q1Wpg9e7Zw+vRpAYDw3//+V7x/6tQpAYDw2muvidcACE8//bTRZ992223CM8880+IcioqKBADC8uXLxWs1NTVCx44dhRUrVgiCIAiLFi0SRo4cafS+4uJiAYBw+vRpQRAEISkpSejbt6/Fv/uXX34ptGnTRny/Je6++25hzpw54uukpCShe/fuQn19vXjt+eefF7p3727xZxKRPDCjRkSy8+OPP6Kmpga33nqreE2j0eDmm28GAJw6dQre3t4YMGCAeP+WW25Bu3btmnzW7bff3uS1NRm1hu83fKfh/bm5ufjqq6/g7+8v/txyyy0AgLNnz4rvazjPlhw9ehQdO3bETTfdZPJ+XV0dli1bht69eyMkJAT+/v7YvXs3zp8/bzTu//7v/6BQKIx+jx9++AF1dXUWz4WInM/b2RMgImpM+F8tVcNAo+F1c/ctZev7Gr+/vr4e48aNw4oVK5qMad++vfjPfn5+Fn+2r69vs/dfffVVvPbaa1i9ejV69eoFPz8/pKamcpMCkZtiRo2IZKdr167w8fHBoUOHxGs6nQ4//PADAKB79+6ora3FkSNHxPunT59GeXl5k8/673//2+S1IetliYbvr62tRW5urvj+fv364cSJE+jcuTO6detm9GNNcNZQ79698fPPP+PMmTMm7x84cAD33HMPHnnkEfTp0wddunQRn4u5eRtex8bGirVuROQaGKgRkewEBARgypQpmDt3Lr766iucOHECycnJaNOmDRQKBW6++WbcddddePLJJ/Htt98iNzcXTzzxhMls1Icffoj169fjzJkzePHFF3Ho0CGkpKRYPJc333wTO3fuxPfff48ZM2agrKwMycnJAIAZM2bgt99+w8SJE3Ho0CH8+OOP2L17N5KTk21eYkxKSsLgwYNx3333ITMzE0VFRfj888/xxRdfAAC6deuGzMxM5OTk4NSpU5g2bRpKSkqafE5xcTHS0tJw+vRpbN26FW+88QZmz55t05yIyHkYqBGRLK1atQq33347xo4di+HDh2PQoEHo3r072rZtCwDYsGEDoqKikJSUhAkTJuCpp55CWFhYk89ZsmQJtm3bht69e2PTpk14//330aNHD4vnsXz5cqxYsQJ9+vTBgQMH8NFHHyE0NBQAEBkZiezsbNTV1WHUqFGIi4vD7NmzodFo0KaN7f953b59OwYOHIiJEyeiR48emDdvnhj4LVq0CP369cOoUaMwZMgQRERE4N57723yGY8++iiqqqpw6623YsaMGZg5cyaeeuopm+dERM6hEAQ21iEi+bt27Ro6dOiAV199FVOnTrXoPQqFAjt37jQZyLTkp59+QkxMDPLz89G3b1+r3+9MQ4YMQd++fXmcFpEb4GYCIpKl/Px8fP/997j11luh1WqxdOlSAMA999zj5JkRETkOlz6JSLZeeeUV9OnTB8OHD8e1a9dw4MABcdmxtdLT043aajT8GT16tCTfYcr7779v9nt79uxpt+8lItfEpU8i8ki//fYbfvvtN5P3fH190aFDB7t879WrV/HLL7+YvOfj44NOnTrZ5XuJyDUxUCMiIiKSKS59EhEREckUAzUiIiIimWKgRkRERCRTDNSIiIiIZIqBGhEREZFMMVAjIiIikikGakREREQyxUCNiIiISKb+H5dZc5N8XBTcAAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.727973301222298\n"
     ]
    }
   ],
   "source": [
    "# Scatterplot of happiness_score vs. gdp_per_cap\n",
    "sns.scatterplot(x='gdp_per_cap', y='happiness_score', data=world_happiness)\n",
    "plt.show()\n",
    "\n",
    "# Calculate correlation\n",
    "cor = world_happiness['gdp_per_cap'].corr(world_happiness['happiness_score'])\n",
    "print(cor)"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 51,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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vP4qbxk2q+Pnw0SSiIhEoftELTg4GF5eXlXSs9zc3CopWwWz2Qyz2eyO5amGjeXyMZEkIiK90H2i5uPjg44dO2LHjh0O13fs2IH4+HiNVuUebCyXh4kkERHphe4TNQBITEzE008/jU6dOqFLly547733cP78ebzwwgtaL40ExUSSiIj0wBCF2rBhw3D16lXMnz8fly9fRtu2bbF161Y0b95c66WRwES9gTwREVEFkyRJtR+B8wA2mw0WiwVWqxWBgYFaL4eIiIgMztnaQ/c9akRERERGxUKNiIiISFAs1IiIiIgExUKNiIiISFAs1IiIiIgExUKNiIiISFAs1IiIiIgExUKNiIiISFAs1IiIiIgExUKNiIiISFCGuNenqyruomWz2TReCREREXmCipqjrjt5slADcP36dQBAZGSkxishIiIiT3L9+nVYLJYan+dN2QGUl5fj0qVLCAgIgMlk0no5umCz2RAZGYkLFy7wRvZuxp+9dviz1w5/9triz195kiTh+vXriIiIQIMGNXeiMVED0KBBA9x5551aL0OXAgMD+S+tRviz1w5/9trhz15b/Pkrq7YkrQIPExAREREJioUaERERkaBYqJEsZrMZr7zyCsxms9ZL8Tj82WuHP3vt8GevLf78tcPDBERERESCYqJGREREJCgWakRERESCYqFGREREJCgWakRERESCYqFG9dKiRQuYTKYqXxMnTtR6aYZXWlqKl19+GdHR0fD19UXLli0xf/58lJeXa700j3D9+nUkJCSgefPm8PX1RXx8PA4cOKD1sgxnz549GDRoECIiImAymbBlyxaH5yVJwty5cxEREQFfX1/07NkTx48f12axBlPXz37Tpk3o168fgoODYTKZcOTIEU3W6WlYqFG9HDhwAJcvX7Z/7dixAwDwxz/+UeOVGd+iRYuwfPlypKen4+TJk0hNTcXrr7+OJUuWaL00jzBu3Djs2LEDq1evxvfff4++ffuid+/euHjxotZLM5QbN26gffv2SE9Pr/b51NRUpKWlIT09HQcOHEBYWBj69Oljv2czyVfXz/7GjRvo2rUrXnvtNTevzLNxPAe5JCEhAZ9++il++OEH3idVZQMHDkRoaCg++OAD+7XHH38cfn5+WL16tYYrM77CwkIEBATgn//8JwYMGGC/3qFDBwwcOBALFizQcHXGZTKZsHnzZgwZMgTArTQtIiICCQkJmDlzJgCgqKgIoaGhWLRoEcaPH6/hao3l9p99ZT/99BOio6Nx+PBhdOjQwe1r8zRM1Ei24uJirFmzBmPGjGGR5gbdunXDrl27cPr0aQDAd999h3379uHRRx/VeGXGV1pairKyMjRq1Mjhuq+vL/bt26fRqjxPdnY2cnJy0LdvX/s1s9mMHj16IDMzU8OVEamHN2Un2bZs2YJr165h9OjRWi/FI8ycORNWqxV33303vLy8UFZWhoULF2LEiBFaL83wAgIC0KVLF7z66qto06YNQkNDsW7dOnzzzTeIjY3VenkeIycnBwAQGhrqcD00NBTnzp3TYklEqmOiRrJ98MEH6N+/PyIiIrReikf46KOPsGbNGqxduxaHDh3CqlWr8MYbb2DVqlVaL80jrF69GpIk4Y477oDZbMbbb7+NkSNHwsvLS+uleZzbE3xJkpjqk2ExUSNZzp07h507d2LTpk1aL8VjTJ8+HbNmzcLw4cMBAO3atcO5c+eQkpKCUaNGabw642vVqhUyMjJw48YN2Gw2hIeHY9iwYYiOjtZ6aR4jLCwMwK1kLTw83H49Nze3SspGZBRM1EiWFStWICQkxKGxmtRVUFCABg0c/5X18vLieA438/f3R3h4OPLy8rBt2zYMHjxY6yV5jOjoaISFhdlPmwO3emUzMjIQHx+v4cqI1MNEjeqtvLwcK1aswKhRo9CwIf8RcpdBgwZh4cKFiIqKwr333ovDhw8jLS0NY8aM0XppHmHbtm2QJAmtW7fGmTNnMH36dLRu3RrPPvus1kszlPz8fJw5c8b+ODs7G0eOHEGzZs0QFRWFhIQEJCcnIzY2FrGxsUhOToafnx9Gjhyp4aqNoa6f/a+//orz58/j0qVLAIBTp04BuJV0VqSdpAKJqJ62bdsmAZBOnTql9VI8is1mk6ZMmSJFRUVJjRo1klq2bCnNnj1bKioq0nppHuGjjz6SWrZsKfn4+EhhYWHSxIkTpWvXrmm9LMP58ssvJQBVvkaNGiVJkiSVl5dLr7zyihQWFiaZzWape/fu0vfff6/tog2irp/9ihUrqn3+lVde0XTdRsc5akRERESCYo8aERERkaBYqBEREREJioUaERERkaBYqBEREREJioUaERERkaBYqBEREREJioUaERERkaBYqBGRanr27ImEhAStl1Gr0aNHY8iQIVovg4ioWizUiIiIiATFQo2ISHAlJSVaL4GINMJCjYjcIi8vD8888wyaNm0KPz8/9O/fHz/88IPDa95//31ERkbCz88Pf/jDH5CWloYmTZo4/T0WLFiAkJAQBAQEYNy4cZg1axY6dOhgf76srAyJiYlo0qQJgoKCMGPGDNx+F72ePXti0qRJmDRpkv11L7/8cpXX1aRFixZ49dVXMXLkSDRu3BgRERFYsmSJw2usViuef/55hISEIDAwEA8//DC+++47+/Nz585Fhw4d8OGHH6Jly5Ywm811fv/y8nIsWrQIMTExMJvNiIqKwsKFC+3Pz5w5E3fddRf8/PzQsmVLzJkzx6EArPie7777rv3vwR//+Edcu3bNqT83EamDhRoRucXo0aNx8OBB/Otf/8LXX38NSZLw6KOP2ouF/fv344UXXsCUKVNw5MgR9OnTx6HQqMvf//53LFy4EIsWLUJWVhaioqKwbNkyh9e8+eab+PDDD/HBBx9g3759+PXXX7F58+Yqn7Vq1So0bNgQ33zzDd5++2289dZb+Otf/+r0Wl5//XXcd999OHToEJKSkjB16lTs2LEDACBJEgYMGICcnBxs3boVWVlZuP/++9GrVy/8+uuv9s84c+YMNmzYgI0bN+LIkSN1fs+kpCQsWrQIc+bMwYkTJ7B27VqEhobanw8ICMDKlStx4sQJ/OUvf8H777+Pt956y+EzKr7nJ598gi+++AJHjhzBxIkTnf5zE5EKNLwhPBEZXI8ePaQpU6ZIp0+flgBI+/fvtz935coVydfXV9qwYYMkSZI0bNgwacCAAQ7vf+qppySLxeLU9+rcubM0ceJEh2tdu3aV2rdvb38cHh4uvfbaa/bHJSUl0p133ikNHjzYYc1t2rSRysvL7ddmzpwptWnTxql1NG/eXHrkkUccrg0bNkzq37+/JEmStGvXLikwMFC6efOmw2tatWolvfvuu5IkSdIrr7wieXt7S7m5uU59T5vNJpnNZun999936vWSJEmpqalSx44d7Y9feeUVycvLS7pw4YL92ueffy41aNBAunz5stOfS0TKYqJGRKo7efIkGjZsiM6dO9uvBQUFoXXr1jh58iQA4NSpU3jwwQcd3nf749rU9X6r1YrLly+jS5cu9msNGzZEp06dqnzW//zP/8BkMtkfd+nSBT/88APKysqcWkvl71HxuOLPmZWVhfz8fAQFBaFx48b2r+zsbJw9e9b+nubNm+N3v/udU9/v5MmTKCoqQq9evWp8zccff4xu3bohLCwMjRs3xpw5c3D+/HmH10RFReHOO+90WHd5eTlOnTrl1DqISHkNtV4AERmfVEN/lSRJ9oKo8l/X9b6auPp+NVWsrby8HOHh4fjqq6+qvKZyP56/v7/Tn+3r61vr8//+978xfPhwzJs3D/369YPFYsH69evx5ptvOrXm23+uROQ+TNSISHX33HMPSktL8c0339ivXb16FadPn0abNm0AAHfffTe+/fZbh/cdPHjQ6e/RunXrWt9vsVgQHh6Of//73/ZrpaWlyMrKqvJZlV9T8Tg2NhZeXl5OraW69999990AgPvvvx85OTlo2LAhYmJiHL6Cg4Od+vzbxcbGwtfXF7t27ar2+f3796N58+aYPXs2OnXqhNjYWJw7d67K686fP49Lly7ZH3/99ddo0KAB7rrrLlnrIiLXMVEjItXFxsZi8ODBeO655/Duu+8iICAAs2bNwh133IHBgwcDACZPnozu3bsjLS0NgwYNwu7du/H55587neZMnjwZzz33HDp16oT4+Hh89NFHOHr0KFq2bGl/zZQpU/Daa68hNjYWbdq0QVpaWrWnGi9cuIDExESMHz8ehw4dwpIlS+pMnyrbv38/UlNTMWTIEOzYsQP/+Mc/8NlnnwEAevfujS5dumDIkCFYtGgRWrdujUuXLmHr1q0YMmRItVuxdWnUqBFmzpyJGTNmwMfHB127dsUvv/yC48ePY+zYsYiJicH58+exfv16PPDAA/jss8+qPUTRqFEjjBo1Cm+88QZsNhtefPFFPPnkkwgLC6v3mohIGUzUiMgtVqxYgY4dO2LgwIHo0qULJEnC1q1b4e3tDQDo2rUrli9fjrS0NLRv3x5ffPEFpk6dikaNGjn1+U899RSSkpLw0ksv4f7770d2djZGjx7t8P5p06bhmWeewejRo9GlSxcEBATgD3/4Q5XPeuaZZ1BYWIgHH3wQEydOxOTJk/H88887/WedNm0asrKyEBcXh1dffRVvvvkm+vXrB+DWNuLWrVvRvXt3jBkzBnfddReGDx+On376yeGUZn3NmTMH06ZNw5///Ge0adMGw4YNQ25uLgBg8ODBmDp1KiZNmoQOHTogMzMTc+bMqfIZMTExGDp0KB599FH07dsXbdu2xdKlS2WviYhcZ5JEauIgIqrkueeew3/+8x/s3btX1vv79OmDsLAwrF692un39OzZEx06dMDixYtlfc8WLVogISFB+Ftn3W7u3LnYsmWLU6NAiMh9uPVJRMJ444030KdPH/j7++Pzzz/HqlWrnE50CgoKsHz5cvTr1w9eXl5Yt24ddu7caZ9fRkSkRyzUiEgY3377LVJTU3H9+nW0bNkSb7/9NsaNGwcAuPfee6ttgAeAd999F0OHDsXWrVuxYMECFBUVoXXr1ti4cSN69+6t2Pr27t2L/v371/h8fn6+Yt+rsvPnz+Oee+6p8fkTJ04gKipKle9NRNri1icR6cK5c+dqvOdlaGgoAgICVF9DYWEhLl68WOPzMTExqnzf0tJS/PTTTzU+36JFCzRsyN+7iYyIhRoRERGRoHjqk4iIiEhQLNSIiIiIBMVCjYiIiEhQLNSIiIiIBMVCjYiIiEhQLNSIiIiIBMVCjYiIiEhQLNSIiIiIBPX/AUA2Hm5H6Ue0AAAAAElFTkSuQmCC",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.8043146004918288\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "'The relationship between GDP per capita and happiness became more linear by applying a log transformation. Log transformations are great to use on variables with a skewed distribution, such as GDP.'"
      ]
     },
     "execution_count": 51,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "# Create log_gdp_per_cap column\n",
    "world_happiness['log_gdp_per_cap'] = np.log(world_happiness['gdp_per_cap'])\n",
    "\n",
    "# Scatterplot of log_gdp_per_cap and happiness_score\n",
    "sns.scatterplot(x='log_gdp_per_cap', y='happiness_score', data=world_happiness)\n",
    "plt.show()\n",
    "\n",
    "# Calculate correlation\n",
    "cor = world_happiness['log_gdp_per_cap'].corr(world_happiness['happiness_score'])\n",
    "print(cor)\n",
    "\n",
    "\"\"\"The relationship between GDP per capita and happiness became more linear by applying a log transformation. Log transformations are great to use on variables with a skewed distribution, such as GDP.\"\"\""
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Does sugar improve happiness?**\n",
    "\n",
    "A new column has been added to world_happiness called grams_sugar_per_day, which contains the average amount of sugar eaten per person per day in each country. In this exercise, you'll examine the effect of a country's average sugar consumption on its happiness score.\n",
    "\n",
    "pandas as pd, matplotlib.pyplot as plt, and seaborn as sns are imported, and world_happiness is loaded.\n",
    "\n",
    "\n",
    "Question: Based on this data, which statement about sugar consumption and happiness scores is true?\n",
    "\n",
    "Possible Answers: <br>\n",
    "\n",
    "- Increased sugar consumption leads to a higher happiness score.\n",
    "- Lower sugar consumption results in a lower happiness score\n",
    "- Increased sugar consumption is associated with a higher happiness score.\n",
    "- Sugar consumption is not related to happiness."
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 55,
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "<class 'pandas.core.frame.DataFrame'>\n",
      "Int64Index: 133 entries, 0 to 132\n",
      "Data columns (total 10 columns):\n",
      " #   Column               Non-Null Count  Dtype  \n",
      "---  ------               --------------  -----  \n",
      " 0   Unnamed: 0           133 non-null    int64  \n",
      " 1   country              133 non-null    object \n",
      " 2   social_support       133 non-null    int64  \n",
      " 3   freedom              133 non-null    int64  \n",
      " 4   corruption           127 non-null    float64\n",
      " 5   generosity           133 non-null    int64  \n",
      " 6   gdp_per_cap          133 non-null    int64  \n",
      " 7   life_exp             133 non-null    float64\n",
      " 8   happiness_score      133 non-null    int64  \n",
      " 9   grams_sugar_per_day  133 non-null    float64\n",
      "dtypes: float64(3), int64(6), object(1)\n",
      "memory usage: 11.4+ KB\n"
     ]
    }
   ],
   "source": [
    "import seaborn as sns\n",
    "world_happiness = pd.read_csv('./datasets/world_happiness_add_sugar.csv', index_col=0)\n",
    "world_happiness.info()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 56,
   "metadata": {},
   "outputs": [
    {
     "data": {
      "image/png": "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",
      "text/plain": [
       "<Figure size 700x500 with 1 Axes>"
      ]
     },
     "metadata": {},
     "output_type": "display_data"
    },
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "0.6939100021829633\n"
     ]
    }
   ],
   "source": [
    "# Scatterplot of grams_sugar_per_day and happiness_score\n",
    "sns.scatterplot(x='grams_sugar_per_day', y='happiness_score', data=world_happiness)\n",
    "plt.show()\n",
    "\n",
    "# Correlation between grams_sugar_per_day and happiness_score\n",
    "cor = world_happiness['grams_sugar_per_day'].corr(world_happiness['happiness_score'])\n",
    "print(cor)"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Confounders**\n",
    "\n",
    "A study is investigating the relationship between neighborhood residence and lung capacity. Researchers measure the lung capacity of thirty people from neighborhood A, which is located near a highway, and thirty people from neighborhood B, which is not near a highway. Both groups have similar smoking habits and a similar gender breakdown.\n",
    "\n",
    "Which of the following could be a confounder in this study?\n",
    "\n",
    "Possible Answers: <br>\n",
    "\n",
    "- Lung capacity\n",
    "- Neighborhood\n",
    "- **Air pollution**\n",
    "- Smoking status\n",
    "- Gender"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "### Design of experiments\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Study types**\n",
    "\n",
    "![](./images/study_types.png)\n"
   ]
  },
  {
   "cell_type": "markdown",
   "metadata": {},
   "source": [
    "> **Longitudinal vs. cross-sectional studies**\n",
    "\n",
    "Longitudinal vs. cross-sectional studies\n",
    "A company manufactures thermometers, and they want to study the relationship between a thermometer's age and its accuracy. To do this, they take a sample of 100 different thermometers of different ages and test how accurate they are. Is this data longitudinal or cross-sectional?\n",
    "\n",
    "\n",
    "Possible Answers: <br>\n",
    "\n",
    "- Longitudinal\n",
    "- **Cross-sectional**\n",
    "- Both\n",
    "- Neither\n",
    "\n",
    "*This is a cross-sectional study since researchers aren't following the same set of thermometers over time and repeatedly measuring their accuracy at different ages.*"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3.9.13 ('my_conda_env')",
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
   "version": "3.9.13"
  },
  "orig_nbformat": 4,
  "vscode": {
   "interpreter": {
    "hash": "0f080ef3f7e154a5496448b61eb994fbc79c03fae547c033702ffc1b7b2a346b"
   }
  }
 },
 "nbformat": 4,
 "nbformat_minor": 2
}
