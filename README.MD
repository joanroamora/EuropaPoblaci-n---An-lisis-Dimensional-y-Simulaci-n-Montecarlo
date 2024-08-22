# EuropePopulation2024 - Dimensional Analysis and Monte Carlo Simulation

![🇨🇴](https://em-content.zobj.net/thumbs/240/twitter/322/flag-colombia_1f1e8-1f1f4.png) **Español**

## Descripción del Proyecto

EuropePopulation2024 es un proyecto de análisis y simulación que utiliza un 
dataset que contiene cifras de población por país para los países europeos 
desde 2013 hasta 2022. El proyecto realiza un análisis de la dimensionalidad 
de los datos y aplica una simulación de Monte Carlo para proyectar la población 
futura en períodos de dos años hasta 2030.

### Estructura del Proyecto

- **preprocesamiento.py**: Contiene funciones para cargar, limpiar y guardar 
el dataset.
- **dimensionalidad.py**: Incluye funciones para reducir la dimensionalidad de 
los datos, combinando pares de años en una sola columna.
- **montecarlo.py**: Realiza la simulación de Monte Carlo para proyectar la 
población futura en cuatro períodos de dos años.
- **app.py**: Orquesta el flujo completo del proyecto, desde la carga y limpieza 
de datos hasta la simulación y guardado de los resultados.

### Uso del Proyecto

1. **Cargar y limpiar los datos**:
   - El proyecto carga el dataset desde un archivo CSV y aplica un proceso de 
   limpieza que imputa los valores faltantes usando la media de cada fila.

2. **Reducción de dimensionalidad**:
   - Los datos se reducen combinando pares de años (por ejemplo, 2013-2014, 
   2015-2016) en columnas únicas.

3. **Simulación de Monte Carlo**:
   - Utilizando las tasas de crecimiento aleatorias, se proyecta la población 
   para los años 2023-2030.

### Instalación

1. Clona el repositorio:
   bash
   git clone https://github.com/tu_usuario/EuropePopulation2024.git

Instala las dependencias:
bash
Copiar código
pip install -r requirements.txt
Ejecución
Para ejecutar el proyecto, usa el siguiente comando:

bash
Copiar código
python app.py
Contribuciones
Las contribuciones son bienvenidas. Por favor, abre un issue o envía un pull
request para contribuir a este proyecto.

 English

## Project Description
EuropePopulation2024 is an analysis and simulation project that uses a dataset
containing population figures by country for European countries from 2013 to 2022.
The project performs a dimensionality analysis of the data and applies a Monte
Carlo simulation to project future population in two-year periods up to 2030.

## Project Structure
**preprocesamiento.py**: Contains functions to load, clean, and save the dataset.
**dimensionalidad.py**: Includes functions to reduce the dimensionality of the
data by combining pairs of years into single columns.
**montecarlo.py**: Conducts the Monte Carlo simulation to project future
population in four two-year periods.
**app.py**: Orchestrates the full project workflow, from data loading and
cleaning to simulation and result saving.

## Project Usage

**Load and clean the data:**
The project loads the dataset from a CSV file and applies a cleaning
process that imputes missing values using the mean of each row.

**Dimensionality reduction:**
The data is reduced by combining pairs of years (e.g., 2013-2014, 2015-2016)
into single columns.

**Monte Carlo simulation:**

Using random growth rates, the population is projected for the years
2023-2030.

## Installation
Clone the repository:
bash
Copiar código
git clone https://github.com/your_username/EuropePopulation2024.git
Install dependencies:
bash
Copiar código
pip install -r requirements.txt
Execution
To run the project, use the following command:

bash
Copiar código
python app.py
Contributions
Contributions are welcome. Please open an issue or submit a pull request to
contribute to this project.