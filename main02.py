import mlflow
import pandas as pd
import click
import logging

@click.command()
@click.argument("in_data")
@click.argument("out_data")
def main(in_data, out_data):
    mlflow.log_param("in_data", in_data)
    mlflow.log_param("out_data", out_data)

    logging.info(f"Reading data from {in_data}")
    mlflow.log_artifact(in_data)
    df = pd.read_csv(in_data)
    df.duration = df.duration + 10
    
    logging.info(f"Writing data to {out_data}")
    df.to_csv(out_data, index=False)
    mlflow.log_artifact(out_data)

if __name__ == "__main__":
    main()