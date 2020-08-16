import { Component, OnInit } from '@angular/core';

import { NodeService } from '../../services/node.service';
import { NodeResult } from '../../models/Node';


@Component({
  selector: 'app-node',
  templateUrl: './node.component.html',
  styleUrls: ['./node.component.scss']
})
export class NodeComponent implements OnInit {
  nodeResults: NodeResult;

  constructor(private nodeService: NodeService) { }

  ngOnInit(): void {
    this.nodeService.getNodeResults().subscribe(nodeResults => {
      this.nodeResults = nodeResults;
    });
  }

}
