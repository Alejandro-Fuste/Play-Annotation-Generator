# Play-Annotation-Generator Annotation Review — InsideZoneRead_29

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `InsideZoneRead_29`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_InsideZoneRead`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 39
- **Ball Tracks:** 0
- **Action Segments:** 96
- **Validation Warnings:** 90
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 0
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 70
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `12` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `3` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `5` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `12` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `19` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `2` | `1` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `19` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `21` | `20` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_ReadDefender` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `18` | `17` |
| ✅ EXACT | `Action_BallCarry` | RB | offense | `14` | `13` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR4 | `1` | `Group` | 6 | START | 6 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `11` | `Group` | 6 | START | 6 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `12` | `Group` | 6 | START | 6 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `14` | `Group` | 6 | START | 6 | 156 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `18` | `Group` | 6 | START | 6 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `19` | `Group` | 6 | START | 6 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `2` | `Group` | 6 | START | 6 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 6 | START | 6 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `21` | `Group` | 6 | START | 6 | 105 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `3` | `Group` | 6 | START | 6 | 101 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `5` | `Group` | 6 | START | 6 | 101 |
| ✅ EXACT | `Action_BallSnap` | C | `19` | `18` | 102 | START | 102 | 115 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `12` | `11` | 106 | START | 106 | 122 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `19` | `18` | 106 | START | 116 | 126 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `2` | `1` | 106 | START | 106 | 165 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `19` | 106 | START | 106 | 157 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `21` | `20` | 106 | START | 106 | 199 |
| ✅ EXACT | `Action_SnapReceive` | QB | `18` | `17` | 115 | END | 102 | 115 |
| ✅ EXACT | `Action_ReadDefender` | QB | `18` | `17` | 120 | START | 120 | 144 |
| ✅ EXACT | `Action_Handoff` | QB | `18` | `17` | 145 | START | 145 | 156 |
| ✅ EXACT | `Action_BallCarry` | RB | `14` | `13` | 157 | START | 157 | 284 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 199 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `18`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_SnapReceive` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_None` | 116 | 119 | 4 | inferred_complete_timeline |
| `Action_ReadDefender` | 120 | 144 | 25 | inferred_complete_timeline |
| `Action_Handoff` | 145 | 156 | 12 | inferred_complete_timeline |
| `Action_None` | 157 | 299 | 143 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `14`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 6–284
- **Visible Samples:** 279

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 156 | 151 | inferred_complete_timeline |
| `Action_BallCarry` | 157 | 284 | 128 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `3`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `3`
- **team_side:** `offense`
- **Visible Frames:** 6–190
- **Visible Samples:** 185

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 190 | 89 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `11`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `5`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 6–137
- **Visible Samples:** 132

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 137 | 36 | inferred_complete_timeline |

</details>

<details>
<summary>WR4 — actor_track_id `1`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 105 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 157 | 52 | inferred_complete_timeline |
| `Action_ZoneBlock` | 161 | 199 | 39 | inferred_complete_timeline |
| `Action_None` | 200 | 299 | 100 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `12`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `12`
- **team_side:** `offense`
- **Visible Frames:** 6–173
- **Visible Samples:** 146

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 105 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 122 | 17 | inferred_complete_timeline |
| `Action_ZoneBlock` | 145 | 173 | 29 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `19`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 6–126
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_BallSnap` | 102 | 115 | 14 | inferred_complete_timeline |
| `Action_ZoneBlock` | 116 | 126 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `21`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 6–299
- **Visible Samples:** 293

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 105 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 199 | 94 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 203 | 299 | 97 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `2`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 6–203
- **Visible Samples:** 196

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 105 | 100 | inferred_complete_timeline |
| `Action_ZoneBlock` | 106 | 165 | 60 | inferred_complete_timeline |
| `Action_ZoneBlock` | 168 | 199 | 32 | inferred_complete_timeline |
| `Action_None` | 200 | 203 | 4 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 267

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 145 | 44 | inferred_complete_timeline |
| `Action_None` | 173 | 299 | 127 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `22`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `22`
- **team_side:** `defense`
- **Visible Frames:** 6–168
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 168 | 67 | inferred_complete_timeline |

</details>

<details>
<summary>DT — actor_track_id `13`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 6–169
- **Visible Samples:** 163

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 166 | 65 | inferred_complete_timeline |
| `Action_None` | 168 | 169 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `16`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `16`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `6`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 274 | 173 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>LB3 — actor_track_id `9`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `17`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 257

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 177 | 76 | inferred_complete_timeline |
| `Action_None` | 186 | 262 | 77 | inferred_complete_timeline |
| `Action_None` | 292 | 299 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `8`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `7`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `10`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 6–287
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 287 | 186 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `15`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 6–299
- **Visible Samples:** 294

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 6 | 101 | 96 | inferred_complete_timeline |
| `Action_None` | 102 | 299 | 198 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 133–213 | 60 | 4 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 142–205 | 58 | 3 | Undefined position; Undefined team |
| `24` | `27` | Position_Unknown | Team_Unknown | 146–147 | 2 | 1 | Undefined position; Undefined team |
| `25` | `28` | Position_Unknown | Team_Unknown | 148–157 | 10 | 1 | Undefined position; Undefined team |
| `26` | `29` | Position_Unknown | Team_Unknown | 154–196 | 26 | 3 | Undefined position; Undefined team |
| `27` | `30` | Position_Unknown | Team_Unknown | 154–299 | 140 | 3 | Undefined position; Undefined team |
| `28` | `31` | Position_Unknown | Team_Unknown | 157–160 | 4 | 1 | Undefined position; Undefined team |
| `29` | `33` | Position_Unknown | Team_Unknown | 167–299 | 124 | 2 | Undefined position; Undefined team |
| `30` | `39` | Position_Unknown | Team_Unknown | 191–299 | 109 | 1 | Undefined position; Undefined team |
| `31` | `40` | Position_Unknown | Team_Unknown | 196–299 | 104 | 1 | Undefined position; Undefined team |
| `32` | `41` | Position_Unknown | Team_Unknown | 206–299 | 94 | 1 | Undefined position; Undefined team |
| `33` | `42` | Position_Unknown | Team_Unknown | 211–292 | 73 | 4 | Undefined position; Undefined team |
| `34` | `43` | Position_Unknown | Team_Unknown | 225–227 | 3 | 1 | Undefined position; Undefined team |
| `35` | `45` | Position_Unknown | Team_Unknown | 241–242 | 2 | 1 | Undefined position; Undefined team |
| `36` | `46` | Position_Unknown | Team_Unknown | 256–299 | 40 | 3 | Undefined position; Undefined team |
| `37` | `50` | Position_Unknown | Team_Unknown | 269–294 | 15 | 3 | Undefined position; Undefined team |
| `38` | `51` | Position_Unknown | Team_Unknown | 290–297 | 7 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `12` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `19` (3 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (3 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `9` (actor_track_id `10`): `SAF1` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `15`): `SAF2` position mapped to `defense` team
- ⚠️ 17 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 17 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 34 |
| Missing visible bounding boxes during action | 51 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '1' (RT) duration 94 frames exceeds threshold 90 frames [start=106, end=199].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [102–115], lower_priority='Action_ZoneBlock' annotated_start=106, effective_Action_ZoneBlock_start=116.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '19' (LT) duration 94 frames exceeds threshold 90 frames [start=106, end=199].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '20' (RG) duration 94 frames exceeds threshold 90 frames [start=106, end=199].
- ⚠️ Action 'Action_ZoneBlock' range [106-165] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-203] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-190] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-145] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [173-299] for track '3' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-137] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-274] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-287] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-122] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [145-173] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-166] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [168-169] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [157-284] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-177] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [186-262] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-299] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [116-126] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [106-157] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [102-168] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-137] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [145-195] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [208-209] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [212-213] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [142-144] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [149-201] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [204-205] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [146-147] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [148-157] for track '25' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-164] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [166-178] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [195-196] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [154-162] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [164-176] for track '27' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-160] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [167-168] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [196-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-220] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-253] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-256] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [261-292] for track '33' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [225-227] for track '34' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [241-242] for track '35' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [256-257] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [259-263] for track '36' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [269-275] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [279-284] for track '37' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '37' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-291] for track '38' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-297] for track '38' has 2 frames without a visible bounding box.
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

</details>