import { Component, OnInit } from '@angular/core';
import { BlogService, BlogPost } from '../blog.service';

@Component({
  selector: 'app-blog-list',
  templateUrl: './blog-list.component.html',
  styleUrls: ['./blog-list.component.css'],
})
export class BlogListComponent implements OnInit {
  blogPosts: BlogPost[] = [];
  page = 1;
  pageSize = 10;
  totalPosts = 0;
  sortField = 'created_at';
  sortOrder = 'desc';

  constructor(private blogService: BlogService) {}

  ngOnInit(): void {
    this.fetchBlogPosts();
  }

  fetchBlogPosts(): void {
    this.blogService
      .getBlogPosts(this.page, this.pageSize, this.sortField, this.sortOrder)
      .subscribe((posts) => {
        this.blogPosts = posts;
        this.totalPosts = posts.length; 
      });
  }

  onPageChange(newPage: number): void {
    this.page = newPage;
    this.fetchBlogPosts();
  }

  onSortChange(sortField: string, sortOrder: string): void {
    this.sortField = sortField;
    this.sortOrder = sortOrder;
    this.fetchBlogPosts();
  }
}
