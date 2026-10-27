# Play-Annotation-Generator Annotation Review — Counter_320

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_320`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 31
- **Ball Tracks:** 0
- **Action Segments:** 82
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 19
- **Exact Matches:** 4
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 5
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 59
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `13` | `12` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `10` | `9` |
| ✅ EXACT | `Action_PullLeadBlock` | RT | offense | `4` | `3` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `6` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `6` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | offense | `1` | `0` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `1` | `Group` | 0 | START | 0 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `10` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `11` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `13` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 0 | START | 0 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 80 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 80 |
| ✅ EXACT | `Action_BallSnap` | C | `13` | `12` | 78 | START | 78 | 93 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `13` | `12` | 81 | START | 94 | 125 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 81 | START | 81 | 188 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 81 | START | 81 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `10` | `9` | 81 | START | 81 | 138 |
| ✅ EXACT | `Action_PullLeadBlock` | RT | `4` | `3` | 81 | START | 81 | 112 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `6` | 93 | END | 78 | 93 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `6` | 109 | START | 109 | 136 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | RB | `1` | `0` | 137 | START | 137 | 138 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 188 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–210
- **Visible Samples:** 211

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_SnapReceive` | 78 | 93 | 16 | inferred_complete_timeline |
| `Action_None` | 94 | 108 | 15 | inferred_complete_timeline |
| `Action_Handoff` | 109 | 136 | 28 | inferred_complete_timeline |
| `Action_None` | 137 | 210 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 288

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 97 | 98 | inferred_complete_timeline |
| `Action_PreSnap` | 99 | 129 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 135 | 136 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 137 | 138 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 140 | 148 | 9 | inferred_complete_timeline |
| `Action_BallCarry` | 152 | 156 | 5 | inferred_complete_timeline |
| `Action_BallCarry` | 159 | 299 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 177

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 112 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 119 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 174 | 23 | inferred_complete_timeline |
| `Action_DownBlock` | 176 | 188 | 13 | inferred_complete_timeline |
| `Action_None` | 189 | 206 | 18 | inferred_complete_timeline |
| `Action_None` | 209 | 212 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_DownBlock` | 81 | 188 | 108 | inferred_complete_timeline |
| `Action_None` | 189 | 299 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_BallSnap` | 78 | 93 | 16 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 125 | 32 | inferred_complete_timeline |
| `Action_DownBlock` | 136 | 188 | 53 | inferred_complete_timeline |
| `Action_None` | 189 | 299 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–255
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullBlock` | 81 | 138 | 58 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 188 | 49 | inferred_complete_timeline |
| `Action_None` | 189 | 209 | 21 | inferred_complete_timeline |
| `Action_None` | 212 | 252 | 41 | inferred_complete_timeline |
| `Action_None` | 254 | 255 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–112
- **Visible Samples:** 113

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 80 | 81 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 81 | 112 | 32 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 170 | 93 | inferred_complete_timeline |
| `Action_None` | 177 | 218 | 42 | inferred_complete_timeline |
| `Action_None` | 220 | 299 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–153
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 153 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 299 | 222 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–220
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 199 | 122 | inferred_complete_timeline |
| `Action_None` | 204 | 220 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–188
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 188 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 88 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 297

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 77 | 78 | inferred_complete_timeline |
| `Action_None` | 78 | 208 | 131 | inferred_complete_timeline |
| `Action_None` | 212 | 299 | 88 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `16` | `17` | Position_Unknown | Team_Unknown | 74–152 | 77 | 4 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 111–299 | 142 | 5 | Undefined position; Undefined team |
| `18` | `20` | Position_Unknown | Team_Unknown | 114–299 | 186 | 1 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 123–171 | 49 | 1 | Undefined position; Undefined team |
| `20` | `22` | Position_Unknown | Team_Unknown | 130–299 | 169 | 2 | Undefined position; Undefined team |
| `21` | `23` | Position_Unknown | Team_Unknown | 158–299 | 142 | 1 | Undefined position; Undefined team |
| `22` | `25` | Position_Unknown | Team_Unknown | 179–251 | 73 | 1 | Undefined position; Undefined team |
| `23` | `27` | Position_Unknown | Team_Unknown | 189–190 | 2 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 202–299 | 86 | 3 | Undefined position; Undefined team |
| `25` | `32` | Position_Unknown | Team_Unknown | 222–299 | 78 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 229–299 | 71 | 1 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 237–299 | 63 | 1 | Undefined position; Undefined team |
| `28` | `37` | Position_Unknown | Team_Unknown | 247–299 | 53 | 1 | Undefined position; Undefined team |
| `29` | `38` | Position_Unknown | Team_Unknown | 271–299 | 29 | 1 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 280–299 | 20 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `13` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (5 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `10` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `1` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `4` (actor_track_id `5`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `15` (actor_track_id `16`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 43 |
| Track-related warning | 5 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '9' (RG) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '12' (C) duration 108 frames exceeds threshold 90 frames [start=81, end=188].
- ⚠️ Resolved action overlap for track '12' (C): higher_priority='Action_BallSnap' [78–93], lower_priority='Action_DownBlock' annotated_start=81, effective_Action_DownBlock_start=94.
- ⚠️ Action 'Action_PreSnap' range [0-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [99-129] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [137-138] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [140-148] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [152-156] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [159-299] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-188] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-199] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-220] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [81-112] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-88] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [137-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [81-112] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [114-119] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-174] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-206] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [209-212] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [81-138] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-209] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-252] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-255] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-125] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-153] for track '13' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-218] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-299] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-208] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-99] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-105] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-152] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-146] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [155-156] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-224] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-256] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-299] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-171] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-136] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-299] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-251] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-262] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-282] for track '24' has 2 frames without a visible bounding box.
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
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '26' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '26' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '27' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '27' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '28' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '28' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '29' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '29' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '30' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '30' has undefined team_side. Will map to Team_Unknown.

</details>