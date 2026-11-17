# Play-Annotation-Generator Annotation Review — Power_229

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Power_229`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_Power`
- **Result:** `Result_Tackle`
- **Result Frame:** 329
- **Player Tracks:** 26
- **Ball Tracks:** 0
- **Action Segments:** 54
- **Validation Warnings:** 45
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 14
- **Exact Matches:** 3
- **Group Expanded Events:** 10
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 0
- **Inferred Coverage Segments (Action_None):** 36
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `10` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `8` | `Group` |
| ✅ EXACT | `Action_DownBlock` | LG | offense | `20` | `20` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `3` | `3` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | offense | `8` | `8` |
| ✅ EXACT | `Action_PullBlock` | RG | offense | `12` | `12` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `0` | `Group` | 8 | START | 8 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `10` | `Group` | 8 | START | 8 | 189 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 8 | START | 8 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `14` | `Group` | 8 | START | 8 | 329 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `19` | `Group` | 8 | START | 8 | 169 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `2` | `Group` | 8 | START | 8 | 317 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `20` | `Group` | 8 | START | 8 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `3` | `Group` | 8 | START | 8 | 151 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `6` | `Group` | 8 | START | 8 | 259 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `8` | `Group` | 8 | START | 8 | 151 |
| ✅ EXACT | `Action_DownBlock` | LG | `20` | `20` | 152 | START | 152 | 181 |
| ✅ EXACT | `Action_DownBlock` | LT | `3` | `3` | 152 | START | 152 | 181 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | C | `8` | `8` | 152 | START | 152 | 157 |
| ✅ EXACT | `Action_PullBlock` | RG | `12` | `12` | 152 | START | 152 | 181 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 8–259
- **Visible Samples:** 252

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 259 | 252 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 169 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 173 | 329 | 157 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 319

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 317 | 310 | inferred_complete_timeline |
| `Action_PreSnap` | 321 | 329 | 9 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `offense`
- **Visible Frames:** 8–246
- **Visible Samples:** 236

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 189 | 182 | inferred_complete_timeline |
| `Action_PreSnap` | 191 | 240 | 50 | inferred_complete_timeline |
| `Action_PreSnap` | 243 | 246 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 299

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 151 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 181 | 30 | inferred_complete_timeline |
| `Action_None` | 182 | 214 | 33 | inferred_complete_timeline |
| `Action_None` | 229 | 230 | 2 | inferred_complete_timeline |
| `Action_None` | 240 | 329 | 90 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 151 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 181 | 30 | inferred_complete_timeline |
| `Action_None` | 182 | 227 | 46 | inferred_complete_timeline |
| `Action_None` | 230 | 329 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 151 | 144 | inferred_complete_timeline |
| `Action_DownBlock` | 152 | 157 | 6 | inferred_complete_timeline |
| `Action_DownBlock` | 159 | 181 | 23 | inferred_complete_timeline |
| `Action_None` | 182 | 329 | 148 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 151 | 144 | inferred_complete_timeline |
| `Action_PullBlock` | 152 | 181 | 30 | inferred_complete_timeline |
| `Action_None` | 182 | 189 | 8 | inferred_complete_timeline |
| `Action_None` | 191 | 329 | 139 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 257 | 250 | inferred_complete_timeline |
| `Action_PreSnap` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 163 | 156 | inferred_complete_timeline |
| `Action_PreSnap` | 167 | 208 | 42 | inferred_complete_timeline |
| `Action_PreSnap` | 212 | 329 | 118 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 8–250
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 169 | 162 | inferred_complete_timeline |
| `Action_PreSnap` | 171 | 173 | 3 | inferred_complete_timeline |
| `Action_PreSnap` | 177 | 178 | 2 | inferred_complete_timeline |
| `Action_PreSnap` | 183 | 195 | 13 | inferred_complete_timeline |
| `Action_PreSnap` | 197 | 250 | 54 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 316

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 216 | 209 | inferred_complete_timeline |
| `Action_PreSnap` | 223 | 329 | 107 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 321

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 308 | 301 | inferred_complete_timeline |
| `Action_PreSnap` | 310 | 329 | 20 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

<details>
<summary>CB4 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 320

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 233 | 226 | inferred_complete_timeline |
| `Action_PreSnap` | 236 | 329 | 94 | inferred_complete_timeline |

</details>

<details>
<summary>CB5 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 8–329
- **Visible Samples:** 322

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 329 | 322 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `1` | Position_Unknown | Team_Unknown | 8–329 | 322 | 1 | Undefined position; Undefined team |
| `15` | `15` | Position_Unknown | Team_Unknown | 8–329 | 322 | 1 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 44–51 | 8 | 1 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 218–221 | 4 | 1 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 226–329 | 102 | 2 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 262–329 | 68 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `8` (2 segments found)

### Track Identity Issues

- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 460: Duplicate assignment for track ID '5' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_PreSnap' range [8-317] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-181] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-214] for track '3' has 7 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-230] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [240-329] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-257] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-163] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [167-208] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-259] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-216] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [223-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [152-157] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [159-181] for track '8' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-189] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [191-240] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [243-246] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-189] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-169] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [171-173] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [177-178] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [183-195] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [197-250] for track '16' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-169] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-227] for track '20' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-329] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-308] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [44-51] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [218-221] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [226-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [302-329] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '15' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '15' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '22' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '22' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '23' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '23' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '24' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '24' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '25' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '25' has undefined team_side. Will map to Team_Unknown.

</details>