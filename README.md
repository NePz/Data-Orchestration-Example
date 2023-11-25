# What is this mini example project?
> This aims to model a data orchestration process (term used in Data Engineering) a simple implementation to understand the basics of the operation
> In the provided Python script, we are simulating a simple data workflow, showcasing a basic form of data orchestration without using dedicated orchestration tools like Apache Airflow.
>  This example demonstrates a basic form of data orchestration by manually calling functions in sequence, dedicated orchestration tools like Apache Airflow provide more advanced features such as automated scheduling, task dependencies, error handling, parallel execution, monitoring, and a graphical interface to manage and visualize complex data workflows efficiently.
> This is a single pipeline/workflow/DAG (Directed Acyclic Graphs) example
>
>[Multiple Pipeline Example](multiple-data-pipeline/multiple-workflow-orchestration.py)

To run this project:
- First Install Apache Airflow library using the `pip install apache-airflow` in the terminal

## What is Data Orchestration?
> data orchestration involves coordinating multiple data-related tasks or pipelines, managing dependencies, scheduling, and ensuring the efficient execution of these tasks. Libraries like Apache Airflow provide capabilities for data orchestration.

## How is this an example of basic Data Orchestration?
### Sequential Execution of Tasks:
- The script defines three functions (`extract_data()`, `transform_data()`, `load_data()`), each representing a specific task in a data workflow: extraction, transformation, and loading.
- These functions are manually called in sequence (`extract_data()` -> `transform_data()` -> `load_data()`), imitating the orchestration of tasks in a data pipeline.

### Task Dependency:
- The tasks (`extract_data()`, `transform_data()`, `load_data()`) are dependent on each other's output. For example, the `load_data()` function relies on the successful completion of `transform_data()` to load the transformed data.

### Data Flow:
- Data flows through the tasks. The extracted data is transformed by `transform_data()` before being loaded by `load_data()`.

### Simple Workflow Representation:
- Each function represents a single step in the data workflow. This script's execution sequence mirrors the flow of data through these tasks.