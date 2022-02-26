import docker as docker_sdk
import pandas as pd
import yaml


from multiprocessing.dummy import Pool

with open('config/param.yml') as stream:
    config = yaml.safe_load(stream)
# list of the sites
sites = config['sites']

# Docker image that already pull to local env
image_name = config['image_name']

number_conn = config['number_conn']
timeout = config['timeout']


# Set of the parallelism
parallel_stream = config['parallel_stream']  # set number parallel streams
docker = docker_sdk.from_env()


def main_process(site):

    name = str(site).replace('.','_').replace('http://','').replace('https://','').rstrip('/')
    print(name)

    docker.containers.run(image=image_name,
                          command=f' -c {number_conn} -d {timeout} -l {site}',
                          name=f"{name}",
                          detach=False
                          )
    container = docker.containers.get(name)
    output_log = container.logs().decode("utf-8")
    print(output_log)
    return None



def get_list_sites():
    # clean and compact list
    site_list_all = [line.strip() for line in str(sites).split(" ") if line.strip()]
    print(site_list_all)
    return site_list_all

if __name__ == '__main__':
    # main runtime

    docker.containers.prune()
    with Pool(processes=parallel_stream) as pool:
        result = pool.map(main_process, get_list_sites(), chunksize=1)

    df = pd.DataFrame(result)
    print(df.info)
