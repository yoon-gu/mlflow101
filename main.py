import mlflow
client = mlflow.MlflowClient()

info = mlflow.run(".", "main1", parameters={"in_data": "input.csv", "out_data": "output_1.csv"})
run = client.get_run(info.run_id)
inpath = run.info.artifact_uri + '/' + run.data.params['out_data']
info = mlflow.run(".", "main2", parameters={"in_data": inpath.replace("file:///", ""), "out_data": "output_2.csv"})
