import { NgModule } from '@angular/core';
import { Routes, RouterModule } from '@angular/router';
import { CompaniesListComponent } from './companies-list/companies-list.component';
import {CompanyPageComponent} from './company-page/company-page.component';


const routes: Routes = [
  {path: '', redirectTo: '/companies', pathMatch: 'full'},
  { path: 'companies', component: CompaniesListComponent },
  { path: 'companies/:id', component: CompanyPageComponent }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
