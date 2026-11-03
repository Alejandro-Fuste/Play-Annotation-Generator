# Play-Annotation-Generator Annotation Review — Post10to15_9

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Post10to15_9`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Pass_Post10to15`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 34
- **Ball Tracks:** 0
- **Action Segments:** 90
- **Validation Warnings:** 87
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 5
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `17` | `17` |
| ⚠️ START CHANGED | `Action_PassBlock` | C | offense | `17` | `17` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `8` | `8` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `8` | `8` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `17` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `18` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `19` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 0 | START | 0 | 37 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 0 | START | 0 | 26 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `6` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `8` | `Group` | 0 | START | 0 | 23 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 26 |
| ✅ EXACT | `Action_BallSnap` | C | `17` | `17` | 24 | START | 24 | 38 |
| ⚠️ START CHANGED | `Action_PassBlock` | C | `17` | `17` | 27 | START | 39 | 66 |
| ✅ EXACT | `Action_PassBlock` | LG | `18` | `18` | 27 | START | 27 | 102 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RG | `20` | `20` | 27 | START | 27 | 46 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `21` | `21` | 27 | START | 27 | 62 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | LT | `9` | `9` | 27 | START | 27 | 125 |
| ✅ EXACT | `Action_RunPostRoute` | WR1 | `2` | `2` | 38 | START | 38 | 170 |
| ✅ EXACT | `Action_SnapReceive` | QB | `8` | `8` | 38 | END | 24 | 38 |
| ✅ EXACT | `Action_ThrowPass` | QB | `8` | `8` | 90 | START | 90 | 99 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–198
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_SnapReceive` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_None` | 39 | 89 | 51 | inferred_complete_timeline |
| `Action_ThrowPass` | 90 | 99 | 10 | inferred_complete_timeline |
| `Action_None` | 100 | 198 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–124
- **Visible Samples:** 109

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 96 | 73 | inferred_complete_timeline |
| `Action_None` | 104 | 110 | 7 | inferred_complete_timeline |
| `Action_None` | 115 | 117 | 3 | inferred_complete_timeline |
| `Action_None` | 123 | 124 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–170
- **Visible Samples:** 171

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 37 | 38 | inferred_complete_timeline |
| `Action_RunPostRoute` | 38 | 170 | 133 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 0–206
- **Visible Samples:** 207

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 206 | 183 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–234
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 234 | 211 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 0–231
- **Visible Samples:** 232

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 231 | 208 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–205
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 125 | 99 | inferred_complete_timeline |
| `Action_PassBlock` | 131 | 179 | 49 | inferred_complete_timeline |
| `Action_PassBlock` | 185 | 205 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–102
- **Visible Samples:** 103

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 102 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 0–66
- **Visible Samples:** 67

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_BallSnap` | 24 | 38 | 15 | inferred_complete_timeline |
| `Action_PassBlock` | 39 | 66 | 28 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–57
- **Visible Samples:** 51

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 46 | 20 | inferred_complete_timeline |
| `Action_PassBlock` | 54 | 57 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–220
- **Visible Samples:** 197

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 26 | 27 | inferred_complete_timeline |
| `Action_PassBlock` | 27 | 62 | 36 | inferred_complete_timeline |
| `Action_PassBlock` | 65 | 67 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 69 | 73 | 5 | inferred_complete_timeline |
| `Action_PassBlock` | 75 | 100 | 26 | inferred_complete_timeline |
| `Action_PassBlock` | 104 | 116 | 13 | inferred_complete_timeline |
| `Action_PassBlock` | 119 | 172 | 54 | inferred_complete_timeline |
| `Action_PassBlock` | 175 | 181 | 7 | inferred_complete_timeline |
| `Action_PassBlock` | 195 | 220 | 26 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–95
- **Visible Samples:** 96

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 95 | 72 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 216

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 126 | 103 | inferred_complete_timeline |
| `Action_None` | 131 | 219 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–216
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 180 | 157 | inferred_complete_timeline |
| `Action_None` | 185 | 216 | 32 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 233 | 210 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 239 | 216 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–203
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 179 | 156 | inferred_complete_timeline |
| `Action_None` | 186 | 203 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 182 | 159 | inferred_complete_timeline |
| `Action_None` | 187 | 239 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–219
- **Visible Samples:** 220

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 219 | 196 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 0–230
- **Visible Samples:** 231

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 230 | 207 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 218

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 174 | 151 | inferred_complete_timeline |
| `Action_None` | 176 | 177 | 2 | inferred_complete_timeline |
| `Action_None` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_None` | 185 | 188 | 4 | inferred_complete_timeline |
| `Action_None` | 203 | 222 | 20 | inferred_complete_timeline |
| `Action_None` | 226 | 239 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 23 | 24 | inferred_complete_timeline |
| `Action_None` | 24 | 239 | 216 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 41–42 | 2 | 1 | Undefined position; Undefined team |
| `23` | `23` | Position_Unknown | Team_Unknown | 56–72 | 5 | 2 | Undefined position; Undefined team |
| `24` | `29` | Position_Unknown | Team_Unknown | 94–227 | 134 | 1 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 94–103 | 8 | 2 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 95–222 | 118 | 3 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 111–215 | 97 | 3 | Undefined position; Undefined team |
| `28` | `33` | Position_Unknown | Team_Unknown | 116–205 | 85 | 3 | Undefined position; Undefined team |
| `29` | `35` | Position_Unknown | Team_Unknown | 145–146 | 2 | 1 | Undefined position; Undefined team |
| `30` | `36` | Position_Unknown | Team_Unknown | 153–225 | 73 | 1 | Undefined position; Undefined team |
| `31` | `38` | Position_Unknown | Team_Unknown | 158–163 | 6 | 1 | Undefined position; Undefined team |
| `32` | `39` | Position_Unknown | Team_Unknown | 195–197 | 3 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 235–236 | 2 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ `Action_PassBlock` for actor_track_id `17` (C): Annotated start 27 != Inferred start 39
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (8 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `9` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `13` (actor_track_id `13`): `SAF1` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 61 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Resolved action overlap for track '17' (C): higher_priority='Action_BallSnap' [24–38], lower_priority='Action_PassBlock' annotated_start=27, effective_Action_PassBlock_start=39.
- ⚠️ Action 'Action_None' range [24-95] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-180] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-216] for track '1' has 6 frames without a visible bounding box.
- ⚠️ Action 'Action_RunPostRoute' range [38-170] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-233] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-179] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-203] for track '4' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-234] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-206] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-182] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-239] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [100-198] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-125] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [131-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [185-205] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-126] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [131-219] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-174] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [176-177] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-222] for track '13' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-96] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [104-110] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [115-117] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [123-124] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-219] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-230] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [39-66] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-102] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [24-231] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-46] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [54-57] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [27-62] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [65-67] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [69-73] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [75-100] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [104-116] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [119-172] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [175-181] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [195-220] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [41-42] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [56-58] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [71-72] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-227] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [94-95] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [98-103] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-180] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [187-188] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-222] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [111-180] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-188] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-215] for track '27' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [116-180] for track '28' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [185-191] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-205] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-146] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-225] for track '30' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-163] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-197] for track '32' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-236] for track '33' has 1 frames without a visible bounding box.
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

</details>