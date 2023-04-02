Date: 2023-04-02
Title: Improved Multideck
Category: random
Slug: improved-multideck
Summary: Let's Bauhaus-ify my previous multideck design. 

My last attempt at a multideck was ill-designed. The card layout was cluttered, the iconography inconsistent, and the overall useability left much to be desired. Luckily, over the last year and a half since my previous blog post, I have grown as a person who designs multidecks. Below is my updated and improved custom deck of cards:

![Photo]({attach}/assets/random/2023/improved-multideck.png){.image_center_style} 


<p align="center">
    <a class="nounderline" href="{attach}/assets/random/2023/multideck_cards.svg">Download SVG File</a>
</p>

``` bash 
# Cut a single image into multiple individual card images
convert card_image.png -crop 16x6@ -background none -gravity center card-%d.png
```
