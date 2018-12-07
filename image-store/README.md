# Image Store

Stores information about our detected and and labeled images. For each detection there should be a record in the `labels_table` table relating the detection to an image. Every stored image should have a record in the `image_location_table` and its stored location in the file system.

The two tables are related to each other through the `image_id` column.

For example the tables could have a state such as this:

labels_table:

| label | image_id |
|:-:|:-:|
| tvmonitor | 1 |
| keyboard | 1 |
| cat | 2 |

image_location_table:

| image_id | file_location_path |
|:-:|:-:|
| 1 | /home/\<user\>/images/image1.jpg |
| 2 | /home/\<user\>/images/image2.jpg |

Based on these table states both a tvmonitor and keyboard were detected in image1.jpg and a cat was detected in image2.jpg