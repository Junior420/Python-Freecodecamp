import numpy as np

def calculate(list):
 
  if len(list)!=9:
    raise ValueError("List must contain nine numbers.")
  ar = np.array(list).reshape((3,3))
  
  # empty dict. add entries with update()
  calculations = {}

 
  calculations.update(mean=[ar.mean(0).tolist(), ar.mean(1).tolist(), ar.mean(None).tolist()])

  calculations.update(variance=[ar.var(0).tolist(), ar.var(1).tolist(), ar.var(None).tolist()])

  calculations.update({'standard deviation':[ar.std(0).tolist(), ar.std(1).tolist(), ar.std(None).tolist()]})


  calculations.update(max=[ar.max(0).tolist(), ar.max(1).tolist(), ar.max(None).tolist()])

  # min
  calculations.update(min=[ar.min(0).tolist(), ar.min(1).tolist(), ar.min(None).tolist()])

  # sum
  calculations.update(sum=[ar.sum(0).tolist(), ar.sum(1).tolist(), ar.sum(None).tolist()])
  
  #print(calculations)
  return calculations