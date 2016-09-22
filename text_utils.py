
import re


# CamelCase to snake_case
def CamelToSnake(name):
  # TODO: if heavily used compile the regexs
  s1 = re.sub('(.)([A-Z][a-z]+)', r'\1_\2', name)
  s2 = re.sub('([a-z0-9])([A-Z])', r'\1_\2', s1).lower()
  return s2.replace(' ', '').replace('-','_')
