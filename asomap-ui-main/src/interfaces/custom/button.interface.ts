export interface IButton {
    children: React.ReactNode;
    onClick?: () => void;
    className?: string;
    disabled?: boolean;
}