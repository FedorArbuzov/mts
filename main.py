from itertools import cycle
from urllib.parse import urlparse

from flask import Flask, request

app = Flask(__name__)

balancing_domains = cycle(['CDN_A', 'CDN_B', None])

@app.route('/')
def balancer():
    video = request.args.get('video')
    balancing_domain = next(balancing_domains)
    if not balancing_domain:
      return video
    else:
      parsed_url = urlparse(video)
      parsed_url = parsed_url._replace(netloc=balancing_domain)
      return parsed_url.geturl()


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
