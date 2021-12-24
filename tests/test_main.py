import unittest
import json

from data_structures.datacenter import Datacenter


class TestDatacenter(unittest.TestCase):
    """
    Inits & tests for datacenter remove_invalid_clusters method
    """
    def setUp(self) -> None:
        with open('test_response.json', "r") as f:
            self.test_data = json.load(f)

    def testRemoveInvalidClusters(self):
        clusters = []
        datacenters = [
            Datacenter(key, value)
            for key, value in self.test_data.items()
        ]

        for dc in datacenters:
            dc.remove_invalid_clusters()
            for cluster in dc.clusters:
                clusters.append(cluster.name)

        self.assertEqual(clusters, ['BER-1', 'BER-203', 'PAR-1'], "should be ['BER-1', 'BER-203', 'PAR-1']")


class TestNetworkCollection(unittest.TestCase):
    """
    Inits & tests for network_collection remove_invalid_records method
    """
    def setUp(self) -> None:
        with open('test_response.json', "r") as f:
            self.test_data = json.load(f)
            print(self.test_data)

    def testRemoveInvalidClusters(self):
        addresses = []
        datacenters = [
            Datacenter(key, value)
            for key, value in self.test_data.items()
        ]

        for dc in datacenters:
            for cluster in dc.clusters:
                for network in cluster.networks:
                    network.remove_invalid_records()
                    for entry in network.entries:
                        addresses.append(entry.address)
        self.assertEqual(addresses, ['192.168.0.1', '192.168.0.4', '192.168.0.2', '192.168.0.3', '10.0.11.254',
                                     '10.0.8.1', '10.0.8.0', '192.168.10.8', '192.168.10.5', '192.168.10.6',
                                     '192.168.11.1', '192.168.203.20', '192.168.203.21', '192.168.203.19'
                                     ]
                         )


if __name__ == "__main__":
    unittest.main()
