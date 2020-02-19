import { Component, OnInit } from '@angular/core';

import { products } from '../products';
import { ProductService} from '../product.service';

@Component({
  selector: 'app-product-list',
  templateUrl: './product-list.component.html',
  styleUrls: ['./product-list.component.css']
})
export class ProductListComponent implements OnInit {
  products: any;

  constructor(private productService: ProductService) {}


  ngOnInit() {
    this.getProducts();
  }

  getProducts() {
    // tslint:disable-next-line:no-shadowed-variable
    this.productService.getProducts().subscribe(products => this.products = products);
  }} 