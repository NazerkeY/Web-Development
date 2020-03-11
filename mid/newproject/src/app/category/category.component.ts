import {Component, OnInit} from '@angular/core';
import {ActivatedRoute, Router} from '@angular/router';
import {BookService} from '../book.service';
import {CategoryService} from '../category.service';

@Component({
  selector: 'app-category',
  templateUrl: './category.component.html',
  styleUrls: ['./category.component.css']
})
export class CategoryComponent implements OnInit {
  books: any;
  category: any;
  constructor(
    private router: Router,
    private route: ActivatedRoute,
    private bookService: BookService,
    private categoryService: CategoryService
  ) {
    this.router.events.subscribe((value => {
      this.getBooks();
      this.getCategory();
    }));
  }

  ngOnInit() {
    this.getBooks();
    this.getCategory();
  }

  getBooks() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.bookService.getBooksByCategoryId(id).subscribe(books => this.books = books);
  }

  getCategory() {
    const id = +this.route.snapshot.paramMap.get('id');
    this.categoryService.getCategory(id).subscribe(category => this.category = category);
  }

}