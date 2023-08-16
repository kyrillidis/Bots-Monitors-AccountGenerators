package main

import (
    "fmt"
    "log"
    "math/rand"
    "net/http"
    "strconv"
    "strings"

    "github.com/PuerkitoBio/goquery"
)

func main() {
    // specify the URL of the product page
    url := "https://www.buzzsneakers.gr/athlitika-papoutsia/18880-nike-nike-dunk-low-bg-d4h#alphamonitors-s"

    // send a GET request to the URL
    response, err := http.Get(url)
    if err != nil {
        log.Fatal(err)
    }
    defer response.Body.Close()

    // parse the HTML content
    document, err := goquery.NewDocumentFromReader(response.Body)
    if err != nil {
        log.Fatal(err)
    }

    // find the available sizes for the product
    var availableSizes []string
    document.Find(".attribute_size").Each(func(i int, sizeElement *goquery.Selection) {
        if !strings.Contains(sizeElement.AttrOr("class", ""), "disabled") {
            availableSizes = append(availableSizes, sizeElement.AttrOr("data-value", ""))
        }
    })

    // randomly select a size from the available sizes
    if len(availableSizes) > 0 {
        selectedSize := availableSizes[rand.Intn(len(availableSizes))]
        fmt.Printf("Selected size: %s\n", selectedSize)

        // add the selected size to the cart
        addToCartURL := fmt.Sprintf("https://www.buzzsneakers.gr/cart?add=1&id_product=18880&id_product_attribute=%s", selectedSize)
        _, err := http.Get(addToCartURL)
        if err != nil {
            log.Fatal(err)
        }

        fmt.Println("Added to cart!")
    } else {
        fmt.Println("No available sizes.")
    }
}
