import React from 'react';
import { IButton } from '@interfaces';

export const Button: React.FC<IButton> = ({ children, onClick, className = '' }) => {
    return (
        <button
            type="button"
            className={` ${className}`}
            onClick={onClick}
        >
            <span className="truncate">
                {children}
            </span>
        </button>
    );
};