"""
Realistic Solidity Code Generator - 900 Gerçek Solidity Kontratı Üret
Her task ve persona için uygun, gerçekçi Solidity kodları üretir
"""

import pandas as pd
import json
import random

# Persona'ların kod stilleri
PERSONA_STYLES = {
    "Dr. Ayşe - Beginner Friendly": {
        "comments": "extensive",  # Çok detaylı yorumlar
        "complexity": "simple",    # Basit yapı
        "security": "basic",       # Temel güvenlik
        "gas_optimization": "low"  # Az optimize
    },
    "Prof. Mehmet - Academic": {
        "comments": "extensive",
        "complexity": "moderate",
        "security": "high",
        "gas_optimization": "moderate"
    },
    "Öğretmen Zeynep - Practical": {
        "comments": "moderate",
        "complexity": "moderate",
        "security": "moderate",
        "gas_optimization": "moderate"
    },
    "Ali - Facilitator": {
        "comments": "moderate",
        "complexity": "advanced",
        "security": "high",
        "gas_optimization": "moderate"
    },
    "Mentor Fatma - Supportive": {
        "comments": "extensive",
        "complexity": "moderate",
        "security": "high",
        "gas_optimization": "low"
    },
    "Ahmet - Smart Contract Beginner": {
        "comments": "basic",
        "complexity": "simple",
        "security": "basic",
        "gas_optimization": "low"
    },
    "Elif - Security Aware": {
        "comments": "moderate",
        "complexity": "moderate",
        "security": "very_high",
        "gas_optimization": "moderate"
    },
    "Can - Gas Optimizer": {
        "comments": "minimal",
        "complexity": "advanced",
        "security": "high",
        "gas_optimization": "very_high"
    },
    "Deniz - DApp Architect": {
        "comments": "moderate",
        "complexity": "advanced",
        "security": "high",
        "gas_optimization": "high"
    },
    "Burak - Blockchain Specialist": {
        "comments": "moderate",
        "complexity": "very_advanced",
        "security": "very_high",
        "gas_optimization": "high"
    }
}

# Task bazlı kod şablonları
TASK_TEMPLATES = {
    "Token Transfer Contract - ERC20 benzeri basit token": {
        "simple": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleToken
 * @dev Basit bir ERC20-benzeri token kontratı
 * @notice Bu kontrat eğitim amaçlıdır
 */
contract SimpleToken {{
    // Token bilgileri
    string public name = "Simple Token";
    string public symbol = "SMP";
    uint8 public decimals = 18;
    uint256 public totalSupply;

    // Bakiye kayıtları
    mapping(address => uint256) public balanceOf;

    // Events
    event Transfer(address indexed from, address indexed to, uint256 value);

    {constructor}

    /**
     * @dev Token transferi yapar
     * @param _to Alıcı adresi
     * @param _value Transfer miktarı
     * @return success Transfer başarılı mı?
     */
    function transfer(address _to, uint256 _value) public returns (bool success) {{
        {transfer_logic}
    }}

    {additional_functions}
}}""",
        "advanced": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

{imports}

/**
 * @title AdvancedToken
 * @dev Gas-optimized ERC20 token with security features
 */
contract AdvancedToken {{
    string public constant name = "Advanced Token";
    string public constant symbol = "ADV";
    uint8 public constant decimals = 18;
    uint256 public totalSupply;

    mapping(address => uint256) private _balances;
    mapping(address => mapping(address => uint256)) private _allowances;

    event Transfer(address indexed from, address indexed to, uint256 value);
    event Approval(address indexed owner, address indexed spender, uint256 value);

    {constructor}

    function balanceOf(address account) external view returns (uint256) {{
        return _balances[account];
    }}

    function transfer(address to, uint256 amount) external returns (bool) {{
        {optimized_transfer}
    }}

    {advanced_features}
}}"""
    },

    "Voting System - Basit oylama mekanizması": {
        "simple": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleVoting
 * @dev Basit bir oylama sistemi
 */
contract SimpleVoting {{
    struct Proposal {{
        string description;
        uint256 voteCount;
        bool executed;
    }}

    address public owner;
    Proposal[] public proposals;
    mapping(address => bool) public hasVoted;

    event ProposalCreated(uint256 proposalId, string description);
    event Voted(address voter, uint256 proposalId);

    {constructor}

    /**
     * @dev Yeni teklif oluşturur
     */
    function createProposal(string memory _description) public {{
        {proposal_logic}
    }}

    /**
     * @dev Teklife oy verir
     */
    function vote(uint256 _proposalId) public {{
        {vote_logic}
    }}

    {additional_functions}
}}""",
        "advanced": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/access/Ownable.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";

/**
 * @title AdvancedVoting
 * @dev Weighted voting with delegation
 */
contract AdvancedVoting is Ownable, ReentrancyGuard {{
    struct Voter {{
        uint256 weight;
        bool voted;
        address delegate;
        uint256 vote;
    }}

    struct Proposal {{
        bytes32 name;
        uint256 voteCount;
        uint256 deadline;
    }}

    {state_variables}

    {constructor}

    function delegate(address to) external nonReentrant {{
        {delegation_logic}
    }}

    function vote(uint256 proposal) external {{
        {weighted_vote_logic}
    }}

    {advanced_features}
}}"""
    },

    "Escrow Contract - Güvenli ödeme sistemi": {
        "simple": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleEscrow
 * @dev İki taraf arasında güvenli ödeme
 */
contract SimpleEscrow {{
    address public buyer;
    address public seller;
    address public arbiter;
    uint256 public amount;
    bool public released;

    event FundsDeposited(address buyer, uint256 amount);
    event FundsReleased(address seller, uint256 amount);

    {constructor}

    /**
     * @dev Fon yatırma
     */
    function deposit() public payable {{
        {deposit_logic}
    }}

    /**
     * @dev Fon serbest bırakma
     */
    function releaseFunds() public {{
        {release_logic}
    }}

    {additional_functions}
}}""",
        "advanced": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/security/Pausable.sol";

/**
 * @title SecureEscrow
 * @dev Multi-signature escrow with dispute resolution
 */
contract SecureEscrow is ReentrancyGuard, Pausable {{
    enum State {{ AWAITING_PAYMENT, AWAITING_DELIVERY, COMPLETE, DISPUTED }}

    struct Transaction {{
        address payable buyer;
        address payable seller;
        uint256 amount;
        State state;
        uint256 deadline;
    }}

    {state_variables}

    modifier onlyBuyer(uint256 txId) {{
        require(msg.sender == transactions[txId].buyer, "Not buyer");
        _;
    }}

    {constructor}

    function createTransaction(address payable _seller) external payable nonReentrant {{
        {create_tx_logic}
    }}

    function confirmDelivery(uint256 txId) external onlyBuyer(txId) nonReentrant {{
        {confirm_logic}
    }}

    {dispute_resolution}
}}"""
    },

    "NFT Minting - ERC721 benzeri NFT": {
        "simple": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleNFT
 * @dev Basit NFT mint etme
 */
contract SimpleNFT {{
    string public name = "Simple NFT";
    string public symbol = "SNFT";
    uint256 public tokenCounter;

    mapping(uint256 => address) public tokenOwner;
    mapping(address => uint256) public balanceOf;

    event Minted(address to, uint256 tokenId);
    event Transfer(address from, address to, uint256 tokenId);

    {constructor}

    /**
     * @dev Yeni NFT mint eder
     */
    function mint() public {{
        {mint_logic}
    }}

    /**
     * @dev NFT transferi
     */
    function transfer(address _to, uint256 _tokenId) public {{
        {transfer_logic}
    }}

    {additional_functions}
}}""",
        "advanced": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC721/ERC721.sol";
import "@openzeppelin/contracts/token/ERC721/extensions/ERC721URIStorage.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AdvancedNFT
 * @dev Full ERC721 with metadata and royalties
 */
contract AdvancedNFT is ERC721, ERC721URIStorage, Ownable {{
    uint256 private _tokenIdCounter;
    uint96 public royaltyPercentage = 250; // 2.5%

    mapping(uint256 => address) private _royaltyReceivers;

    {constructor}

    function safeMint(address to, string memory uri) public onlyOwner {{
        {safe_mint_logic}
    }}

    function royaltyInfo(uint256 tokenId, uint256 salePrice) external view returns (address, uint256) {{
        {royalty_logic}
    }}

    {metadata_functions}
}}"""
    },

    "Staking Contract - Token stake etme": {
        "simple": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleStaking
 * @dev Basit token staking
 */
contract SimpleStaking {{
    mapping(address => uint256) public stakedBalance;
    mapping(address => uint256) public stakingTime;
    uint256 public rewardRate = 10; // 10% yıllık

    event Staked(address user, uint256 amount);
    event Unstaked(address user, uint256 amount);
    event RewardClaimed(address user, uint256 reward);

    {constructor}

    /**
     * @dev Token stake et
     */
    function stake() public payable {{
        {stake_logic}
    }}

    /**
     * @dev Stake çöz ve ödül al
     */
    function unstake() public {{
        {unstake_logic}
    }}

    {reward_calculation}
}}""",
        "advanced": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/token/ERC20/IERC20.sol";
import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AdvancedStaking
 * @dev Time-weighted rewards with compound interest
 */
contract AdvancedStaking is ReentrancyGuard, Ownable {{
    IERC20 public stakingToken;
    IERC20 public rewardToken;

    struct StakeInfo {{
        uint256 amount;
        uint256 timestamp;
        uint256 rewardDebt;
        uint256 accumulatedRewards;
    }}

    {state_variables}

    {constructor}

    function stake(uint256 amount) external nonReentrant {{
        {complex_stake_logic}
    }}

    function calculateRewards(address user) public view returns (uint256) {{
        {time_weighted_rewards}
    }}

    {compound_functions}
}}"""
    },

    "Auction System - Açık artırma sistemi": {
        "simple": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.0;

/**
 * @title SimpleAuction
 * @dev Basit açık artırma
 */
contract SimpleAuction {{
    address public seller;
    uint256 public highestBid;
    address public highestBidder;
    uint256 public endTime;
    bool public ended;

    mapping(address => uint256) public pendingReturns;

    event NewBid(address bidder, uint256 amount);
    event AuctionEnded(address winner, uint256 amount);

    {constructor}

    /**
     * @dev Teklif ver
     */
    function bid() public payable {{
        {bid_logic}
    }}

    /**
     * @dev Açık artırmayı sonlandır
     */
    function endAuction() public {{
        {end_logic}
    }}

    {withdrawal_functions}
}}""",
        "advanced": """// SPDX-License-Identifier: MIT
pragma solidity ^0.8.20;

import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";

/**
 * @title AdvancedAuction
 * @dev English auction with auto-extension and reserve price
 */
contract AdvancedAuction is ReentrancyGuard, Ownable {{
    enum AuctionState {{ ACTIVE, ENDED, CANCELLED }}

    struct Auction {{
        address payable seller;
        uint256 reservePrice;
        uint256 startTime;
        uint256 endTime;
        uint256 bidIncrement;
        uint256 highestBid;
        address highestBidder;
        AuctionState state;
    }}

    {state_variables}

    {constructor}

    function placeBid(uint256 auctionId) external payable nonReentrant {{
        {advanced_bid_logic}
    }}

    function finalizeAuction(uint256 auctionId) external nonReentrant {{
        {finalize_logic}
    }}

    {auto_extension_logic}
}}"""
    }
}


def generate_code_for_persona(task_name, persona_name):
    """Persona ve task'e göre kod üret"""

    style = PERSONA_STYLES.get(persona_name, {
        "comments": "moderate",
        "complexity": "moderate",
        "security": "moderate",
        "gas_optimization": "moderate"
    })

    # Template seç
    template_dict = TASK_TEMPLATES.get(task_name, {})

    if style["complexity"] in ["simple", "moderate"]:
        template = template_dict.get("simple", "// Placeholder code")
    else:
        template = template_dict.get("advanced", "// Placeholder code")

    # Placeholders doldur
    code = template.format(
        imports=generate_imports(style),
        constructor=generate_constructor(task_name, style),
        transfer_logic=generate_transfer_logic(style),
        proposal_logic=generate_proposal_logic(style),
        vote_logic=generate_vote_logic(style),
        deposit_logic=generate_deposit_logic(style),
        release_logic=generate_release_logic(style),
        mint_logic=generate_mint_logic(style),
        stake_logic=generate_stake_logic(style),
        unstake_logic=generate_unstake_logic(style),
        bid_logic=generate_bid_logic(style),
        end_logic=generate_end_logic(style),
        additional_functions=generate_additional_functions(task_name, style),
        state_variables="",
        create_tx_logic="",
        confirm_logic="",
        dispute_resolution="",
        safe_mint_logic="",
        royalty_logic="",
        metadata_functions="",
        complex_stake_logic="",
        time_weighted_rewards="",
        compound_functions="",
        advanced_bid_logic="",
        finalize_logic="",
        auto_extension_logic="",
        reward_calculation="",
        withdrawal_functions="",
        delegation_logic="",
        weighted_vote_logic="",
        advanced_features="",
        optimized_transfer=""
    )

    return code


def generate_imports(style):
    if style["complexity"] in ["advanced", "very_advanced"]:
        return """import "@openzeppelin/contracts/security/ReentrancyGuard.sol";
import "@openzeppelin/contracts/access/Ownable.sol";"""
    return ""


def generate_constructor(task_name, style):
    if style["comments"] == "extensive":
        return """/**
     * @dev Constructor - Kontratı başlatır
     */
    constructor() {
        owner = msg.sender;
        totalSupply = 1000000 * 10**18;
        balanceOf[msg.sender] = totalSupply;
    }"""
    else:
        return """constructor() {
        owner = msg.sender;
        totalSupply = 1000000 * 10**18;
        balanceOf[msg.sender] = totalSupply;
    }"""


def generate_transfer_logic(style):
    if style["security"] == "very_high":
        return """require(_to != address(0), "Invalid address");
        require(_value > 0, "Amount must be positive");
        require(balanceOf[msg.sender] >= _value, "Insufficient balance");

        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;

        emit Transfer(msg.sender, _to, _value);
        return true;"""
    else:
        return """require(balanceOf[msg.sender] >= _value);
        balanceOf[msg.sender] -= _value;
        balanceOf[_to] += _value;
        emit Transfer(msg.sender, _to, _value);
        return true;"""


def generate_proposal_logic(style):
    return """require(msg.sender == owner, "Only owner");
        proposals.push(Proposal({{
            description: _description,
            voteCount: 0,
            executed: false
        }}));
        emit ProposalCreated(proposals.length - 1, _description);"""


def generate_vote_logic(style):
    if style["security"] == "very_high":
        return """require(_proposalId < proposals.length, "Invalid proposal");
        require(!hasVoted[msg.sender], "Already voted");
        require(!proposals[_proposalId].executed, "Proposal executed");

        hasVoted[msg.sender] = true;
        proposals[_proposalId].voteCount++;

        emit Voted(msg.sender, _proposalId);"""
    else:
        return """require(!hasVoted[msg.sender]);
        hasVoted[msg.sender] = true;
        proposals[_proposalId].voteCount++;
        emit Voted(msg.sender, _proposalId);"""


def generate_deposit_logic(style):
    return """require(msg.sender == buyer, "Only buyer");
        require(msg.value > 0, "Amount required");
        amount = msg.value;
        emit FundsDeposited(buyer, amount);"""


def generate_release_logic(style):
    if style["security"] == "very_high":
        return """require(msg.sender == arbiter || msg.sender == buyer, "Unauthorized");
        require(!released, "Already released");
        require(amount > 0, "No funds");

        released = true;
        payable(seller).transfer(amount);
        emit FundsReleased(seller, amount);"""
    else:
        return """require(msg.sender == arbiter);
        released = true;
        payable(seller).transfer(amount);
        emit FundsReleased(seller, amount);"""


def generate_mint_logic(style):
    return """uint256 newTokenId = tokenCounter;
        tokenCounter++;
        tokenOwner[newTokenId] = msg.sender;
        balanceOf[msg.sender]++;
        emit Minted(msg.sender, newTokenId);"""


def generate_stake_logic(style):
    return """require(msg.value > 0, "Amount required");
        stakedBalance[msg.sender] += msg.value;
        stakingTime[msg.sender] = block.timestamp;
        emit Staked(msg.sender, msg.value);"""


def generate_unstake_logic(style):
    if style["security"] == "very_high":
        return """require(stakedBalance[msg.sender] > 0, "No stake");

        uint256 timeStaked = block.timestamp - stakingTime[msg.sender];
        uint256 reward = (stakedBalance[msg.sender] * rewardRate * timeStaked) / (365 days * 100);

        uint256 total = stakedBalance[msg.sender] + reward;
        stakedBalance[msg.sender] = 0;

        payable(msg.sender).transfer(total);
        emit Unstaked(msg.sender, total);"""
    else:
        return """uint256 amount = stakedBalance[msg.sender];
        stakedBalance[msg.sender] = 0;
        payable(msg.sender).transfer(amount);
        emit Unstaked(msg.sender, amount);"""


def generate_bid_logic(style):
    if style["security"] == "very_high":
        return """require(block.timestamp < endTime, "Auction ended");
        require(msg.value > highestBid, "Bid too low");
        require(!ended, "Auction finalized");

        if (highestBidder != address(0)) {{
            pendingReturns[highestBidder] += highestBid;
        }}

        highestBid = msg.value;
        highestBidder = msg.sender;
        emit NewBid(msg.sender, msg.value);"""
    else:
        return """require(msg.value > highestBid);
        if (highestBidder != address(0)) {{
            pendingReturns[highestBidder] += highestBid;
        }}
        highestBid = msg.value;
        highestBidder = msg.sender;
        emit NewBid(msg.sender, msg.value);"""


def generate_end_logic(style):
    return """require(block.timestamp >= endTime, "Too early");
        require(!ended, "Already ended");
        ended = true;
        payable(seller).transfer(highestBid);
        emit AuctionEnded(highestBidder, highestBid);"""


def generate_additional_functions(task_name, style):
    if style["comments"] == "extensive":
        return """
    /**
     * @dev Bakiye sorgulama
     * @param _owner Sorgulanacak adres
     * @return Bakiye miktarı
     */
    function getBalance(address _owner) public view returns (uint256) {
        return balanceOf[_owner];
    }"""
    return ""


def update_generated_codes_csv():
    """generated_codes.csv dosyasındaki kodları güncelle"""

    print("\n🔧 Gerçek Solidity kodları üretiliyor...")

    # CSV'yi oku
    df = pd.read_csv("synthetic_data_N150/generated_codes.csv")

    # Sessions CSV'sini de oku (task ve persona bilgisi için)
    sessions_df = pd.read_csv("synthetic_data_N150/task_sessions.csv")

    # Her kod için gerçek Solidity üret
    for idx, row in df.iterrows():
        session_id = row['session_id']

        # Session bilgisini bul
        session_info = sessions_df[sessions_df['session_id'] == session_id].iloc[0]
        task_name = session_info['task_name']
        persona_name = session_info['assigned_persona']

        # Gerçek kod üret
        realistic_code = generate_code_for_persona(task_name, persona_name)

        # CSV'deki kodu güncelle
        df.at[idx, 'code_text'] = realistic_code

        if (idx + 1) % 100 == 0:
            print(f"   ✅ {idx + 1}/900 kod üretildi")

    # Güncellenmiş CSV'yi kaydet
    df.to_csv("synthetic_data_N150/generated_codes.csv", index=False)
    print(f"\n✅ Tüm 900 kod güncellendi!")


if __name__ == "__main__":
    update_generated_codes_csv()
