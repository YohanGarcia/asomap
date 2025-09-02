import React, { useState, useEffect } from 'react';
import { motion, AnimatePresence } from 'framer-motion';
import { FaTimes } from 'react-icons/fa';
import {
    calculatorLabels,
    InputFieldProps,
    ModalProps,
    CalculatorModalProps,
    initialValues,
    DEFAULT_LOAN_RATE
} from '@/mocks';

// Utility functions
const formatNumber = (value: number | undefined, decimals: number = 0) => {
    if (value === undefined || isNaN(value)) {
        return '';
    }
    return value.toLocaleString('es-DO', {
        minimumFractionDigits: decimals,
        maximumFractionDigits: decimals,
    });
};

const parseFormattedNumber = (value: string) => {
    return parseFloat(value.replace(/,/g, ''));
};

const generateLoanSchedule = (loanAmount: number, interestRate: number, loanTerm: number) => {
    const monthlyRate = interestRate / 100 / 12;
    const monthlyPayment = (loanAmount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -loanTerm));
    let balance = loanAmount;
    const schedule = [];

    for (let month = 1; month <= loanTerm; month++) {
        const interest = balance * monthlyRate;
        const principal = monthlyPayment - interest;
        balance -= principal;

        schedule.push({
            month,
            payment: monthlyPayment,
            principal,
            interest,
            balance: Math.max(0, balance)
        });
    }

    return schedule;
};

const generateCertificateSchedule = (certificateAmount: number, interestRate: number, certificateTerm: number) => {
    const dailyRate = interestRate / 100 / 360;
    const schedule = [];

    for (let month = 1; month <= Math.ceil(certificateTerm / 30); month++) {
        const daysInMonth = Math.min(30, certificateTerm - (month - 1) * 30);
        const interest = certificateAmount * dailyRate * daysInMonth;

        schedule.push({
            month,
            daysInMonth,
            interest,
            accumulatedInterest: interest * month
        });
    }

    return schedule;
};

const Modal: React.FC<ModalProps> = ({ isOpen, onClose, children }) => {
    useEffect(() => {
        const handleEscape = (event: KeyboardEvent) => {
            if (event.key === 'Escape') {
                onClose();
            }
        };

        if (isOpen) {
            document.addEventListener('keydown', handleEscape);
        }

        return () => {
            document.removeEventListener('keydown', handleEscape);
        };
    }, [isOpen, onClose]);

    return (
        <AnimatePresence>
            {isOpen && (
                <motion.div
                    className="fixed inset-0 z-50 overflow-hidden flex items-center justify-center p-4 bg-black bg-opacity-50 backdrop-blur-sm"
                    initial={{ scale: 0.8, opacity: 0 }}
                    animate={{ scale: 1, opacity: 1 }}
                    exit={{ scale: 0.8, opacity: 0 }}
                    transition={{ type: 'spring', damping: 20, stiffness: 300 }}
                >
                    <motion.div
                        className="bg-white w-full max-w-4xl rounded-xl overflow-hidden"
                        initial={{ scale: 0.9, opacity: 0 }}
                        animate={{ scale: 1, opacity: 1 }}
                        exit={{ scale: 0.9, opacity: 0 }}
                        transition={{ duration: 0.3 }}
                        onClick={(e) => e.stopPropagation()} // Evita que los clics en el modal cierren el fondo
                    >
                        <div className="flex justify-between items-center p-4 bg-gray-50">
                            <h3 className="text-lg font-semibold text-gray-900">Calculadora Financiera</h3>
                            <button
                                type="button"
                                className="text-xl text-primary hover:text-primary-accent transition-colors duration-200"
                                onClick={onClose}
                                aria-label="Cerrar calculadora"
                            >
                                <FaTimes />
                            </button>
                        </div>
                        <div className="p-6 max-h-[80vh] overflow-y-auto">
                            {children}
                        </div>
                    </motion.div>
                </motion.div>
            )}
        </AnimatePresence>
    );
};

const InputField: React.FC<InputFieldProps> = ({
    id,
    label,
    value,
    onChange,
    min = 0,
    max,
    decimals = 0,
    readOnly = false
}) => {
    const [inputValue, setInputValue] = useState(formatNumber(value ?? 0, decimals));

    useEffect(() => {
        setInputValue(formatNumber(value ?? 0, decimals));
    }, [value, decimals]);

    const handleChange = (e: React.ChangeEvent<HTMLInputElement>) => {
        const newValue = e.target.value.replace(/[^0-9.]/g, '');
        setInputValue(newValue);

        const parsed = parseFloat(newValue);
        if (!isNaN(parsed) && parsed >= min && (max === undefined || parsed <= max)) {
            onChange(parsed);
        }
    };

    const handleBlur = () => {
        const parsed = parseFormattedNumber(inputValue);
        if (isNaN(parsed) || parsed < min || (max !== undefined && parsed > max)) {
            setInputValue(formatNumber(value ?? 0, decimals));
        } else {
            setInputValue(formatNumber(parsed, decimals));
            onChange(parsed);
        }
    };

    return (
        <div>
            <label htmlFor={id} className="block text-sm font-medium text-gray-700 mb-1">
                {label}
            </label>
            <input
                type="text"
                id={id}
                value={inputValue}
                onChange={handleChange}
                onBlur={handleBlur}
                className={`w-full px-3 py-2 border border-gray-300 rounded-md focus:outline-none focus:ring-2 focus:ring-primary ${readOnly ? 'bg-gray-100' : ''}`}
                readOnly={readOnly}
            />
        </div>
    );
};

// CalculatorModal component
const CalculatorModal: React.FC<CalculatorModalProps> = ({ isOpen, closeModal }) => {
    const [loanAmount, setLoanAmount] = useState(initialValues.loan.amount);
    const [loanTerm, setLoanTerm] = useState(initialValues.loan.term);
    const [certificateAmount, setCertificateAmount] = useState(initialValues.certificate.amount);
    const [certificateTerm, setCertificateTerm] = useState(initialValues.certificate.term);
    const [calculatorType, setCalculatorType] = useState<'loan' | 'certificate'>('loan');
    const [interestRate, setInterestRate] = useState(DEFAULT_LOAN_RATE);
    const [showDetails, setShowDetails] = useState(false);

    useEffect(() => {
        if (!isOpen) {
            setLoanAmount(initialValues.loan.amount);
            setLoanTerm(initialValues.loan.term);
            setCertificateAmount(initialValues.certificate.amount);
            setCertificateTerm(initialValues.certificate.term);
            setInterestRate(DEFAULT_LOAN_RATE);
            setShowDetails(false);
        }
    }, [isOpen]);

    const calculateLoanPayment = () => {
        const monthlyRate = interestRate / 100 / 12;
        const payment = (loanAmount * monthlyRate) / (1 - Math.pow(1 + monthlyRate, -loanTerm));
        return formatNumber(payment, 2);
    };

    const calculateCertificateInterest = () => {
        const interest = (certificateAmount * interestRate * certificateTerm) / (360 * 100);
        return formatNumber(interest, 2);
    };

    const calculateMonthsFromDays = (days: number) => {
        const months = days / 30;
        return months.toFixed(1);
    };

    const handleInterestRateChange = (newRate: number) => {
        setInterestRate(newRate);
    };

    const loanSchedule = generateLoanSchedule(loanAmount, interestRate, loanTerm);
    const certificateSchedule = generateCertificateSchedule(certificateAmount, interestRate, certificateTerm);

    return (
        <Modal isOpen={isOpen} onClose={closeModal}>
            <motion.div
                className="modal-container animate-fade-in p-2"
                initial={{ scale: 0.8, opacity: 0 }}
                animate={{ scale: 1, opacity: 1 }}
                exit={{ scale: 0.8, opacity: 0 }}
                transition={{ duration: 0.3 }}
            >
                <div className="modal-header">
                    <motion.h2
                        className="modal-title text-lg font-bold"
                        key={calculatorType}
                        initial={{ opacity: 0 }}
                        animate={{ opacity: 1 }}
                        exit={{ opacity: 0 }}
                        transition={{ duration: 0.3 }}
                    >
                        {calculatorType === 'loan' ? 'Calculadora de Préstamos' : 'Calculadora de Certificados'}
                    </motion.h2>
                </div>
                <motion.div
                    className="modal-body space-y-2 p-2"
                    key={calculatorType}
                    initial={{ opacity: 0 }}
                    animate={{ opacity: 1 }}
                    exit={{ opacity: 0 }}
                    transition={{ duration: 0.3 }}
                >
                    <div className="flex space-x-4">
                        <button
                            type="button"
                            onClick={() => setCalculatorType('loan')}
                            className={`flex-1 py-2 px-4 rounded-md transition-colors duration-200 ${calculatorType === 'loan' ? 'bg-primary text-white' : 'bg-gray-200 text-gray-700 hover:bg-primary-accent'}`}
                        >
                            {calculatorLabels.loan.title}
                        </button>
                        <button
                            onClick={() => setCalculatorType('certificate')}
                            className={`flex-1 py-2 px-4 rounded-md transition-colors duration-200 ${calculatorType === 'certificate' ? 'bg-primary text-white' : 'bg-gray-200 text-gray-700 hover:bg-primary-accent'}`}
                        >
                            {calculatorLabels.certificate.title}
                        </button>
                    </div>
                    {calculatorType === 'loan' && (
                        <React.Fragment>
                            <InputField
                                id="loanAmount"
                                label="Monto del Préstamo"
                                value={loanAmount}
                                onChange={setLoanAmount}
                                className="rounded-md focus:ring focus:ring-blue-300"
                            />
                            <InputField
                                id="interestRate"
                                label="Tasa de Interés (%)"
                                value={interestRate}
                                onChange={handleInterestRateChange}
                                className="rounded-md focus:ring focus:ring-blue-300"
                            />
                            <InputField
                                id="loanTerm"
                                label="Plazo (meses)"
                                value={loanTerm}
                                onChange={setLoanTerm}
                                className="rounded-md focus:ring focus:ring-blue-300"
                            />
                            <button
                                type="button"
                                className="calculate-button w-full py-1 px-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors duration-200"
                                onClick={() => setShowDetails(!showDetails)}
                            >
                                Calcular
                            </button>
                        </React.Fragment>
                    )}
                    {calculatorType === 'certificate' && (
                        <React.Fragment>
                            <InputField
                                id="certificateAmount"
                                label="Monto del Certificado"
                                value={certificateAmount}
                                onChange={setCertificateAmount}
                                className="rounded-md focus:ring focus:ring-blue-300"
                            />
                            <InputField
                                id="interestRate"
                                label="Tasa de Interés (%)"
                                value={interestRate}
                                onChange={handleInterestRateChange}
                                className="rounded-md focus:ring focus:ring-blue-300"
                            />
                            <div>
                                <InputField
                                    id="certificateTerm"
                                    label="Plazo (días)"
                                    value={certificateTerm}
                                    onChange={setCertificateTerm}
                                    className="rounded-md focus:ring focus:ring-blue-300"
                                />
                                <p className="text-xs text-primary mt-1 ">
                                    {calculatorLabels.certificate.monthsEquivalent.replace('{0}', calculateMonthsFromDays(certificateTerm))}
                                </p>
                            </div>
                            <button
                                type="button"
                                className="calculate-button w-full py-1 px-3 bg-blue-600 text-white rounded-md hover:bg-blue-700 transition-colors duration-200"
                                onClick={() => setShowDetails(!showDetails)}
                            >
                                Calcular
                            </button>
                        </React.Fragment>
                    )}
                </motion.div>
                <div className="modal-footer p-2 bg-gray-50 rounded-md shadow">
                    {calculatorType === 'loan' && (
                        <React.Fragment>
                            <p className="schedule-title font-semibold">Pago Mensual</p>
                            <p className="text-lg text-primary font-bold mb-2">${calculateLoanPayment()}</p>
                            {showDetails && (
                                <div className="mt-2 overflow-x-auto">
                                    <table className="min-w-full divide-y divide-gray-200">
                                        <thead className="bg-gray-50">
                                            <tr>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Mes</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Cuota</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Interés</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Amortización</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Balance</th>
                                            </tr>
                                        </thead>
                                        <tbody className="bg-white divide-y divide-gray-200">
                                            {loanSchedule.map((row) => (
                                                <tr key={row.month}>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">{row.month}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">${formatNumber(row.payment, 2)}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">${formatNumber(row.interest, 2)}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">${formatNumber(row.principal, 2)}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">${formatNumber(row.balance, 2)}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            )}
                        </React.Fragment>
                    )}
                    {calculatorType === 'certificate' && (
                        <React.Fragment>
                            <p className="schedule-title font-semibold">Interés Ganado</p>
                            <p className="text-lg text-primary font-bold mb-2">${calculateCertificateInterest()}</p>
                            {showDetails && (
                                <div className="mt-2 overflow-x-auto">
                                    <table className="min-w-full divide-y divide-gray-200">
                                        <thead className="bg-gray-50">
                                            <tr>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Mes</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Días</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Interés</th>
                                                <th className="px-4 py-2 text-left text-xs font-medium text-gray-500 uppercase tracking-wider">Interés Acumulado</th>
                                            </tr>
                                        </thead>
                                        <tbody className="bg-white divide-y divide-gray-200">
                                            {certificateSchedule.map((row) => (
                                                <tr key={row.month}>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">{row.month}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">{row.daysInMonth}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">${formatNumber(row.interest, 2)}</td>
                                                    <td className="px-4 py-1 whitespace-nowrap text-sm text-gray-500">${formatNumber(row.accumulatedInterest, 2)}</td>
                                                </tr>
                                            ))}
                                        </tbody>
                                    </table>
                                </div>
                            )}
                            <p className="text-xs text-primary">
                                {calculatorLabels.certificate.note}
                            </p>
                        </React.Fragment>
                    )}
                </div>
            </motion.div>
        </Modal>
    );
};

export default CalculatorModal;