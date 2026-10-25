# Play-Annotation-Generator Annotation Review — BootPass_64

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `BootPass_64`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_BootPass`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 239
- **Player Tracks:** 35
- **Ball Tracks:** 2
- **Action Segments:** 94
- **Validation Warnings:** 102
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 9
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 2
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 74
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `10` | `10` |
| ✅ EXACT | `Action_RunBlock` | LT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | offense | `7` | `7` |
| ✅ EXACT | `Action_RunBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_FakeHandoff` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_BootAway` | QB | offense | `2` | `2` |
| ✅ EXACT | `Action_RunFlatRoute` | TE | offense | `6` | `6` |
| ✅ EXACT | `Action_ThrowPass` | RB | offense | `1` | `1` |
| ✅ EXACT | `Action_SecureCatch` | TE | offense | `6` | `6` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 65 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `10` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `2` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR | `4` | `Group` | 0 | START | 0 | 30 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `6` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `7` | `Group` | 0 | START | 0 | 39 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 39 |
| ✅ EXACT | `Action_BallSnap` | C | `10` | `10` | 31 | START | 31 | 46 |
| ✅ EXACT | `Action_RunBlock` | LT | `0` | `0` | 40 | START | 40 | 110 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | C | `10` | `10` | 40 | START | 47 | 50 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunBlock` | RG | `7` | `7` | 40 | START | 40 | 57 |
| ✅ EXACT | `Action_RunBlock` | LG | `8` | `8` | 40 | START | 40 | 120 |
| ✅ EXACT | `Action_SnapReceive` | QB | `2` | `2` | 46 | END | 31 | 46 |
| ✅ EXACT | `Action_FakeHandoff` | QB | `2` | `2` | 49 | START | 49 | 68 |
| ✅ EXACT | `Action_BootAway` | QB | `2` | `2` | 69 | START | 69 | 98 |
| ✅ EXACT | `Action_RunFlatRoute` | TE | `6` | `6` | 72 | START | 72 | 101 |
| ✅ EXACT | `Action_ThrowPass` | RB | `1` | `1` | 100 | START | 100 | 110 |
| ✅ EXACT | `Action_SecureCatch` | TE | `6` | `6` | 121 | START | 121 | 129 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_SnapReceive` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_None` | 47 | 48 | 2 | inferred_complete_timeline |
| `Action_FakeHandoff` | 49 | 68 | 20 | inferred_complete_timeline |
| `Action_BootAway` | 69 | 98 | 30 | inferred_complete_timeline |
| `Action_None` | 99 | 102 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 228

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 65 | 66 | inferred_complete_timeline |
| `Action_PreSnap` | 68 | 99 | 32 | inferred_complete_timeline |
| `Action_ThrowPass` | 100 | 110 | 11 | inferred_complete_timeline |
| `Action_None` | 111 | 221 | 111 | inferred_complete_timeline |
| `Action_None` | 231 | 234 | 4 | inferred_complete_timeline |
| `Action_None` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–99
- **Visible Samples:** 100

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 99 | 69 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_RunFlatRoute` | 72 | 101 | 30 | inferred_complete_timeline |
| `Action_None` | 102 | 120 | 19 | inferred_complete_timeline |
| `Action_SecureCatch` | 121 | 129 | 9 | inferred_complete_timeline |
| `Action_None` | 130 | 171 | 42 | inferred_complete_timeline |
| `Action_None` | 183 | 239 | 57 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–110
- **Visible Samples:** 111

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 110 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–120
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 120 | 81 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_BallSnap` | 31 | 46 | 16 | inferred_complete_timeline |
| `Action_RunBlock` | 47 | 50 | 4 | inferred_complete_timeline |
| `Action_RunBlock` | 55 | 124 | 70 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–121
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 39 | 40 | inferred_complete_timeline |
| `Action_RunBlock` | 40 | 57 | 18 | inferred_complete_timeline |
| `Action_RunBlock` | 59 | 110 | 52 | inferred_complete_timeline |
| `Action_RunBlock` | 112 | 114 | 3 | inferred_complete_timeline |
| `Action_RunBlock` | 120 | 121 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–57
- **Visible Samples:** 58

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 57 | 27 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 239 | 209 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–121
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 4 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 7 | 30 | 24 | inferred_complete_timeline |
| `Action_None` | 31 | 34 | 4 | inferred_complete_timeline |
| `Action_None` | 38 | 81 | 44 | inferred_complete_timeline |
| `Action_None` | 86 | 121 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–115
- **Visible Samples:** 108

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 44 | 14 | inferred_complete_timeline |
| `Action_None` | 47 | 87 | 41 | inferred_complete_timeline |
| `Action_None` | 94 | 115 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–214
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 37 | 7 | inferred_complete_timeline |
| `Action_None` | 39 | 111 | 73 | inferred_complete_timeline |
| `Action_None` | 116 | 137 | 22 | inferred_complete_timeline |
| `Action_None` | 139 | 184 | 46 | inferred_complete_timeline |
| `Action_None` | 186 | 187 | 2 | inferred_complete_timeline |
| `Action_None` | 189 | 197 | 9 | inferred_complete_timeline |
| `Action_None` | 199 | 203 | 5 | inferred_complete_timeline |
| `Action_None` | 213 | 214 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–224
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 137 | 107 | inferred_complete_timeline |
| `Action_None` | 139 | 195 | 57 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |
| `Action_None` | 221 | 224 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–98
- **Visible Samples:** 57

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 15 | 16 | inferred_complete_timeline |
| `Action_None` | 31 | 68 | 38 | inferred_complete_timeline |
| `Action_None` | 96 | 98 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–104
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_None` | 31 | 68 | 38 | inferred_complete_timeline |
| `Action_None` | 71 | 104 | 34 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `16` | Position_Unknown | Team_Unknown | 4–38 | 35 | 2 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 38–39 | 2 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 56–86 | 31 | 1 | Undefined position; Undefined team |
| `19` | `20` | Position_Unknown | Team_Unknown | 64–178 | 115 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 80–125 | 46 | 1 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 80–86 | 7 | 1 | Undefined position; Undefined team |
| `22` | `26` | Position_Unknown | Team_Unknown | 90–239 | 134 | 4 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 94–116 | 23 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 118–120 | 3 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 121–216 | 77 | 3 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 122–149 | 22 | 3 | Undefined position; Undefined team |
| `29` | `40` | Position_Unknown | Team_Unknown | 127–152 | 26 | 1 | Undefined position; Undefined team |
| `30` | `43` | Position_Unknown | Team_Unknown | 150–239 | 90 | 1 | Undefined position; Undefined team |
| `31` | `44` | Position_Unknown | Team_Unknown | 156–239 | 84 | 1 | Undefined position; Undefined team |
| `32` | `45` | Position_Unknown | Team_Unknown | 159–239 | 73 | 2 | Undefined position; Undefined team |
| `33` | `46` | Position_Unknown | Team_Unknown | 204–227 | 24 | 1 | Undefined position; Undefined team |
| `34` | `48` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |
| `35` | `49` | Position_Unknown | Team_Unknown | 237–239 | 3 | 1 | Undefined position; Undefined team |
| `36` | `50` | Position_Unknown | Team_Unknown | 238–239 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

| xml_track_id | actor_track_id | First Visible Frame | Last Visible Frame | Visible Samples | Coverage | Missing Frame Ranges |
| --- | --- | --- | --- | --- | --- | --- |
| `24` | `31` | 100 | 100 | 1 | 100.0% | None |
| `26` | `34` | 118 | 118 | 1 | 100.0% | None |

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_RunBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_RunBlock` and target `7` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 19 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 19 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 38 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 108: Duplicate assignment for track ID '13' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '10' (C): higher_priority='Action_BallSnap' [31–46], lower_priority='Action_RunBlock' annotated_start=40, effective_Action_RunBlock_start=47.
- ⚠️ Action 'Action_RunBlock' range [40-110] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-65] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-221] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-234] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-102] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-195] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-224] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-99] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-15] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-68] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-98] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-171] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-57] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [59-110] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [112-114] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [120-121] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [40-120] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-57] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [47-50] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunBlock' range [55-124] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-37] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [39-111] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-137] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-184] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-197] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-203] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [213-214] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-68] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-104] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-44] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-87] for track '14' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-115] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-4] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-34] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-81] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [31-38] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [38-39] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-86] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [64-178] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-125] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-86] for track '21' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [90-93] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [97-109] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-120] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-116] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-120] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-161] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-184] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [122-132] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-140] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-149] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-152] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-199] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-227] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Player track '16' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '16' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '18' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '18' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '19' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '19' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '20' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '20' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '21' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '21' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '31' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '31' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '32' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '32' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '33' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '33' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '34' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '34' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '35' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '35' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '36' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '36' has undefined team_side. Will map to Team_Unknown.

</details>