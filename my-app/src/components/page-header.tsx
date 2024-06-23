import React from "react";
import banner from "../../public/images/GOHNupCXIAATu4j.jpeg"
import "../styles/header.css"
import Image from "next/image";


export default function PageHeader() {
    return(
        <div>
            <Image src={banner} className="header-image" alt="Banner" />
        </div>
    )
}

