#!/usr/bin/env python
# coding: utf-8

# # Overview
# 
# This example demonstrates how to import a material from a POSCAR file via [Material](https://docs.exabyte.io/api/Material/post_materials_import) endpoints.

# # Execution
# 
# > <span style="color: orange">**NOTE**</span>: In order to run this example, an active Exabyte.io account is required. RESTful API credentials shall be updated in [settings](../settings.ipynb). The generation of the credentials is also explained therein.
# 
# ## Import packages

# In[4]:


import json

from settings import ENDPOINT_ARGS
from endpoints.materials import MaterialEndpoints


# ## Set Parameters
# 
# - **NAME**: material name
# - **POSCAR_PATH**: absolute path to the POSCAR file

# In[5]:


NAME = "My Material"
POSCAR_PATH = "mp-978534.poscar"


# ## Import material
# 
# Initialize `MaterialEndpoints` class and call `import_from_file` function to import the material.

# In[6]:


content  = ""
with open(POSCAR_PATH) as f:
    content = f.read()

endpoint = MaterialEndpoints(*ENDPOINT_ARGS)
material = endpoint.import_from_file(NAME, content)


# ## Print imported material
# 
# Print the list of imported materials in pretty JSON below.

# In[7]:


print json.dumps(material, indent=4)
