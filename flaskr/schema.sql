
CREATE TABLE Users (
    UserID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Role TEXT CHECK(Role IN ('customenr', 'sales', 'service')) NOT NULL,
    Email TEXT UNIQUE NOT NULL,
    Phone TEXT UNIQUE NOT NULL,
    Password TEXT NOT NULL
);

-- 创建车辆表
CREATE TABLE Vehicles (
    VehicleID INTEGER PRIMARY KEY AUTOINCREMENT,
    OwnerID INTEGER,
    Model TEXT NOT NULL,
    LicensePlate TEXT UNIQUE NOT NULL,
    VIN TEXT UNIQUE NOT NULL,
    PurchaseDate DATE NOT NULL,
    FOREIGN KEY (OwnerID) REFERENCES Users(UserID)
);

-- 创建零配件表
CREATE TABLE Parts (
    PartID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    VehicleModel TEXT NOT NULL,
    StockQuantity INTEGER NOT NULL CHECK(StockQuantity >= 0)
);

-- 创建营销活动表
CREATE TABLE Campaigns (
    CampaignID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Type TEXT NOT NULL,
    StartDate DATE NOT NULL,
    EndDate DATE NOT NULL,
    Budget REAL
);

-- 创建客户服务记录表
CREATE TABLE ServiceRecords (
    RecordID INTEGER PRIMARY KEY AUTOINCREMENT,
    VehicleID INTEGER,
    ServiceType TEXT CHECK(ServiceType IN ('充电', '换电', '维修')) NOT NULL,
    Date DATE NOT NULL,
    Description TEXT,
    Cost REAL,
    FOREIGN KEY (VehicleID) REFERENCES Vehicles(VehicleID)
);

-- 创建社交圈表
CREATE TABLE SocialCircles (
    CircleID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name TEXT NOT NULL,
    Description TEXT
);

-- 创建用户社交圈关系表
CREATE TABLE UserSocialRelations (
    UserID INTEGER,
    CircleID INTEGER,
    PRIMARY KEY (UserID, CircleID),
    FOREIGN KEY (UserID) REFERENCES Users(UserID),
    FOREIGN KEY (CircleID) REFERENCES SocialCircles(CircleID)
);
