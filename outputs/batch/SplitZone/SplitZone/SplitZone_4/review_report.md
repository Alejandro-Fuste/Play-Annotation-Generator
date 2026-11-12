# Play-Annotation-Generator Annotation Review — SplitZone_4

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_4`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 27
- **Ball Tracks:** 0
- **Action Segments:** 68
- **Validation Warnings:** 57
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 20
- **Exact Matches:** 8
- **Group Expanded Events:** 8
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 1
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 50
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `4` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `8` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | RT | offense | `0` | `0` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `14` | `14` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `4` | `4` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `8` | `8` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `7` | `7` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `7` | `7` |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | offense | `3` | `3` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `0` | `Group` | 13 | START | 13 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `14` | `Group` | 13 | START | 13 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 13 | START | 13 | 126 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `3` | `Group` | 13 | START | 13 | 158 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `4` | `Group` | 13 | START | 13 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `7` | `Group` | 13 | START | 13 | 120 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `8` | `Group` | 13 | START | 13 | 123 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `9` | `Group` | 13 | START | 13 | 123 |
| ✅ EXACT | `Action_BallSnap` | C | `14` | `14` | 121 | START | 121 | 133 |
| ✅ EXACT | `Action_ZoneBlock` | RT | `0` | `0` | 124 | START | 124 | 195 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `14` | `14` | 124 | START | 134 | 191 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `4` | `4` | 124 | START | 124 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `8` | `8` | 124 | START | 124 | 195 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `9` | `9` | 124 | START | 124 | 195 |
| ✅ EXACT | `Action_SplitBlock` | TE | `2` | `2` | 127 | START | 127 | 195 |
| ✅ EXACT | `Action_SnapReceive` | QB | `7` | `7` | 133 | END | 121 | 133 |
| ✅ EXACT | `Action_Handoff` | QB | `7` | `7` | 144 | START | 144 | 161 |
| ⚠️ START CHANGED | `Action_BallCarry` | RB | `3` | `3` | 162 | START | 163 | 273 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 195 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 13–211
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_SnapReceive` | 121 | 133 | 13 | inferred_complete_timeline |
| `Action_None` | 134 | 143 | 10 | inferred_complete_timeline |
| `Action_Handoff` | 144 | 161 | 18 | inferred_complete_timeline |
| `Action_None` | 162 | 211 | 50 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 13–273
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 158 | 146 | inferred_complete_timeline |
| `Action_BallCarry` | 163 | 273 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 126 | 114 | inferred_complete_timeline |
| `Action_SplitBlock` | 127 | 195 | 69 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 123 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 195 | 72 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 123 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 195 | 72 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_BallSnap` | 121 | 133 | 13 | inferred_complete_timeline |
| `Action_ZoneBlock` | 134 | 191 | 58 | inferred_complete_timeline |
| `Action_ZoneBlock` | 193 | 195 | 3 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 123 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 195 | 72 | inferred_complete_timeline |
| `Action_None` | 196 | 299 | 104 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 13–210
- **Visible Samples:** 198

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 123 | 111 | inferred_complete_timeline |
| `Action_ZoneBlock` | 124 | 195 | 72 | inferred_complete_timeline |
| `Action_None` | 196 | 210 | 15 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 227

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_None` | 121 | 136 | 16 | inferred_complete_timeline |
| `Action_None` | 196 | 250 | 55 | inferred_complete_timeline |
| `Action_None` | 252 | 299 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 13–156
- **Visible Samples:** 140

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_None` | 121 | 135 | 15 | inferred_complete_timeline |
| `Action_None` | 140 | 156 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 13–46
- **Visible Samples:** 34

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 46 | 34 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `defense`
- **Visible Frames:** 13–208
- **Visible Samples:** 162

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_None` | 121 | 172 | 52 | inferred_complete_timeline |
| `Action_None` | 207 | 208 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 263

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_None` | 121 | 183 | 63 | inferred_complete_timeline |
| `Action_None` | 193 | 194 | 2 | inferred_complete_timeline |
| `Action_None` | 197 | 210 | 14 | inferred_complete_timeline |
| `Action_None` | 224 | 299 | 76 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

<details>
<summary>SAF — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 13–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 13 | 120 | 108 | inferred_complete_timeline |
| `Action_None` | 121 | 299 | 179 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `15` | `15` | Position_Unknown | Team_Unknown | 59–268 | 168 | 8 | Undefined position; Undefined team |
| `16` | `17` | Position_Unknown | Team_Unknown | 158–256 | 58 | 2 | Undefined position; Undefined team |
| `17` | `18` | Position_Unknown | Team_Unknown | 170–299 | 130 | 1 | Undefined position; Undefined team |
| `18` | `19` | Position_Unknown | Team_Unknown | 196–197 | 2 | 1 | Undefined position; Undefined team |
| `19` | `24` | Position_Unknown | Team_Unknown | 214–299 | 86 | 1 | Undefined position; Undefined team |
| `20` | `25` | Position_Unknown | Team_Unknown | 233–299 | 66 | 2 | Undefined position; Undefined team |
| `21` | `26` | Position_Unknown | Team_Unknown | 248–299 | 52 | 1 | Undefined position; Undefined team |
| `22` | `28` | Position_Unknown | Team_Unknown | 259–299 | 41 | 1 | Undefined position; Undefined team |
| `23` | `29` | Position_Unknown | Team_Unknown | 261–299 | 39 | 1 | Undefined position; Undefined team |
| `24` | `30` | Position_Unknown | Team_Unknown | 267–268 | 2 | 1 | Undefined position; Undefined team |
| `25` | `31` | Position_Unknown | Team_Unknown | 276–299 | 24 | 1 | Undefined position; Undefined team |
| `26` | `32` | Position_Unknown | Team_Unknown | 292–299 | 8 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `14` (2 segments found)
- ⚠️ `Action_BallCarry` for actor_track_id `3` (RB): Annotated start 162 != Inferred start 163

### Track Identity Issues

- ⚠️ Player track XML ID `12` (actor_track_id `12`): `SAF` position mapped to `defense` team
- ⚠️ 12 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 12 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 24 |
| Missing visible bounding boxes during action | 31 |
| Track-related warning | 1 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Resolved action overlap for track '14' (C): higher_priority='Action_BallSnap' [121–133], lower_priority='Action_ZoneBlock' annotated_start=124, effective_Action_ZoneBlock_start=134.
- ⚠️ Action 'Action_None' range [196-210] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-172] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [207-208] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-158] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [163-273] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-183] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [193-194] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [197-210] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [162-211] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [124-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-135] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [140-156] for track '10' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [13-46] for track '11' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [121-136] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-250] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [134-191] for track '14' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [59-76] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [79-120] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' for track '15' starts at frame 121, but the player has no visible bounding box on this frame.
- ⚠️ Action 'Action_None' range [121-121] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [153-156] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-162] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [165-167] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [169-172] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [178-268] for track '15' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [158-168] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [210-256] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-197] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-256] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-299] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-268] for track '24' has 1 frames without a visible bounding box.
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

</details>