import {
    Card,
    CardContent,
    CardDescription,
    CardFooter,
    CardHeader,
    CardTitle,
} from "@/components/ui/card"
import { Button } from "@/components/ui/button"
import newsData from '../data/data.json'
import React, {useEffect, useState} from 'react'
import '../styles/grid.css'

interface NewsItem {
    image_link: string;
    title: string;
  }

export default function GridLayout () {
    const [news] = useState<NewsItem[]>(newsData);
    return (
        <div className="grid-container">
            {news.map((item, index) => (
            <Card key={index} className="grid-item">
                <img src={item.image_link} alt={item.title} className="card-image" />
                <CardHeader>
                    <CardTitle className="card-title">{item.title}</CardTitle>
                </CardHeader>
            </Card>
            ))}
        </div>
    
    )
}