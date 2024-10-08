import time

import pytest
from selenium.common import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from test_products import TestProducts

# Penser à supprimer Test Product avant de tester
@pytest.mark.usefixtures('driver')
class TestAddProduct(TestProducts):
    # Ajouter un produit
    def test_add_new_product(self, driver):
        self.test_click_on_product(driver)
        time.sleep(1)
        new_product_button = driver.find_element(By.XPATH, "//a[@href='/admin/products/new' and contains(@class, 'button primary')]")
        new_product_button.click()

        # Vérifier que la page de création de produit est bien chargée
        time.sleep(1)
        create_product_heading = driver.find_element(By.XPATH, "//h1[text()='Create A New Product']")
        assert create_product_heading.is_displayed(), "Create New Product page did not load correctly"

        # Remplir les champs requis pour créer un nouveau produit
        name_input = driver.find_element(By.ID, "name")
        sku_input = driver.find_element(By.ID, "sku")
        price_input = driver.find_element(By.ID, "price")
        weight_input = driver.find_element(By.ID, "weight")
        qty = driver.find_element(By.ID, "qty")
        urlKey = driver.find_element(By.ID, "urlKey")

        name_input.send_keys("Test Product")
        sku_input.send_keys("TP-9999")
        price_input.send_keys("99.99")
        weight_input.send_keys("1.5")

        # Sélectionner la catégorie du produit
        select_category = driver.find_element(By.XPATH, "//a[text()='Select category']")
        select_category.click()
        time.sleep(2)
        select_category = driver.find_element(By.CSS_SELECTOR, ".flex.justify-start.gap-1.items-center")

        select_category = select_category.find_elements(By.TAG_NAME, "a")[1]
        select_category.click()
        # Simuler la sélection de la catégorie, en fonction de l'implémentation du sélecteur

        # Sélectionner la classe de taxe
        tax_class_dropdown = driver.find_element(By.ID, "tax_class")
        tax_class_dropdown.click()
        tax_class_option = driver.find_element(By.XPATH, "//option[text()='Taxable Goods']")
        tax_class_option.click()

        # Ajouter une description
        description_input = driver.find_element(By.CSS_SELECTOR, "div.ck-content")
        driver.execute_script("arguments[0].innerHTML = '<p>This is a test product description.</p>'", description_input)

        # Quantité
        qty.send_keys("5")
        urlKey.send_keys("produitTest")

        # Soumettre le formulaire
        save_button = driver.find_element(By.XPATH, "//button[contains(@class, 'button primary') and contains(., 'Save')]")
        save_button.click()

        # Vérifier que le produit a été créé avec succès (Cela dépend de la façon dont la page se comporte après la soumission)
        success_message = WebDriverWait(driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".Toastify__toast-body"))
        )
        assert success_message.text == "Product saved successfully!", "Product was not created successfully"



