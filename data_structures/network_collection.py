import ipaddress

from data_structures.entry import Entry


class NetworkCollection:
    def __init__(self, ipv4_network, raw_entry_list):
        """
        Constructor for NetworkCollection data structure.

        self.ipv4_network -> ipaddress.IPv4Network
        self.entries -> list(Entry)
        """
        try:
            self.ipv4_network = ipaddress.IPv4Network(ipv4_network)
        except ValueError:
            print(ValueError)
            pass
        self.entries = []
        for entry in raw_entry_list:
            self.entries.append(Entry(entry['address'], entry['available'], entry['last_used']))

    def remove_invalid_records(self):
        """
        Removes invalid objects from the entries list.
        """
        subnet_ip_list = []
        valid_entries = []
        for ip in self.ipv4_network:
            subnet_ip_list.append(ip)

        for entry in self.entries:
            try:
                if ipaddress.IPv4Address(entry.address) in subnet_ip_list:
                    valid_entries.append(entry)
            except ValueError:
                continue
        self.entries = valid_entries

    def sort_records(self):
        """
        Sorts the list of associated entries in ascending order.
        DO NOT change this method, make the changes in entry.py :)
        """

        self.entries = sorted(self.entries)


