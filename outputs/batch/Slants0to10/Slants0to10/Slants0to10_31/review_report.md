# Play-Annotation-Generator Annotation Review — Slants0to10_31

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Slants0to10_31`
- **Frame Range:** 0 to 269 (270 total frames)
- **Play:** `Play_Pass_Slants0to10`
- **Result:** `Result_Touchdown`
- **Result Frame:** 269
- **Player Tracks:** 30
- **Ball Tracks:** 0
- **Action Segments:** 75
- **Validation Warnings:** 79
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 21
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 48
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `15` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `5` | `Group` |
| ✅ EXACT | `Action_PassBlock` | LT | offense | `11` | `11` |
| ✅ EXACT | `Action_PassBlock` | RG | offense | `15` | `15` |
| ✅ EXACT | `Action_PassBlock` | LG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | offense | `4` | `4` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `16` | `16` |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | offense | `0` | `0` |
| ✅ EXACT | `Action_ThrowPass` | QB | offense | `16` | `16` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | offense | `0` | `0` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 45 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `1` | `Group` | 0 | START | 0 | 114 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `11` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `15` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `16` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `18` | `Group` | 0 | START | 0 | 3 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `2` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `21` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `4` | `Group` | 0 | START | 0 | 2 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `5` | `Group` | 0 | START | 0 | 49 |
| ✅ EXACT | `Action_PassBlock` | LT | `11` | `11` | 3 | START | 3 | 152 |
| ✅ EXACT | `Action_PassBlock` | RG | `15` | `15` | 3 | START | 3 | 146 |
| ✅ EXACT | `Action_PassBlock` | LG | `20` | `20` | 3 | START | 3 | 24 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | C | `21` | `21` | 3 | START | 3 | 81 |
| ⚠️ AMBIGUOUS MATCH | `Action_PassBlock` | RT | `4` | `4` | 3 | START | 3 | 135 |
| ✅ EXACT | `Action_SnapReceive` | QB | `16` | `16` | 3 | END | 3 | 3 |
| ✅ EXACT | `Action_RunSlantRoute` | WR1 | `0` | `0` | 46 | START | 46 | 63 |
| ✅ EXACT | `Action_ThrowPass` | QB | `16` | `16` | 46 | START | 46 | 56 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | WR1 | `0` | `0` | 87 | START | 87 | 103 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–138
- **Visible Samples:** 139

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_SnapReceive` | 3 | 3 | 1 | inferred_complete_timeline |
| `Action_None` | 4 | 45 | 42 | inferred_complete_timeline |
| `Action_ThrowPass` | 46 | 56 | 11 | inferred_complete_timeline |
| `Action_None` | 57 | 138 | 82 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–70
- **Visible Samples:** 62

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 3 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 11 | 62 | 52 | inferred_complete_timeline |
| `Action_PreSnap` | 65 | 70 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–265
- **Visible Samples:** 258

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 45 | 46 | inferred_complete_timeline |
| `Action_RunSlantRoute` | 46 | 63 | 18 | inferred_complete_timeline |
| `Action_None` | 64 | 86 | 23 | inferred_complete_timeline |
| `Action_BallCarry` | 87 | 103 | 17 | inferred_complete_timeline |
| `Action_BallCarry` | 106 | 107 | 2 | inferred_complete_timeline |
| `Action_BallCarry` | 110 | 230 | 121 | inferred_complete_timeline |
| `Action_BallCarry` | 235 | 265 | 31 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–269
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 49 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 51 | 269 | 219 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 168

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 114 | 115 | inferred_complete_timeline |
| `Action_PreSnap` | 119 | 126 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 130 | 158 | 29 | inferred_complete_timeline |
| `Action_PreSnap` | 166 | 172 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 175 | 183 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 0–163
- **Visible Samples:** 164

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–152
- **Visible Samples:** 153

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 152 | 150 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–24
- **Visible Samples:** 25

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 24 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 142

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 81 | 79 | inferred_complete_timeline |
| `Action_PassBlock` | 87 | 146 | 60 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `offense`
- **Visible Frames:** 0–146
- **Visible Samples:** 147

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 146 | 144 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–153
- **Visible Samples:** 144

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 2 | 3 | inferred_complete_timeline |
| `Action_PassBlock` | 3 | 135 | 133 | inferred_complete_timeline |
| `Action_PassBlock` | 141 | 142 | 2 | inferred_complete_timeline |
| `Action_PassBlock` | 144 | 147 | 4 | inferred_complete_timeline |
| `Action_PassBlock` | 152 | 153 | 2 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–193
- **Visible Samples:** 194

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 193 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 0–52
- **Visible Samples:** 53

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–154
- **Visible Samples:** 152

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 52 | 53 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 154 | 99 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–147
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 30 | 31 | inferred_complete_timeline |
| `Action_PreSnap` | 32 | 33 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 36 | 40 | 5 | inferred_complete_timeline |
| `Action_PreSnap` | 47 | 67 | 21 | inferred_complete_timeline |
| `Action_PreSnap` | 70 | 147 | 78 | inferred_complete_timeline |

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
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 269 | 270 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–227
- **Visible Samples:** 224

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_PreSnap` | 148 | 227 | 80 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 56 | 57 | inferred_complete_timeline |
| `Action_PreSnap` | 61 | 239 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–237
- **Visible Samples:** 238

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 237 | 238 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–269
- **Visible Samples:** 253

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 243 | 244 | inferred_complete_timeline |
| `Action_PreSnap` | 254 | 255 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 263 | 269 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 236 | 237 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `22` | Position_Unknown | Team_Unknown | 22–85 | 18 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 46–157 | 112 | 1 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 51–56 | 6 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 63–150 | 80 | 3 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 91–142 | 46 | 2 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 93–95 | 3 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 134–152 | 19 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 136–189 | 31 | 6 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_PassBlock` and target `21` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PassBlock` and target `4` (4 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `0` (4 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `7` (actor_track_id `7`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF2` position mapped to `defense` team
- ⚠️ 8 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 8 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 16 |
| Missing visible bounding boxes during action | 60 |
| Other | 3 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 269 as fallback play end.
- ⚠️ Action_SnapReceive present in CSV, but paired Action_BallSnap is missing.
- ⚠️ Action 'Action_BallCarry' range [87-103] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [106-107] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [110-230] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [235-265] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-114] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-126] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [130-158] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [166-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [175-183] for track '1' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-143] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [148-227] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-135] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [141-142] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [144-147] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [152-153] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-49] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-269] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-243] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [254-255] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-56] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [61-239] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-152] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-193] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-237] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-30] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [32-33] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [36-40] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [47-67] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [70-147] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-146] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [57-138] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-52] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-154] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-3] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [11-62] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [65-70] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-236] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-24] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [3-81] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PassBlock' range [87-146] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [22-27] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [34-35] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-85] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [46-157] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [51-56] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [63-108] for track '25' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [110-111] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [119-150] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [91-93] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [100-142] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [93-95] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [134-152] for track '28' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [136-143] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [146-149] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-157] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-178] for track '29' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [182-184] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [187-189] for track '29' has 1 frames without a visible bounding box.
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
- ⚠️ Play definition: no definition found for 'Play_Pass_Slants0to10'.

</details>