<a name="readme-top"></a>

<br />
<div align="center">
  <a href="https://github.com/kitkot2/CircEIS">
    <img src="img/circeis.png" alt="Logo" width="300">
  </a>

<h3 align="center">CircEIS</h3>

  <p align="center">
    Circumference fitting for EIS
    <br />
    <a href="https://github.com/kitkot2/CircEIS"><strong>Files</strong></a>
    <br />
    <br />
    <a href="https://github.com/kitkot2/CircEIS/issues">Report an error</a>
  </p>
</div>


<details>
  <summary>Table of contents</summary>
  <ol>
    <li>
      <a href="#About">About</a>
      <ul>
        <li><a href="#Main libraries">Main libraries</a></li>
      </ul>
    </li>
    <li><a href="#Setup">Setup</a></li>
    <li><a href="#Contacts">Contacts</a></li>
  </ol>
</details>


## About the project

CiecEIS is designed for Electrochemical Impedance Spectroscopy (EIS) research. It allows user to quickly select data, simultaneously fit multiple circumferences using the least squares method, and extract pertinent parameters such as center coordinates, radius, and intersection points with the real axis.

To enhance fitting accuracy in the presence of significant noise, several data 'cleaning' methods have been implemented.

This tool can be useful in EIS-related fields as a main analysis method or as an adittion to conventional circuit model fitting approaches by providing reliable reference values.

<p align="right">(<a href="#readme-top">up</a>)</p>

### Main libraries

[![Matplotlib](https://img.shields.io/badge/Matplotlib-%23ffffff.svg?style=for-the-badge&logo=Matplotlib&logoColor=black)][Matplotlib-url]
[![NumPy](https://img.shields.io/badge/numpy-%23013243.svg?style=for-the-badge&logo=numpy&logoColor=white)][NumPy-url]
[![Pandas](https://img.shields.io/badge/pandas-%23150458.svg?style=for-the-badge&logo=pandas&logoColor=white)][Pandas-url]
[![SciPy](https://img.shields.io/badge/SciPy-%230C55A5.svg?style=for-the-badge&logo=scipy&logoColor=%white)][SciPy-url]

<p align="right">(<a href="#readme-top">up</a>)</p>

## Setup

1. Copy repository
   ```sh
   git clone https://github.com/kitkot2/CircEIS.git
   ```
   or download .zip file
2. Make shure you have python and pip installed
3. Using command line change directory to CircEIS
   ```sh
   cd path_to_the_project/
   ```
4. To install all required libraries
  for windows:
   ```sh
   pip install -r requirements.txt
   ```
   for mac:
   ```sh
   pip3 install -r requirements.txt
   ```
5. After installation, run main.py using command line or compiler

<p align="right">(<a href="#readme-top">up</a>)</p>

## Contacts

Nikita Kotenko - kotenko.na@phystech.edu

Project Link: [https://github.com/kitkot2/CircEIS](https://github.com/kitkot2/CircEIS)

<p align="right">(<a href="#readme-top">up</a>)</p>

[contributors-shield]: https://img.shields.io/github/contributors/kitkot2/CircEIS.svg?style=for-the-badge
[contributors-url]: https://github.com/kitkot2/CircEIS/graphs/contributors
[forks-shield]: https://img.shields.io/github/forks/kitkot2/CircEIS.svg?style=for-the-badge
[forks-url]: https://github.com/kitkot2/CircEIS/network/members
[stars-shield]: https://img.shields.io/github/stars/kitkot2/CircEIS.svg?style=for-the-badge
[stars-url]: https://github.com/kitkot2/CircEIS/stargazers
[issues-shield]: https://img.shields.io/github/issues/kitkot2/CircEIS.svg?style=for-the-badge
[issues-url]: https://github.com/kitkot2/CircEIS/issues
[Pandas-url]: https://pandas.pydata.org/
[Matplotlib-url]: https://matplotlib.org/
[SciPy-url]: https://docs.scipy.org/doc/
[NumPy-url]: https://numpy.org/
