#!/usr/bin/env python
# -*- coding: utf-8 -*-

import numpy as np
from scipy.misc import logsumexp

class Forecaster(object):
  """Base forecaster class"""
  def __init__(self, N):
    super(Forecaster, self).__init__()
    self.N = N
  
  def predict(e):
    raise NotImplementedError("Function must be extended by child class")

  def observe(l):
    raise NotImplementedError("Function must be extended by child class")

class EWAForecaster(Forecaster):
  """Exponentialy weighted average forecaster"""
  def __init__(self, N, eta, w0=None):
    super(EWAForecaster, self).__init__(N)
    self.eta = eta
    if w0:
      self.w = w0
    else:
      self.w = np.ones(N,) / N

  def predict(self, e):
    return self.w.dot(e)

  def observe(self, l):
    log_w = np.log(self.w)
    log_w_new = log_w - self.eta * l
    log_w_new = log_w_new - logsumexp(log_w_new)
    self.w = np.exp(log_w_new)
    assert self.w.shape == (self.N,)
