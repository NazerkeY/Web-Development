import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import {BookItemComponent} from './book-item/book-item.component';
import {CategoryComponent} from './category/category.component';


const routes: Routes = [
  { path: '', redirectTo: '/books', pathMatch: 'full'},
  { path: 'book-id/:id', component: BookItemComponent},
  { path: 'category/:id', component: CategoryComponent}
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }