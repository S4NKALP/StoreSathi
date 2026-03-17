# ROADMAP

## Phase 1: Foundation & Core Identity
*Focus on the structural backbone and base entity.*
- [ ] **[core]**: Base models (Audit logs, Soft deletes), Shared utilities, and Global mixins.
- [ ] **[accounts]**: User registration, Multi-role RBAC (Admin, Cashier, Manager), and Authentication flow.
- [ ] **[products]**: Product catalog management: Categories, Units (UOM), Brands, and Attributes.

## Phase 2: Supply Chain & Inventory Control
*Focus on how products enter the system and where they reside.*
- [ ] **[suppliers]**: Vendor profiles, contact management, and performance tracking.
- [ ] **[inventory]**: Warehouse/Store management, Stock levels, Stock transfers (Inter-store), and Stock adjustments.
- [ ] **[purchases]**: Purchase Orders (PO), Supplier bills, and Stock Inward (GRN) processing.

## Phase 3: Sales Operations & POS
*Focus on the revenue-generating engine of the application.*
- [ ] **[pos]**: The POS Interface: Cart management, Quick search, Barcode entry, and Receipt printing.
- [ ] **[customers]**: Customer database, Purchase history, and basic CRM features.
- [ ] **[barcode]**: Dynamic Barcode (EAN-13/QR) generation for products and Label printing.

## Phase 4: Financials & Analytics
*Focus on tracking the health of the business.*
- [ ] **[expenses]**: Miscellaneous store expenses: Rent, Salaries, Utility bills, etc.
- [ ] **[reports]**: Dashboards for Sales, Inventory Valuation, Low stock alerts, and Profit/Loss reports.

## Phase 5: Engagement & Polish
*Focus on advanced features and user experience.*
- [ ] **[notifications]**: Real-time alerts (Websockets), Email/SMS for low stock or purchase order updates.
- [ ] **[UI/UX Refinement]**: Final Polish, Mobile responsiveness check, and Dark mode optimizations.

---