import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { HttpClient } from '@angular/common/http';

import { Node, NodeResult } from '../models/Node';



@Injectable({
  providedIn: 'root'
})
export class NodeService {
  // url: string = 'https://jsonplaceholder.typicode.com/todos';
  url: string = 'http://192.168.31.148/api/nodes';

  constructor(private http:HttpClient) { }

  getNodeResults():Observable<NodeResult> {
    return this.http.get<NodeResult>(`${this.url}`);
  }
}
