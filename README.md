# mipt-devops-labs
MIPT DevOps class lab assignments.

1- Our Use case is Football match prediction and it has two parts
    * Knowledge Graph(KG) idea to learn the embeddings of the features
    * Perform Classification(XGB) with the embeddings as the features

2- So, in this case, we need the following
    * Main Task for finding the candidates for hyper-parameter optimization
    * Opt Task 1 --> hyper-parameter optimization of KG train parameters
    * Opt Task 2 --> hyper-parameter optimization of XGB train parameters

3- Here is the overview of command list to achieve the above goal
    * `clearml.browser_login()`
    * `MainTask = Task.get_task()`
    * `OptTask1 = HyperParameterOptimizer()` (imported from `clearml.automation`) --> `OptimizerOptuna`
    * `OptTask2 = HyperParameterOptimizer()` (imported from `clearml.automation`) --> `GridSearch`

4- Finally, Report the Top Experiments as results for 
    * KG Task
    * XGB Task

5- Replace the initialized hyper-parameters with the optimal parameter values obtained through the search (refer .ipynb `assignment03_clearML.ipynb` for code) 


