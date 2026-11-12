# Play-Annotation-Generator Annotation Review — SplitZone_127

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_127`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_Tackle`
- **Result Frame:** 299
- **Player Tracks:** 33
- **Ball Tracks:** 0
- **Action Segments:** 111
- **Validation Warnings:** 93
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 24
- **Exact Matches:** 6
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 0
- **Missing Segments:** 1
- **Ambiguous Matches:** 4
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 90
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `11` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | offense | `13` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `19` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `5` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | offense | `6` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `9` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | offense | `11` | `11` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | offense | `16` | `16` |
| ✅ EXACT | `Action_ZoneBlock` | RG | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `21` | `21` |
| ✅ EXACT | `Action_ZoneBlock` | LT | offense | `9` | `9` |
| ✅ EXACT | `Action_SplitBlock` | TE1 | offense | `6` | `6` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `19` | `19` |
| ✅ EXACT | `Action_Handoff` | QB | offense | `19` | `19` |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | offense | `5` | `5` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | defense | `15` | `15` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `1` | `Group` | 9 | START | 10 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `11` | `Group` | 9 | START | 10 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE2 | `13` | `Group` | 9 | START | 10 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `16` | `Group` | 9 | START | 10 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `19` | `Group` | 9 | START | 10 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `2` | `Group` | 9 | START | 10 | 95 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `20` | `Group` | 9 | START | 10 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `21` | `Group` | 9 | START | 10 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `5` | `Group` | 9 | START | 10 | 124 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE1 | `6` | `Group` | 9 | START | 10 | 103 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `9` | `Group` | 9 | START | 10 | 98 |
| ✅ EXACT | `Action_BallSnap` | C | `11` | `11` | 96 | START | 96 | 113 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | C | `11` | `11` | 99 | START | 114 | 128 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LG | `16` | `16` | 99 | START | 99 | 180 |
| ✅ EXACT | `Action_ZoneBlock` | RG | `20` | `20` | 99 | START | 99 | 146 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `21` | `21` | 99 | START | 99 | 141 |
| ✅ EXACT | `Action_ZoneBlock` | LT | `9` | `9` | 99 | START | 99 | 187 |
| ✅ EXACT | `Action_SplitBlock` | TE1 | `6` | `6` | 104 | START | 104 | 187 |
| ✅ EXACT | `Action_SnapReceive` | QB | `19` | `19` | 113 | END | 96 | 113 |
| ✅ EXACT | `Action_Handoff` | QB | `19` | `19` | 118 | START | 118 | 125 |
| ❌ MISSING SEGMENT | `Action_BallCarry` | RB | `5` | `5` | 126 | START | N/A | N/A |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | DT1 | `15` | `15` | 136 | START | 136 | 163 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 187 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_SnapReceive` | 96 | 113 | 18 | inferred_complete_timeline |
| `Action_None` | 114 | 117 | 4 | inferred_complete_timeline |
| `Action_Handoff` | 118 | 125 | 8 | inferred_complete_timeline |
| `Action_None` | 126 | 269 | 144 | inferred_complete_timeline |
| `Action_None` | 286 | 293 | 8 | inferred_complete_timeline |
| `Action_None` | 299 | 299 | 1 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `offense`
- **Visible Frames:** 10–124
- **Visible Samples:** 115

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 124 | 115 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 230 | 135 | inferred_complete_timeline |
| `Action_None` | 236 | 289 | 54 | inferred_complete_timeline |
| `Action_None` | 292 | 296 | 5 | inferred_complete_timeline |
| `Action_None` | 298 | 299 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>TE1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 103 | 94 | inferred_complete_timeline |
| `Action_SplitBlock` | 104 | 187 | 84 | inferred_complete_timeline |
| `Action_None` | 188 | 224 | 37 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>TE2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `offense`
- **Visible Frames:** 10–130
- **Visible Samples:** 121

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 130 | 35 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `offense`
- **Visible Frames:** 10–195
- **Visible Samples:** 186

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 187 | 89 | inferred_complete_timeline |
| `Action_None` | 188 | 195 | 8 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 180 | 82 | inferred_complete_timeline |
| `Action_ZoneBlock` | 185 | 187 | 3 | inferred_complete_timeline |
| `Action_None` | 191 | 299 | 109 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_BallSnap` | 96 | 113 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 114 | 128 | 15 | inferred_complete_timeline |
| `Action_ZoneBlock` | 131 | 162 | 32 | inferred_complete_timeline |
| `Action_ZoneBlock` | 166 | 169 | 4 | inferred_complete_timeline |
| `Action_ZoneBlock` | 173 | 187 | 15 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 10–146
- **Visible Samples:** 137

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 146 | 48 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 10–299
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 98 | 89 | inferred_complete_timeline |
| `Action_ZoneBlock` | 99 | 141 | 43 | inferred_complete_timeline |
| `Action_ZoneBlock` | 154 | 187 | 34 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 223 | 128 | inferred_complete_timeline |
| `Action_None` | 227 | 236 | 10 | inferred_complete_timeline |
| `Action_None` | 238 | 290 | 53 | inferred_complete_timeline |
| `Action_None` | 294 | 299 | 6 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 135 | 126 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 136 | 163 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 167 | 187 | 21 | inferred_complete_timeline |
| `Action_None` | 188 | 299 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 287

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 121 | 26 | inferred_complete_timeline |
| `Action_None` | 125 | 299 | 175 | inferred_complete_timeline |

</details>

<details>
<summary>DT3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 269

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 223 | 128 | inferred_complete_timeline |
| `Action_None` | 230 | 231 | 2 | inferred_complete_timeline |
| `Action_None` | 233 | 234 | 2 | inferred_complete_timeline |
| `Action_None` | 244 | 247 | 4 | inferred_complete_timeline |
| `Action_None` | 253 | 299 | 47 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `defense`
- **Visible Frames:** 10–290
- **Visible Samples:** 278

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 176 | 81 | inferred_complete_timeline |
| `Action_None` | 180 | 290 | 111 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 223 | 128 | inferred_complete_timeline |
| `Action_None` | 229 | 233 | 5 | inferred_complete_timeline |
| `Action_None` | 238 | 299 | 62 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 10–299
- **Visible Samples:** 290

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 10 | 95 | 86 | inferred_complete_timeline |
| `Action_None` | 96 | 299 | 204 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `24` | Position_Unknown | Team_Unknown | 133–268 | 134 | 2 | Undefined position; Undefined team |
| `23` | `26` | Position_Unknown | Team_Unknown | 138–299 | 162 | 1 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 157–275 | 98 | 6 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 163–299 | 137 | 1 | Undefined position; Undefined team |
| `26` | `33` | Position_Unknown | Team_Unknown | 211–299 | 81 | 4 | Undefined position; Undefined team |
| `27` | `37` | Position_Unknown | Team_Unknown | 227–272 | 22 | 4 | Undefined position; Undefined team |
| `28` | `38` | Position_Unknown | Team_Unknown | 228–236 | 9 | 1 | Undefined position; Undefined team |
| `29` | `39` | Position_Unknown | Team_Unknown | 232–263 | 10 | 4 | Undefined position; Undefined team |
| `30` | `40` | Position_Unknown | Team_Unknown | 233–299 | 31 | 7 | Undefined position; Undefined team |
| `31` | `42` | Position_Unknown | Team_Unknown | 283–299 | 10 | 3 | Undefined position; Undefined team |
| `32` | `43` | Position_Unknown | Team_Unknown | 293–299 | 3 | 2 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `11` (4 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `21` (2 segments found)
- ❌ Missing segment for action `Action_BallCarry` on target `5` (RB)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `15` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `10` (actor_track_id `10`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `14` (actor_track_id `14`): `SAF1` position mapped to `defense` team
- ⚠️ 11 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 11 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 22 |
| Missing visible bounding boxes during action | 68 |
| Track-related warning | 2 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Segment 'Action_BallCarry' for track '5' has invalid range: start=126, end=124. Clamping end to start.
- ⚠️ Resolved action overlap for track '11' (C): higher_priority='Action_BallSnap' [96–113], lower_priority='Action_ZoneBlock' annotated_start=99, effective_Action_ZoneBlock_start=114.
- ⚠️ Action 'Action_None' range [96-223] for track '0' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [230-231] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-234] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [244-247] for track '0' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-230] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [236-289] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [292-296] for track '1' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-223] for track '4' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-236] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [238-290] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-124] for track '5' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-224] for track '6' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-176] for track '7' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [180-290] for track '7' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-299] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-195] for track '9' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [114-128] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [131-162] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [166-169] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [173-187] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-299] for track '12' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-130] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-223] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-233] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [10-135] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [136-163] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [188-299] for track '15' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-180] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [185-187] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [96-121] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [125-299] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [126-269] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-293] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-146] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [99-141] for track '21' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [133-223] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [226-268] for track '22' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [157-183] for track '24' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [191-236] for track '24' has 4 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [239-243] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-256] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [260-265] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-275] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [163-299] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [211-219] for track '26' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [222-223] for track '26' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [229-236] for track '26' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [227-230] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [246-250] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [258-264] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [267-272] for track '27' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [228-236] for track '28' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-233] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [243-246] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [248-249] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [262-263] for track '29' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [233-235] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [252-253] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [255-262] for track '30' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [265-266] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [271-272] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-278] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [290-299] for track '30' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [283-284] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [286-288] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [295-299] for track '31' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [293-294] for track '32' has 1 frames without a visible bounding box.
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

</details>