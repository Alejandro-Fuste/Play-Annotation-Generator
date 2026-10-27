# Play-Annotation-Generator Annotation Review — Counter_86

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `Counter_86`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_Counter`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 72
- **Validation Warnings:** 75
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 18
- **Exact Matches:** 4
- **Group Expanded Events:** 7
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 2
- **Ambiguous Matches:** 3
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 53
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `10` |
| ✅ EXACT | `Action_DownBlock` | LT | offense | `1` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | offense | `12` | `11` |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | offense | `5` | `4` |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | offense | `8` | `7` |
| ✅ EXACT | `Action_SnapReceive` | RB | offense | `3` | `2` |
| ✅ EXACT | `Action_Handoff` | RB | offense | `3` | `2` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | Team_Unknown | `2` | `1` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `1` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `5` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `8` | `Group` | 0 | START | 0 | 139 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `9` | `Group` | 0 | START | 0 | 137 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `10` | 138 | START | 138 | 153 |
| ✅ EXACT | `Action_DownBlock` | LT | `1` | `0` | 140 | START | 140 | 199 |
| ⚠️ AMBIGUOUS MATCH | `Action_DownBlock` | LG | `12` | `11` | 140 | START | 140 | 168 |
| ❌ MISSING SEGMENT | `Action_DownBlock` | RG | `5` | `4` | 140 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_PullBlock` | RG | `5` | `4` | 140 | START | 140 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_PullLeadBlock` | RT | `8` | `7` | 140 | START | 140 | 171 |
| ✅ EXACT | `Action_SnapReceive` | RB | `3` | `2` | 153 | END | 138 | 153 |
| ✅ EXACT | `Action_Handoff` | RB | `3` | `2` | 161 | START | 161 | 177 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | Position_Unknown | `2` | `1` | 178 | START | N/A | N/A |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 199 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 0–240
- **Visible Samples:** 241

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_SnapReceive` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_None` | 154 | 160 | 7 | inferred_complete_timeline |
| `Action_Handoff` | 161 | 177 | 17 | inferred_complete_timeline |
| `Action_None` | 178 | 240 | 63 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 299 | 162 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 300

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 199 | 60 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_DownBlock` | 140 | 168 | 29 | inferred_complete_timeline |
| `Action_DownBlock` | 174 | 182 | 9 | inferred_complete_timeline |
| `Action_DownBlock` | 187 | 199 | 13 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 0–216
- **Visible Samples:** 157

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_BallSnap` | 138 | 153 | 16 | inferred_complete_timeline |
| `Action_None` | 214 | 216 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–299
- **Visible Samples:** 295

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PullBlock` | 140 | 165 | 26 | inferred_complete_timeline |
| `Action_PullBlock` | 171 | 199 | 29 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–247
- **Visible Samples:** 245

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 139 | 140 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 140 | 171 | 32 | inferred_complete_timeline |
| `Action_PullLeadBlock` | 175 | 199 | 25 | inferred_complete_timeline |
| `Action_None` | 200 | 247 | 48 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–244
- **Visible Samples:** 244

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 220 | 83 | inferred_complete_timeline |
| `Action_None` | 222 | 244 | 23 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 179

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 160 | 23 | inferred_complete_timeline |
| `Action_None` | 167 | 176 | 10 | inferred_complete_timeline |
| `Action_None` | 179 | 186 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 0–159
- **Visible Samples:** 160

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 159 | 22 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 198 | 61 | inferred_complete_timeline |
| `Action_None` | 208 | 210 | 3 | inferred_complete_timeline |
| `Action_None` | 214 | 223 | 10 | inferred_complete_timeline |
| `Action_None` | 225 | 299 | 75 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 0–186
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 182 | 45 | inferred_complete_timeline |
| `Action_None` | 184 | 186 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–233
- **Visible Samples:** 234

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 233 | 96 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `1` | `2` | Position_Unknown | Team_Unknown | 0–168 | 169 | 1 | Undefined position; Undefined team |
| `14` | `16` | Position_Unknown | Team_Unknown | 24–299 | 276 | 2 | Undefined position; Undefined team |
| `15` | `17` | Position_Unknown | Team_Unknown | 160–299 | 121 | 6 | Undefined position; Undefined team |
| `16` | `18` | Position_Unknown | Team_Unknown | 166–299 | 134 | 1 | Undefined position; Undefined team |
| `17` | `19` | Position_Unknown | Team_Unknown | 171–235 | 64 | 2 | Undefined position; Undefined team |
| `18` | `21` | Position_Unknown | Team_Unknown | 179–299 | 120 | 2 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 194–299 | 101 | 2 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 194–200 | 6 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 206–285 | 80 | 1 | Undefined position; Undefined team |
| `22` | `27` | Position_Unknown | Team_Unknown | 207–299 | 93 | 1 | Undefined position; Undefined team |
| `23` | `31` | Position_Unknown | Team_Unknown | 237–299 | 53 | 3 | Undefined position; Undefined team |
| `24` | `32` | Position_Unknown | Team_Unknown | 238–284 | 47 | 1 | Undefined position; Undefined team |
| `25` | `33` | Position_Unknown | Team_Unknown | 243–299 | 57 | 1 | Undefined position; Undefined team |
| `26` | `34` | Position_Unknown | Team_Unknown | 253–299 | 47 | 1 | Undefined position; Undefined team |
| `27` | `35` | Position_Unknown | Team_Unknown | 270–276 | 7 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_DownBlock` and target `12` (3 segments found)
- ❌ Missing segment for action `Action_DownBlock` on target `5` (RG)
- ⚠️ Ambiguous match for action `Action_PullBlock` and target `5` (2 segments found)
- ⚠️ Ambiguous match for action `Action_PullLeadBlock` and target `8` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `2` (Position_Unknown)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 3 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ Row 174: Duplicate assignment for track ID '7' in grid. Overwriting previous assignment.
- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '1' has invalid range: start=178, end=168. Clamping end to start.
- ⚠️ Overlapping action conflict at frame 140 for track '4': 'Action_DownBlock' vs 'Action_PullBlock'. Overriding with 'Action_PullBlock'.
- ⚠️ Action 'Action_PreSnap' range [0-168] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-240] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-198] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-210] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-223] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-299] for track '3' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PullBlock' range [140-165] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-220] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-244] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-160] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-176] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-186] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PullLeadBlock' range [140-171] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-247] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-233] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallSnap' range [138-153] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-216] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [140-168] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [174-182] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_DownBlock' range [187-199] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-159] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-182] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [184-186] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [160-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-206] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-216] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [231-289] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-173] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [175-235] for track '17' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [179-287] for track '18' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-201] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '19' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [194-197] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [199-200] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-285] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-299] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [237-247] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-276] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-284] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [270-276] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Player track '1' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '1' has undefined team_side. Will map to Team_Unknown.
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

</details>