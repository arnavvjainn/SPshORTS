"use client";

import React, {useEffect, useState} from 'react'
import newsData from '../data/data.json';
import '../styles/page.css';
import {
  Card,
  CardContent,
  CardDescription,
  CardFooter,
  CardHeader,
  CardTitle,
} from "@/components/ui/card"
import PageHeader from '@/components/page-header';"../components/page-header"
import Banner from '../data/GOHNupCXIAATu4j.jpeg'



interface NewsItem {
  image_link: string;
  title: string;
}


export default function Home() {
  const [news] = useState<NewsItem[]>(newsData);

  return (
    <div>
      <PageHeader/>
      <div className="grid-container">
        {news.map((item, index) => (
          <Card key={index} className="grid-item">
            <CardHeader>
              <CardTitle className="card-title">{item.title}</CardTitle>
            </CardHeader>
            <CardContent className="card-content">
              <img src={item.image_link} alt={item.title} className="card-image" />
            </CardContent>
          </Card>
        ))}
      </div>
    </div>
  );
}