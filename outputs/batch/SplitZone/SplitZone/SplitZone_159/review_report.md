# Play-Annotation-Generator Annotation Review — SplitZone_159

**Overall Status:** WARNING

## 1. Clip & Validation Summary

- **Video:** `SplitZone_159`
- **Frame Range:** 0 to 299 (300 total frames)
- **Play:** `Play_Run_SplitZone`
- **Result:** `Result_OutOfBounds`
- **Result Frame:** 299
- **Player Tracks:** 28
- **Ball Tracks:** 0
- **Action Segments:** 84
- **Validation Warnings:** 58
- **Validation Errors:** 0
- **Overall Status:** WARNING

## 2. Action Annotation Audit

<details>
<summary><strong>Open Action Audit</strong></summary>

### Audit Summary
- **Input Action Events:** 23
- **Exact Matches:** 3
- **Group Expanded Events:** 11
- **Boundary-Terminated Events:** 0
- **Priority-Adjusted Events:** 0
- **Start-Frame Differences:** 1
- **Missing Segments:** 0
- **Ambiguous Matches:** 6
- **Global Events (no player segment expected):** 2
- **Inferred Coverage Segments (Action_None):** 62
- **Unmatched Unexpected Segments:** 0

### Player / Track Mapping

| Status | Action | Position | Team | actor_track_id | xml_track_id |
| --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | offense | `0` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | offense | `1` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | offense | `14` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | offense | `16` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | offense | `17` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | offense | `18` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | offense | `2` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | offense | `20` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | offense | `21` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | offense | `7` | `Group` |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | offense | `8` | `Group` |
| ✅ EXACT | `Action_BallSnap` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | offense | `16` | `16` |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | offense | `18` | `18` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | offense | `20` | `20` |
| ✅ EXACT | `Action_ZoneBlock` | LG | offense | `21` | `21` |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | offense | `7` | `7` |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | offense | `2` | `2` |
| ✅ EXACT | `Action_SnapReceive` | QB | offense | `14` | `14` |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | offense | `20` | `20` |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | offense | `14` | `14` |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | N/A |

### Timing Mapping

| Status | Action | Position | actor_track_id | xml_track_id | Annotated Frame | Annotated Role | Generated Start | Generated End |
| --- | --- | --- | --- | --- | --- | --- | --- | --- |
| ℹ️ GLOBAL EVENT | `Action_PlayEnd` | N/A | N/A | N/A | 0 | BOUNDARY | N/A | N/A |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR3 | `0` | `Group` | 7 | START | 8 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR2 | `1` | `Group` | 7 | START | 8 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | QB | `14` | `Group` | 7 | START | 8 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RG | `16` | `Group` | 7 | START | 8 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RB | `17` | `Group` | 7 | START | 8 | 77 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | C | `18` | `Group` | 7 | START | 8 | 94 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | TE | `2` | `Group` | 7 | START | 8 | 98 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LT | `20` | `Group` | 7 | START | 8 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | LG | `21` | `Group` | 7 | START | 8 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | RT | `7` | `Group` | 7 | START | 8 | 97 |
| ✅ GROUP_EXPANDED | `Action_PreSnap` | WR1 | `8` | `Group` | 7 | START | 8 | 94 |
| ✅ EXACT | `Action_BallSnap` | C | `18` | `18` | 95 | START | 95 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RG | `16` | `16` | 98 | START | 98 | 104 |
| ⚠️ START CHANGED | `Action_ZoneBlock` | C | `18` | `18` | 98 | START | 113 | 213 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | LT | `20` | `20` | 98 | START | 98 | 117 |
| ✅ EXACT | `Action_ZoneBlock` | LG | `21` | `21` | 98 | START | 98 | 108 |
| ⚠️ AMBIGUOUS MATCH | `Action_ZoneBlock` | RT | `7` | `7` | 98 | START | 98 | 118 |
| ⚠️ AMBIGUOUS MATCH | `Action_SplitBlock` | TE | `2` | `2` | 99 | START | 99 | 175 |
| ✅ EXACT | `Action_SnapReceive` | QB | `14` | `14` | 112 | END | 95 | 112 |
| ⚠️ AMBIGUOUS MATCH | `Action_BlockSecondLevel` | LT | `20` | `20` | 126 | START | 126 | 153 |
| ⚠️ AMBIGUOUS MATCH | `Action_BallCarry` | QB | `14` | `14` | 142 | START | 142 | 287 |
| ℹ️ GLOBAL EVENT | `Action_None` | N/A | N/A | N/A | 213 | BOUNDARY | N/A | N/A |

### Output Segments Without Matching Input

None.

</details>

## 3. Player Action Timelines

<details>
<summary><strong>Offense</strong></summary>

<details>
<summary>QB — actor_track_id `14`</summary>

- **xml_track_id:** `14`
- **actor_track_id:** `14`
- **team_side:** `offense`
- **Visible Frames:** 8–292
- **Visible Samples:** 283

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_SnapReceive` | 95 | 112 | 18 | inferred_complete_timeline |
| `Action_None` | 113 | 141 | 29 | inferred_complete_timeline |
| `Action_BallCarry` | 142 | 287 | 146 | inferred_complete_timeline |
| `Action_BallCarry` | 290 | 292 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>RB — actor_track_id `17`</summary>

- **xml_track_id:** `17`
- **actor_track_id:** `17`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 271

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 77 | 70 | inferred_complete_timeline |
| `Action_PreSnap` | 86 | 94 | 9 | inferred_complete_timeline |
| `Action_None` | 95 | 108 | 14 | inferred_complete_timeline |
| `Action_None` | 112 | 117 | 6 | inferred_complete_timeline |
| `Action_None` | 128 | 299 | 172 | inferred_complete_timeline |

</details>

<details>
<summary>WR1 — actor_track_id `8`</summary>

- **xml_track_id:** `8`
- **actor_track_id:** `8`
- **team_side:** `offense`
- **Visible Frames:** 8–215
- **Visible Samples:** 192

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 195 | 101 | inferred_complete_timeline |
| `Action_None` | 200 | 201 | 2 | inferred_complete_timeline |
| `Action_None` | 214 | 215 | 2 | inferred_complete_timeline |

</details>

<details>
<summary>WR2 — actor_track_id `1`</summary>

- **xml_track_id:** `1`
- **actor_track_id:** `1`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>WR3 — actor_track_id `0`</summary>

- **xml_track_id:** `0`
- **actor_track_id:** `0`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>TE — actor_track_id `2`</summary>

- **xml_track_id:** `2`
- **actor_track_id:** `2`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 98 | 91 | inferred_complete_timeline |
| `Action_SplitBlock` | 99 | 175 | 77 | inferred_complete_timeline |
| `Action_SplitBlock` | 177 | 213 | 37 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

<details>
<summary>LT — actor_track_id `20`</summary>

- **xml_track_id:** `20`
- **actor_track_id:** `20`
- **team_side:** `offense`
- **Visible Frames:** 8–159
- **Visible Samples:** 149

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 97 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 117 | 20 | inferred_complete_timeline |
| `Action_ZoneBlock` | 119 | 125 | 7 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 126 | 153 | 28 | inferred_complete_timeline |
| `Action_BlockSecondLevel` | 156 | 159 | 4 | inferred_complete_timeline |

</details>

<details>
<summary>LG — actor_track_id `21`</summary>

- **xml_track_id:** `21`
- **actor_track_id:** `21`
- **team_side:** `offense`
- **Visible Frames:** 8–108
- **Visible Samples:** 101

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 97 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 108 | 11 | inferred_complete_timeline |

</details>

<details>
<summary>C — actor_track_id `18`</summary>

- **xml_track_id:** `18`
- **actor_track_id:** `18`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 291

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_BallSnap` | 95 | 112 | 18 | inferred_complete_timeline |
| `Action_ZoneBlock` | 113 | 213 | 101 | inferred_complete_timeline |
| `Action_None` | 214 | 224 | 11 | inferred_complete_timeline |
| `Action_None` | 226 | 299 | 74 | inferred_complete_timeline |

</details>

<details>
<summary>RG — actor_track_id `16`</summary>

- **xml_track_id:** `16`
- **actor_track_id:** `16`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 274

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 97 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 104 | 7 | inferred_complete_timeline |
| `Action_ZoneBlock` | 117 | 213 | 97 | inferred_complete_timeline |
| `Action_None` | 214 | 270 | 57 | inferred_complete_timeline |
| `Action_None` | 274 | 275 | 2 | inferred_complete_timeline |
| `Action_None` | 279 | 299 | 21 | inferred_complete_timeline |

</details>

<details>
<summary>RT — actor_track_id `7`</summary>

- **xml_track_id:** `7`
- **actor_track_id:** `7`
- **team_side:** `offense`
- **Visible Frames:** 8–299
- **Visible Samples:** 270

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 97 | 90 | inferred_complete_timeline |
| `Action_ZoneBlock` | 98 | 118 | 21 | inferred_complete_timeline |
| `Action_ZoneBlock` | 141 | 213 | 73 | inferred_complete_timeline |
| `Action_None` | 214 | 299 | 86 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Defense</strong></summary>

<details>
<summary>DE1 — actor_track_id `11`</summary>

- **xml_track_id:** `11`
- **actor_track_id:** `11`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 143 | 49 | inferred_complete_timeline |
| `Action_None` | 147 | 149 | 3 | inferred_complete_timeline |
| `Action_None` | 153 | 299 | 147 | inferred_complete_timeline |

</details>

<details>
<summary>DE2 — actor_track_id `3`</summary>

- **xml_track_id:** `3`
- **actor_track_id:** `3`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>DT1 — actor_track_id `9`</summary>

- **xml_track_id:** `9`
- **actor_track_id:** `9`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 276

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 182 | 88 | inferred_complete_timeline |
| `Action_None` | 199 | 299 | 101 | inferred_complete_timeline |

</details>

<details>
<summary>DT2 — actor_track_id `13`</summary>

- **xml_track_id:** `13`
- **actor_track_id:** `13`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 286

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 210 | 116 | inferred_complete_timeline |
| `Action_None` | 214 | 279 | 66 | inferred_complete_timeline |
| `Action_None` | 283 | 299 | 17 | inferred_complete_timeline |

</details>

<details>
<summary>LB1 — actor_track_id `19`</summary>

- **xml_track_id:** `19`
- **actor_track_id:** `19`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 275

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 174 | 80 | inferred_complete_timeline |
| `Action_None` | 192 | 299 | 108 | inferred_complete_timeline |

</details>

<details>
<summary>LB2 — actor_track_id `4`</summary>

- **xml_track_id:** `4`
- **actor_track_id:** `4`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>CB1 — actor_track_id `12`</summary>

- **xml_track_id:** `12`
- **actor_track_id:** `12`
- **team_side:** `defense`
- **Visible Frames:** 8–206
- **Visible Samples:** 199

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 206 | 112 | inferred_complete_timeline |

</details>

<details>
<summary>CB2 — actor_track_id `15`</summary>

- **xml_track_id:** `15`
- **actor_track_id:** `15`
- **team_side:** `defense`
- **Visible Frames:** 8–288
- **Visible Samples:** 281

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 288 | 194 | inferred_complete_timeline |

</details>

<details>
<summary>CB3 — actor_track_id `10`</summary>

- **xml_track_id:** `10`
- **actor_track_id:** `10`
- **team_side:** `defense`
- **Visible Frames:** 8–299
- **Visible Samples:** 292

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 299 | 205 | inferred_complete_timeline |

</details>

<details>
<summary>SAF1 — actor_track_id `6`</summary>

- **xml_track_id:** `6`
- **actor_track_id:** `6`
- **team_side:** `defense`
- **Visible Frames:** 8–296
- **Visible Samples:** 282

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 248 | 154 | inferred_complete_timeline |
| `Action_None` | 251 | 252 | 2 | inferred_complete_timeline |
| `Action_None` | 254 | 289 | 36 | inferred_complete_timeline |
| `Action_None` | 294 | 296 | 3 | inferred_complete_timeline |

</details>

<details>
<summary>SAF2 — actor_track_id `5`</summary>

- **xml_track_id:** `5`
- **actor_track_id:** `5`
- **team_side:** `defense`
- **Visible Frames:** 8–296
- **Visible Samples:** 289

| Action | Start | End | Duration | Source |
| --- | --- | --- | --- | --- |
| `Action_PreSnap` | 8 | 94 | 87 | inferred_complete_timeline |
| `Action_None` | 95 | 296 | 202 | inferred_complete_timeline |

</details>

</details>

<details>
<summary><strong>Unassigned / Unknown Player Tracks</strong></summary>

| xml_track_id | actor_track_id | Position | Team | Visible Frames | Visible Samples | Action Segments | Notes |
| --- | --- | --- | --- | --- | --- | --- | --- |
| `22` | `23` | Position_Unknown | Team_Unknown | 134–190 | 4 | 2 | Undefined position; Undefined team |
| `23` | `24` | Position_Unknown | Team_Unknown | 139–299 | 152 | 2 | Undefined position; Undefined team |
| `24` | `28` | Position_Unknown | Team_Unknown | 177–299 | 118 | 2 | Undefined position; Undefined team |
| `25` | `30` | Position_Unknown | Team_Unknown | 268–269 | 2 | 1 | Undefined position; Undefined team |
| `26` | `31` | Position_Unknown | Team_Unknown | 275–280 | 6 | 1 | Undefined position; Undefined team |
| `27` | `32` | Position_Unknown | Team_Unknown | 289–299 | 11 | 1 | Undefined position; Undefined team |

</details>

## 4. Ball Tracking Summary

*No ball tracks found.*

## 5. Issues Requiring Review

### Action Mapping Issues

- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `16` (2 segments found)
- ⚠️ `Action_ZoneBlock` for actor_track_id `18` (C): Annotated start 98 != Inferred start 113
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_ZoneBlock` and target `7` (2 segments found)
- ⚠️ Ambiguous match for action `Action_SplitBlock` and target `2` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BlockSecondLevel` and target `20` (2 segments found)
- ⚠️ Ambiguous match for action `Action_BallCarry` and target `14` (2 segments found)

### Track Identity Issues

- ⚠️ Player track XML ID `5` (actor_track_id `5`): `SAF2` position mapped to `defense` team
- ⚠️ Player track XML ID `6` (actor_track_id `6`): `SAF1` position mapped to `defense` team
- ⚠️ 6 player tracks have undefined position (`Position_Unknown`)
- ⚠️ 6 player tracks have undefined team (`Team_Unknown`)

### Validation Errors

None.

### Validation Warnings by Category

| Category | Count |
| --- | --- |
| Unknown position/team | 12 |
| Missing visible bounding boxes during action | 41 |
| Track-related warning | 4 |
| Other | 1 |

<details>
<summary><strong>Detailed Validation Warnings</strong></summary>

- ⚠️ No result_frame or PlayEnd action found in CSV. Using final clip frame 299 as fallback play end.
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '7' (RT) duration 116 frames exceeds threshold 90 frames [start=98, end=213].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '16' (RG) duration 116 frames exceeds threshold 90 frames [start=98, end=213].
- ⚠️ Validation warning: Action 'Action_ZoneBlock' for track '18' (C) duration 116 frames exceeds threshold 90 frames [start=98, end=213].
- ⚠️ Resolved action overlap for track '18' (C): higher_priority='Action_BallSnap' [95–112], lower_priority='Action_ZoneBlock' annotated_start=98, effective_Action_ZoneBlock_start=113.
- ⚠️ Action 'Action_SplitBlock' range [99-175] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-299] for track '2' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-299] for track '4' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-296] for track '5' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-248] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [251-252] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [254-289] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [294-296] for track '6' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-118] for track '7' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-195] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [200-201] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-215] for track '8' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-182] for track '9' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-143] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [147-149] for track '11' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-206] for track '12' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-210] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-279] for track '13' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [142-287] for track '14' has 2 frames without a visible bounding box.
- ⚠️ Action 'Action_BallCarry' range [290-292] for track '14' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-288] for track '15' has 3 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-104] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-270] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [274-275] for track '16' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_PreSnap' range [8-77] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-108] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [112-117] for track '17' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [214-224] for track '18' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [95-174] for track '19' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-117] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [126-153] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_BlockSecondLevel' range [156-159] for track '20' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_ZoneBlock' range [98-108] for track '21' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [134-135] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [189-190] for track '22' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [139-161] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [171-299] for track '23' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [177-226] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [232-299] for track '24' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [268-269] for track '25' has 1 frames without a visible bounding box.
- ⚠️ Action 'Action_None' range [275-280] for track '26' has 1 frames without a visible bounding box.
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