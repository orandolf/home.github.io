rom seleniumbase import BaseCase


class MyTestClass(BaseCase):
    def test_swag_labs(self):

        #open homepage and check title

        self.open("https://www.saucedemo.com")
        self.assert_title("Swag Labs")

        #login into the page

        self.type("#user-name", "standard_user")
        self.type("#password", "secret_sauce")

        self.click("#login-button")
         #click on a product
        #1. We have to check whether we are on the products page
        text = self.get_text("#header_container > div.header_secondary_container > span").strip()
        self.assert_true("Products" == text) #Or we could have just done:"self.assert_exact_text("Products", "its selector")"

        #checking if the container with the list of products is present
        self.assert_element("#inventory_container", timeout=20)

        #selecting the item backpack
        self.assert_exact_text("Sauce Labs Backpack","#item_4_title_link > div")
        self.click("#add-to-cart-sauce-labs-backpack")
        

         #checkout
        self.click("#shopping_cart_container > a")
        self.get_current_url()
        visit_cart_url = self.get_current_url()
        self.assert_true("cart.html" in visit_cart_url) #checking whether we are in the visit cart page
        self.click("#checkout")

        #Entering the dummy details 
        self.assert_text("Checkout: Your Information", timeout=20)
        self.type("#first-name", "Quality")
        self.add_text("#last-name", "Assurance")
        self.send_keys("#postal-code", "00233")
        self.click("#continue")

        self.assert_text("Checkout: Overview") #checking whether we are on the finish checkout page
        self.assert_exact_text("Total: $32.39", "#checkout_summary_container > div > div.summary_info > div.summary_total_label")
        self.click("#finish")

        #checking whether we are on the order page
        self.assert_exact_text("Thank you for your order!", "#checkout_complete_container > h2")

        #return home
        self.click("#back-to-products")