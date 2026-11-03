# Play-Annotation-Generator Annotation Review — Post10to15_67

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_67`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 269
- **Player Tracks:** 38
- **Ball Tracks:** 0
- **Action Segments:** 106
- **Validation Warnings:** 109
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 86
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `4` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `17` | `17` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `19` | `19` |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR4 | offense | `10` | `10` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `1` | `1` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `1` | `1` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `1` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `10` | `Group` | 0 | START | 0 | 22 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `16` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `19` | `Group` | 0 | START | 0 | 9 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `2` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `3` | `Group` | 0 | START | 0 | 6 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `4` | `Group` | 0 | START | 0 | 6 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 7 | START | 7 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `15` | `15` | 10 | START | 10 | 106 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `16` | `16` | 10 | START | 10 | 35 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `17` | `17` | 10 | START | 27 | 55 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LG | `18` | `18` | 10 | START | 10 | 21 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `19` | `19` | 10 | START | 10 | 111 |
| ⚠️ AMBIGUOUS MATCH | `Action_RunPostRoute` | WR4 | `10` | `10` | 23 | START | 23 | 64 |
| ✅ EXACT | `Action_SnapReceive` | QB | `1` | `1` | 23 | END | 7 | 23 |
| ✅ EXACT | `Action_ThrowPass` | QB | `1` | `1` | 68 | START | 68 | 79 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–218
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_SnapReceive` | 7 | 23 | 17 | inferred_complete_timeline |
| `Action_None` | 24 | 67 | 44 | inferred_complete_timeline |
| `Action_ThrowPass` | 68 | 79 | 12 | inferred_complete_timeline |
| `Action_None` | 80 | 98 | 19 | inferred_complete_timeline |
| `Action_None` | 100 | 129 | 30 | inferred_complete_timeline |
| `Action_None` | 136 | 139 | 4 | inferred_complete_timeline |
| `Action_None` | 158 | 218 | 61 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 269 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 214

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 213 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 88

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 58 | 52 | inferred_complete_timeline |
| `Action_None` | 60 | 88 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–259
- **Visible Samples:** 260

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 259 | 253 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 189

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_RunPostRoute` | 23 | 64 | 42 | inferred_complete_timeline |
| `Action_RunPostRoute` | 68 | 191 | 124 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–203
- **Visible Samples:** 201

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 35 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 38 | 53 | 16 | inferred_complete_timeline |
| `Action_PassBlock` | 55 | 203 | 149 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–88
- **Visible Samples:** 82

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 21 | 12 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 28 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 30 | 42 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 44 | 88 | 45 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–227
- **Visible Samples:** 203

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_BallSnap` | 7 | 21 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 55 | 29 | inferred_complete_timeline |
| `Action_PassBlock` | 62 | 64 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 70 | 77 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 227 | 141 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–229
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 106 | 97 | inferred_complete_timeline |
| `Action_PassBlock` | 117 | 137 | 21 | inferred_complete_timeline |
| `Action_PassBlock` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 154 | 161 | 8 | inferred_complete_timeline |
| `Action_PassBlock` | 163 | 164 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 171 | 229 | 59 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–230
- **Visible Samples:** 200

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 9 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 10 | 111 | 102 | inferred_complete_timeline |
| `Action_PassBlock` | 113 | 134 | 22 | inferred_complete_timeline |
| `Action_PassBlock` | 158 | 167 | 10 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 230 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–205
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 137 | 131 | inferred_complete_timeline |
| `Action_None` | 146 | 205 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `defense`
- **Visible Frames:** 0–17
- **Visible Samples:** 18

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 17 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–234
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 128 | 122 | inferred_complete_timeline |
| `Action_None` | 130 | 167 | 38 | inferred_complete_timeline |
| `Action_None` | 170 | 234 | 65 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 0–88
- **Visible Samples:** 89

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 88 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 269 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–222
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 222 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 0–251
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 251 | 245 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 269 | 263 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 117 | 111 | inferred_complete_timeline |
| `Action_None` | 119 | 269 | 151 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–179
- **Visible Samples:** 169

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 56 | 50 | inferred_complete_timeline |
| `Action_None` | 68 | 179 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–199
- **Visible Samples:** 191

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 6 | 7 | inferred_complete_timeline |
| `Action_None` | 7 | 169 | 163 | inferred_complete_timeline |
| `Action_None` | 178 | 180 | 3 | inferred_complete_timeline |
| `Action_None` | 182 | 199 | 18 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 13–17 | 5 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 22–231 | 194 | 5 | Undefined position; Undefined team |
| `24` | `25` | Position_Unknown | Team_Unknown | 47–52 | 6 | 1 | Undefined position; Undefined team |
| `25` | `27` | Position_Unknown | Team_Unknown | 89–248 | 160 | 1 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 113–133 | 21 | 1 | Undefined position; Undefined team |
| `27` | `33` | Position_Unknown | Team_Unknown | 135–232 | 97 | 2 | Undefined position; Undefined team |
| `28` | `36` | Position_Unknown | Team_Unknown | 150–180 | 26 | 3 | Undefined position; Undefined team |
| `29` | `37` | Position_Unknown | Team_Unknown | 151–166 | 8 | 2 | Undefined position; Undefined team |
| `30` | `38` | Position_Unknown | Team_Unknown | 159–216 | 56 | 2 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 192–269 | 76 | 2 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 196–220 | 12 | 2 | Undefined position; Undefined team |
| `33` | `43` | Position_Unknown | Team_Unknown | 202–269 | 56 | 2 | Undefined position; Undefined team |
| `34` | `46` | Position_Unknown | Team_Unknown | 220–231 | 12 | 1 | Undefined position; Undefined team |
| `35` | `56` | Position_Unknown | Team_Unknown | 233–269 | 35 | 3 | Undefined position; Undefined team |
| `36` | `60` | Position_Unknown | Team_Unknown | 235–242 | 8 | 1 | Undefined position; Undefined team |
| `37` | `65` | Position_Unknown | Team_Unknown | 255–269 | 15 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `15` (6 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `16` (3 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `17` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `18` (4 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `19` (4 segments found)
- ⚠️ Ambiguous match for action `Action_RunPostRoute` and target `10` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 16 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 16 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 32 |
| Missing visible bounding boxes during action | 75 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [7–23], lower_priority='Action_PassBlock' annotated_start=10, effective_Action_PassBlock_start=24.
- ⚠️ Action 'Action_None' range [7-213] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-98] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-129] for track '1' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [136-139] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-218] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-58] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [60-88] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-259] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-251] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-117] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-269] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-56] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [68-179] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [23-64] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [68-191] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-222] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-180] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-199] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-128] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [130-167] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [170-234] for track '13' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-137] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-205] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-106] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [117-137] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [147-149] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [154-161] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [163-164] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [171-229] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-35] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [38-53] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [55-203] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [7-21] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-55] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [62-64] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [70-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-227] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-21] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-28] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [30-42] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [44-88] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [10-111] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [113-134] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [158-167] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-230] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-17] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [7-88] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [13-17] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [22-42] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-75] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [80-105] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [107-111] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [119-231] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [47-52] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [89-248] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [113-133] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [135-229] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-232] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [150-151] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-167] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-180] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [151-156] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-166] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [159-198] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [201-216] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [192-193] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-269] for track '31' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-201] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [215-220] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [202-233] for track '33' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-231] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-244] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-249] for track '35' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-242] for track '36' has 1 frames without a visible bounding box.
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

</details>