"use client";

import React, {useEffect, useState} from 'react'
import '../styles/page.css';
import PageHeader from '@/components/page-header';"../components/page-header"
import GridLayout from '@/components/grid-layout';


export default function Home() {
  return (
    <div className='relative-container'>
      <div className='header'>
        <PageHeader />
      </div>
      <div className='title'>
        <h1>You'll Never Walk Alone</h1>
      </div>
      <div className='grid'>
        <GridLayout/>
      </div>
    </div>
  );
}