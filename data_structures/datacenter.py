import re

from data_structures.cluster import Cluster


class Datacenter:
    def __init__(self, name, cluster_dict):
        """
        Constructor for Datacenter data structure.

        self.name -> str
        self.clusters -> list(Cluster)
        """

        self.name = name
        self.clusters = [Cluster(key, value['networks'], value['security_level'])
                         for key, value in cluster_dict.items()]

    def remove_invalid_clusters(self):
        """
        Removes invalid objects from the clusters list.
        """

        valid_clusters = []
        for index, cluster in enumerate(self.clusters):
            if re.search('^[A-Z]{3}-\\d{1,3}$', cluster.name):
                valid_clusters.append(cluster)
        self.clusters = valid_clusters



