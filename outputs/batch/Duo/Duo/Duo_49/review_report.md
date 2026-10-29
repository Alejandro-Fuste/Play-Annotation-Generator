# Play-Annotation-Generator Annotation Review — Duo_49

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Duo_49`
- **Frame Range:** 0 to 239 (240 total frames)
- **Play:** `Play_Run_Duo`
- **Result:** `Result_Tackle`
- **Result Frame:** 239
- **Player Tracks:** 25
- **Ball Tracks:** 0
- **Action Segments:** 80
- **Validation Warnings:** 88
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 15
- **Exact Matches:** 0
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `9` | `Group` |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | DE2 | defense | `15` | `15` |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | offense | `18` | `18` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `0` | `Group` | 0 | START | 0 | 165 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `13` | `Group` | 0 | START | 0 | 132 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `16` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `18` | `Group` | 0 | START | 0 | 143 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 0 | START | 0 | 81 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `21` | `Group` | 0 | START | 0 | 12 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `4` | `Group` | 0 | START | 0 | 177 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `5` | `Group` | 0 | START | 0 | 239 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `7` | `Group` | 0 | START | 0 | 163 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `8` | `Group` | 0 | START | 0 | 212 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `9` | `Group` | 0 | START | 0 | 174 |
| ❌ MISSING SEGMENT | `Action_ComboBlock` | DE2 | `15` | `15` | 144 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_ComboBlock` | RG | `18` | `18` | 144 | START | 144 | 166 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 188 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 0–174
- **Visible Samples:** 119

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 12 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 14 | 19 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 25 | 38 | 14 | inferred_complete_timeline |
| `Action_PreSnap` | 76 | 153 | 78 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 166 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 174 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 0–191
- **Visible Samples:** 190

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 177 | 178 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 191 | 12 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 210

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 165 | 166 | inferred_complete_timeline |
| `Action_PreSnap` | 170 | 205 | 36 | inferred_complete_timeline |
| `Action_PreSnap` | 211 | 212 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 231 | 232 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 239 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–212
- **Visible Samples:** 213

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 212 | 213 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–235
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 174 | 175 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 179 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 192 | 231 | 40 | inferred_complete_timeline |
| `Action_PreSnap` | 233 | 235 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–225
- **Visible Samples:** 221

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 132 | 133 | inferred_complete_timeline |
| `Action_PreSnap` | 138 | 225 | 88 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 163 | 164 | inferred_complete_timeline |
| `Action_PreSnap` | 225 | 239 | 15 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 0–182
- **Visible Samples:** 165

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 81 | 82 | inferred_complete_timeline |
| `Action_PreSnap` | 85 | 88 | 4 | inferred_complete_timeline |
| `Action_PreSnap` | 96 | 111 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 120 | 182 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–183
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 143 | 144 | inferred_complete_timeline |
| `Action_ComboBlock` | 144 | 166 | 23 | inferred_complete_timeline |
| `Action_ComboBlock` | 170 | 183 | 14 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 223

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 135 | 136 | inferred_complete_timeline |
| `Action_PreSnap` | 139 | 147 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 151 | 159 | 9 | inferred_complete_timeline |
| `Action_PreSnap` | 163 | 192 | 30 | inferred_complete_timeline |
| `Action_PreSnap` | 201 | 239 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–131
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 131 | 132 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 126 | 127 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 169 | 16 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 176 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 182 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 186 | 192 | 7 | inferred_complete_timeline |
| `Action_PreSnap` | 195 | 213 | 19 | inferred_complete_timeline |
| `Action_PreSnap` | 216 | 217 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 222 | 239 | 18 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 0–170
- **Visible Samples:** 141

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 72 | 73 | inferred_complete_timeline |
| `Action_PreSnap` | 75 | 76 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 78 | 85 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 87 | 135 | 49 | inferred_complete_timeline |
| `Action_PreSnap` | 162 | 170 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–215
- **Visible Samples:** 175

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 138 | 139 | inferred_complete_timeline |
| `Action_PreSnap` | 154 | 155 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 180 | 191 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 194 | 215 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>OLB2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–236
- **Visible Samples:** 235

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 196 | 197 | inferred_complete_timeline |
| `Action_PreSnap` | 199 | 236 | 38 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–207
- **Visible Samples:** 193

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_PreSnap` | 142 | 143 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 145 | 152 | 8 | inferred_complete_timeline |
| `Action_PreSnap` | 159 | 164 | 6 | inferred_complete_timeline |
| `Action_PreSnap` | 169 | 207 | 39 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 229

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 213 | 214 | inferred_complete_timeline |
| `Action_PreSnap` | 224 | 235 | 12 | inferred_complete_timeline |
| `Action_PreSnap` | 237 | 239 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 240

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 239 | 240 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–239
- **Visible Samples:** 237

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 215 | 216 | inferred_complete_timeline |
| `Action_PreSnap` | 219 | 239 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 0–140
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 22 | 23 | inferred_complete_timeline |
| `Action_PreSnap` | 24 | 50 | 27 | inferred_complete_timeline |
| `Action_PreSnap` | 53 | 54 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 56 | 140 | 85 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `25` | Position_Unknown | Team_Unknown | 132–226 | 77 | 6 | Undefined position; Undefined team |
| `23` | `30` | Position_Unknown | Team_Unknown | 172–191 | 20 | 1 | Undefined position; Undefined team |
| `24` | `33` | Position_Unknown | Team_Unknown | 203–239 | 35 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ❌ Missing segment for action `Action_ComboBlock` on target `15` (DE2)
- ⚠️ Ambiguous match for action `Action_ComboBlock` and target `18` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `2` (actor_track_id `2`): `SAF` position mapped to `defense` team
- ⚠️ Player track XML ID `19` (actor_track_id `19`): `SAF` position mapped to `defense` team
- ⚠️ 3 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 3 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 6 |
| Missing visible bounding boxes during action | 79 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 100: Duplicate assignment for track ID '14' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 239 as fallback play end.
- ⚠️ Segment 'Action_ComboBlock' for track '15' has invalid range: start=144, end=131. Clamping end to start.
- ⚠️ Action 'Action_PreSnap' range [0-165] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [170-205] for track '0' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [211-212] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [231-232] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [236-239] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-215] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [219-239] for track '2' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-196] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [199-236] for track '3' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-177] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-191] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-213] for track '6' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-235] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [237-239] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-163] for track '7' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [225-239] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-212] for track '8' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-174] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-179] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [192-231] for track '9' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [233-235] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-138] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-155] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-191] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [194-215] for track '10' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-72] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [75-76] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [78-85] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [87-135] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [162-170] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-135] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [139-147] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [151-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-192] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [201-239] for track '12' has 5 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-132] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [138-225] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-137] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [142-143] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [145-152] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [159-164] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [169-207] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-131] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-239] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-126] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [154-169] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-176] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-182] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [186-192] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [195-213] for track '17' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [216-217] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [222-239] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [144-166] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ComboBlock' range [170-183] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-22] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [24-50] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [53-54] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [56-140] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-81] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [85-88] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [96-111] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [120-182] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [0-12] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [14-19] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [25-38] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [76-153] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [163-166] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-174] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [132-174] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [180-193] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [200-204] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [208-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [217-222] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [224-226] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [172-191] for track '23' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [203-235] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [238-239] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.

</details>