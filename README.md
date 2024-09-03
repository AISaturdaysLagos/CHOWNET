# CHOWNET-V1: An Image Dataset of Nigerian Food

> CHOWNET-V1 is a high-quality dataset containing 118 human-annotated food images, designed for multi-label classification, food object detection, and food captioning tasks. We curated a dataset of 118 food images with 99 unique labels. The dataset is available for download at [link](https://zenodo.org/records/13633554).

People from diverse cultural backgrounds often have distinct food preferences, with studies [1] indicating that individuals connect with their food choices as an expression of identity. Building on our community's 2018 initiative to gather a dataset of Nigerian food images—aimed at addressing the poor classification of Nigerian cuisine by object detection models (see Fig)—we present CHOWNET-V1. 

![image](https://github.com/user-attachments/assets/0bb7b77a-4da1-499d-9d27-22b654dd0f78)

*Image Link: https://towardsdatascience.com/real-time-object-detection-api-using-tensorflow-and-opencv-47b505d745c4*


## Data Collection
In 2018, our community initiated a project to curate a dataset of the foods we consume. We employed three different approaches to gather this data:

- Approach 1: We developed an Android app to facilitate the easy acquisition and tagging of food item images. These images were then uploaded to a popular cloud image service, Cloudinary, and organized into separate folders. However, this approach yielded only a small amount of data.

- Approach 2: We created a GitHub repository where community members could upload food images. Unfortunately, this method did not scale well.

- Approach 3: We utilized Google Cloud by creating a public Google Drive folder where anyone could access and easily drag and drop images into different folders. This method generated the most data but proved to be unsustainable in the long term.

Through these three approaches, we collected a total of 568 image submissions across 15 different categories in 2018.


## Data Cleaning
This dataset, contributed by our community members in 2018, is being published for the first time. We engaged in extensive cleaning to ensure quality and compliance which significantly reduced the dataset from the initially collected and reported 568 images to 118 clean, non-copyrighted images. The cleaning steps taken include:

- Duplicate Removal: We used CLIP with a similarity threshold of over 90% to identify duplicates and near-duplicates, which were then manually inspected and removed.
Image Quality: Blurry images were excluded.
- Privacy Considerations: Images with visible body parts, such as hands, were removed.
- Copyright Compliance: Google Image Lens was used to identify and remove copyrighted images.
- Resolution Considerations: Lower-resolution images were retained in some cases since real-life scenarios may not always provide high-quality images due to variations in user camera capabilities.

## Supported Tasks
- Food Clustering
- Multi-label Classification
- Food object Detection
- Food Captioning

## Experiments
Please explore our [experiments](./experiments) folder.

## BibTex Citation


## License
Copyright (C) 2024 AI Saturdays Lagos Community.

<!-- CHOWNET is open dataset: you can redistribute it and/or modify it under the terms of the GNU Affero General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version.

CHOWNET is distributed in the hope that it will be useful, but WITHOUT ANY WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU Affero General Public License for more details.

You should have received a copy of the GNU Affero General Public License along with CHOWNET. If not, see https://www.gnu.org/licenses/.
-->

## References
1. Gina M. Almerico. Food and Identity: Food studies, cultural, and personal identity. Journal of International Business and Cultural Studies Volume 8 - June, 2014 	
