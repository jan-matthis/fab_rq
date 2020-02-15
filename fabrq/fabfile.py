from invoke import Collection

import fab_rq.tasks.open
import fab_rq.tasks.queue
import fab_rq.tasks.redis
import fab_rq.tasks.workers

ns = Collection()
ns.add_collection(Collection.from_module(fab_rq.tasks.open))
ns.add_collection(Collection.from_module(fab_rq.tasks.queue))
ns.add_collection(Collection.from_module(fab_rq.tasks.redis))
ns.add_collection(Collection.from_module(fab_rq.tasks.workers))
