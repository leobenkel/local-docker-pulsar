# local-docker-pulsar

# How to use?

* `git clone git@github.com:leobenkel/local-docker-pulsar.git`
* `git clone https://github.com/apache/pulsar`
* `cp -r ./pulsar/conf ./local-docker-pulsar/.`
* `cd local-docker-pulsar`
* `mkdir data`
* `docker-compose up`
* [Visit the metrics page](http://localhost:48080/admin/v2/persistent/public/default/my-topic/stats)
