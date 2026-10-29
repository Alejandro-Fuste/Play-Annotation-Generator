# Play-Annotation-Generator Annotation Review — Duo_2

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_2`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 29
- **Ball Tracks:** 0
- **Action Segments:** 77
- **Validation Warnings:** 94
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 17
- **Exact Matches:** 4
- **Group Expanded Events:** 9
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 58
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `9` | `Group` |
| ✅ EXACT | `Action_ComboBlock` | LG | offense | `10` | `10` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | offense | `11` | `11` |
| ⚠️ START CHANGED | `Action_ComboBlock` | DT1 | defense | `14` | `14` |
| ✅ EXACT | `Action_ComboBlock` | RG | offense | `3` | `3` |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | offense | `10` | `10` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `2` | `2` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `0` | `Group` | 0 | START | 0 | 198 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 0 | START | 0 | 154 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `10` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `11` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `12` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 102 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `3` | `Group` | 0 | START | 0 | 71 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `7` | `Group` | 0 | START | 0 | 216 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `9` | `Group` | 0 | START | 0 | 239 |
| ✅ EXACT | `Action_ComboBlock` | LG | `10` | `10` | 72 | START | 72 | 99 |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RT | `11` | `11` | 72 | START | 72 | 102 |
| ⚠️ START CHANGED | `Action_ComboBlock` | DT1 | `14` | `14` | 72 | START | 73 | 133 |
| ✅ EXACT | `Action_ComboBlock` | RG | `3` | `3` | 72 | START | 72 | 133 |
| ✅ EXACT | `Action_BlockSecondLevel` | LG | `10` | `10` | 100 | START | 100 | 133 |
| ✅ EXACT | `Action_BallCarry` | RB | `2` | `2` | 103 | START | 103 | 117 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 133 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–117
- **Visible Samples:** 118

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 102 | 103 | inferred_complete_timeline |
| `Action_BallCarry` | 103 | 117 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_PreSnap` | 41 | 239 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 154 | 155 | inferred_complete_timeline |
| `Action_PreSnap` | 156 | 235 | 80 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 219

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 216 | 217 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 220 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 198 | 199 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ComboBlock` | 72 | 99 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 100 | 133 | 34 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 155 | 3 | inferred_complete_timeline |
| `Action_None` | 157 | 170 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ComboBlock` | 72 | 133 | 62 | inferred_complete_timeline |
| `Action_None` | 134 | 239 | 106 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–223
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |
| `Action_ComboBlock` | 72 | 102 | 31 | inferred_complete_timeline |
| `Action_ComboBlock` | 105 | 133 | 29 | inferred_complete_timeline |
| `Action_None` | 135 | 223 | 89 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 185 | 186 | inferred_complete_timeline |
| `Action_PreSnap` | 189 | 192 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 239 | 41 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–71
- **Visible Samples:** 72

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 71 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–198
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |
| `Action_ComboBlock` | 73 | 133 | 61 | inferred_complete_timeline |
| `Action_None` | 134 | 198 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 67 | 68 | inferred_complete_timeline |
| `Action_PreSnap` | 105 | 110 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 124 | 152 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 157 | 181 | 25 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 193 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 232 | 239 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–160
- **Visible Samples:** 154

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 121 | 122 | inferred_complete_timeline |
| `Action_PreSnap` | 125 | 129 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 132 | 133 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 136 | 160 | 25 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–162
- **Visible Samples:** 105

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 92 | 93 | inferred_complete_timeline |
| `Action_PreSnap` | 97 | 106 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 161 | 162 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 222

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 127 | 128 | inferred_complete_timeline |
| `Action_PreSnap` | 146 | 239 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–164
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 26 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 28 | 33 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 68 | 33 | inferred_complete_timeline |
| `Action_PreSnap` | 71 | 73 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 79 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 89 | 150 | 62 | inferred_complete_timeline |
| `Action_PreSnap` | 153 | 164 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–64
- **Visible Samples:** 65

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 64 | 65 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `18` | `19` | Position_Unknown | Team_Unknown | 25–239 | 202 | 2 | Undefined position; Undefined team |
| `19` | `21` | Position_Unknown | Team_Unknown | 46–66 | 19 | 3 | Undefined position; Undefined team |
| `20` | `26` | Position_Unknown | Team_Unknown | 107–239 | 120 | 5 | Undefined position; Undefined team |
| `21` | `27` | Position_Unknown | Team_Unknown | 119–180 | 62 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 139–239 | 97 | 3 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 158–239 | 82 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 192–229 | 38 | 1 | Undefined position; Undefined team |
| `25` | `34` | Position_Unknown | Team_Unknown | 194–196 | 3 | 1 | Undefined position; Undefined team |
| `26` | `35` | Position_Unknown | Team_Unknown | 204–239 | 30 | 2 | Undefined position; Undefined team |
| `27` | `36` | Position_Unknown | Team_Unknown | 212–239 | 28 | 1 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 228–239 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `11` (2 segments found)
- ⚠️ `Action_ComboBlock` for actor_track_id `14` (DT1): Annotated start 72 != Inferred start 73

### Track Identity Issues

- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 71 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [0-198] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-154] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [156-235] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [103-117] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-239] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-121] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [125-129] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-133] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-160] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-92] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [97-106] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [161-162] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-127] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-239] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-216] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-220] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-185] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [189-192] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-239] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [100-133] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-170] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [72-102] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [105-133] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-223] for track '11' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-37] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [41-239] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-64] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [73-133] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-198] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-71] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-9] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-26] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [28-33] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-68] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [71-73] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-79] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [89-150] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [153-164] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-67] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [105-110] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [124-152] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [157-181] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-193] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [232-239] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-165] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [179-239] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-47] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [49-63] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-66] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [107-110] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [117-194] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [205-206] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-239] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-180] for track '21' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-189] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-235] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [158-239] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-229] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-196] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [204-205] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-239] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [212-239] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [228-239] for track '28' has 1 frames without a visible bounding box.
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

</details>