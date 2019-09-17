To run this version use the following command

```

docker run -it --mount type=bind,source="$(pwd)",target="/project" \
--hostname evotext evotext:alpine /bin/bash

```
