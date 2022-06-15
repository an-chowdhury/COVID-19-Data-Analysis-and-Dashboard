[![Contributors][contributors-shield]][contributors-url]
[![Forks][forks-shield]][forks-url]
[![Stargazers][stars-shield]][stars-url]
[![Issues][issues-shield]][issues-url]
[![MIT License][license-shield]][license-url]
[![LinkedIn][linkedin-shield]][linkedin-url]

<!-- PROJECT LOGO -->
<p align="center">

  <h1 align="center">COVID 19 India Data Analysis using Python</h1>

  <p align="center">
    <br />
    <a href="https://github.com/an-chowdhury/COVID-19-India-Case-Study"></a>
    <br />
    <br />
      </p>
</p>

<!-- TABLE OF CONTENTS -->
## Table of Contents
<details open="open">
  <summary>Contents</summary>
  <ol>
    <li>
      <a href="#Background">Background</a>
      <ul>
        <li><a href="#Summery">Summery</a></li>
        <li><a href="#Project-Objective">Project Objective</a></li>
        <li><a href="#Project-Data-Source">Project Data Source</a></li>
      </ul>
    </li>
    <li>
      <a href="#Findings">Findings</a>
      <ul>
        </ul>
    </li>
    <li><a href="#Reference">Reference</a></li>
    <li><a href="#license">License</a></li>
  </ol>
</details>

## Background

![product-screenshot]

The first case of COVID-19 in India, which originated from China, was reported on 30 January 2020. India currently has the largest number of confirmed cases in Asia, and has the second-highest number of confirmed cases in the world after the United States with more than 10.3 million reported cases of COVID-19 infection and more than 154,000 deaths as of February 2, 2021. The per day cases peaked mid-September in India with over 90,000 cases reported per day and have since come down to below 15,000 as of 2021 January.
### Summery

The COVID-19 pandemic is the defining global health crisis of our time and the greatest global humanitarian challenge the world has faced since World War II. The virus has spread widely, and the number of cases is rising daily as governments work to slow its spread. India has moved quickly, implementing a proactive, nationwide, lockdown, with the goal of flattening the curve and using the time to plan and resource responses adequately.

### Project Objective
The goal of this project is to use techniques of statistical analysis to visualize and estimate impact of COVID-19 in India from different aspects i.e 
how the virus has affected people from different regions, age groups etc. In a nutshell the visualizations will help to understand COVID-19 situation in India in a detailed manner.  
### Project Data Source
* Raw data about COVID-19 cases at daily level is collected from [covid19india.org's API.](https://api.covid19india.org/) 
* Statewise data as well as district-wise data has also been collected from [covid19india.org's API.](https://api.covid19india.org/)
* population data is collected from [Wikipedia.](https://en.wikipedia.org/wiki/Demographics_of_India)
* Coordinates of indian States obtained from [Geohacker's Github repository.](https://github.com/geohacker/india)

### Findings
![Figure-1]
**Figure1** shows cumulative sum of all confrimed, recovered, deceased and active cases through line chart which to a good approximation, are distributed over the days since origination.

![Figure-2]

**Figure2** we see the current situation in India. It shows that more than 95% patients who contracted COVID-19 has recovered already.

![Figure-3]

**Figure3** shows through histogram that which age group has most number of COVID-19 cases. As we can see aapeople between 20-40 has contracted the disease most.

![Figure-4]

**Figure4** indicate that state with the darkest color i.e Maharashtra and other southern states has had chunk number of confirmed cases.

![Figure-5]

**Figure5**, we can see that now  Kerala, floowed by maharashtra has most number of active cases.

## Reference

1. https://www.kaggle.com/sudalairajkumar/covid19-in-india
2. https://www.covid19india.org/

<!-- MARKDOWN LINKS & IMAGES -->
[contributors-shield]: https://img.shields.io/github/contributors/an-chowdhury/COVID-19-India-Case-Study?style=for-the-badge
[contributors-url]: https://github.com/an-chowdhury/COVID-19-India-Case-Study/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/an-chowdhury/COVID-19-India-Case-Study?style=for-the-badge
[forks-url]: https://github.com/an-chowdhury/COVID-19-India-Case-Study/network/members
[stars-shield]: https://img.shields.io/github/stars/an-chowdhury/COVID-19-India-Case-Study?style=for-the-badge
[stars-url]: https://github.com/an-chowdhury/COVID-19-India-Case-Study/stargazers
[issues-shield]: https://img.shields.io/github/issues/an-chowdhury/COVID-19-India-Case-Study?style=for-the-badge
[issues-url]: https://github.com/an-chowdhury/COVID-19-India-Case-Study/issues
[license-shield]: https://img.shields.io/github/license/an-chowdhury/COVID-19-India-Case-Study?style=for-the-badge
[license-url]: https://github.com/an-chowdhury/COVID-19-India-Case-Study/blob/master/LICENSE.txt
[linkedin-shield]: https://img.shields.io/badge/-LinkedIn-black.svg?style=for-the-badge&logo=linkedin&colorB=555
[linkedin-url]: https://www.linkedin.com/in/ankan-chowdhury-00bb3b141/
[product-screenshot]: https://i.imgur.com/HdKy1CA.png
[Figure-1]: Insights/India%20Cumulative%20Curve.png
[Figure-2]: Insights/Current%20Situation.jpg
[Figure-3]: Insights/Age%20Group%20Analysis.jpg
[Figure-4]: Insights/Heatmap-India.png
[Figure-5]: Insights/Active%20Cases.png
