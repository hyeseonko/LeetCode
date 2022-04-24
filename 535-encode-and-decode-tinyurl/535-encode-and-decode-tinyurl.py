class Codec:
    def __init__(self):
        self.codec_dict = dict()
        self.codec_reversed = dict()
        self.codec_len = 0

    def encode(self, longUrl: str) -> str:
        """Encodes a URL to a shortened URL.
        """
        if longUrl not in self.codec_dict:
            self.codec_dict[longUrl]=self.codec_len
            self.codec_reversed[self.codec_len] = longUrl
            self.codec_len+=1
        return "http://tinyurl.com/{}".format(self.codec_dict[longUrl])

    def decode(self, shortUrl: str) -> str:
        """Decodes a shortened URL to its original URL.
        """
        val = int(shortUrl.split("/")[-1])
        return self.codec_reversed[val]
        

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(url))