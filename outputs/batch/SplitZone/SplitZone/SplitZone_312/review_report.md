# Play-Annotation-Generator Annotation Review — SplitZone_312

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_312`
- **Frame Range:** 0 to 329 (330 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 329
- **Player Tracks:** 32
- **Ball Tracks:** 0
- **Action Segments:** 89
- **Validation Warnings:** 67
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 22
- **Exact Matches:** 13
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 0
- **Global Events (no player segment expected):** 1
- **Inferred Coverage Segments (Action_None):** 68
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `12` | `12` |
| ✅ EXACT | `Action_ZoneBlock` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `18` | `18` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `5` | `5` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | Team_Unknown | `11` | `11` |
| ✅ EXACT | `Action_PressEdge` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_ReadEdgeDefender` | Position_Unknown | Team_Unknown | `17` | `17` |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF2 | defense | `4` | `4` |
| ✅ EXACT | `Action_Handoff` | C | offense | `16` | `16` |
| ✅ EXACT | `Action_BallCarry` | C | offense | `16` | `16` |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `12` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `13` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `16` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `18` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `5` | `Group` | 0 | START | 0 | 148 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `8` | `Group` | 0 | START | 0 | 137 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 0 | START | 0 | 148 |
| ✅ EXACT | `Action_BallSnap` | RT | `18` | `18` | 138 | START | 138 | 148 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `12` | `12` | 149 | START | 149 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | C | `16` | `16` | 149 | START | 149 | 159 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `18` | `18` | 149 | START | 149 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `5` | `5` | 149 | START | 149 | 202 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 149 | START | 149 | 202 |
| ✅ EXACT | `Action_SnapReceive` | Position_Unknown | `17` | `17` | 153 | END | 138 | 153 |
| ✅ EXACT | `Action_SplitBlock` | Position_Unknown | `11` | `11` | 155 | START | 155 | 198 |
| ✅ EXACT | `Action_PressEdge` | C | `16` | `16` | 160 | START | 160 | 183 |
| ✅ EXACT | `Action_ReadEdgeDefender` | Position_Unknown | `17` | `17` | 166 | START | 166 | 170 |
| ✅ EXACT | `Action_BlockSecondLevel` | SAF2 | `4` | `4` | 176 | START | 176 | 219 |
| ✅ EXACT | `Action_Handoff` | C | `16` | `16` | 184 | START | 184 | 184 |
| ✅ EXACT | `Action_BallCarry` | C | `16` | `16` | 185 | START | 185 | 329 |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 0–213
- **Visible Samples:** 212

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 204 | 67 | inferred_complete_timeline |
| `Action_None` | 207 | 213 | 7 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 0–181
- **Visible Samples:** 181

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 170 | 33 | inferred_complete_timeline |
| `Action_None` | 172 | 181 | 10 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 202 | 54 | inferred_complete_timeline |
| `Action_None` | 203 | 329 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 202 | 54 | inferred_complete_timeline |
| `Action_None` | 203 | 329 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 159 | 11 | inferred_complete_timeline |
| `Action_PressEdge` | 160 | 183 | 24 | inferred_complete_timeline |
| `Action_Handoff` | 184 | 184 | 1 | inferred_complete_timeline |
| `Action_BallCarry` | 185 | 329 | 145 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 148 | 149 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 202 | 54 | inferred_complete_timeline |
| `Action_None` | 203 | 329 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 0–329
- **Visible Samples:** 328

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_BallSnap` | 138 | 148 | 11 | inferred_complete_timeline |
| `Action_ZoneBlock` | 149 | 202 | 54 | inferred_complete_timeline |
| `Action_None` | 203 | 227 | 25 | inferred_complete_timeline |
| `Action_None` | 229 | 272 | 44 | inferred_complete_timeline |
| `Action_None` | 274 | 329 | 56 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 329 | 192 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 330

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 175 | 176 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 176 | 219 | 44 | inferred_complete_timeline |
| `Action_None` | 220 | 329 | 110 | inferred_complete_timeline |

</details>

<details>
<summary>SAF3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 0–329
- **Visible Samples:** 303

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 0 | 137 | 138 | inferred_complete_timeline |
| `Action_None` | 138 | 208 | 71 | inferred_complete_timeline |
| `Action_None` | 211 | 213 | 3 | inferred_complete_timeline |
| `Action_None` | 220 | 221 | 2 | inferred_complete_timeline |
| `Action_None` | 224 | 230 | 7 | inferred_complete_timeline |
| `Action_None` | 235 | 238 | 4 | inferred_complete_timeline |
| `Action_None` | 249 | 255 | 7 | inferred_complete_timeline |
| `Action_None` | 259 | 329 | 71 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `11` | `11` | Position_Unknown | Team_Unknown | 0–329 | 330 | 3 | Undefined position; Undefined team |
| `17` | `17` | Position_Unknown | Team_Unknown | 0–329 | 330 | 5 | Undefined position; Undefined team |
| `19` | `19` | Position_Unknown | Team_Unknown | 0–329 | 315 | 6 | Undefined position; Undefined team |
| `20` | `20` | Position_Unknown | Team_Unknown | 0–329 | 330 | 2 | Undefined position; Undefined team |
| `21` | `21` | Position_Unknown | Team_Unknown | 0–329 | 291 | 4 | Undefined position; Undefined team |
| `22` | `22` | Position_Unknown | Team_Unknown | 145–163 | 11 | 3 | Undefined position; Undefined team |
| `23` | `25` | Position_Unknown | Team_Unknown | 158–329 | 109 | 2 | Undefined position; Undefined team |
| `24` | `26` | Position_Unknown | Team_Unknown | 161–222 | 50 | 2 | Undefined position; Undefined team |
| `25` | `29` | Position_Unknown | Team_Unknown | 205–241 | 8 | 2 | Undefined position; Undefined team |
| `26` | `30` | Position_Unknown | Team_Unknown | 206–209 | 4 | 1 | Undefined position; Undefined team |
| `27` | `31` | Position_Unknown | Team_Unknown | 221–303 | 83 | 1 | Undefined position; Undefined team |
| `28` | `32` | Position_Unknown | Team_Unknown | 226–234 | 9 | 1 | Undefined position; Undefined team |
| `29` | `34` | Position_Unknown | Team_Unknown | 263–276 | 13 | 2 | Undefined position; Undefined team |
| `30` | `35` | Position_Unknown | Team_Unknown | 301–329 | 29 | 1 | Undefined position; Undefined team |
| `31` | `36` | Position_Unknown | Team_Unknown | 315–326 | 12 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

None.

### Track Identity Issues

- ⚠️ Player track XML ID `0` (actor_track_id `0`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `4` (actor_track_id `4`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF3` position mapped to `defense` team
- ⚠️ 15 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 15 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 30 |
| Missing visible bounding boxes during action | 36 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 329 as fallback play end.
- ⚠️ Action 'Action_None' range [138-329] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-329] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-208] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-213] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [220-221] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [224-230] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [235-238] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [249-255] for track '10' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-329] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-204] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-213] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-170] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [172-181] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [185-329] for track '16' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [203-227] for track '18' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-272] for track '18' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-227] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [234-274] for track '19' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [280-281] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-287] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [138-164] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [198-200] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-151] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-163] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-159] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [161-169] for track '24' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [182-222] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [205-209] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-241] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [206-209] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [221-303] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-234] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [263-270] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [272-276] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [315-326] for track '31' has 4 frames without a visible bounding box.
- ⚠️ Player track '11' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '11' has undefined team_side. Will map to Team_Unknown.
- ⚠️ Player track '17' has undefined position. Will map to Position_Unknown.
- ⚠️ Player track '17' has undefined team_side. Will map to Team_Unknown.
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

</details>