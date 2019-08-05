def precision(tp, fp):
  if (tp + fp) == 0:
    return -9999
  return tp / (tp + fp)

def recall(tp, fn):
  if (tp + fn) == 0:
    return -9999
  return tp / (tp + fn)

def f1(prec, rec):
  if (prec + rec) <= 0:
    return -9999
  return (2 * prec * rec) / (prec + rec)
