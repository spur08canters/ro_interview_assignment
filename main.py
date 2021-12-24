import requests
import time

from data_structures.datacenter import Datacenter

URL = "http://www.mocky.io/v2/5e539b332e00007c002dacbe"


def get_data(url, max_retries=5, delay_between_retries=1):
    """
    Fetch the data from http://www.mocky.io/v2/5e539b332e00007c002dacbe
    and return it as a JSON object.

    Args:
        url (str): The url to be fetched.
        max_retries (int): Number of retries.
        delay_between_retries (int): Delay between retries in seconds.
    Returns:
        data (dict)
    """

    for retry in range(0, max_retries):
        time.sleep(delay_between_retries)
        try:
            response = requests.get(url)
            if response.status_code == requests.codes.ok:
                return response.json()
        except requests.exceptions.RequestException as request_exception:
            # log exception
            print(request_exception)
            continue


def main():
    """
    Main entry to our program.
    """

    data = get_data(URL)

    if not data:
        raise ValueError('No data to process')

    datacenters = [
        Datacenter(key, value)
        for key, value in data.items()
    ]

    for dc in datacenters:
        dc.remove_invalid_clusters()
        for cluster in dc.clusters:
            for network in cluster.networks:
                network.remove_invalid_records()
                network.sort_records()


if __name__ == '__main__':
    main()
