from invoke import Collection

import fabrq.tasks.open
import fabrq.tasks.queue
import fabrq.tasks.redis
import fabrq.tasks.workers

ns = Collection()
ns.add_collection(Collection.from_module(fabrq.tasks.open))
ns.add_collection(Collection.from_module(fabrq.tasks.queue))
ns.add_collection(Collection.from_module(fabrq.tasks.redis))
ns.add_collection(Collection.from_module(fabrq.tasks.workers))
