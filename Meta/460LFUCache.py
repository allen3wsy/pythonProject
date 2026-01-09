from collections import defaultdict, OrderedDict

class LFUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        # same as {}: these 2 maps are the same as HashMap<Integer, Pair<Integer, Integer>>
        self.key2val = defaultdict(int)
        self.key2freq = defaultdict(int)
        # HashMap<Integer, LinkedHashSet<Integer>> but OrderedDict has the value we dont' care...
        self.freq2key = defaultdict(OrderedDict)
        self.minf = 0

    def get(self, key: int) -> int:
        if key not in self.key2val:
            return -1
        oldfreq = self.key2freq[key]
        self.key2freq[key] = oldfreq + 1
        # pop(key) will work for both defaultdict and OrderedDict
        self.freq2key[oldfreq].pop(key)
        if not self.freq2key[oldfreq]:
            del self.freq2key[oldfreq]
        # 100: just a placeholder
        self.freq2key[oldfreq + 1][key] = 100
        if self.minf not in self.freq2key:
            self.minf += 1
        return self.key2val[key]

    def put(self, key: int, value: int) -> None:
        if self.cap <= 0:
            return
        if key in self.key2val:
            # Smartly it uses self.get(key) so we don't have to rewrite it
            self.get(key)
            self.key2val[key] = value
            return

        # Decide if we need to evict, if so we evict the LRU entry with min frequency
        if len(self.key2val) == self.cap:
            # _: is the same as unused...
            # popitem(last=False): popping the left one in OrderedDict
            delkey, _ = self.freq2key[self.minf].popitem(last=False)
            del self.key2val[delkey]
            del self.key2freq[delkey]
        self.key2val[key] = value
        self.key2freq[key] = 1
        # 100: just a placeholder
        self.freq2key[1][key] = 100
        self.minf = 1