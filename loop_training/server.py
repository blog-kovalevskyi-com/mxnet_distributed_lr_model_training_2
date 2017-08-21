import os

os.environ.update({
  "DMLC_ROLE": "server",
  "DMLC_PS_ROOT_URI": "127.0.0.1",
  "DMLC_PS_ROOT_PORT": "9000",
  "DMLC_NUM_SERVER": "1",
  "DMLC_NUM_WORKER": "2",
  "PS_VERBOSE": "0"
})
import mxnet
