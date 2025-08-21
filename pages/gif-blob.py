import streamlit as st
import numpy as np

import io
import base64

# requirements.txt should include "pillow"
# https://pypi.org/project/pillow/
from PIL import Image

st.markdown("# Embeding GIF Blob")

def show_ndarray_frames_as_gif(frames_np: list[np.ndarray]):
  """
  Takes a list of ndarrays as input, representing frames of an image,
  and embeds them as a GIF on the streamlit page.  The GIF data is
  embedded directly on the page using a blob URL, bypassing the filesystem.
  """

  # step 1: convert each ndarray frame to a PIL image
  frames_pil = [Image.fromarray(frame) for frame in frames_np]

  # step 2: use pillow to save the .gif image to a byte stream
  gif_bytes = io.BytesIO(b"")
  frames_pil[0].save(gif_bytes, format="gif", save_all=True, append_images=frames_pil[1:], loop=0)
  
  # step 3: convert the byte stream to a base64 string representation
  base64_image_string = base64.b64encode(gif_bytes.getvalue()).decode()

  # step 4: create a blob URL 
  img_data_url = 'data:image/gif;base64,' + base64_image_string
  
  # step 5: embed the blob URL directly inside of an HTML image tag
  st.write(
    f'<video poster="{img_data_url}" loop autoPlay playsInline preload="auto"></video>',
    unsafe_allow_html=True
  )

# EXAMPLE USAGE
def make_noisy_image():
  return np.random.randint(0, 256, (100, 100, 3), dtype=np.uint8)

frames_np = [make_noisy_image() for k in range(100)]
show_ndarray_frames_as_gif(frames_np)
