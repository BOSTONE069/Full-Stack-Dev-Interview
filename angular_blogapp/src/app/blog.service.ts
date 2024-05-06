import { Injectable } from '@angular/core';
import { HttpClient, HttpParams, HttpErrorResponse } from '@angular/common/http';
import { Observable, throwError } from 'rxjs';
import { catchError, map } from 'rxjs/operators';


export interface BlogPost {
  id: number;
  title: string;
  content: string;
  author: string;
  created_at: string;
  updated_at: string;
}
@Injectable({
  providedIn: 'root'
})
export class BlogService {

  private apiUrl = 'http://localhost:8000/api/blogposts/';

  constructor(private http: HttpClient) {}

  private handleError(error: HttpErrorResponse): Observable<never> {
    if (error.error instanceof ErrorEvent) {
      console.error('An error occurred:', error.error.message);
    } else {
      console.error(
        `Backend returned code ${error.status}, body was: ${error.error}`
      );
    }
    return throwError('Something went wrong; please try again later.');
  }


  getBlogPosts(
    page: number = 1,
    pageSize: number = 10,
    sortField: string = 'created_at',
    sortOrder: string = 'desc'
  ): Observable<BlogPost[]> {
    const params = new HttpParams()
      .set('page', page.toString())
      .set('page_size', pageSize.toString())
      .set('ordering', `${sortOrder === 'desc' ? '-' : ''}${sortField}`);

    return this.http.get<any>(this.apiUrl, { params }).pipe(
      map(response => response.results)
    );
  }

  getBlogPost(id: number): Observable<BlogPost> {
    return this.http.get<BlogPost>(`${this.apiUrl}${id}/`);
  }
}
