# Training a Segmentation CNN

Artifacts from Section 2:  
  
* Functional code that trains the segmentation model. Begin model training by running script *run_ml_pipeline.py*, modified to include correct path to dataset.
* Test report with Dice scores on test set (json file). Final average Dice is around .90
* Screenshots from Tensorboard output, showing Train and Validation loss plots, along with images of the predictions that the model is making at different stages of training
* Trained model PyTorch parameter file (`model.pth`, exceeds Github file size)

Tensorboard
1. Make sure you enable GPU.
2. In a terminal move to the src directory through cd src
3. Then run the following command to start tensorboardtensorboard --logdir runs --bind_all
4. The output should have a URL
5. Copy that URL
6. Open the Desktop with the Desktop button at the bottom right hand corner and copy the URL. (It will look something like http://f8196ac7f2cc:6006/)
7. If not already open, open a browser.
8. On the left hand side there will be an arrow, if you click the arrow, a sidebar that will popup.
9. Click on the 2nd icon on the sidebar which is a clipboard and paste the URL here.
10. In the address bar you can right click and select Paste & Go.
