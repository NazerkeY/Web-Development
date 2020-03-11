import { Component, OnInit } from '@angular/core';

import { books } from '../books';
import { BookService} from '../book.service';

@Component({
  selector: 'app-book-list',
  templateUrl: './book-list.component.html',
  styleUrls: ['./book-list.component.css']
})
export class BookListComponent implements OnInit {
  books: any;

  constructor(private bookService: BookService) {}


  ngOnInit() {
    this.getBooks();
  }

  getBooks() {
    // tslint:disable-next-line:no-shadowed-variable
    this.bookService.getBooks().subscribe(books => this.books = books);
  }} 