import { Component, OnInit } from '@angular/core';
import { CompanyService } from "../company.service";
import { Company } from "../models";
import { Observable } from 'rxjs';


@Component({
  selector: 'app-company',
  templateUrl: './company.component.html',
  styleUrls: ['./company.component.css']
})
export class CompanyComponent implements OnInit {
  companies: Company[] = [];

  constructor(public companyService: CompanyService) {
  }

  ngOnInit(): void {
    this.getCompanyList();
  }

  getCompanyList() {
    this.companyService.getCompanyList()
      .subscribe(companies => {
        this.companies = companies
      });
  }

  deleteCompany(id){
    this.companyService.deleteCompany(id).subscribe(  res => {
      this.companies=this.companies.filter(c=>c.id!=id);
    });
  }
}
