# Play-Annotation-Generator Annotation Review — Counter_112

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_112`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 45
- **Ball Tracks:** 0
- **Action Segments:** 141
- **Validation Warnings:** 181
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 1
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 124
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | Team_Unknown | `18` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | Team_Unknown | `18` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `8` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | offense | `9` | `8` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `6` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LB2 | defense | `11` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `5` | `4` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `1` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `5` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `6` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 0 | START | 0 | 29 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 29 |
| ❌ MISSING SEGMENT | `Action_BallSnap` | Position_Unknown | `18` | `15` | 27 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | Position_Unknown | `18` | `15` | 30 | START | 33 | 41 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `8` | `7` | 30 | START | 30 | 49 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LT | `9` | `8` | 30 | START | 30 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `6` | `5` | 30 | START | 30 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | LB2 | `11` | `10` | 30 | START | 30 | 59 |
| ✅ EXACT | `Action_SnapReceive` | QB | `5` | `4` | 42 | END | 27 | 42 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `5` | `4` | 53 | START | 53 | 103 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 131 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_SnapReceive` | 27 | 42 | 16 | inferred_complete_timeline |
| `Action_None` | 43 | 52 | 10 | inferred_complete_timeline |
| `Action_BallCarry` | 53 | 103 | 51 | inferred_complete_timeline |
| `Action_BallCarry` | 125 | 247 | 123 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–169
- **Visible Samples:** 134

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 57 | 31 | inferred_complete_timeline |
| `Action_None` | 63 | 119 | 57 | inferred_complete_timeline |
| `Action_None` | 135 | 137 | 3 | inferred_complete_timeline |
| `Action_None` | 141 | 143 | 3 | inferred_complete_timeline |
| `Action_None` | 151 | 160 | 10 | inferred_complete_timeline |
| `Action_None` | 167 | 169 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 266

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 70 | 44 | inferred_complete_timeline |
| `Action_None` | 75 | 269 | 195 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–136
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 30 | 62 | 33 | inferred_complete_timeline |
| `Action_DownBlock` | 64 | 71 | 8 | inferred_complete_timeline |
| `Action_DownBlock` | 73 | 91 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 93 | 111 | 19 | inferred_complete_timeline |
| `Action_DownBlock` | 114 | 131 | 18 | inferred_complete_timeline |
| `Action_None` | 132 | 136 | 5 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 215

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_DownBlock` | 30 | 49 | 20 | inferred_complete_timeline |
| `Action_DownBlock` | 51 | 92 | 42 | inferred_complete_timeline |
| `Action_DownBlock` | 94 | 124 | 31 | inferred_complete_timeline |
| `Action_None` | 175 | 176 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 269 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 254

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullBlock` | 30 | 62 | 33 | inferred_complete_timeline |
| `Action_PullBlock` | 70 | 93 | 24 | inferred_complete_timeline |
| `Action_PullBlock` | 103 | 131 | 29 | inferred_complete_timeline |
| `Action_None` | 132 | 269 | 138 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–100
- **Visible Samples:** 86

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 61 | 35 | inferred_complete_timeline |
| `Action_None` | 74 | 90 | 17 | inferred_complete_timeline |
| `Action_None` | 92 | 93 | 2 | inferred_complete_timeline |
| `Action_None` | 95 | 97 | 3 | inferred_complete_timeline |
| `Action_None` | 99 | 100 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 217

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_None` | 40 | 56 | 17 | inferred_complete_timeline |
| `Action_None` | 59 | 65 | 7 | inferred_complete_timeline |
| `Action_None` | 70 | 78 | 9 | inferred_complete_timeline |
| `Action_None` | 103 | 154 | 52 | inferred_complete_timeline |
| `Action_None` | 165 | 171 | 7 | inferred_complete_timeline |
| `Action_None` | 174 | 269 | 96 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–119
- **Visible Samples:** 83

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 49 | 23 | inferred_complete_timeline |
| `Action_None` | 56 | 82 | 27 | inferred_complete_timeline |
| `Action_None` | 91 | 94 | 4 | inferred_complete_timeline |
| `Action_None` | 118 | 119 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–120
- **Visible Samples:** 106

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 47 | 21 | inferred_complete_timeline |
| `Action_None` | 49 | 76 | 28 | inferred_complete_timeline |
| `Action_None` | 91 | 120 | 30 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 114

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 29 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 30 | 59 | 30 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 64 | 75 | 12 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 82 | 103 | 22 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 108 | 119 | 12 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 124 | 131 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>OLB1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 127 | 101 | inferred_complete_timeline |
| `Action_None` | 188 | 269 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_None` | 27 | 98 | 72 | inferred_complete_timeline |
| `Action_None` | 101 | 124 | 24 | inferred_complete_timeline |
| `Action_None` | 127 | 216 | 90 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `13` | `16` | Position_Unknown | Team_Unknown | 12–16 | 5 | 1 | Undefined position; Undefined team |
| `14` | `17` | Position_Unknown | Team_Unknown | 19–179 | 106 | 8 | Undefined position; Undefined team |
| `15` | `18` | Position_Unknown | Team_Unknown | 33–45 | 11 | 2 | Undefined position; Undefined team |
| `16` | `19` | Position_Unknown | Team_Unknown | 47–102 | 31 | 3 | Undefined position; Undefined team |
| `17` | `21` | Position_Unknown | Team_Unknown | 61–70 | 10 | 1 | Undefined position; Undefined team |
| `18` | `22` | Position_Unknown | Team_Unknown | 83–85 | 3 | 1 | Undefined position; Undefined team |
| `19` | `23` | Position_Unknown | Team_Unknown | 94–159 | 64 | 3 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 95–269 | 85 | 5 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 100–117 | 17 | 2 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 133–198 | 66 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 135–168 | 31 | 2 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 138–269 | 125 | 4 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 139–269 | 87 | 4 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 142–173 | 27 | 2 | Undefined position; Undefined team |
| `27` | `34` | Position_Unknown | Team_Unknown | 142–147 | 6 | 1 | Undefined position; Undefined team |
| `28` | `35` | Position_Unknown | Team_Unknown | 149–267 | 85 | 4 | Undefined position; Undefined team |
| `29` | `36` | Position_Unknown | Team_Unknown | 153–190 | 37 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 167–249 | 82 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 168–269 | 102 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 170–269 | 76 | 4 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 175–239 | 65 | 1 | Undefined position; Undefined team |
| `34` | `44` | Position_Unknown | Team_Unknown | 175–269 | 90 | 2 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 180–269 | 90 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 182–198 | 17 | 1 | Undefined position; Undefined team |
| `37` | `48` | Position_Unknown | Team_Unknown | 186–269 | 79 | 4 | Undefined position; Undefined team |
| `38` | `49` | Position_Unknown | Team_Unknown | 204–233 | 27 | 2 | Undefined position; Undefined team |
| `39` | `50` | Position_Unknown | Team_Unknown | 205–269 | 64 | 2 | Undefined position; Undefined team |
| `40` | `51` | Position_Unknown | Team_Unknown | 208–209 | 2 | 1 | Undefined position; Undefined team |
| `41` | `52` | Position_Unknown | Team_Unknown | 212–269 | 58 | 1 | Undefined position; Undefined team |
| `42` | `53` | Position_Unknown | Team_Unknown | 215–269 | 32 | 2 | Undefined position; Undefined team |
| `43` | `58` | Position_Unknown | Team_Unknown | 267–269 | 3 | 1 | Undefined position; Undefined team |
| `44` | `59` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_BallSnap` on target `18` (Position_Unknown)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `18` (2 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (8 segments found)
- ⚠️ Ambiguous match for action `Action_DownBlock` and target `9` (5 segments found)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `6` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `11` (5 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `5` (2 segments found)

### Track Identity Issues

- ⚠️ 32 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 32 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 64 |
| Missing visible bounding boxes during action | 113 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Validation warning: Action 'Action_PullBlock' for track '5' (RG) duration 102 frames exceeds threshold 90 frames [start=30, end=131].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '7' (LG) duration 102 frames exceeds threshold 90 frames [start=30, end=131].
- ⚠️ Validation warning: Action 'Action_DownBlock' for track '8' (LT) duration 102 frames exceeds threshold 90 frames [start=30, end=131].
- ⚠️ Action 'Action_None' range [27-61] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [74-90] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [92-93] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-97] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [99-100] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-70] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [75-269] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-98] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-124] for track '2' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [127-216] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-57] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [63-119] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-137] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [141-143] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-160] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-169] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [53-103] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [125-247] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [30-62] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [70-93] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [103-131] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-127] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-49] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [51-92] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [94-124] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-176] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [30-62] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [64-71] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [73-91] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [93-111] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [132-136] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-49] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-82] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-94] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [118-119] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [30-59] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [64-75] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [82-103] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [108-119] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [124-131] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-47] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [49-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [91-120] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-26] for track '12' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [27-28] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [40-56] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [59-65] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [70-78] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [103-154] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-171] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [12-16] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '14' starts at frame 27, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [27-27] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [35-41] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [44-45] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [78-111] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [114-155] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-166] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-179] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [33-41] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [44-45] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-71] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [86-89] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [101-102] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [61-70] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [83-85] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-143] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-149] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-159] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [183-196] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-226] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-242] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-269] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-114] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-117] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-198] for track '22' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-168] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-177] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [181-185] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-217] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-144] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [152-202] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-235] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [242-269] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-162] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-173] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-147] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-178] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-185] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [218-236] for track '28' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-267] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-185] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-190] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-198] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-249] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-191] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-240] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-252] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-239] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-198] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-198] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-217] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [223-225] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-269] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-224] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-233] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-225] for track '39' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '40' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-240] for track '42' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-269] for track '43' has 1 frames without a visible bounding box.
- ⚠️ Player track '13' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '13' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '14' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '14' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
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
- ⚠️ Player track '37' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '37' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '38' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '38' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '39' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '39' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '40' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '40' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '41' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '41' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '42' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '42' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '43' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '43' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '44' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '44' has undefined team_side. Will map to Team_Unknown.

</details>