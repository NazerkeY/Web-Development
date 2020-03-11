import { Injectable } from '@angular/core';
import {Observable, of} from 'rxjs';
import { books } from './books';

@Injectable({
  providedIn: 'root'
})
export class BookService {

  constructor() { }

  getBook(id: number): Observable<any> {
    return of(books.find(book => book.id === id));
  }

  getBooks(): Observable<any> {
    return of(books);
  }

  getBooksByCategoryId(id: number): Observable<any> {
    return of(books.filter(book => book.category_id === id));
  }
}